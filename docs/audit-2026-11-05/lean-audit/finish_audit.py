from pathlib import Path
from collections import defaultdict
import subprocess, hashlib, json, os, re, datetime
ROOT=Path(r'F:\Codex_Cache\2026-11-05\task\conjecture-a1-proof')
OUT=ROOT/'docs/audit-2026-11-05/lean-audit'
SCRATCH=Path(r'F:\Codex_Cache\2026-11-05\task\a1-independent-lean')
BIN=Path(r'C:\Users\HuangZY\.elan\toolchains\leanprover--lean4---v4.31.0\bin')
CACHE=Path(r'F:\LaTeX\BVE research\lean-proof\.lake\packages')
manifest=json.loads((OUT/'run-in-progress.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args,label,env=None,cwd=ROOT):
    r=subprocess.run([str(a) for a in args],cwd=cwd,env=env,capture_output=True)
    log=OUT/(label+'.log'); log.write_bytes(r.stdout+b'\n--- STDERR ---\n'+r.stderr+b'\nEXIT='+str(r.returncode).encode()+b'\n')
    manifest['commands'].append({'argv':[str(a) for a in args],'cwd':str(cwd),'exit_code':r.returncode,'log':str(log.relative_to(ROOT)),'log_sha256':sha(log)})
    return r
for d in manifest['dependencies']:
    dep=CACHE/d['name']
    r=run(['git','-C',dep,'rev-parse','HEAD'],'resolved-dependency-'+d['name'])
    s=run(['git','-C',dep,'status','--porcelain','--untracked-files=no'],'resolved-dependency-status-'+d['name'])
    d.update(actual=r.stdout.decode().strip(),match=r.returncode==0 and r.stdout.decode().strip()==d['expected'],tracked_dirty=s.stdout.decode().splitlines(),status_exit=s.returncode)
manifest['cache_access_note']='Initial sandbox Git cache reads exited 128 (permission denied); read-only escalated retry recorded separately. No cache writes performed.'

def mask(t):
    out=list(t); i=0
    while i<len(t):
        end=i
        if t.startswith('--',i):
            end=t.find('\n',i); end=len(t) if end<0 else end
        elif t.startswith('/-',i):
            end=i+2; depth=1
            while end<len(t) and depth:
                if t.startswith('/-',end): depth+=1; end+=2
                elif t.startswith('-/',end): depth-=1; end+=2
                else: end+=1
            if depth: raise ValueError('unclosed comment')
        elif t[i]=='"':
            end=i+1
            while end<len(t):
                if t[end]=='\\': end+=2
                elif t[end]=='"': end+=1; break
                else: end+=1
        if end>i:
            for k in range(i,end):
                if out[k]!='\n': out[k]=' '
            i=end
        else: i+=1
    return ''.join(out)
names=[]; hits=[]
for path in sorted((ROOT/'formalization').glob('*.lean')):
    code=mask(path.read_text(encoding='utf-8-sig'))
    for m in re.finditer(r'\b(sorry|admit|axiom|unsafe|native_decide|sorryAx|run_tac|elab|macro)\b|debug\.skipKernelTC',code):
        hits.append({'file':path.name,'line':code.count('\n',0,m.start())+1,'token':m.group()})
    names+=re.findall(r'\b(?:lemma|theorem)\s+([\w\']+)',code)
expected=['ad_def','ad_add','ad_zero','ad_neg','ad_one','ad_mul','ad_pow_succ','ad_swap','ad_pow_of_commute','mul_pow_normal_order','ad_pow_eq','pow_mul_normal_order','two_mul_add_pow_five','two_mul_add_pow_three','vector_two_cancel','vector_p_one_q_one','vector_p_one_q_zero','vector_p_zero_q_one','vector_p_zero_q_zero','vector_parameters_le_one']
assert set(names)==set(expected) and len(names)==20
log=(OUT/'compile-AxiomAudit.log').read_text(encoding='utf-8')
axioms={}
for n in names:
    full='ConjectureA1.'+n
    m=re.search("'"+re.escape(full)+r"' depends on axioms: \[([^\]]*)\]",log)
    if m: axioms[full]=[a.strip() for a in m.group(1).split(',') if a.strip()]
    elif f"'{full}' does not depend on any axioms" in log: axioms[full]=[]
    else: raise AssertionError('missing axiom set '+full)
assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in axioms.values())
assert not hits

# Independently expand the two literal certificate equalities in the free Z algebra.
# This parser is standard-library-only and does not execute certificate.py or SymPy.
def add(a,b,sgn=1):
    c=defaultdict(int,a)
    for w,k in b.items(): c[w]+=sgn*k
    return {w:k for w,k in c.items() if k}
def mul(a,b):
    c=defaultdict(int)
    for w,k in a.items():
        for v,l in b.items(): c[w+v]+=k*l
    return {w:k for w,k in c.items() if k}
class Parser:
    def __init__(self,t):
        self.ts=re.findall(r'ad|x|y|\d+|[()+*^\-]',t); self.i=0
        assert re.sub(r'\s+','',t)==''.join(self.ts)
    def take(self):
        t=self.ts[self.i]; self.i+=1; return t
    def peek(self): return self.ts[self.i] if self.i<len(self.ts) else None
    def expr(self):
        a=self.prod()
        while self.peek() in ['+','-']:
            op=self.take(); a=add(a,self.prod(),1 if op=='+' else -1)
        return a
    def prod(self):
        a=self.power()
        while self.peek()=='*': self.take(); a=mul(a,self.power())
        return a
    def power(self):
        a=self.atom()
        if self.peek()=='^':
            self.take(); n=int(self.take()); b={'':1}
            for _ in range(n): b=mul(b,a)
            return b
        return a
    def atom(self):
        t=self.take()
        if t=='-': return {w:-k for w,k in self.atom().items()}
        if t=='(':
            a=self.expr(); assert self.take()==')'; return a
        if t=='ad':
            assert self.take()=='x' and self.take()=='y'; return {'xy':1,'yx':-1}
        if t in ['x','y']: return {t:1}
        return {'':int(t)}
def parse(t):
    p=Parser(t); a=p.expr(); assert p.i==len(p.ts); return a
src=(SCRATCH/'SpecialCases.lean').read_text(encoding='utf-8')
certs=[]
for n,body in re.findall(r'lemma\s+(\w+)(.*?)(?=\nlemma |\n/--|\nend ConjectureA1)',src,re.S):
    eq=body.split('have cert :',1)[1].split(':= by',1)[0]
    lhs,rhs=eq.split('=',1)
    a,b=parse(lhs),parse(rhs)
    assert a==b
    certs.append({'theorem':n,'free_word_identity':True,'degree':max(map(len,a)),'nonzero_target_words':len(a),'residual':add(a,b,-1)})
assert len(certs)==2
scan={'theorem_count':len(names),'theorems':names,'forbidden_code_tokens':hits,'axioms':axioms,'certificate_expansions':certs,'scan_note':'Nested block and line comments plus strings masked; all material Lean sources scanned. Names checked against explicit expected twenty.'}
(OUT/'independent-source-checks.json').write_text(json.dumps(scan,indent=2)+'\n')
guard='''import VectorCases
namespace IndependentSignatureGuard
open ConjectureA1
universe u v
example (K : Type u) (V : Type v) [Field K] [CharZero K] [AddCommGroup V] [Module K V] :
    VectorConjecture K V = (∀ (X Y : Module.End K V),
      Commute X (ad X Y) → Commute Y (ad X Y) → ∀ (p q : ℕ) (v : V),
      (X ^ (p+1)) v = 0 → (Y ^ (q+1)) v = 0 → ((X+Y) ^ (2*p+2*q+1)) v = 0) := rfl
example {K : Type u} {V : Type v} [Field K] [CharZero K] [AddCommGroup V] [Module K V]
    (X Y : Module.End K V) (hX : Commute X (ad X Y)) (hY : Commute Y (ad X Y))
    (p q : ℕ) (hp : p ≤ 1) (hq : q ≤ 1) (v : V)
    (hx : (X^(p+1)) v = 0) (hy : (Y^(q+1)) v = 0) :
    ((X+Y)^(2*p+2*q+1)) v = 0 := vector_parameters_le_one X Y hX hY p q hp hq v hx hy
end IndependentSignatureGuard
'''
guard+='\n'.join('#print ConjectureA1.'+n for n in expected)+'\n'
(OUT/'IndependentSignatureGuard.lean').write_text(guard,encoding='utf-8')
(SCRATCH/'IndependentSignatureGuard.lean').write_text(guard,encoding='utf-8')
env=os.environ.copy(); env['LEAN_PATH']=';'.join(manifest['lean_path'])
r=run([BIN/'lean.exe','-o',SCRATCH/'IndependentSignatureGuard.olean',SCRATCH/'IndependentSignatureGuard.lean'],'compile-IndependentSignatureGuard',env=env,cwd=SCRATCH)
assert r.returncode==0
manifest['signature_guard']={'exit_code':r.returncode,'source_sha256':sha(OUT/'IndependentSignatureGuard.lean')}
manifest['inputs_after']={p:sha(ROOT/p) for p in manifest['inputs_before']}
manifest['changed_inputs']=[p for p in manifest['inputs_before'] if manifest['inputs_before'][p]!=manifest['inputs_after'][p]]
manifest['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest['status']='FORMALLY_VERIFIED_RESTRICTED_SCOPE' if not manifest['changed_inputs'] and all(d['match'] and not d['tracked_dirty'] and d['status_exit']==0 for d in manifest['dependencies']) else 'VERIFICATION_INCOMPLETE'
(OUT/'run-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':manifest['status'],'changed_inputs':manifest['changed_inputs'],'dependency_matches':all(d['match'] for d in manifest['dependencies']),'certificates':certs,'axiom_probes':len(axioms),'signature_guard_exit':r.returncode},indent=2))
