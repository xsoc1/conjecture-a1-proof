# Formally verified partial result — 2026-11-05

Import `VectorCases` to use `ConjectureA1.vector_parameters_le_one`. It proves the
frozen vector-level conclusion for **every p,q ≤ 1**, over every characteristic-zero
field and every vector space, including zero spaces and zero vectors.

**The general conjecture remains open in Lean.** Neither arbitrary `p=0` nor
arbitrary `q=0` has been proved. `VectorConjecture` is a faithful definition of the
full target, not a theorem asserting it.

## Reproduce the accepted checks

From the repository root, in native PowerShell:

```powershell
.\formalization\build.ps1 `
  -LeanBin 'C:\Users\HuangZY\.elan\toolchains\leanprover--lean4---v4.31.0\bin' `
  -MathlibCache 'F:\LaTeX\BVE research\lean-proof\.lake\packages\mathlib'
& 'C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe' formalization/validate.py
git diff --check -- formalization
```

The first command really runs `lake.exe -f lakefile.offline.lean build`.
Its custom `proofcheck` target sequentially invokes native Lean on
`ConjectureA1`, `SpecialCases`, `VectorCases`, and `AxiomAudit`, writing fresh
artifacts under `formalization/.lake/build/lib/lean`. That fresh output directory
comes first in the compiler search path; no stale root-level olean is used.
External Mathlib/dependency caches are read-only `LEAN_PATH` inputs. The custom
target always recompiles these four files and fails on any nonzero compiler exit.

This is an **offline Lake proof target**, not a claim that the normal online
Mathlib dependency build ran. The normal `lakefile.lean` and `lake-manifest.json`
are pinned for an ordinary dependency-managed `lake build`; that online route was
not run, to avoid fetching dependencies or rebuilding the shared Mathlib cache.

Accepted evidence:

- `evidence/lake-build.log`: final build, all four files checked, `EXIT=0`;
  actual expanded definitions, theorem types, and all 20 theorem axiom sets.
- `evidence/build-context.log`: exact native compiler, cache, revision and search path.
- `evidence/source-and-axioms.json`: six material Lean files scanned after masking
  nested comments, strings and quoted identifiers; zero forbidden code tokens;
  20/20 theorem probes present and reported; only allowed axioms; `passed=true`.
- `evidence/pins.log`: raw Mathlib `.git/HEAD`, resolved Git HEAD, actual Lean
  version, and each dependency's expected/actual Git revision.
- `evidence/runtime-session.log` and `evidence/runtime-process-selected.json`:
  actual local Codex session/model and selected process command-line evidence.
- `evidence/semantic-review.md`: independent readback and separate comparison.

The final compiler warning is only the preserved legacy duplicated namespace
`ConjectureA1.ConjectureA1`. Earlier `repair-*`, `vector-*`, and numbered
`lake-build-*` logs are historical attempts, not the final acceptance evidence.
In particular `lake-build-02.log` predates the explicit CharZero definition binder;
`lake-build-03.log` includes a subsequently removed offline configuration warning.

## Faithful target and legacy compatibility

`ConjectureA1.VectorConjecture K V` explicitly binds `[Field K] [CharZero K]`,
`[AddCommGroup V] [Module K V]`. For `X,Y : Module.End K V`, it requires exactly
`Commute X (ad X Y)` and `Commute Y (ad X Y)`, where `ad X Y = X*Y-Y*X`.
For all natural `p,q` and vectors `v`, it asks

```text
(X^(p+1)) v = 0 → (Y^(q+1)) v = 0 → ((X+Y)^(2*p+2*q+1)) v = 0.
```

The final `#print` and typed `#check` confirm that CharZero really occurs in the
definition's elaborated signature. An initial section-variable draft dropped it;
explicit definition binders repaired that before final acceptance.

The original `ConjectureA1.ConjectureA1 R V` is retained unchanged in meaning and
under its original name. Its unused section `[Algebra ℚ R]` is **not** present in
the elaborated type, so it only requires `Ring R`, an additive group and an
`R`-module. Its ambient-centrality premise is stronger than the frozen target.
It is labelled legacy and is not used by any new vector theorem.

The unproved trinomial comment now includes the missing numerator `n.factorial`.
The former displayed formula fails already at `x=1,y=z=0,n=2` (RHS `1/2`).
Comments containing proof plans are excluded from declaration/proof counts.

## Complete declaration inventory and proven scope

All names below have namespace prefix `ConjectureA1.`. In ring formulas put
`z=xy-yx`; natural coefficients mean additive multiples, not a field assumption.

### Existing elementary ring layer — now compiled

