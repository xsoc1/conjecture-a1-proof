FORMALLY_VERIFIED — restricted scope only

# Independent Lean audit, 2026-11-05

**The full Conjecture A.1 is NOT formally proved.** This verdict certifies exactly the twenty theorem/lemma declarations below, including the four vector cases p,q ∈ {0,1} and the arbitrary-power commutator/one-generator normal-order formulas. It does not certify the general arbitrary-parameter theorem, novelty, or commented proof plans.

The auditor read the frozen problem contract and proof sources in a separate pass from the formalizer. No shared Lean source was edited. All generated files are in the assigned audit directory or `F:\Codex_Cache\2026-11-05\task\a1-independent-lean`. No cache files or global settings were changed, and no network installation was used.

## Target fidelity

`VectorConjecture K V` faithfully defines the contract for a characteristic-zero field K, any K-vector space V, endomorphisms X,Y, and Z=XY−YX. `Commute X Z` and `Commute Y Z` impose exactly local centrality. There is no finite-dimensionality assumption. The hypotheses are annihilation of the particular vector by X^(p+1), Y^(q+1), and the exponent is exactly 2p+2q+1 for every natural p,q. Zero vectors and zero spaces are permitted. Explicit `[CharZero K]` survives elaboration. A fresh signature guard checks definitional equality with an independently restated complete target and separately typechecks the restricted theorem in arbitrary universes.

`ConjectureA1.ConjectureA1` is a legacy definition of a different proposition. Its unused `[Algebra ℚ R]` is dropped from the elaborated signature; only the ring/module structures remain. It assumes centrality against every ambient ring element, stronger than local X-Z/Y-Z commutation, and does not retain the characteristic-zero field hypothesis. It is neither a faithful replacement nor a theorem. No accepted vector proof uses it to assert the target.

## Independent obligation audit

These twenty obligations are derived by enumerating every material `lemma`/`theorem` outside nested comments, then checking the explicit expected set. Auxiliary ring statements are faithful to the local claims listed here; that designation does not equate them with the full vector target.

| Obligation | Declaration | Result | Independent reasoning |
|---|---|---|---|
| O01 | `ConjectureA1.ad_def` | PASS / FAITHFUL | Definitional unfolding gives xy-yx; the sign agrees with XY-YX=Z. |
| O02 | `ConjectureA1.ad_add` | PASS / FAITHFUL | Distribute x(y+z) and (y+z)x, then regroup in the additive abelian group. |
| O03 | `ConjectureA1.ad_zero` | PASS / FAITHFUL | Both x0 and 0x vanish. |
| O04 | `ConjectureA1.ad_neg` | PASS / FAITHFUL | Distribute negation; x(-y)-(-y)x=-(xy-yx). |
| O05 | `ConjectureA1.ad_one` | PASS / FAITHFUL | The two unit products are equal. |
| O06 | `ConjectureA1.ad_mul` | PASS / FAITHFUL | Expand [x,y]z+y[x,z]; the middle yxz terms cancel without exchanging factors. |
| O07 | `ConjectureA1.ad_pow_succ` | PASS / FAITHFUL | Expand wx^(r+1)+(xw-wx)x^r, using x^(r+1)=x*x^r; associativity cancels wx*x^r. |
| O08 | `ConjectureA1.ad_swap` | PASS / FAITHFUL | yx-xy=-(xy-yx), by additive group identities. |
| O09 | `ConjectureA1.ad_pow_of_commute` | PASS / FAITHFUL | Induct on n. Leibniz gives [x,y^(n+2)]=[x,y^(n+1)]y+y^(n+1)[x,y]. Move [x,y] past y using only the stated Y-Z commute hypothesis and combine the two natural-number multiples. |
| O10 | `ConjectureA1.mul_pow_normal_order` | PASS / FAITHFUL | Rearrange the previous commutator formula to xy^(n+1)=y^(n+1)x+(n+1)y^n[x,y]; the correction has positive sign. |
| O11 | `ConjectureA1.ad_pow_eq` | PASS / FAITHFUL | Split n=0 from n=m+1. At zero the natural scalar is zero and [x,1]=0; truncated n-1 causes no boundary defect. |
| O12 | `ConjectureA1.pow_mul_normal_order` | PASS / FAITHFUL | Swap x and y, use [y,x]=-[x,y], and transport X-Z commutation across negation. Rearrangement yields the positive correction (n+1)x^n[x,y]. |
| O13 | `ConjectureA1.two_mul_add_pow_five` | PASS / FAITHFUL | Independently expand the literal full certificate in the free associative integer algebra: both sides have coefficient 2 on all 32 words of length five, residual zero. The correction terms are left/right multiples of RX=x[x,y]-[x,y]x and RY=y[x,y]-[x,y]y, so vanish by the local commuting hypotheses. The remaining summands end on the RIGHT in x^2 and y^2. |
| O14 | `ConjectureA1.two_mul_add_pow_three` | PASS / FAITHFUL | Independently expand the literal full certificate: both sides have coefficient 2 on all eight words of length three, residual zero. Corrections are -RX-2RY. The surviving right factors are x^2 and y, giving the asymmetric (1,0) case. |
| O15 | `ConjectureA1.vector_two_cancel` | PASS / FAITHFUL | Rewrite v+v as (2:K) scalar-multiplying v; multiply by inverse 2. Field and characteristic zero imply 2 is nonzero. K is explicitly retained by include K, avoiding loss of the scalar field binder. |
| O16 | `ConjectureA1.vector_p_one_q_one` | PASS / FAITHFUL | Evaluate the degree-five ring identity in End_K(V) at v. Endomorphism multiplication is composition with right factor acting first; Ax^2(v) and By^2(v) vanish from the vector hypotheses. Apply vector_two_cancel to the remaining twice-output vector. No operator annihilation or finite dimension is used. |
| O17 | `ConjectureA1.vector_p_one_q_zero` | PASS / FAITHFUL | Evaluate the degree-three certificate at v; its right factors X^2 and Y vanish at v. Cancel the factor 2 in the characteristic-zero vector space. |
| O18 | `ConjectureA1.vector_p_zero_q_one` | PASS / FAITHFUL | Apply the preceding case after swapping X,Y. The commutator changes sign, and both commuting hypotheses are transported by neg_right. Y+X=X+Y for endomorphism addition; exponents remain three. |
| O19 | `ConjectureA1.vector_p_zero_q_zero` | PASS / FAITHFUL | At exponent one, (X+Y)v=Xv+Yv=0. The actual signature needs neither characteristic zero nor commutator assumptions; this stronger auxiliary statement applies to the target boundary case. |
| O20 | `ConjectureA1.vector_parameters_le_one` | PASS / FAITHFUL | For natural numbers p,q with each at most one, exhaust p=0/1 and q=0/1. Exponent 2p+2q+1 becomes respectively 1,3,3,5, and annihilator powers become 1 or 2. These are exactly the four proved vector cases. |

