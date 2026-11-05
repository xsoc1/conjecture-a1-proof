# Conjecture A.1 research workspace

Audit the vector-level Heisenberg nilpotence conjecture and its proof before extending Lean.
Preserve the author's proof route and existing work. Distinguish a definition of the target,
proved auxiliary lemmas, computation, and a complete proof. Characteristic zero and the
commutator convention `XY - YX = Z` are part of the contract. Centrality means commuting
with X and Y; centrality in an arbitrary ambient ring is a stronger auxiliary assumption.

Read `docs/audit-2026-11-05/problem_contract.md` for the frozen target and
`docs/audit-2026-11-05/research_ledger.md` for current evidence and open obligations.
Run exact Python checks from `verification/`. Run the pinned Lean build from
`formalization/`; report actual build, placeholder scan, and theorem axiom checks.
Record toolchain/library pins and the precise scope of every formalized declaration.

## Current state

Baseline: `f8f7235dca197933cd97ac74b6d35d64f67e693d`, clean clone on 2026-11-05.
The corrected written main proof and all-parameter tensor sharpness construction
passed independent mathematical review; frozen hashes are in revised-paper-audit.md.
Twenty Lean lemmas/theorems compiled, including general commutator-power identities
and the original vector conclusion for all four p,q≤1 cases. Independent scratch
compilation, signature guards and axiom audits passed. The full target remains a
`def`; arbitrary parameter assembly and arbitrary zero-boundary families remain open
in Lean. Read formalization/PROGRESS.md and lean-audit-report.md before extending it.
All nine Python scripts and six regression groups pass; they check finite ranges.
The existing PDF binaries remain historical baselines; corrected TeX is authoritative
for this revision. No novelty, canonical integration, human final approval or merge
is claimed.

## Conversation and decisions — 2026-11-05

- User requested auditing Huangjw-Math/conjecture-a1-proof, strictly repairing any gaps,
  formalizing correct results with local Codex using gpt-6.1-sol and fast, and submitting a PR.
- Delegation specifies a draft PR, preserving collaborator work and never merging.
- Local default config records gpt-6.1-sol and priority; actual formalizer runtime must also
  be checked. The connected GitHub account is xsoc1 with read access to upstream.
- Initial clone used an authorized network escalation after the configured proxy was unavailable.
- Review hints about coefficients, left ideals, finite coverage, and source fidelity remain
  hypotheses until independently checked against the source and exact scripts.
- Subsequent checks confirmed and repaired both induction coefficient errors,
  left-ideal degree and false one-sided tests, vector-polynomial wording/boundaries,
  and source/application scope. See the dated ledger for exact claims and counterexamples.
- Added a separately audited tensor model proving sharpness for every p,q, rather
  than inferring it from the 49 exact cases.
- Local Codex actually ran gpt-6.1-sol with priority; the model catalog maps priority
  to Fast. There is no separate backend tier echo. Pinned Lean4.31.0/Mathlib
  fabf563a7c95a166b8d7b6efca11c8b4dc9d911f were used with read-only existing caches.
- Rebound normalized source bytes before final independent compilation. Preserve
  raw evidence byte hashes; standalone validate.py output is insufficient without
  a paired fresh build and source-bound manifest.
- Authorized delivery is a draft PR from the xsoc1 fork. Retain explicit partial
  formalization scope and unresolved general obligations; do not merge it.
