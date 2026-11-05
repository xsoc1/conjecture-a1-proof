from pathlib import Path
import hashlib,json,datetime
ROOT=Path(r'F:\Codex_Cache\2026-11-05\task\conjecture-a1-proof')
OUT=ROOT/'docs/audit-2026-11-05/lean-audit'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((OUT/'run-manifest.json').read_text())
files=['problem_contract.md','obligation_graph.md','research_ledger.md','approach_registry.md','candidate_proof.md']
context={p:sha(ROOT/'docs/audit-2026-11-05'/p) for p in files}
readback={'verdict':'CONSISTENT_LAYERED_STATUS','input_hashes':context,'scope':'Fresh file-only readback of the contract, obligation graph, ledger, approach registry and candidate reference; not a new independent audit of the written proof.','conclusion':'The updated files distinguish complete corrected written proof and all-parameter tensor sharpness from formally verified partial Lean results. F4/general Lean assembly is open; finite computations are evidence only; no canonical integration or merge is claimed. The earlier stale pending-ledger note is resolved.','lean_status':'FORMALLY_VERIFIED restricted to20 declarations; complete conjecture NOT formally proved.'}
(OUT/'context-convergence.json').write_text(json.dumps(readback,indent=2)+'\n')
note='''\n## Final coordination readback\n\nA fresh file-only read of the frozen contract, obligation graph, updated research ledger, approach registry and candidate reference gives a consistent layered status: the corrected written proof and general tensor sharpness are recorded as independently audited; the general Lean assembly F4 remains open; the finite computations are evidence only; no canonical integration or merge is claimed. This readback verifies consistency of project records, not the written proof anew. The earlier stale pending-ledger note has been resolved. Exact readback input hashes are in `lean-audit/context-convergence.json`.\n'''
for p in [ROOT/'docs/audit-2026-11-05/lean-audit-report.md',OUT/'audit_report.md']:
    p.write_text(p.read_text(encoding='utf-8')+note,encoding='utf-8')
v=json.loads((OUT/'verification.json').read_text())
v['coordination_readback']={'artifact':'context-convergence.json','sha256':sha(OUT/'context-convergence.json'),'verdict':readback['verdict']}
(OUT/'verification.json').write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
current={p:sha(ROOT/p) for p in m['inputs_before']}
changes=[p for p in current if current[p]!=m['inputs_before'][p]]
assert all(p=='AGENTS.md' for p in changes),changes
m['post_audit_context_changes']={p:{'audited':m['inputs_before'][p],'current':current[p],'reason':'Root updated high-level context after releasing the audit hold; mathematical source/config/helper bytes unchanged.'} for p in changes}
m['final_material_source_check']={p:current[p] for p in current if p!='AGENTS.md'}
m['context_convergence_sha256']=sha(OUT/'context-convergence.json')
m['report_sha256']=sha(ROOT/'docs/audit-2026-11-05/lean-audit-report.md')
m['verification_sha256']=sha(OUT/'verification.json')
m['audit_scripts']['close_audit.py']=sha(OUT/'close_audit.py')
binary=Path(r'C:\Users\HuangZY\.elan\toolchains\leanprover--lean4---v4.31.0\bin')
m['compiler_executable_sha256']=sha(binary/'lean.exe')
m['lake_executable_sha256']=sha(binary/'lake.exe')
m['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'run-manifest.json').write_text(json.dumps(m,indent=2)+'\n')
summary={'subgoal_id':'LEAN-INDEPENDENT-AUDIT','verdict':'FORMALLY_VERIFIED','scope':v['scope'],'full_target_verdict':'VERIFICATION_INCOMPLETE','full_conjecture_formally_proved':False,'artifacts':{str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'docs/audit-2026-11-05/lean-audit-report.md',OUT/'verification.json',OUT/'run-manifest.json',OUT/'independent-source-checks.json',OUT/'context-convergence.json']},'final_material_hashes':{b['module']:b['source_sha256'] for b in m['build']},'build_exits':{b['module']:b['exit_code'] for b in m['build']},'signature_guard_exit':m['signature_guard']['exit_code'],'remaining_obligations':v['remaining_obligations'],'post_audit_context_changes':m['post_audit_context_changes']}
(OUT/'delivery.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