Both certificates were independently parsed from the frozen literal `have cert` equalities and expanded over free noncommutative integer words, using a separate standard-library checker. The degree-five identity has all 32 words with coefficient 2; the degree-three identity has all eight words with coefficient 2. Both residual dictionaries are empty. More importantly, Lean itself checks the final polynomial equalities via `noncomm_ring`; neither `certificate.py`, SymPy nor numerical evaluation is a proof oracle. `certificate.py` is discovery code and was not executed by this audit.

The orientation matters: A*X² and B*Y² act on v with the annihilator first. No assumption X²=0 as an operator is introduced, and no left ideal is treated as two-sided. Natural scalars in ring identities do not require characteristic zero; the vector cancellation of 2 uses the actual characteristic-zero field hypothesis. The zero-parameter exponent-one case has a legitimately stronger signature without characteristic zero.

## Machine evidence and environment

Lean: `Lean (version 4.31.0, x86_64-w64-windows-gnu, commit 68218e876d2a38b1985b8590fff244a83c321783, Release)`. Lake: `Lake version 5.0.0-src+68218e8 (Lean version 4.31.0)`. Toolchain file pins `leanprover/lean4:v4.31.0`. Mathlib is pinned and observed at `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`; all nine dependency revisions match `formalization/lake-manifest.json`, and Git reports no tracked modifications in any dependency checkout. Exact expected/actual pins and per-command logs are in `run-manifest.json`.

The four source copies were compiled sequentially with direct `lean.exe -o` commands, with the isolated output directory first in LEAN_PATH and existing read-only library/dependency build paths afterward. Thus project imports resolve to freshly produced audit oleans. All four exits are zero, as is the extra signature guard. The sole compiler warning is the existing duplicated legacy namespace. The author's `lake.exe -f lakefile.offline.lean build` log was separately read and reports success; its helper explicitly recompiles the same four modules. **The ordinary dependency-managed online `lake build` was not run.**

- `['C:\\Users\\HuangZY\\.elan\\toolchains\\leanprover--lean4---v4.31.0\\bin\\lean.exe', '-o', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\ConjectureA1.olean', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\ConjectureA1.lean']` — exit 0; `docs\audit-2026-11-05\lean-audit\compile-ConjectureA1.log`.
- `['C:\\Users\\HuangZY\\.elan\\toolchains\\leanprover--lean4---v4.31.0\\bin\\lean.exe', '-o', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\SpecialCases.olean', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\SpecialCases.lean']` — exit 0; `docs\audit-2026-11-05\lean-audit\compile-SpecialCases.log`.
- `['C:\\Users\\HuangZY\\.elan\\toolchains\\leanprover--lean4---v4.31.0\\bin\\lean.exe', '-o', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\VectorCases.olean', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\VectorCases.lean']` — exit 0; `docs\audit-2026-11-05\lean-audit\compile-VectorCases.log`.
- `['C:\\Users\\HuangZY\\.elan\\toolchains\\leanprover--lean4---v4.31.0\\bin\\lean.exe', '-o', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\AxiomAudit.olean', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\AxiomAudit.lean']` — exit 0; `docs\audit-2026-11-05\lean-audit\compile-AxiomAudit.log`.
- `['C:\\Users\\HuangZY\\.elan\\toolchains\\leanprover--lean4---v4.31.0\\bin\\lean.exe', '-o', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\IndependentSignatureGuard.olean', 'F:\\Codex_Cache\\2026-11-05\\task\\a1-independent-lean\\IndependentSignatureGuard.lean']` — exit 0; `docs\audit-2026-11-05\lean-audit\compile-IndependentSignatureGuard.log`.

