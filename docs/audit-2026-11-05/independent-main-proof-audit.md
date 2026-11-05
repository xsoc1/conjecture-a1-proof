# Independent audit of the main vector-level proof

RIGOROUS_PARTIAL_RESULT

## Scope, inputs, and verdict

- Subgoal: `MAIN-AUDIT`; independent mathematical verifier, not the author or formalizer.
- Frozen paper: `report/src/report.tex`, baseline commit `f8f7235dca197933cd97ac74b6d35d64f67e693d`, SHA-256 `073781b42f874e31b47f440d6df2da59772e659946b4afc02b89eda7e560f2b8`.
- Contract: `docs/audit-2026-11-05/problem_contract.md`; characteristic-zero field, arbitrary vector space, `XY-YX=Z`, `XZ=ZX`, `YZ=ZY`, vector annihilation only.
- Read `AGENTS.md` and the rigorous-open-math-research skill. No source file was edited by this verifier. No commit was made, as the delegated task explicitly forbids it.
- **Verdict on the submitted text: `REPAIRABLE_GAP`; status `PARTIAL`.** The main line-system method is mathematically sound. I found no theorem-strength missing lemma or counterexample to its conclusion. Local corrections below make the argument complete; the frozen paper is not a clean PASS because it contains false displayed equalities and a mistyped justification involving vector polynomials.
- This audit does not certify Lean, original-source fidelity, novelty, or the application to every folding situation. A separately supplied tensor construction for universal sharpness is audited below; it is not part of the frozen paper. This report makes no global completion claim.

## First error

The earliest false assertion in reading order is at baseline lines 103–104: `YX=Z-XY` is said to be an equivalent commutator convention after replacing `Y,Z` by their negatives. It is instead the anticommutator relation `XY+YX=Z`. The stated simultaneous sign change preserves this anticommutator relation and does not turn it into `XY-YX=Z`.

The first false displayed equality in a dependency actually used by the main line-system proof is the normal-order induction coefficient at baseline line 322: the second contribution must carry `(-1)^j`, not `(-1)^(j-1)`. The lemma's statement is correct and its proof has a one-sign repair. The earlier trinomial induction also has a false coefficient, but the line-system proof needs only homogeneity of `(X+Y)^N` and does not depend on that formula.

## Main obligations independently checked

### Universal module and left ideal

The action map from the presented Heisenberg algebra to `End_K(V)` exists under exactly the contract hypotheses. The image of `Z` need only commute with the images of `X,Y`; centrality in the whole ambient endomorphism ring is not required. An element of `AX^(p+1)+AY^(q+1)` annihilates the distinguished vector. Conversely, `A/I` is a left module satisfying the hypotheses, so the universal membership formulation is faithful. There is no right multiplication of a left-ideal membership assertion in this reduction.

The weighted grading is compatible with all defining relations. PBW applies to the three-dimensional Heisenberg Lie algebra with the stated bracket; even the spanning part suffices for the degree-vanishing argument. The proof of `A_(n+1)=X A_n+Y A_n` correctly handles the pure `Z^K` monomials using `Z=XY-YX`. Consequently vanishing of degree `N` propagates to all higher degrees by left ideal closure.

### Normal ordering and line relations

The formula

`Y^B X^n = sum_j (-1)^j (B!/(B-j)!) binom(n,j) X^(n-j) Y^(B-j) Z^j`

is correct. In its induction, the second predecessor has both its original `(-1)^(j-1)` and the additional minus from `Y X^(n-j+1)`. Their product is `(-1)^j`. With this correction the next displayed bracket and the desired recurrence follow. Multiplication by `X^(A-p-1) Z^K` is on the left throughout, giving exactly the stated line relation. All nonzero diagonal coefficients later used are nonzero characteristic-zero integers.

For a degree-`N` monomial, `delta=A-B`, `M=(N-delta)/2`, and `b=B` are integral, and the legal interval is `max(0,-delta)<=b<=M`. Relations are available at `b>=max(p+1-delta,0)` and `b<=M`. These anchors are legal PBW monomials: in particular `p+1-delta> -delta` for negative `delta`. Setting illegal classes to zero is harmless because every nonzero-coefficient summand in a legal relation actually has nonnegative exponents. Classes with `b>=q+1` vanish by left multiplication of `Y^(q+1)` with central `Z` moved to the left.

