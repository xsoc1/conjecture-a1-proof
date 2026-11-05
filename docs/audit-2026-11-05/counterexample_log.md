# Counterexamples and failed claims

1. A left ideal is not two-sided: at p=q=1, X² belongs to I, but X²Y does not.
   Its degree-three span is A₁X²+A₁Y², not A₂X²+A₂Y².
2. The proposed vector-level lemma Z^J X^(p+1−J)∈I is false. ZX, ZY and Z²
   survive in M_(1,1). It cannot be imported from element-level nilpotence.
3. Z^k B_m∈I need not have 2k+m≥N. At (p,q)=(1,0), B₂=X²/2+XY+Y²/2∈I
   despite 2<3. At (1,1), an exact certificate is
   B₄=(X²/24+XY/6+Z/3)X²+(X²/4+XY/6+Y²/24)Y². It is independently expanded
   in the exact regression script. The sufficient degree direction remains true.
4. The old double-truncation computation yields index 2 at (0,1). The correct
   left quotient has T²v0=Zv0≠0 and T³v0=0. Baseline logs retain this failure.
5. The old commented Lean trinomial formula omits n!. With R=Q, x=1,y=z=0,n=2,
   its two sides are 1 and 1/2. This was a comment, not an accepted Lean theorem.
6. The positive-characteristic fewnomial obstruction is t^r−1=(t−1)^r in
   prime characteristic r. The old example t^r−t has derivative −1 and does
   not demonstrate a multiple nonzero root.

Finite checks: all 49 p,q≤6 quotient cases and independent symmetric-tensor
models passed; these searches found no counterexample to the main conjecture.
Their finite domains do not imply the general theorem. General proof evidence
is the corrected symbolic argument, with boundary/parity checks in the audit.
