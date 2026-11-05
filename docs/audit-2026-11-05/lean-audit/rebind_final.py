from pathlib import Path
import subprocess,json,hashlib,shutil,sys
ROOT=Path(r'F:\Codex_Cache\2026-11-05\task\conjecture-a1-proof')
OUT=ROOT/'docs/audit-2026-11-05/lean-audit'
OLD=OUT/'initial-pass'
OLD.mkdir(exist_ok=True)
before=json.loads((OUT/'run-manifest.json').read_text())['inputs_before']
now={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in before}
changed={p:{'old':before[p],'new':now[p]} for p in before if before[p]!=now[p]}
for p in OUT.iterdir():
    if p.is_file() and p.suffix in ['.json','.log']:
        shutil.copyfile(p,OLD/p.name)
note={'detected_changed_inputs':changed,'reason':'Root normalized source/config/helper line endings before commit. Initial final hash assertion detected this and prevented certification. New frozen-byte compilation follows.','prior_evidence':'initial-pass/','initial_pass_status':'Successful four-module build and signature guard, superseded byte snapshot; not final certificate.'}
(OUT/'normalization-rebind.json').write_text(json.dumps(note,indent=2)+'\n')
for name in ['run_audit.py','finish_audit.py','write_report.py']:
    r=subprocess.run([sys.executable,str(OUT/name)],cwd=ROOT,capture_output=True)
    (OUT/('driver-'+name+'.log')).write_bytes(r.stdout+b'\nSTDERR:\n'+r.stderr+b'\nEXIT='+str(r.returncode).encode()+b'\n')
    print(name,'EXIT='+str(r.returncode),flush=True)
    if r.returncode:
        print(r.stdout.decode(errors='replace'),r.stderr.decode(errors='replace'));raise SystemExit(r.returncode)
print((OUT/'driver-write_report.py.log').read_text())