### Positive and negative triangular cases

For `delta>=p+1`, anchors `b=0,...,D` exist, and the unknown coefficient matrix is lower triangular with diagonal 1. This argument is valid for vector-valued unknowns: scalar inversion or recursive substitution gives zero vectors.

For `delta<=-1`, write `d=|delta|`. If `d>q`, no unknown remains. Otherwise the unknowns are `u_d,...,u_q`, and the anchors are `b=p+1+d+i`, `0<=i<=q-d`. Because `delta` is odd, `d>=1` is odd and `M=p+q+(1+d)/2>=p+q+1`; the last anchor `p+q+1` is available. With unknown index `j=c-d`, the coefficient is zero for `i>j` and the diagonal is `(-1)^(p+1) b!/c!`, nonzero. Thus the upper triangular argument is correct, including the one-unknown boundary.

### Fewnomial and vector-polynomial argument

The scalar fewnomial lemma is correct over every characteristic-zero field. Scale the variable by the nonzero root to reduce to 1; no translation is needed. The falling-factorial evaluation matrix is invertible because its determinant is the Vandermonde product of distinct nonnegative integer exponents.

The vector-polynomial lemma is also true. Here is a precise local justification of its two compressed steps. Put `U=sum_(b=0)^D u_b t^b/b!` and `H=(1-t)^(p+1) U` in the polynomial module `W[t]`. Define the summand coefficient to be zero when `j>b`. Then `coeff_b(H)=r_b/b!`. The assumed zero coefficient interval leaves at most

`b0 + max(0,D+p+1-M)`

possible nonzero coefficients. If `U` is nonzero, work in the finite-dimensional span of its coefficients and choose a coordinate functional `lambda` with `lambda(U)` nonzero. Then `lambda(H)=(1-t)^(p+1) lambda(U)` is a nonzero scalar polynomial. It has at most `p+1` terms but a root of multiplicity at least `p+1` at 1, contradicting the scalar lemma. Hence `U=0`. Alternatively, after proving `H=0`, use its constant coefficient, then successive coefficients, to obtain `u_0=u_1=...=0`. This is cancellation in a polynomial module; it does not assert that `W[t]` is an integral domain.

For `1<=delta<=p`, `delta` is odd, `D=q`, and

`M-b0 = q+(delta-1)/2 >= 0`.

Thus the lemma's anchor hypothesis `0<=b0<=M` does hold. Also `D+p+1-M=(delta+1)/2>0`, and the number of possible coefficients is

`p+1-delta+(delta+1)/2 = p+1-(delta-1)/2 <= p+1`.

All hypotheses therefore fit simultaneously. No unproved surjectivity, finite dimension assumption on `V`, or computation-to-theorem inference occurs here.

### Parity and boundaries

Since `N=2p+2q+1` is odd and `N-delta=2(B+K)`, every relevant `delta` is odd. In particular zero is impossible, so the three cases exhaust the lines. For `p=0` the middle case is empty; for `q=0` the negative case has no unknowns, and the other two cases remain valid. At `p=q=0`, `N=1` and the two degree-one generators belong to `I`. The zero vector and zero vector space require no additional step. All systems use finitely many vectors, so there is no dimension restriction.

## Exact errors and repair hints in the submitted text

Line numbers refer to the frozen hash, not future edits.

