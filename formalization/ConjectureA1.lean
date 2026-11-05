/-
  ConjectureA1.lean
  ============================================================================
  Lean 4 + Mathlib formalisation, elementary and commutator-power layers of
  《报告_ConjectureA1的证明》 (Conjecture A.1 of Liu–Wu–Zhang–Zhou,
  Comm. Math. Phys. 375 (2020) 785–832, Appendix A).

  ⚠️  STATUS  ⚠️
  ----------------------------------------------------------------------------
  The original layer-1 file was uncompiled. The 2026-11-05 revision is compiled
  with Lean 4.31.0; see PROGRESS.md and evidence/. The file contains
      * no `sorry`,
      * no user-declared `axiom`,
      * no `unsafe` / `native_decide` shortcuts.
  General commutator-power and one-generator normal-order formulas are proved
  here. SpecialCases.lean and VectorCases.lean prove all vector cases p,q ≤ 1.
  The remaining general steps
  (Taylor expansion, the `z`-power lemma, the trinomial formula, the two-sided
  theorem, and a fortiori Conjecture A.1 itself) are recorded as **comments**
  with their exact Lean statements and proof plans — a comment is not a proof
  obligation, so nothing here is faked, and nothing is assumed.

  Neither proposition definition below is an assertion of the general conjecture.
  ============================================================================
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.NormNum

open Finset
open scoped BigOperators

namespace ConjectureA1

/-! ## 1. The inner derivation `ad` -/

section Derivation

variable {R : Type*} [Ring R]

