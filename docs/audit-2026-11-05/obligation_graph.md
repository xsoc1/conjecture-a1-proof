# Proof obligations

| ID | Exact obligation | Dependencies | Evidence/status |
|---|---|---|---|
| C0 | Original characteristic-zero vector contract, all p,q≥0 | Original Appendix A | Source checked; problem_contract.md |
| M1 | Universal left-ideal reduction and homogeneous spanning | Heisenberg relations; PBW background | Audited symbolic argument |
| M2 | Signed normal-order identity and legal line relations | M1; ascending induction | Local sign repaired; independently audited |
| M3 | All degree-N lines vanish for δ≥p+1 | M2; lower triangular diagonal 1 | Symbolic proof; finite consistency checks separately |
| M4 | All degree-N lines vanish for δ≤−1 | M2; upper triangular nonzero diagonal | Symbolic proof; legal anchors and empty cases checked |
| M5 | Scalar fewnomial multiplicity bound | Falling-factorial/Vandermonde determinant | Scaling and row direction repaired |
| M6 | Vector-polynomial support lemma | M5; finite coefficient-span coordinate functional | Scalarization and module cancellation made explicit |
| M7 | Middle lines 1≤δ≤p vanish | M2,M6; M−b0=q+(δ−1)/2≥0 | Symbolic proof |
| M8 | Degree-N cutoff and all greater degrees | M3,M4,M7; odd parity; left stability | Main upper bound |
| M9 | Conjecture A.1 | C0,M1,M8 | Complete corrected written proof; not a complete Lean proof |
| S1 | Explicit tensor representation satisfies all hypotheses | Natural and contragredient K³ actions | Independently audited general construction |
| S2 | T^(2p+2q)v≠0 and Z^(p+q)v≠0 | S1; commuting-factor multinomial identity | General lower bounds, including empty tensor |
| S3 | Pairwise optimality for every p,q | M9,S2 | Complete corrected written proof |
| F1 | General faithful Lean proposition | C0 | Defines a proposition; does not prove M9 |
| F2 | General commutator/one-X normal-order lemmas | Ring identities; local commutation | Local Codex formalization; see PROGRESS.md |
| F3 | Lean vector cases (0,0),(1,0),(0,1),(1,1) | Exact noncommutative certificates; characteristic-zero cancellation | Local Codex compiled; final independent audit recorded separately |
| F4 | Lean general M3–M8 and tensor S1–S2 | General parameter induction/polynomial infrastructure | OPEN |

The root conjecture is in the audited written-proof closure. It is not in the
Lean proof closure while F4 is open. No canonical research knowledge base is
present, and no canonical integration or merge is claimed.