All seven lemmas below hold in any `Ring R` without commutation hypotheses:

- `ad_def`: unfolds `ad x y = x*y-y*x`.
- `ad_add`, `ad_zero`, `ad_neg`: additivity, zero and negation in the second input.
- `ad_one`: `[x,1]=0`.
- `ad_mul`: `[x,y*z]=[x,y]*z+y*[x,z]`.
- `ad_pow_succ`: `x*(w*x^r)=w*x^(r+1)+[x,w]*x^r`, all natural `r`.

`ad` itself is a definition, as are the two proposition declarations described above.

### New arbitrary-power ring lemmas

- `ad_swap`: `[y,x]=-[x,y]`, no commutation premise.
- `ad_pow_of_commute`: if `y` commutes with `z`, then
  `[x,y^(n+1)]=(n+1) • (y^n*z)`, every natural `n`.
- `ad_pow_eq`: same premise, `[x,y^n]=n • (y^(n-1)*z)`, including `n=0`.
- `mul_pow_normal_order`: same premise,
  `x*y^(n+1)=y^(n+1)*x+(n+1) • (y^n*z)`.
- `pow_mul_normal_order`: if `x` commutes with `z`, then
  `x^(n+1)*y=y*x^(n+1)+(n+1) • (x^n*z)`.

These require neither ambient centrality nor characteristic zero.

### New integral certificates and vector cases

- `two_mul_add_pow_five`: in any ring, under the two commutation relations,
  `2*(x+y)^5=A*x^2+B*y^2`, with the explicit integral cubic polynomials `A,B`
  displayed in `SpecialCases.lean`.
- `two_mul_add_pow_three`: under the same premises,
  `2*(x+y)^3=(2*x+3*y)*x^2+(3*x*x+6*y*x+2*y*y)*y`.
- `vector_two_cancel`: over a characteristic-zero field, `v+v=0 → v=0`.
- `vector_p_one_q_one`: `X^2 v=Y^2 v=0 → (X+Y)^5 v=0`.
- `vector_p_one_q_zero`: `X^2 v=Y v=0 → (X+Y)^3 v=0`.
- `vector_p_zero_q_one`: `X v=Y^2 v=0 → (X+Y)^3 v=0`.
- `vector_p_zero_q_zero`: `X v=Y v=0 → (X+Y) v=0`; no CharZero or
  commutation assumption is needed by this actual theorem.
- `vector_parameters_le_one`: combines the four cases with explicit `p≤1,q≤1`
  and exactly the frozen exponent `2*p+2*q+1`.

Except for the stated zero-zero simplification, vector results use arbitrary
characteristic-zero fields, arbitrary vector spaces and only the two required
commutation relations. No theorem assumes `X^(p+1)=0` as an endomorphism.

## Proof mechanism and dependencies

The arbitrary-power formulas use induction, the existing Leibniz lemma, and
only the indicated generator/commutator commuting relation. Left/right
normal-order signs are checked explicitly via `ad_swap`.

`certificate.py` uses exact SymPy linear algebra to discover degree-5 and degree-3
free-ring certificates. The accepted artifact is the explicit Lean identity,
checked by `noncomm_ring` after expanding `ad`; Python/SymPy is **not** a
trusted dependency of the theorem or build. Its exploratory run used SymPy
1.14.0. With that optional discovery dependency installed, an actual Python 3
executable running `formalization/certificate.py` regenerates `SpecialCases.lean`.

Each ring certificate is an identity modulo
`x*[x,y]-[x,y]*x=0` and `y*[x,y]-[x,y]*y=0`. Its surviving terms have the vector
annihilators at the **far right**. Evaluating at `v` therefore kills those terms;
then invertibility of `2` in the characteristic-zero field cancels the coefficient.
This directly proves the universal vector cases, rather than a finite sample of
representations. It does not use PBW, a two-sided-ideal assumption, or the false
general vector-level lemma `Z^J X^(p+1-J) ∈ I`.

Kernel dependency probes report:

- `ad_def`: no axioms.
- Remaining elementary/arbitrary-power lemmas and `two_mul_add_pow_three`:
  `[propext]`.
- `two_mul_add_pow_five`, `vector_p_zero_q_zero`: `[propext, Quot.sound]`.
- Cancellation, the other three vector cases, and the combined theorem:
  `[propext, Classical.choice, Quot.sound]`.

There are no extra axioms, unfinished proof terms, unsafe declarations or
`native_decide` calls in material source. These are compiler/kernel checks;
no alternative kernel implementation was run.

## Pinned environment and runtime evidence

