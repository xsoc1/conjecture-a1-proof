# Research ledger

## 2026-11-05 — inventory

Clean clone at f8f7235dca197933cd97ac74b6d35d64f67e693d. No repository AGENTS.md,
.agents, or local skills existed at baseline. Read host AGENTS.md and relevant Codex
memory summaries; no A.1-specific memory found. Host config: gpt-6.1-sol, priority.
Installed Lean versions include 4.31.0, 4.33.0-rc2, 4.34.0-rc2, 4.34.1; repository
pins 4.15.0 with an unpinned mathlib dependency. Available Python 3.10 installation
and Codex CLI 0.166.0-alpha.6. No existing checkout edits were overwritten.

## Source and mathematical audit

Read the original arXiv:1811.10137v2 Appendix A directly. The characteristic-zero,
arbitrary-dimensional vector contract matches; original special cases are p=0
or q=0, and p=q=1, with affine linking assumptions in the application.
MAIN-AUDIT reconstructed the main line proof and found local repairable errors,
not a theorem-strength missing lemma. Repaired the two induction coefficients,
commutator convention, involution terminology, left-ideal degree, ascending
induction, Vandermonde row direction/scaling, vector-polynomial scalarization,
factorial conventions and anchor bounds, and orbit summation/application scope.
Removed the false necessary degree threshold for individual Z^k B_m.

Added the all-parameter natural/contragredient K³ tensor sharpness construction.
Its unique surviving top multinomial term proves the lower bound for every p,q,
including zero parameters. The independently reviewed revised mathematical
bundle received PASS, bound to the four hashes in revised-paper-audit.md.
No novelty or first-resolution claim was made. Existing PDF binaries were not
regenerated; README identifies the corrected TeX as the revised source.

## Computation and formalization

EXACT-CHECKS first ran all eight baseline scripts and retained misleading outputs.
It repaired the old two-sided truncation, false one-sided lemma checks and swallowed
failures; added meaningful counterexample/input/failure-propagation regressions.
All nine current scripts and six regression groups passed. Quotient checks cover
all49 p,q≤6 pairs; a separate symmetric-tensor implementation checks the same49
examples and all-basis Heisenberg relations for p,q≤3. These are finite checks.

Local Codex CLI 0.166.0-alpha.6 session 01a1ac05-20d8-7ed2-9686-94b4fe1d7a66
actually ran gpt-6.1-sol. The running process used service_tier=priority; the local
model catalog identifies that tier as Fast. Server-returned tier was not available.
No persistent global model/tier setting was changed. An initial incompatible pair
of CLI sandbox flags failed before starting; the supported auto-review flag worked.

The Lean baseline failed at ad_pow_succ against the available pinned4.31 pair;
the left-power rewrite fixed it without changing its statement. The faithful
VectorConjecture uses explicit CharZero binders and local generator commutation.
The legacy definition is preserved and labelled: its unused AlgebraQ section
instance was dropped and its ambient centrality is stronger than the target.

The local formalizer proved twenty declarations, including arbitrary-power
commutator identities and all four vector cases0≤p,q≤1. Its offline Lake target
compiled all four modules, and all declaration axiom queries used only standard
propext/Classical.choice/Quot.sound. General parameter assembly and arbitrary
zero-boundary families remain OPEN in Lean. Independent scratch compilation and
statement/proof auditing are recorded in lean-audit-report.md.

## Final reproducibility preparation

Normalized source bytes to the existing Git line-ending policy before committing;
raw evidence directories explicitly preserve their recorded bytes. This changed
SpecialCases.lean only in CRLF/LF, and normalized several Python/helper files.
The independent Lean auditor's before/after guard caught the change, so the final
snapshot was re-frozen and freshly compiled. The complete Python aggregate was
rerun against normalized sources, all nine exits0; final results.json SHA256 is
7ed28e668b257a0792e2d3d6940d4cb8ce05a727e0f3b5ad3973f9dc080ccde4.
The same numerical outputs persist, with updated input hashes/timings.

The upstream head was rechecked at f8f7235 with no open PRs at that checkpoint.
Created xsoc1/conjecture-a1-proof as a verified fork via the local Git credential
helper; credentials were neither displayed nor persisted. The draft PR submission
receipt and exact audited source commit are recorded at delivery. No merge or
review-request messages were authorized or sent.
