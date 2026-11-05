# Integrated proof reference

The complete corrected written proof is `report/src/report.tex`, especially
the left-ideal reduction, signed normal-order relation, three line cases, and
the final weighted-degree induction. The independent review binds its final
source hash. `report/src/techdoc.tex` gives the corrected companion exposition.

For sharpness, use the new all-parameter tensor construction in the report and
`docs/sharpness.md`; the key nonzero term is
T^(2m)v=((2m)!/2^m) ε₃^⊗p⊗e₁^⊗q, m=p+q. No finite table is used as a proof.

The main proof needs only Z commuting with X,Y. Ambient centrality and operator
annihilation are not substituted for these hypotheses. Dimension may be infinite.

This reference is a written-proof artifact. Actual Lean theorem names and their
precise limited scope are recorded in `formalization/PROGRESS.md`; the general
Lean target remains a proposition definition until all general obligations close.