/-- `ad x y = x * y - y * x`.  (Report's convention `[x,y] = x*y - y*x`.) -/
def ad (x y : R) : R := x * y - y * x

@[simp] lemma ad_def (x y : R) : ad x y = x * y - y * x := rfl

lemma ad_add (x y z : R) : ad x (y + z) = ad x y + ad x z := by
  unfold ad
  rw [mul_add, add_mul]
  abel

lemma ad_zero (x : R) : ad x 0 = 0 := by
  unfold ad
  simp

lemma ad_neg (x y : R) : ad x (-y) = -ad x y := by
  unfold ad
  noncomm_ring

lemma ad_one (x : R) : ad x (1 : R) = 0 := by
  unfold ad
  simp

/-- Leibniz rule: `ad x` is a derivation. -/
lemma ad_mul (x y z : R) : ad x (y * z) = ad x y * z + y * ad x z := by
  unfold ad
  noncomm_ring

/-- `ad x` is additive and a derivation; packaged form used by `taylor`. -/
lemma ad_pow_succ (x : R) (w : R) (r : ℕ) :
    x * (w * x ^ r) = w * x ^ (r + 1) + ad x w * x ^ r := by
  unfold ad
  rw [pow_succ']
  noncomm_ring

end Derivation

section CommutatorPowers

variable {R : Type*} [Ring R]

lemma ad_swap (x y : R) : ad y x = -ad x y := by
  unfold ad
  noncomm_ring

/-- Commutator with a positive power. Only Y-Z commutation is required. -/
lemma ad_pow_of_commute (x y : R) (hy : Commute y (ad x y)) (n : ℕ) :
    ad x (y ^ (n + 1)) = (n + 1) • (y ^ n * ad x y) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ad_mul, ih]
    calc
      (n + 1) • (y ^ n * ad x y) * y + y ^ (n + 1) * ad x y =
          (n + 1) • (y ^ (n + 1) * ad x y) + y ^ (n + 1) * ad x y := by
        rw [smul_mul_assoc, mul_assoc, ← hy.eq, ← mul_assoc, ← pow_succ]
      _ = (n + 1 + 1) • (y ^ (n + 1) * ad x y) := by
        simp only [add_nsmul, one_nsmul]

/-- One-X normal ordering, with the sign fixed by XY-YX=Z. -/
lemma mul_pow_normal_order (x y : R) (hy : Commute y (ad x y)) (n : ℕ) :
    x * y ^ (n + 1) = y ^ (n + 1) * x + (n + 1) • (y ^ n * ad x y) := by
  have h := ad_pow_of_commute x y hy n
  unfold ad at h
  have h' := sub_eq_iff_eq_add.mp h
  simpa only [ad, add_comm] using h'

/-- Power-commutator formula including n=0 (truncated subtraction is harmless). -/
lemma ad_pow_eq (x y : R) (hy : Commute y (ad x y)) (n : ℕ) :
    ad x (y ^ n) = n • (y ^ (n - 1) * ad x y) := by
  cases n with
  | zero => simp
  | succ n => simpa only [Nat.add_sub_cancel] using ad_pow_of_commute x y hy n

/-- Normal ordering with the power on the left. Only X-Z commutation is needed. -/
lemma pow_mul_normal_order (x y : R) (hx : Commute x (ad x y)) (n : ℕ) :
    x ^ (n + 1) * y = y * x ^ (n + 1) + (n + 1) • (x ^ n * ad x y) := by
  have hx' : Commute x (ad y x) := by rw [ad_swap]; exact hx.neg_right
  have h := mul_pow_normal_order y x hx' n
  rw [ad_swap, mul_neg, smul_neg] at h
  have h' : y * x ^ (n + 1) =
      x ^ (n + 1) * y - (n + 1) • (x ^ n * ad x y) := by
    simpa only [sub_eq_add_neg] using h
  exact (eq_sub_iff_add_eq.mp h').symm

end CommutatorPowers

/-! ## 2. Statement of the target (a `def`, hence no proof is claimed)

Legacy statement, retained under its original name for compatibility. Lean drops
the unused `Algebra ℚ R` section instance: its actual signature has only `Ring R`.
It also requires ambient centrality, stronger than commuting with X and Y.
The faithful characteristic-zero endomorphism target is `VectorConjecture` below.
-/

section Statement

variable (R V : Type*) [Ring R] [Algebra ℚ R] [AddCommGroup V] [Module R V]

/-- Legacy ring/module proposition; NOT the frozen characteristic-zero target. -/
def ConjectureA1 : Prop :=
  ∀ (x y : R) (z : R), z = ad x y → (∀ w : R, z * w = w * z) →
  ∀ (p q : ℕ) (v : V),
    (x ^ (p + 1)) • v = 0 → (y ^ (q + 1)) • v = 0 →
    ((x + y) ^ (2 * p + 2 * q + 1)) • v = 0

end Statement

section FaithfulStatement

/-- The frozen vector-level target. This declaration defines a proposition only.
No finite-dimensionality or ambient-centrality assumption is imposed. Explicit
binders retain CharZero, which an unused section instance would silently drop. -/
def VectorConjecture (K V : Type*) [Field K] [CharZero K]
    [AddCommGroup V] [Module K V] : Prop :=
  ∀ (X Y : Module.End K V),
    Commute X (ad X Y) → Commute Y (ad X Y) →
    ∀ (p q : ℕ) (v : V),
      (X ^ (p + 1)) v = 0 → (Y ^ (q + 1)) v = 0 →
      ((X + Y) ^ (2 * p + 2 * q + 1)) v = 0

end FaithfulStatement

/-! ## 3. NOT FORMALISED HERE — exact statements and proof plans

The following block lists, in Lean syntax, every lemma that the report proves and
that this file does **not** prove.  They are comments on purpose.  `形式化说明与差异.md`
gives, for each one, the effort estimate and the reason.

```
section Layer2

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Report Lemma 4.1 / Appendix A.2.  Needs `Finset.sum_range_succ` bookkeeping. -/
lemma taylor (x y : R) (n : ℕ) :
    x ^ n * y
      = ∑ j in range (n + 1), ((n.choose j : ℕ) : R) * ((ad x)^[j] y) * x ^ (n - j) := by
  -- induction on n; step:
  --   x^(n+1) * y = x * (x^n * y)
  --   = ∑_j C(n,j) * x * ((ad x)^[j] y * x^(n-j))
  --   = ∑_j C(n,j) * ((ad x)^[j] y * x^(n-j+1) + ((ad x)^[j+1] y) * x^(n-j))
  --   (uses `ad_pow_succ` above)
  -- then reindex the second sum and use Pascal: C(n,j) + C(n,j-1) = C(n+1,j).
  -- Mathlib ingredients: `Finset.sum_range_succ`, `Finset.sum_range_succ'`,
  -- `Nat.choose_succ_succ`, `Function.iterate_succ_apply'`.

/-- Report Lemma 4.1, iterated form.  Hypothesis `hxy : z = ad x y`, `hz` = centrality. -/
lemma ad_iterate_y_pow (x y z : R) (hxy : z = ad x y) (hz : ∀ w : R, z * w = w * z)
    (m j : ℕ) :
    ((ad x)^[j]) (y ^ m) = ((m.descFactorial j : ℕ) : R) * (y ^ (m - j) * z ^ j) := by
  -- induction on j; step uses `ad_y_pow` and `z*w = w*z`
  -- (`Nat.descFactorial_succ`), truncated subtraction handles `j > m`
  -- because `m.descFactorial j = 0` then.

/-- Report Lemma 4.2 "key relation" (`R(A,B,K) = (X^{A-p-1} Y^B Z^K) X^{p+1} ∈ I`),
    here in the two-sided form used by Proposition 4.5 of the report. -/
lemma z_pow_mul_x_pow (x y z : R) (hxy : z = ad x y) (hz : ∀ w : R, z * w = w * z)
    (p : ℕ) (hx : x ^ (p + 1) = 0) :
    ∀ J : ℕ, 1 ≤ J → J ≤ p + 1 → z ^ J * x ^ (p + 1 - J) = 0 := by
  -- `x^(p+1) * y^J = 0`; expand by `taylor` and `ad_iterate_y_pow`;
  -- the j = 0 term vanishes (`x^(p+1) = 0`), terms j < J by induction,
  -- leaving C(p+1,J) * J! * (z^J * x^(p+1-J)) = 0;
  -- conclude since char 0 (`Nat.cast_ne_zero` of `(p+1).choose J * J.factorial`).

/-- Report Theorem 3.1 (generalised binomial theorem / trinomial formula). -/
lemma trinomial (x y z : R) (hxy : z = ad x y) (hz : ∀ w : R, z * w = w * z) (n : ℕ) :
    (x + y) ^ n
      = ∑ k in range (n / 2 + 1), (((-1 : ℚ) ^ k * n.factorial / (2 ^ k * k.factorial) : ℚ) : R)
          * (z ^ k * ∑ ab in Finset.antidiagonal (n - 2 * k),
              ((1 : ℚ) / ((ab.1.factorial * ab.2.factorial : ℕ) : ℚ) : ℚ) * (x ^ ab.1 * y ^ ab.2)) := by
  -- induction on n via the divided-power recursion
  --   (m+1) B_{m+1} = (x+y) B_m + z B_{m-1},  B_m = ∑_{a+b=m} x^a y^b /(a! b!)
  -- which follows from `d/dt e^{tx}e^{ty} = (x+y+t z) e^{tx}e^{ty}`.

/-- Report Proposition 4.5: the **two-sided** theorem. -/
theorem two_sided (x y z : R) (hxy : z = ad x y) (hz : ∀ w : R, z * w = w * z)
    (p q : ℕ) (hx : x ^ (p + 1) = 0) (hy : y ^ (q + 1) = 0) :
    (x + y) ^ (2 * p + 2 * q + 1) = 0 := by
  -- assemble `trinomial` with the vanishing of `z^J x^(p+1-J)` and
  -- `z^J y^(q+1-J)`; see the report, Proof of Proposition 4.5.

end Layer2
```

## 4. The missing layer (why the conjecture itself is not proved here)

Conjecture A.1 is the **one-sided** statement: the hypothesis is `x^(p+1) • v = 0`
(vector level), not `x^(p+1) = 0` (element level). The report's general route uses

  (a) the Heisenberg algebra as a ring with a **PBW normal form and its grading**
      (`A = U(h₁)`, basis `X^a Y^b Z^k`, `I = A X^{p+1} + A Y^{q+1}`),
  (b) the **"line" linear-algebra argument** (triangular minors) and
  (c) the **fewnomial multiplicity bound for module-valued polynomials**
      (`Module.Dual` separation on a finitely spanned submodule).

These general constructions remain open here. The independently checked finite
ring certificates in SpecialCases.lean instead bypass PBW for p,q ≤ 1.
-/

end ConjectureA1