1. **Lines 103–104, statement error, adjacent:** the asserted alternative `YX=Z-XY` is an anticommutator relation, not an equivalent commutator sign convention. Delete it or replace the alternative with `YX=XY+Z` under the explicit alternative convention `Z=YX-XY`.
2. **Line 166, statement error, adjacent:** `X->X,Y->-Y,Z->-Z` is an involutive automorphism, not an antiautomorphism. For an antiautomorphism with `X->X,Y->-Y`, one needs `Z->Z`. The map is unused in the main proof.
3. **Lines 221–226, dependency/forward-reference issue:** the two preceding propositions establish that all-degree monomial membership is sufficient for the conjecture, not the displayed equivalence. The stronger monomial theorem is established later independently. Replace this early corollary with a sufficient criterion, or label the equivalence as a consequence of the later theorem. This does not obstruct the main proof.
4. **Line 252, proof error, auxiliary:** for predecessor `(A+1,B,K-1)`, the contribution is `-(A+1)n!/((A+1)! B! (K-1)!)(-1/2)^(K-1)`, equivalently `-n!/(A! B! (K-1)!)(-1/2)^(K-1)`. The printed extra factor `A` is false. At `n=1,A=B=0,K=1` it incorrectly gives zero instead of `-Z`. The identity's statement and the BCH derivation are correct.
5. **Line 322, proof error, main dependency:** replace the second `(-1)^(j-1)` with `(-1)^j`, or insert the missing minus before that term. The next displayed expression already assumes this correction. At `B=1,n=1,j=1`, the printed expression gives 0 whereas the required coefficient in `Y^2 X` is `-2`.
6. **Line 363, grading typo, adjacent:** the displayed degree-three subspace is `A_1 X^2+A_1 Y^2`, not `A_2 X^2+A_2 Y^2`. With `A_1`, the stated span and counterexample `X^2Y notin I` are correct.
7. **Line 380, induction direction, adjacent:** the two-sided proof uses ascending induction in `J` because terms `j<J` have already vanished, despite the wording saying descending induction. Its conclusion is otherwise correct for operator/element annihilation under its stronger assumptions. It is not imported into the vector-level proof.
8. **Lines 484,487, cosmetic precision:** use scaling alone to reduce the root to 1; translation need not preserve term count. With rows ordered by increasing derivative degree, the monic polynomial change from power rows is unit lower triangular, not upper triangular. The determinant argument remains valid.
9. **Lines 492–510, boundary convention, main proof:** explicitly require integral `D,M,b0` in their intended nonnegative ranges and set the factorial-ratio coefficient to zero for `j>b`. A negative factorial is undefined, even when the corresponding vector is zero. This convention was supplied for the preceding line-system formula, but should be repeated in the standalone lemma.
10. **Line 512, coefficient wording typo, main proof:** the coefficient of `t^b` is `r_b/b!`; multiplying the coefficient by `b!` yields `r_b`. It is not obtained by dividing that coefficient by `b!`.
11. **Lines 519–523, proof/type precision, main proof:** justify `lambda(H)!=0` from `lambda(U)!=0` using the scalar product identity, and replace the integral-domain justification for vector-polynomial cancellation by scalarization or coefficient recursion as given above. The required conclusion is true, with a local repair only.
12. **Lines 531–539, omitted hypothesis check, main proof:** add `M-b0=q+(delta-1)/2>=0` when applying the vector-polynomial lemma. The inequality follows immediately but is a hypothesis of the cited lemma.
13. **Lines 135–136,290–291,629–643, sharpness scope:** the stated proposition is finite (`p,q<=6`) and explicitly described as computation. It does not prove sharpness for every fixed pair of nonnegative integers. Preserve that finite scope unless a separate universal construction is proved. The sentence suggesting the affine subcases admit a smaller exponent conflicts with the stated sharpness at `p=q=1` (which requires exponent 5) unless an additional restricted class of representations is specified and proved.
14. **Numerical-check item (6), line 738, false assertion:** `Z^k B_m in I iff 2k+m>=N` is false. Take `p=1,q=0,k=0,m=2`, `N=3`. Then `B_2=X^2/2+XY+Y^2/2` belongs to `AX^2+AY` term by term, although its degree is 2. Only the sufficient direction follows from the main theorem. This error also invalidates claims that all the listed intermediate assertions passed literally. It does not affect the proof, which never needs necessity for `Z^k B_m`.

## Separate bounded audit: tensor construction for sharpness

After the frozen-proof audit, the coordinator supplied a new proposed construction. This section audits only that construction, not an unseen revised manuscript. **Verdict for the construction: PASS; mathematical status PROVED.**

Let `W=K^3`, with matrix units acting on column basis vectors, and let the Heisenberg generators act naturally by `x=E12`, `y=E23`, `z=E13`. Then `[x,y]=z` and `[x,z]=[y,z]=0`. On the dual use the contragredient Lie action `D(a)=-a^T`. It is a Lie representation because `[D(a),D(b)]=D([a,b])`. Explicitly, the dual commutator is `[-E21,-E32]=-E31`, which is the dual action of `z`; centrality is preserved.

