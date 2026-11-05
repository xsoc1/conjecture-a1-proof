RIGOROUS_PARTIAL_RESULT

# Result

## Exact theorem or result proved

The corrected written proof establishes Conjecture A.1 over every
characteristic-zero field and arbitrary-dimensional vector space, with exactly
the original local commutation and vector-annihilation hypotheses. A separate
tensor construction proves that the exponent 2p+2q+1 is necessary for each pair
of nonnegative p,q. The frozen mathematical bundle passed independent review.

The Lean result is partial: twenty declarations, including arbitrary-power
commutator/one-generator normal-order formulas and the original vector conclusion
for all four p,q∈{0,1} cases, with exponents1,3,3,5. The full general target is
faithfully stated but not proved in Lean. Arbitrary p=0 or q=0 families are also
not fully formalized. Do not promote these restricted theorems to the general result.

## Proof or construction

The main paper retains the author's weighted-degree/line-system method. Corrected
normal ordering supplies legal left-ideal relations. Two triangular cases and a
fewnomial support lemma kill all odd-difference degree-N lines, then left stability
propagates the degree cutoff. The vector-polynomial step now explicitly scalarizes
on the finite coefficient span and uses valid module cancellation.

For sharpness, use the diagonal Heisenberg action on (K³*)^⊗p⊗(K³)^⊗q and
v=ε₁^⊗p⊗e₃^⊗q. The sole surviving top multinomial term is
T^(2m)v=((2m)!/2^m)ε₃^⊗p⊗e₁^⊗q≠0, m=p+q. The empty tensor covers m=0.
The finite Lean cases use exact free-ring certificates with vector annihilators
on the right, followed by characteristic-zero cancellation of2. No stronger
operator-nilpotence or ambient-centrality assumption is substituted.

## Verification performed

- Original arXiv Appendix A read directly; exact contract and affine application
  scope checked. The final revised paper/source bundle received independent PASS.
- All nine exact Python scripts and six regression groups passed, including49
  quotient pairs p,q≤6 and an independent symmetric-tensor implementation. False
  historical claims have explicit regression counterexamples; finite tests remain finite.
- Lean4.31.0 and pinned Mathlib/dependencies: offline Lake target compiled four
  modules. A separate auditor freshly compiled frozen copies in a clean scratch
  directory, independently restated signatures, checked all twenty obligations,
  expanded both integer certificates and queried every theorem's axioms.
- No unfinished proof terms or disallowed axiom tokens. Observed axioms are only
  the reported subsets of propext, Classical.choice and Quot.sound.
- Final source normalization was detected by the hash guard; the snapshot was
  rebound and all four modules plus the signature guard freshly recompiled.

## Remaining gaps

The general normal-order sums, line/fewnomial machinery and assembly into a theorem
of type VectorConjecture remain unformalized, as does the general sharpness model.
Ordinary online dependency-managed lake build and full Mathlib source rebuild were
not run; verified existing prebuilt dependency caches are trusted inputs. Existing
PDF binaries were not regenerated; README points to corrected TeX and audit records.
Human final semantic approval and expert novelty review are not claimed; the draft
PR supplies the requested reviewable artifact. No permission action remains pending.

## Failed and blocked routes

The baseline double-X/Y truncation was invalid for the left quotient. The false
single-sided z-power lemma and necessary threshold for Z^k B_m were removed.
The baseline Lean ad_pow_succ failed compilation and was repaired with the correct
power multiplication orientation. Historical failed logs remain labelled as such.
The two-sided-element theorem is not used as a proof of the vector target.

## Novelty status

UNKNOWN / INDEPENDENT_REDISCOVERY_POSSIBLE. Limited primary-source retrieval did
not establish a later exact solution or priority. Correctness is separate from novelty.

## Human/model/tool contributions

The collaborator authored the original report and route. The user requested audit,
repair, local Codex gpt-6.1-sol Fast and a PR. The parent supplied review leads and
the tensor-model idea; these were independently verified before use. The coordinator
repaired/integrated the manuscript and documentation. Separate proof and exact-check
agents audited mathematics and computations. A local Codex process authored Lean;
separate fresh-context agents audited its signatures/proofs and a separate auditor
compiled final frozen copies. No model-generated report alone substitutes for kernel
checking. Actual model/tier evidence is retained, with no server tier echo claimed.

## Reproducibility manifest

See repro_manifest.md, revised-paper-audit.md, lean-audit-report.md and
lean-audit/run-manifest.json; exact Python inputs/logs are bound by
verification/audit-2026-11-05/results.json. Git submission provenance is appended
after committing the audited source package. No canonical knowledge base exists;
transaction/integration status is not conflated with research status.

## Confidence by axis

- Semantic fidelity: high for the written target and precisely restricted Lean statements.
- Mathematical correctness: high after independent proof/certificate audits.
- Completeness: written theorem and sharpness complete; general Lean formalization incomplete.
- Novelty: unknown.
- Reproducibility: pinned versions, actual logs and final source-bound independent builds;
  trusted prebuilt imports and unrun online/PDF paths are explicit limits.
