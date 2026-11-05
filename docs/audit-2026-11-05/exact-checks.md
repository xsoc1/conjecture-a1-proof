# Exact computation audit, 2026-11-05

Coordinator update: the original signed/hash-bound review note is preserved as
`exact-checks.initial.md`. After Git line-ending normalization the coordinator
reran all nine scripts; all exited zero, with six regression groups passing.
The current result manifest below binds that final run.

Status: PASS_FINITE_CHECKS. This audit supplies exact finite evidence and refutes
specific intermediate claims. It does not prove the universal conjecture.

Baseline commit: `f8f7235dca197933cd97ac74b6d35d64f67e693d`. Initial worktree had
untracked host-provided `AGENTS.md` and the parent audit directory; no verification
source edits were present. Baseline verify.py SHA256 was
`13d2d753e15fcfef1302e93b94c16c68ae744d3ff089f59ed39ad78840167207`, and conj2.py
was `759f2b2dacc9a7df5bfbf7583eeefe379f8e913d4380ce89361e03f3b6f07c2c`.
All original script hashes are preserved in
`verification/audit-2026-11-05/baseline-source-hashes.json`.

## Reproduce

```powershell
& 'C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe' verification/run_all.py
```

Runtime: CPython 3.10.11, 64 bit Windows; standard library only. Deterministic,
exact rational/integer arithmetic; no random seeds or floating-point tests.
The runner limits each child to 180 seconds. Final aggregate exit: 0. All nine
script invocations exit 0, including six unittest regression groups. Mocked
child failures and timeouts are separately tested to force aggregate exit 1.

Current result manifest: `verification/audit-2026-11-05/results.json`.
SHA256 after the final normalized-source rerun: `7ed28e668b257a0792e2d3d6940d4cb8ce05a727e0f3b5ad3973f9dc080ccde4`.
It contains each script hash, stdout/stderr log hash, exit code and elapsed time.
Original outputs remain as `*.baseline.txt`; all eight baseline scripts exited 0,
even though verify.py printed failures for 24 of its 25 parameter pairs.
verify2.py inherited those failures as an import side effect.

## Confirmed defects and repairs

1. Original conj.py assumed both X and Y powers could be truncated. This treats a
   left ideal as two-sided and does not define the claimed module action. Its
   output at p=0,q=1 was index 2, whereas the exact quotient has T^2.1=Z.1 nonzero
   and T^3.1=0. It now delegates to the valid homogeneous quotient backend, with
   a regression comparing classes rather than arbitrary PBW representatives.
2. Original conj2.py ran only 25 pairs p,q=0..4 while README asserted 49 pairs
   p,q=0..6. The executable run now actually covers all 49 pairs and asserts that
   the first zero is N=2p+2q+1. Its previous overlarge scan bound was unnecessary.
3. Original verify.py tested the false lemma
   Z^J X^(p+1-J), Z^J Y^(q+1-J) in I. It merely printed failures and exited 0.
   It now checks explicit counterexamples to that lemma, retains the genuine
   finite identities and indices, asserts required claims, and is quiet on import.
4. verify2.py, sharpness.py and pureZ_check.py now assert their required outcomes.
   sharpness.py's unused first_zero calculation could never find a zero because
   it searched a list of nonzero indices; this is fixed and checked. Dead,
   incorrect unused operator helper functions were removed.
5. conj2.py rejected no malformed homogeneous inputs: wrong-degree nonzero terms
   were silently dropped, creating false zeros. Such inputs now raise ValueError.
   Its elimination data are correctly described as forward echelon, not reduced
   row echelon. No change to valid Gaussian elimination was required.
6. run_all.py provides meaningful aggregate exit status, reproducible logs and
   hashes. audit_checks.py independently cross-checks PBW reduction, left-ideal
   stability, the explicit counterexamples, and a polynomial representation.
   structure.py/probe2.py remain explicitly diagnostic, without universal claims.

## Exact finite domains

- Quotient T index: all 49 pairs 0<=p,q<=6, all powers 0..N. Compatibility
  entry point separately checks 25 pairs 0..4.
- PBW expansion of T^n: n=0..8. Z and T nilpotence indices: all 25 p,q=0..4;
  Z index equals p+q+1, T index equals 2p+2q+1 in these cases.
- Normal ordering: p,B=0..5. Full left multiple relation: p=0..3,
  A=p+1..p+4, B=0..4, K=0..2 (240 identities).
- Line equation matrix: p,q=0..4, each parity-compatible delta in [-N,N]
  with unknown columns; every such matrix has full column rank. Six explicit
  nonempty triangular determinants are checked, including 1440 at (2,2,-1).
  Support bound: p=1..5,q=0..5, parity-compatible 1<=delta<=p.
- One-variable eps sharpness model: p=0,q=0..6, first zero 2q+1, exact
  T^(2q).1 coefficient (2q)!/(2^q q!). Commutator identity tested on
  x^i eps^j, i=0..3,j=0..q,q=1..3.
- Pure-Z coefficient in A: the eight original listed pairs
  (1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(4,4),(5,4).
- Direct PBW versus iterative quotient action: p,q=0..3, all n=0..N.
  Left stability: all ideal generators in d=0..8,p,q=0..2 under X and Y.
- Independent polynomial model Sym^p(W*) tensor Sym^q(W), W=Q^3,
  X=E12,Y=E23,v=epsilon1^p tensor e3^q: all 49 p,q=0..6 satisfy
  X^(p+1)v=Y^(q+1)v=0, T^N v=0, and the exact top coefficient
  T^(N-1)v=((N-1)!/2^(p+q)) epsilon3^p tensor e1^q is nonzero.
  The Heisenberg commutator and both centrality relations are checked on every
  basis vector for p,q=0..3. This model is independent of PBW elimination.
- Diagnostics: structure.py uses (1,1),(1,2),(2,2); probe2.py dimensions use
  p,q=0..4 and membership tables use (1,1),(1,2),(2,2),(2,3). Precise degree
  and table ranges are printed in their retained transcripts.

## Explicit refutations

For p=q=1, ZX and ZY are nonzero in degree 3, Z^2 is nonzero in degree 4,
and T^4 is nonzero. Nevertheless the exact identity in A is

```
B4 = (X^2/24+XY/6+Z/3) X^2 + (X^2/4+XY/6+Y^2/24) Y^2,
B4 = sum_(a+b=4) X^aY^b/(a!b!).
```

Therefore B4 belongs to I in degree 4, below N=5. This refutes an unconditional
iff degree threshold for individual Z^k B_m. The identity is checked as an exact
PBW equality, independently of the quotient membership test.

## Scope and remaining obligations

No universal conjecture, universal sharpness statement, source fidelity claim,
or Lean theorem is established by these finite computations. The independent
polynomial model suggests a uniform sharpness construction, but a general
mathematical proof belongs to the separate proof audit. Baseline pure-Z
coefficient calculations do not prove nonmembership in a left ideal.

No network, escalation, approval denial or unresolved execution blocker occurred.
Edits were restricted to verification/** and this audit note; no commit was made.
