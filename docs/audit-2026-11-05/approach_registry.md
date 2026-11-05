# Approach registry

| Route | Mechanism | State | Concrete outcome / gap |
|---|---|---|---|
| R-LINE | PBW weighted grading + signed line systems + fewnomial support | PROVED in corrected manuscript; frozen revised review PASS | Keeps original proof route; no theorem-strength gap found |
| R-TENSOR | Natural/contragredient K³ tensor action | PROVED in manuscript | All-parameter sharpness by one surviving multinomial term |
| R-EXACT | Rational homogeneous left-ideal row elimination | FINITE_COMPUTATIONAL_RESULT | 49 pairs p,q≤6; never a universal proof |
| R-LEAN-CERT | Integer free-ring certificates with right annihilator factors | FORMALIZED bounded cases | Four vector cases; no stronger operator annihilation assumption |
| R-LEAN-GENERAL | Direct endomorphism proof of the general line method | PARTIAL | General commutator step proved; support lemma and assembly remain |
| R-TWO-SIDED | Replace vector annihilation by element annihilation | REFUTED as route to original theorem | Stronger hypotheses do not imply the required left-ideal membership |
| R-TRUNCATE | Truncate both PBW X and Y exponents | FALSIFIED | Old conj.py returns 2 rather than 3 at (p,q)=(0,1) |
| R-Z-SYMBOL | Infer nonmembership from lowest-Z symbol or a pure-Z component | BLOCKED | Symbols may already belong to the graded ideal; component projection does not preserve membership |

Independent roles: MAIN-AUDIT audited paper math; EXACT-CHECKS repaired and ran
verification scripts; a local gpt-6.1-sol Fast process owns Lean authoring. The
coordinator owns synthesis and final source/statement review. Proof audit reports
are not self-certification of coordinator edits; frozen revised sources are
returned to the independent reviewer.
