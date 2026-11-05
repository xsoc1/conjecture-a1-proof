from pathlib import Path
import subprocess, hashlib, json, os, re, datetime, shutil

ROOT = Path(r'F:\Codex_Cache\2026-11-05\task\conjecture-a1-proof')
OUT = ROOT/'docs/audit-2026-11-05/lean-audit'
SCRATCH = Path(r'F:\Codex_Cache\2026-11-05\task\a1-independent-lean')
BIN = Path(r'C:\Users\HuangZY\.elan\toolchains\leanprover--lean4---v4.31.0\bin')
CACHE = Path(r'F:\LaTeX\BVE research\lean-proof\.lake\packages')
MODULES = ['ConjectureA1','SpecialCases','VectorCases','AxiomAudit']
OUT.mkdir(parents=True, exist_ok=True)
SCRATCH.mkdir(parents=True, exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
inputs = [ROOT/'AGENTS.md', ROOT/'docs/audit-2026-11-05/problem_contract.md']
inputs += list((ROOT/'formalization').glob('*.lean'))
inputs += [ROOT/'formalization'/s for s in ['lean-toolchain','lake-manifest.json','build.ps1','setup.ps1','validate.py','certificate.py','evidence/source-and-axioms.json','evidence/lake-build.log','evidence/build-context.log']]
start = {str(p.relative_to(ROOT)):sha(p) for p in inputs}
(OUT/'frozen-input-hashes.json').write_text(json.dumps(start,indent=2)+'\n')
commands=[]
def run(args,label,cwd=ROOT,env=None):
    result=subprocess.run([str(a) for a in args],cwd=cwd,env=env,capture_output=True)
    log=OUT/(label+'.log')
    log.write_bytes(result.stdout+b'\n--- STDERR ---\n'+result.stderr+b'\nEXIT='+str(result.returncode).encode()+b'\n')
    commands.append({'argv':[str(a) for a in args],'cwd':str(cwd),'exit_code':result.returncode,'log':str(log.relative_to(ROOT)),'log_sha256':sha(log)})
    return result
lean_version=run([BIN/'lean.exe','--version'],'lean-version').stdout.decode().strip()
lake_version=run([BIN/'lake.exe','--version'],'lake-version').stdout.decode().strip()
run(['git','rev-parse','HEAD'],'git-head')
run(['git','status','--short'],'git-status')
manifest=json.loads((ROOT/'formalization/lake-manifest.json').read_text())
deps=[]
paths=[str(SCRATCH)]
for p in manifest['packages']:
    dep=CACHE/p['name']
    r=run(['git','-C',dep,'rev-parse','HEAD'],'dependency-'+p['name'])
    actual=r.stdout.decode().strip()
    dirty=run(['git','-C',dep,'status','--porcelain','--untracked-files=no'],'dependency-status-'+p['name'])
    deps.append({'name':p['name'],'expected':p['rev'],'actual':actual,'match':actual==p['rev'],'tracked_dirty':dirty.stdout.decode().splitlines()})
    lib=dep/'.lake/build/lib/lean'
    if lib.exists(): paths.append(str(lib))
env=os.environ.copy(); env['LEAN_PATH']=';'.join(paths)
build=[]
for name in MODULES:
    source=ROOT/'formalization'/(name+'.lean')
    target=SCRATCH/(name+'.lean')
    shutil.copyfile(source,target)
    assert sha(target)==start[str(source.relative_to(ROOT))]
    r=run([BIN/'lean.exe','-o',SCRATCH/(name+'.olean'),target],'compile-'+name,cwd=SCRATCH,env=env)
    build.append({'module':name,'exit_code':r.returncode,'source_sha256':sha(target),'olean_sha256':sha(SCRATCH/(name+'.olean')) if (SCRATCH/(name+'.olean')).exists() else None})
    if r.returncode: break
result={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'lean_version':lean_version,'lake_version':lake_version,'lean_path':paths,'dependencies':deps,'commands':commands,'build':build,'inputs_before':start}
(OUT/'run-in-progress.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'versions':[lean_version,lake_version],'build':build,'dependency_matches':all(d['match'] for d in deps),'dependency_dirty':{d['name']:d['tracked_dirty'] for d in deps if d['tracked_dirty']}},indent=2))
