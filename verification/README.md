# Exact finite verification

These scripts use Python 3.9+ standard-library integer/rational arithmetic. They
check explicitly bounded cases and algebraic identities; they do not prove
Conjecture A.1 or sharpness for arbitrary parameters.

From the repository root in PowerShell:

```powershell
$py = "C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe"
& $py verification/run_all.py
```

The runner executes every script below, saves stdout/stderr and SHA256 hashes in
`verification/audit-2026-11-05/`, and exits nonzero if a script fails or times out.
Run without `-O`: assertions are part of the checks. The checked runtime for this
audit is CPython 3.10.11. No third-party dependencies are needed.

## Mathematical setup

The convention is `XY-YX=Z`, with Z commuting with X and Y. In the PBW basis
`X^a Y^b Z^k`, degrees are `a+b+2k`. The left ideal is
`I=A X^(p+1)+A Y^(q+1)` and `M=A/I`. In each homogeneous degree d, `conj2.py`
constructs the complete spanning set of `I_d` and tests membership by exact
fraction Gaussian elimination. It never truncates X powers as if I were
two-sided. Homogeneous input with a nonzero term in the wrong degree is rejected.

## Scripts and tested domains

| Script | Exact finite scope |
| --- | --- |
| `conj2.py` | All 49 pairs `0<=p,q<=6`: the first zero of `T^n.1` is `N=2p+2q+1`, where `T=X+Y`; checks every `0<=n<=N`. |
| `conj.py` | Compatibility entry point using the same valid quotient backend, `0<=p,q<=4`; regression at `(0,1)`. The old independent truncation was invalid. |
| `verify.py` | PBW binomial identity `0<=n<=8`; Z index `p+q+1` and T index N for `0<=p,q<=4`; explicit counterexamples to discarded intermediate claims. |
| `verify2.py` | Normal ordering `p,B=0..5`; key relation `p=0..3`, `A=p+1..p+4`, `B=0..4`, `K=0..2`; full column rank for `p,q=0..4`, all parity-compatible `delta=-N..N` with unknown columns; six explicit nonempty determinant examples; support bound for `p=1..5,q=0..5,1<=delta<=p` of correct parity. |
| `sharpness.py` | Model `Q[x,eps]/(eps^(q+1))`, `X=d/dx,Y=eps*x,v=1`, `p=0,q=0..6`; coefficient `(2q)!/(2^q q!)`, first zero `2q+1`; commutator on basis monomials `i=0..3,j=0..q,q=1..3`. |
| `pureZ_check.py` | Eight listed `(p,q)` pairs: pure-Z coefficient of `Y^(p+1) Z^(q-1) X^(p+1)` in A equals `(-1)^(p+1)(p+1)!`. This says nothing by itself about nonmembership in I. |
| `structure.py` | Diagnostic quotient-dimension/monomial tables at `(1,1),(1,2),(2,2)`; no asserted general formula. |
| `probe2.py` | Diagnostic dimension tables for `p,q=0..4` and `Z^k B_m` membership tables at `(1,1),(1,2),(2,2),(2,3)`; no asserted universal threshold. |
| `audit_checks.py` | Six regression groups: runner failure/timeout propagation; refuted claims and an exact B4 certificate; homogeneous input validation; iterative versus direct PBW powers `p,q=0..3`; left stability of all ideal generators in degrees `0..8,p,q=0..2`; independent symmetric-tensor model below. |

The independent representation is `Sym^p(W*) tensor Sym^q(W)` over Q, with
`W=Q^3`, `X=E12`, `Y=E23` and the induced dual action. The vector is
`epsilon1^p tensor e3^q`. The implementation uses six-variable homogeneous
polynomials, independently of PBW elimination. It checks `[X,Y]=Z` and commuting
with Z on every basis vector for `p,q=0..3`. For `p,q=0..6`, it checks the two
annihilation hypotheses, nonzero `T^(N-1)v` with exact coefficient
`(N-1)!/2^(p+q)`, and `T^N v=0`. These are 49 finite examples, not a general proof.

## Refuted historical claims

The baseline `conj.py` treated the left ideal as two-sided. It reported index 2
at `(p,q)=(0,1)`, whereas `T^2.1=Z.1!=0` and `T^3.1=0` in the correct quotient.
Its public power function now delegates to `conj2.py`.

The baseline `verify.py` printed failures of the false one-sided lemma
`Z^J X^(p+1-J), Z^J Y^(q+1-J) in I`, yet exited 0. Importing it made
`verify2.py` print the same failures. The false lemma has been replaced by
nonmembership regressions; actual checked claims now assert success.

At `p=q=1`, `ZX,ZY,Z^2` are nonzero in M, while

```
B4 = sum_(a+b=4) X^a Y^b/(a! b!)
   = (X^2/24+XY/6+Z/3) X^2 + (X^2/4+XY/6+Y^2/24) Y^2.
```

Thus `B4 in I` even though `4<N=5`; an unconditional iff threshold for individual
`Z^k B_m` is false. The exact certificate is checked in A independently of the
quotient reduction. `T^4.1` remains nonzero, so this does not refute Conjecture A.1.

Baseline transcripts are retained as `*.baseline.txt`; they are evidence of
historical errors, not outputs of the repaired scripts. `baseline-results.json`
records all eight historical exits and printed failures. `results.json` and the
unsuffixed transcripts record the current aggregate run.
