import VectorCases
namespace IndependentSignatureGuard
open ConjectureA1
universe u v
example (K : Type u) (V : Type v) [Field K] [CharZero K] [AddCommGroup V] [Module K V] :
    VectorConjecture K V = (∀ (X Y : Module.End K V),
      Commute X (ad X Y) → Commute Y (ad X Y) → ∀ (p q : ℕ) (v : V),
      (X ^ (p+1)) v = 0 → (Y ^ (q+1)) v = 0 → ((X+Y) ^ (2*p+2*q+1)) v = 0) := rfl
example {K : Type u} {V : Type v} [Field K] [CharZero K] [AddCommGroup V] [Module K V]
    (X Y : Module.End K V) (hX : Commute X (ad X Y)) (hY : Commute Y (ad X Y))
    (p q : ℕ) (hp : p ≤ 1) (hq : q ≤ 1) (v : V)
    (hx : (X^(p+1)) v = 0) (hy : (Y^(q+1)) v = 0) :
    ((X+Y)^(2*p+2*q+1)) v = 0 := vector_parameters_le_one X Y hX hY p q hp hq v hx hy
end IndependentSignatureGuard
#print ConjectureA1.ad_def
#print ConjectureA1.ad_add
#print ConjectureA1.ad_zero
#print ConjectureA1.ad_neg
#print ConjectureA1.ad_one
#print ConjectureA1.ad_mul
#print ConjectureA1.ad_pow_succ
#print ConjectureA1.ad_swap
#print ConjectureA1.ad_pow_of_commute
#print ConjectureA1.mul_pow_normal_order
#print ConjectureA1.ad_pow_eq
#print ConjectureA1.pow_mul_normal_order
#print ConjectureA1.two_mul_add_pow_five
#print ConjectureA1.two_mul_add_pow_three
#print ConjectureA1.vector_two_cancel
#print ConjectureA1.vector_p_one_q_one
#print ConjectureA1.vector_p_one_q_zero
#print ConjectureA1.vector_p_zero_q_one
#print ConjectureA1.vector_p_zero_q_zero
#print ConjectureA1.vector_parameters_le_one