On `V=(W*)^(tensor p) tensor W^(tensor q)`, give each generator its diagonal Lie action: a sum of its action on individual factors. Operators on different factors commute, so the diagonal operators still satisfy `[X,Y]=Z` and commute with `Z`. Put `v=epsilon_1^(tensor p) tensor e_3^(tensor q)` and `m=p+q`.

On a dual factor, `X epsilon_1=-epsilon_2`, `X^2 epsilon_1=0`, and `Y epsilon_1=0`. On a natural factor, `X e_3=0`, `Y e_3=e_2`, and `Y^2 e_3=0`. Multinomial expansion therefore gives `X^(p+1)v=Y^(q+1)v=0` by the pigeonhole principle, including either zero parameter.

For `T=X+Y=sum_i T_i`, each factor operator satisfies `T_i^3=0`, while `T_i^2 epsilon_1=epsilon_3` on the dual and `T_i^2 e_3=e_1` on the natural module. In the multinomial expansion of `T^(2m)v`, a nonzero summand has every factor exponent at most 2. Since the total is `2m`, every exponent must equal 2. Thus

`T^(2m)v = ((2m)!/2^m) epsilon_3^(tensor p) tensor e_1^(tensor q) != 0`.

The pure tensor on the right is nonzero over every field, and the coefficient is nonzero in characteristic zero. The same expansion gives `T^(2m+1)=0` on this entire tensor module. Since one zero earlier power on `v` would force `T^(2m)v=0`, all earlier nonnegative powers on `v` are nonzero. This proves the exact lower bound `2p+2q+1` for every pair, with no finite-test inference.

Likewise each factor `Z_i` has square zero; `Z_i epsilon_1=-epsilon_3` on a dual factor and `Z_i e_3=e_1` on a natural factor. Hence

`Z^m v=(-1)^p m! epsilon_3^(tensor p) tensor e_1^(tensor q) != 0`, and `Z^(m+1)=0`.

For `m=0`, use the empty tensor `V=K`, `v=1`, and zero operators. The displayed zeroth-power formulas give 1 and the first powers vanish, exactly as required.

The universal module maps to the cyclic submodule generated by this `v`. Therefore the nonvanishing lower bounds hold in `M_(p,q)`. The main degree theorem gives the corresponding upper bound for `T` on the universal module and kills `Z^(m+1)v_0`; centrality then kills `Z^(m+1)` on every `a v_0`. Thus, conditional only on the locally corrected main upper-bound proof, both universal exact indices follow for all pairs. No claim is made here that the new construction has already been written correctly into the revised shared source.

## Supporting computation and limits

I ran a fresh exact Python check using Python 3.10 at `C:\Users\HuangZY\AppData\Local\Programs\Python\Python310\python.exe`, with `fractions.Fraction` and the inspected `Quotient`/`basis_degree` helpers from `verification/conj2.py`. It checked all 3,136 degree-`N` PBW monomials for `0<=p,q<=6`: each reduced to zero. A separate integer-arithmetic loop checked legal anchors and the support inequality for all 18,522 nonempty odd-delta lines with `0<=p,q<=20`. It also confirmed `B_2=0` and `Z!=0` in `M_(1,0)`.

The quotient helper was inspected for left-ideal generator placement and exact row reduction. These are finite consistency checks, not the reason for accepting the symbolic proof. Other agents were editing verification scripts concurrently; these executed checks supplement the frozen-paper audit and are not claimed to be runs of the untouched baseline. The paper's SHA-256 was checked again after the analysis and still matched the frozen input.

## Remaining obligations and confidence

- Apply the local repairs and independently re-read the resulting source before assigning PASS to a repaired artifact. This verifier did not mutate shared sources.
- Independently verify the source-paper contract, folded-Serre application hypotheses, literature/novelty claims, and formalization in their assigned tasks. They are outside this scoped verdict.
- Semantic fidelity to the frozen contract: high. Main mathematical mechanism: high. Baseline text completeness: requires the local repairs above. Universal sharpness: the separately supplied tensor construction passes the mathematical audit above. Lean verification: not performed by this verifier. Reproducibility: input hash and exact finite ranges recorded; no service-tier inference beyond runtime evidence.
