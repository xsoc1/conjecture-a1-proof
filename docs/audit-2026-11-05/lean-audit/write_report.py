from pathlib import Path
import hashlib,json,datetime,re,os,subprocess
ROOT=Path(r'F:\Codex_Cache\2026-11-05\task\conjecture-a1-proof')
OUT=ROOT/'docs/audit-2026-11-05/lean-audit'
manifest=json.loads((OUT/'run-manifest.json').read_text())
scan=json.loads((OUT/'independent-source-checks.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert manifest['status']=='FORMALLY_VERIFIED_RESTRICTED_SCOPE'
notes={
'ad_def':'Definitional unfolding gives xy-yx; the sign agrees with XY-YX=Z.',
'ad_add':'Distribute x(y+z) and (y+z)x, then regroup in the additive abelian group.',
'ad_zero':'Both x0 and 0x vanish.',
'ad_neg':'Distribute negation; x(-y)-(-y)x=-(xy-yx).',
'ad_one':'The two unit products are equal.',
'ad_mul':'Expand [x,y]z+y[x,z]; the middle yxz terms cancel without exchanging factors.',
'ad_pow_succ':'Expand wx^(r+1)+(xw-wx)x^r, using x^(r+1)=x*x^r; associativity cancels wx*x^r.',
'ad_swap':'yx-xy=-(xy-yx), by additive group identities.',
'ad_pow_of_commute':'Induct on n. Leibniz gives [x,y^(n+2)]=[x,y^(n+1)]y+y^(n+1)[x,y]. Move [x,y] past y using only the stated Y-Z commute hypothesis and combine the two natural-number multiples.',
'mul_pow_normal_order':'Rearrange the previous commutator formula to xy^(n+1)=y^(n+1)x+(n+1)y^n[x,y]; the correction has positive sign.',
'ad_pow_eq':'Split n=0 from n=m+1. At zero the natural scalar is zero and [x,1]=0; truncated n-1 causes no boundary defect.',
'pow_mul_normal_order':'Swap x and y, use [y,x]=-[x,y], and transport X-Z commutation across negation. Rearrangement yields the positive correction (n+1)x^n[x,y].',
'two_mul_add_pow_five':'Independently expand the literal full certificate in the free associative integer algebra: both sides have coefficient 2 on all 32 words of length five, residual zero. The correction terms are left/right multiples of RX=x[x,y]-[x,y]x and RY=y[x,y]-[x,y]y, so vanish by the local commuting hypotheses. The remaining summands end on the RIGHT in x^2 and y^2.',
'two_mul_add_pow_three':'Independently expand the literal full certificate: both sides have coefficient 2 on all eight words of length three, residual zero. Corrections are -RX-2RY. The surviving right factors are x^2 and y, giving the asymmetric (1,0) case.',
'vector_two_cancel':'Rewrite v+v as (2:K) scalar-multiplying v; multiply by inverse 2. Field and characteristic zero imply 2 is nonzero. K is explicitly retained by include K, avoiding loss of the scalar field binder.',
'vector_p_one_q_one':'Evaluate the degree-five ring identity in End_K(V) at v. Endomorphism multiplication is composition with right factor acting first; Ax^2(v) and By^2(v) vanish from the vector hypotheses. Apply vector_two_cancel to the remaining twice-output vector. No operator annihilation or finite dimension is used.',
'vector_p_one_q_zero':'Evaluate the degree-three certificate at v; its right factors X^2 and Y vanish at v. Cancel the factor 2 in the characteristic-zero vector space.',
'vector_p_zero_q_one':'Apply the preceding case after swapping X,Y. The commutator changes sign, and both commuting hypotheses are transported by neg_right. Y+X=X+Y for endomorphism addition; exponents remain three.',
'vector_p_zero_q_zero':'At exponent one, (X+Y)v=Xv+Yv=0. The actual signature needs neither characteristic zero nor commutator assumptions; this stronger auxiliary statement applies to the target boundary case.',
'vector_parameters_le_one':'For natural numbers p,q with each at most one, exhaust p=0/1 and q=0/1. Exponent 2p+2q+1 becomes respectively 1,3,3,5, and annihilator powers become 1 or 2. These are exactly the four proved vector cases.'}
obligations=[{'obligation':f'O{i:02d}','declaration':'ConjectureA1.'+n,'result':'FAITHFUL','independent_audit':'PASS','notes':notes[n]} for i,n in enumerate(scan['theorems'],1)]
remaining=[
'Prove VectorConjecture for arbitrary natural p,q. It is only a def; no theorem asserts it.',
'The arbitrary p=0 or q=0 families are not proved here; only p,q simultaneously at most one are covered.',
'A general one-sided proof must formalize its own valid dependencies (for example PBW/grading, left-ideal membership and the line/fewnomial argument), or provide another complete route. Commented Taylor, iterated commutator, z-power, trinomial and two-sided proof plans are not accepted theorems.',
'General sharpness is a separate target and has not been formally proved by these modules.'
]
verification={
'verdict':'FORMALLY_VERIFIED',
'scope':'Only the 20 listed theorem/lemma declarations, including commutator-power formulas and the frozen vector conclusion for p,q in {0,1}.',
'full_target_verdict':'VERIFICATION_INCOMPLETE','full_conjecture_formally_proved':False,
'machine':{'lean_version':manifest['lean_version'],'lake_version':manifest['lake_version'],'build_passed':True,'build_mode':'Independent direct sequential lean -o compilation of four frozen copies; author offline Lake log separately inspected; ordinary online lake build not run.','sorry_axiom_hits':[],'axiom_allowlist':['propext','Classical.choice','Quot.sound'],'axiom_probe_count':20,'signature_guard_exit_code':0,'certificate_integer_expansions':scan['certificate_expansions'],'dependency_pins_match':True,'tracked_dependency_sources_clean':True},
'statement_fidelity':obligations,
'definitions':[{'declaration':'ConjectureA1.VectorConjecture','result':'FAITHFUL','proof_status':'DEFINITION_ONLY','notes':'Explicit Field and CharZero; arbitrary dimension; all natural p,q; vector annihilation; local X-Z and Y-Z commutation. Definitional equality to independently restated contract checked by rfl.'},{'declaration':'ConjectureA1.ConjectureA1','result':'UNFAITHFUL_AS_FULL_TARGET','proof_status':'LEGACY_DEFINITION_ONLY','notes':'Elaborated signature drops unused Algebra Q R; it has only Ring R, AddCommGroup V, Module R V and requires centrality in every ambient ring element. Not used to assert the frozen target.'}],
'critical_errors':[],'gaps':[],'remaining_obligations':remaining,
'reproducibility_notes':['Initial sandbox Git dependency reads exited 128; read-only escalated retries all exited zero. Initial failure logs are preserved.','Default-trust Lean imports existing prebuilt Mathlib/dependency oleans; dependencies were not rebuilt independently. Their source HEAD pins and tracked-clean status were checked.','validate.py is a diagnostic that reads an existing log; it does not itself rebuild or bind that log to current source hashes. This independent run supplies fresh compilation and before/after source-hash binding.','The attempted py -3 launcher invocation exited 1 because no launcher installations were registered. Scripts actually ran with the explicit CPython310 executable.','The skill asset schema/template paths were unavailable in the installed skill; output follows the schema fields embedded in SKILL.md, with additional scope/provenance fields.'],
'repair_hints':'No repairs required for the certified restricted scope. Complete and independently audit the arbitrary-parameter vector theorem before claiming the full conjecture.'}
(OUT/'verification.json').write_text(json.dumps(verification,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
rows='\n'.join(f"| {o['obligation']} | `{o['declaration']}` | PASS / FAITHFUL | {o['notes']} |" for o in obligations)
cmds='\n'.join(f"- `{c['argv']}` — exit {c['exit_code']}; `{c['log']}`." for c in manifest['commands'] if any('compile-' in c['log'] for _ in [0]))
hashrows='\n'.join(f"| `{p}` | `{h}` |" for p,h in manifest['inputs_before'].items() if p.endswith('.lean') and Path(p).stem in ['ConjectureA1','SpecialCases','VectorCases','AxiomAudit'])
rebind_note='The first final hash assertion detected line-ending normalization of SpecialCases.lean, lake-manifest.json and build.ps1 and prevented certification of that changed snapshot. Initial evidence is preserved under `initial-pass/`; `normalization-rebind.json` records both hashes. All four modules and the independent signature guard were then freshly recompiled against the final normalized bytes. The final before/after inventory has no differences.' if (OUT/'normalization-rebind.json').exists() else ''
report=f'''FORMALLY_VERIFIED — restricted scope only

# Independent Lean audit, 2026-11-05

**The full Conjecture A.1 is NOT formally proved.** This verdict certifies exactly the twenty theorem/lemma declarations below, including the four vector cases p,q ∈ {{0,1}} and the arbitrary-power commutator/one-generator normal-order formulas. It does not certify the general arbitrary-parameter theorem, novelty, or commented proof plans.

The auditor read the frozen problem contract and proof sources in a separate pass from the formalizer. No shared Lean source was edited. All generated files are in the assigned audit directory or `F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean`. No cache files or global settings were changed, and no network installation was used.

## Target fidelity

`VectorConjecture K V` faithfully defines the contract for a characteristic-zero field K, any K-vector space V, endomorphisms X,Y, and Z=XY−YX. `Commute X Z` and `Commute Y Z` impose exactly local centrality. There is no finite-dimensionality assumption. The hypotheses are annihilation of the particular vector by X^(p+1), Y^(q+1), and the exponent is exactly 2p+2q+1 for every natural p,q. Zero vectors and zero spaces are permitted. Explicit `[CharZero K]` survives elaboration. A fresh signature guard checks definitional equality with an independently restated complete target and separately typechecks the restricted theorem in arbitrary universes.

`ConjectureA1.ConjectureA1` is a legacy definition of a different proposition. Its unused `[Algebra ℚ R]` is dropped from the elaborated signature; only the ring/module structures remain. It assumes centrality against every ambient ring element, stronger than local X-Z/Y-Z commutation, and does not retain the characteristic-zero field hypothesis. It is neither a faithful replacement nor a theorem. No accepted vector proof uses it to assert the target.

## Independent obligation audit

These twenty obligations are derived by enumerating every material `lemma`/`theorem` outside nested comments, then checking the explicit expected set. Auxiliary ring statements are faithful to the local claims listed here; that designation does not equate them with the full vector target.

| Obligation | Declaration | Result | Independent reasoning |
|---|---|---|---|
{rows}

Both certificates were independently parsed from the frozen literal `have cert` equalities and expanded over free noncommutative integer words, using a separate standard-library checker. The degree-five identity has all 32 words with coefficient 2; the degree-three identity has all eight words with coefficient 2. Both residual dictionaries are empty. More importantly, Lean itself checks the final polynomial equalities via `noncomm_ring`; neither `certificate.py`, SymPy nor numerical evaluation is a proof oracle. `certificate.py` is discovery code and was not executed by this audit.

The orientation matters: A*X² and B*Y² act on v with the annihilator first. No assumption X²=0 as an operator is introduced, and no left ideal is treated as two-sided. Natural scalars in ring identities do not require characteristic zero; the vector cancellation of 2 uses the actual characteristic-zero field hypothesis. The zero-parameter exponent-one case has a legitimately stronger signature without characteristic zero.

## Machine evidence and environment

Lean: `{manifest['lean_version']}`. Lake: `{manifest['lake_version']}`. Toolchain file pins `leanprover/lean4:v4.31.0`. Mathlib is pinned and observed at `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`; all nine dependency revisions match `formalization/lake-manifest.json`, and Git reports no tracked modifications in any dependency checkout. Exact expected/actual pins and per-command logs are in `run-manifest.json`.

The four source copies were compiled sequentially with direct `lean.exe -o` commands, with the isolated output directory first in LEAN_PATH and existing read-only library/dependency build paths afterward. Thus project imports resolve to freshly produced audit oleans. All four exits are zero, as is the extra signature guard. The sole compiler warning is the existing duplicated legacy namespace. The author's `lake.exe -f lakefile.offline.lean build` log was separately read and reports success; its helper explicitly recompiles the same four modules. **The ordinary dependency-managed online `lake build` was not run.**

{cmds}

`compile-AxiomAudit.log` independently prints all twenty axiom sets; `independent-source-checks.json` maps them. The only axioms are `propext`, `Classical.choice`, and `Quot.sound`, the permitted standard Lean logical/quotient principles. None is a problem-specific mathematical assumption. The independent code scan masks nested block comments, line comments and strings, and found no executable `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, `sorryAx`, `run_tac`, `elab`, `macro`, or `debug.skipKernelTC` token. All expected declarations are present exactly once.

Initial sandbox Git reads of the external cache failed with permission denied (exit 128); the raw failed logs are retained. Explicit read-only escalated retries verified all pins/statuses successfully. The first `py -3` invocation failed (exit 1) because the launcher has no registered installation; both audit scripts then ran using `C:\\Users\\HuangZY\\AppData\\Local\\Programs\\Python\\Python310\\python.exe`. No failed build was hidden.

## Source binding and reproducibility limits

| Material input | SHA-256 |
|---|---|
{hashrows}

All inventoried source, configuration, contract and prior-evidence hashes were checked again at the end, with **no differences**. The independent manifest binds each command to its raw log hash and each rebuilt olean to its exact copied source hash. `IndependentSignatureGuard.lean` is preserved in the audit directory, and its checked output is in the scratch directory. The repository baseline is `f8f7235dca197933cd97ac74b6d35d64f67e693d`; the checkout is intentionally dirty with author/root work, listed in `git-status.log`.

{rebind_note}

The usual Lean trusted-environment assumption applies: this run imports prebuilt standard/library oleans at the verified source pins, rather than rebuilding or independently checking all of Mathlib from source. `validate.py` is useful for token/probe diagnostics, but reads a pre-existing log and does not alone bind that log to current sources or cause a build. Its positive output alone is insufficient; the fresh independent builds and frozen hashes supply that missing binding. The offline helper verifies mathlib HEAD, but does not itself enforce every dependency HEAD or tracked-clean status; this audit performs those additional checks. The installed skill schema/template asset files were absent, so the JSON follows the fields printed in the skill instructions rather than claiming an unavailable schema validator ran.

## Remaining full-target obligations

'''+ '\n'.join('- '+r for r in remaining)+'''

The complete target status is `VERIFICATION_INCOMPLETE`. No localized defect was found in the twenty certified declarations. Formalizing arbitrary p,q and auditing that proof is necessary before changing the full-target status.
'''
(ROOT/'docs/audit-2026-11-05/lean-audit-report.md').write_text(report,encoding='utf-8')
(OUT/'audit_report.md').write_text(report,encoding='utf-8')
if 'started_utc' in manifest:
    manifest['inventory_recorded_utc']=manifest.pop('started_utc')
manifest['timestamp_note']='inventory_recorded_utc was recorded after the four compilations; exact initial wall-clock start was not recorded.'
manifest['remaining_obligations']=remaining
manifest['cache_access_note']='Initial-pass sandbox cache Git reads exited 128 and are archived in initial-pass; read-only escalated retries and all final-pass dependency checks passed. No cache writes performed.'
if (OUT/'normalization-rebind.json').exists():
    manifest['normalization_rebind']=json.loads((OUT/'normalization-rebind.json').read_text())
manifest['verdict']='FORMALLY_VERIFIED'
manifest['full_target_verdict']='VERIFICATION_INCOMPLETE'
manifest['scope']=verification['scope']
manifest['independent_scan_sha256']=sha(OUT/'independent-source-checks.json')
manifest['verification_sha256']=sha(OUT/'verification.json')
manifest['report_sha256']=sha(ROOT/'docs/audit-2026-11-05/lean-audit-report.md')
manifest['audit_scripts']={p.name:sha(p) for p in OUT.glob('*.py')}
manifest['inputs_after']={p:sha(ROOT/p) for p in manifest['inputs_before']}
manifest['changed_inputs']=[p for p in manifest['inputs_before'] if manifest['inputs_before'][p]!=manifest['inputs_after'][p]]
assert not manifest['changed_inputs'],manifest['changed_inputs']
manifest['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'run-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'subgoal_id':'LEAN-INDEPENDENT-AUDIT','verdict':'FORMALLY_VERIFIED','scope':verification['scope'],'full_conjecture_formally_proved':False,'report':str(ROOT/'docs/audit-2026-11-05/lean-audit-report.md'),'report_sha256':sha(ROOT/'docs/audit-2026-11-05/lean-audit-report.md'),'verification_sha256':sha(OUT/'verification.json'),'manifest_sha256':sha(OUT/'run-manifest.json'),'changed_inputs':manifest['changed_inputs']},indent=2))
