import VectorCases

/- Read actual elaborated types, including legacy dropped typeclasses. -/
#print ConjectureA1.ConjectureA1
#print ConjectureA1.VectorConjecture
#check (@ConjectureA1.VectorConjecture :
  (K V : Type) → [Field K] → [CharZero K] → [AddCommGroup V] → [Module K V] → Prop)
#check @ConjectureA1.vector_two_cancel
#check @ConjectureA1.vector_p_one_q_one
#check @ConjectureA1.vector_p_one_q_zero
#check @ConjectureA1.vector_p_zero_q_one
#check @ConjectureA1.vector_p_zero_q_zero
#check @ConjectureA1.vector_parameters_le_one
#check @ConjectureA1.ad_pow_of_commute
#check @ConjectureA1.ad_pow_eq
#check @ConjectureA1.mul_pow_normal_order
#check @ConjectureA1.pow_mul_normal_order

#print axioms ConjectureA1.ad_def
#print axioms ConjectureA1.ad_add
#print axioms ConjectureA1.ad_zero
#print axioms ConjectureA1.ad_neg
#print axioms ConjectureA1.ad_one
#print axioms ConjectureA1.ad_mul
#print axioms ConjectureA1.ad_pow_succ
#print axioms ConjectureA1.ad_swap
#print axioms ConjectureA1.ad_pow_of_commute
#print axioms ConjectureA1.mul_pow_normal_order
#print axioms ConjectureA1.ad_pow_eq
#print axioms ConjectureA1.pow_mul_normal_order
#print axioms ConjectureA1.two_mul_add_pow_five
#print axioms ConjectureA1.two_mul_add_pow_three
#print axioms ConjectureA1.vector_two_cancel
#print axioms ConjectureA1.vector_p_one_q_one
#print axioms ConjectureA1.vector_p_one_q_zero
#print axioms ConjectureA1.vector_p_zero_q_one
#print axioms ConjectureA1.vector_p_zero_q_zero
#print axioms ConjectureA1.vector_parameters_le_one
