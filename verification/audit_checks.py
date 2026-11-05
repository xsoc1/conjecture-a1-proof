"""Independent exact regressions; all parameter ranges are finite."""
import unittest
import contextlib
import io
import json
import pathlib
import subprocess
import tempfile
from unittest.mock import patch
from fractions import Fraction as F
from itertools import product
from math import factorial
from conj2 import Quotient, T_powers, I_basis
from conj import T_power_on_v
from verify import X, Y, Z, one, mul, pw, add
import run_all


def poly_op(poly, terms):
    """Apply sum c*x_target*d/dx_source to six-variable monomials."""
    out = {}
    for mono, coeff in poly.items():
        for target, source, sign in terms:
            if mono[source]:
                dest = list(mono)
                dest[source] -= 1
                dest[target] += 1
                dest = tuple(dest)
                out[dest] = out.get(dest, 0) + coeff * mono[source] * sign
    return {m: c for m, c in out.items() if c}


# Sym^p(W*) tensor Sym^q(W), coordinates u1,u2,u3,v1,v2,v3.
# This is independent of PBW quotient elimination. Dual action is -transpose.
PX = [(1, 0, -1), (3, 4, 1)]
PY = [(2, 1, -1), (4, 5, 1)]
PZ = [(2, 0, -1), (3, 5, 1)]


def compositions3(n):
    return [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]


class ExactRegressions(unittest.TestCase):
    def test_runner_propagates_failure_and_timeout(self):
        # Exercise the public runner without changing the real result artifacts.
        for timeout in [False, True]:
            with tempfile.TemporaryDirectory(prefix="a1-check-runner-") as tmp:
                root = pathlib.Path(tmp)
                for name in run_all.SCRIPTS:
                    (root/name).write_text("# stub", encoding="utf-8")
                effect = (subprocess.TimeoutExpired("stub", 180) if timeout
                          else subprocess.CompletedProcess("stub", 7, "", "failure"))
                options = {"side_effect": effect} if timeout else {"return_value": effect}
                with patch.object(run_all, "__file__", str(root/"run_all.py")), \
                     patch.object(run_all.subprocess, "run", **options), \
                     contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(run_all.main(), 1)
                report = json.loads((root/"audit-2026-11-05"/"results.json").read_text())
                self.assertEqual(report["status"], "FAIL")
                self.assertEqual(len(report["results"]), len(run_all.SCRIPTS))

    def test_old_two_sided_truncation_counterexample(self):
        value = T_power_on_v(0, 1, 2)
        self.assertTrue(value)
        # Echelon reduction may choose XY rather than Z as the representative.
        self.assertFalse(Quotient(0, 1, 2).reduce(add(value, Z, -1), 2))
        self.assertEqual(T_power_on_v(0, 1, 3), {})

    def test_false_claims_and_explicit_B4_membership_certificate(self):
        Q = Quotient(1, 1, 5)
        B4 = {(a, 4-a, 0): F(1, factorial(a)*factorial(4-a)) for a in range(5)}
        left_x = {(2, 0, 0): F(1,24), (1, 1, 0): F(1,6), (0, 0, 1): F(1,3)}
        left_y = {(2, 0, 0): F(1,4), (1, 1, 0): F(1,6), (0, 2, 0): F(1,24)}
        self.assertEqual(B4, add(mul(left_x, pw(X, 2)), mul(left_y, pw(Y, 2))))
        self.assertFalse(Q.reduce(B4, 4))
        for element, degree in [(mul(Z,X),3), (mul(Z,Y),3), (pw(Z,2),4)]:
            self.assertTrue(Q.reduce(element, degree))
        self.assertTrue(Q.reduce(pw(add(X,Y),4), 4))

    def test_homogeneous_input_is_not_silently_dropped(self):
        Q = Quotient(0, 1, 3)
        with self.assertRaises(ValueError):
            Q.reduce(Z, 1)
        with self.assertRaises(ValueError):
            Quotient(-1, 0, 3)

    def test_reduced_action_agrees_with_direct_PBW_power(self):
        for p, q in product(range(4), repeat=2):
            N = 2*(p+q)+1
            Q = Quotient(p,q,N)
            values = T_powers(p,q,N)
            for n in range(N+1):
                self.assertEqual(Q.reduce(pw(add(X,Y),n),n), Q.reduce(values[n],n), (p,q,n))
        # Multiplication by X or Y preserves the actual left-ideal relations.
        for p, q in product(range(3), repeat=2):
            Q = Quotient(p,q,9)
            for d in range(9):
                for relation in I_basis(d,p,q):
                    self.assertFalse(Q.reduce(mul(X,relation),d+1), (p,q,d,'X'))
                    self.assertFalse(Q.reduce(mul(Y,relation),d+1), (p,q,d,'Y'))

    def test_independent_tensor_model(self):
        # Check Heisenberg relations on every basis vector for p,q <= 3.
        for p, q in product(range(4), repeat=2):
            for u, v in product(compositions3(p), compositions3(q)):
                state = {u+v: 1}
                xy = poly_op(poly_op(state,PY),PX)
                yx = poly_op(poly_op(state,PX),PY)
                self.assertEqual(add(xy,yx,-1),poly_op(state,PZ))
                for op in [PX,PY]:
                    self.assertEqual(poly_op(poly_op(state,PZ),op),poly_op(poly_op(state,op),PZ))
        # Independently test the annihilation and sharpness conditions in 49 cases.
        for p, q in product(range(7), repeat=2):
            state = {(p,0,0,0,0,q): 1}
            for op, count in [(PX,p+1),(PY,q+1)]:
                value = state
                for _ in range(count):
                    value = poly_op(value,op)
                self.assertFalse(value,(p,q,count))
            N = 2*(p+q)+1
            value = state
            for n in range(N+1):
                if n == N-1:
                    self.assertEqual(value, {(0,0,p,q,0,0): factorial(N-1)//2**(p+q)},(p,q))
                if n == N:
                    self.assertFalse(value,(p,q))
                value = poly_op(value,PX+PY)


if __name__ == '__main__':
    unittest.main(verbosity=2)