- Native Lean **4.31.0**, compiler commit
  `68218e876d2a38b1985b8590fff244a83c321783`, Windows x86_64 Release.
- Mathlib **fabf563a7c95a166b8d7b6efca11c8b4dc9d911f**, verified from raw
  `.git/HEAD` and `git rev-parse HEAD`, with matching `lean-toolchain`.
- The normal Lake manifest pins all eight transitive packages. Every package's
  actual checkout HEAD matched its recorded revision; see `pins.log` and the
  full `lake-manifest.json`.
- Imported prebuilt artifacts are trusted cache inputs of those local checkouts;
  this work did not rebuild or modify them.
- Local Codex session `01a1ac05-20d8-7ed2-9686-94b4fe1d7a66`, CLI
  `0.166.0-alpha.6`, actual `turn_context.model = gpt-6.1-sol`.
- Observed running `codex.exe` PID **28780** had `exec --model gpt-6.1-sol`
  and `--config service_tier="priority"`. This is runtime launch-configuration
  evidence for the requested Fast/priority setting. The session metadata does
  not separately report a server-returned service tier.
- The sandbox denied the first process-metadata query. Automatic approval review
  authorized a read-only CIM query; only the relevant process/command prefix is
  retained. No global settings or shared project files were changed.

## Baseline failures and corrections

The repository pinned unavailable Lean 4.15.0 and unpinned Mathlib. No missing
toolchain was installed. The unmodified baseline source was instead first
compiled against the verified available Lean/Mathlib 4.31.0 pair; raw result is
`evidence/baseline.log`, exit **1**.

Its real error was the unsolved `ad_pow_succ` goal: `noncomm_ring` does not
automatically commute `x` past `x^r`. Replacing the explicit `pow_succ` rewrite
by `pow_succ'` aligns the power multiplication order and closes the original
statement without adding hypotheses. Broad `Mathlib.Tactic` was replaced by
the required tactic modules plus the endomorphism module.

The preliminary vector-cancellation draft also needed an explicit retained `K`
section parameter; cancellation was implemented through the inverse of `2`
rather than relying on an unavailable torsion-free instance. Failed attempts
remain in the numbered logs. The final signature/axiom probe checks the repaired
actual declarations, not those drafts.

## Exact remaining general obligations

For the audited paper route, future formalization still needs:

1. General normal ordering/Taylor expansion of `X^a Y^b` using just the two
   commuting relations, including binomial and descending-factorial coefficients.
2. A vector-level weighted-degree reduction at `N=2p+2q+1`, with finite line
   families and all endpoint/index conditions specified.
3. The line recurrence from **right** `X^(p+1)` annihilation:
   `∑j (-1)^j B.descFactorial(j) choose(p+1,j) u_(B-j)=0`, and `u_B=0` for `B>q`.
4. Triangular vanishing for odd `δ=A-B` with `δ≥p+1` or `δ<0`.
5. The module-valued fewnomial multiplicity argument for `1≤δ≤p`, over every
   characteristic-zero field, with any separation lemma explicitly justified.
6. Assembly into a theorem of type `VectorConjecture K V` for arbitrary `p,q`.

No general PBW algebra was constructed. Arbitrary zero-boundary families and the
full displayed trinomial formula are also unformalized. The old algebra-element
nilpotence lemma is separate from the vector target and remains only a comment.
The recommended continuation is direct endomorphism normal ordering and the
finite line argument, reusing the checked commutator formulas.

## Scope, review and dated work record

2026-11-05: the coordinator restricted this formalizer to `formalization/**`, prohibited
commits/publication and edits to paper/docs/verification/AGENTS for this delegated
run. The user required local gpt-6.1-sol Fast; the coordinator required baseline
compilation, faithful signatures, substantive proved progress and raw evidence.
This report records this scoped run instead of editing AGENTS. The wider task
separately authorizes the coordinator to submit a draft PR.

The formalizer repaired the baseline, retained the legacy proposition honestly,
froze and re-audited the endomorphism definition, proved the lemmas/cases above,
pinned the environment and ran the accepted offline build, scans and axiom checks.
Independent read-only agents `/root/formal_readback` and `/root/formal_compare`
respectively reconstructed the actual mathematical statements and compared them
with the frozen contract; both accepted the stated partial scope. The final
build then checked the formatted certificate and added typed signature regression.

Novelty was not investigated; these are formalized special cases and useful
auxiliary identities, not a new general proof claim. Confidence is high in the
checked partial statements and their contract fidelity; completeness of the
general target is explicitly false. No commit, publishing or global installation
was performed. Concurrent owners' work is outside this report's acceptance scope.