`compile-AxiomAudit.log` independently prints all twenty axiom sets; `independent-source-checks.json` maps them. The only axioms are `propext`, `Classical.choice`, and `Quot.sound`, the permitted standard Lean logical/quotient principles. None is a problem-specific mathematical assumption. The independent code scan masks nested block comments, line comments and strings, and found no executable `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, `sorryAx`, `run_tac`, `elab`, `macro`, or `debug.skipKernelTC` token. All expected declarations are present exactly once.

Initial sandbox Git reads of the external cache failed with permission denied (exit 128); the raw failed logs are retained. Explicit read-only escalated retries verified all pins/statuses successfully. The first `py -3` invocation failed (exit 1) because the launcher has no registered installation; both audit scripts then ran using `C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe`. No failed build was hidden.

## Source binding and reproducibility limits

| Material input | SHA-256 |
|---|---|
| `formalization\AxiomAudit.lean` | `321e9b36275f21406f46f78461d4f13d52c83dba698facdd37063727be332bc0` |
| `formalization\ConjectureA1.lean` | `aa9bb362b88e68404948c25021f9d57c986ba0a4924f50b610f37df0836312fa` |
| `formalization\SpecialCases.lean` | `35dea501e6e456ccfbf4ff08143cc8978ebb7afd8393d716ea28290413ad52ca` |
| `formalization\VectorCases.lean` | `cd0525eeb9ba9f8c12b411b9cb9a9ccf798dbed4ab8e3acea66a82623ed49807` |

All inventoried source, configuration, contract and prior-evidence hashes were checked again at the end, with **no differences**. The independent manifest binds each command to its raw log hash and each rebuilt olean to its exact copied source hash. `IndependentSignatureGuard.lean` is preserved in the audit directory, and its checked output is in the scratch directory. The repository baseline is `f8f7235dca197933cd97ac74b6d35d64f67e693d`; the checkout is intentionally dirty with author/root work, listed in `git-status.log`.

The first final hash assertion detected line-ending normalization of SpecialCases.lean, lake-manifest.json and build.ps1 and prevented certification of that changed snapshot. Initial evidence is preserved under `initial-pass/`; `normalization-rebind.json` records both hashes. All four modules and the independent signature guard were then freshly recompiled against the final normalized bytes. The final before/after inventory has no differences.

The usual Lean trusted-environment assumption applies: this run imports prebuilt standard/library oleans at the verified source pins, rather than rebuilding or independently checking all of Mathlib from source. `validate.py` is useful for token/probe diagnostics, but reads a pre-existing log and does not alone bind that log to current sources or cause a build. Its positive output alone is insufficient; the fresh independent builds and frozen hashes supply that missing binding. The offline helper verifies mathlib HEAD, but does not itself enforce every dependency HEAD or tracked-clean status; this audit performs those additional checks. The installed skill schema/template asset files were absent, so the JSON follows the fields printed in the skill instructions rather than claiming an unavailable schema validator ran.

## Remaining full-target obligations

- Prove VectorConjecture for arbitrary natural p,q. It is only a def; no theorem asserts it.
- The arbitrary p=0 or q=0 families are not proved here; only p,q simultaneously at most one are covered.
- A general one-sided proof must formalize its own valid dependencies (for example PBW/grading, left-ideal membership and the line/fewnomial argument), or provide another complete route. Commented Taylor, iterated commutator, z-power, trinomial and two-sided proof plans are not accepted theorems.
- General sharpness is a separate target and has not been formally proved by these modules.

The complete target status is `VERIFICATION_INCOMPLETE`. No localized defect was found in the twenty certified declarations. Formalizing arbitrary p,q and auditing that proof is necessary before changing the full-target status.

## Final coordination readback

A fresh file-only read of the frozen contract, obligation graph, updated research ledger, approach registry and candidate reference gives a consistent layered status: the corrected written proof and general tensor sharpness are recorded as independently audited; the general Lean assembly F4 remains open; the finite computations are evidence only; no canonical integration or merge is claimed. This readback verifies consistency of project records, not the written proof anew. The earlier stale pending-ledger note has been resolved. Exact readback input hashes are in `lean-audit/context-convergence.json`.
