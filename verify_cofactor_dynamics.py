"""
Supplementary Verification Code for:
"Cofactor Dynamics and Pell Equations in GCD-Augmented Fibonacci Recurrences:
 The Algebraic Structure of Geometric Stabilization"

Submission ID: AIR-2026-000571 (v2)
Author: Mosab Hawarey

This script independently verifies all computational claims in the paper:
  1. Table 1: Pell equation solutions and cofactor orbit validity
  2. Table 2: Lock-in verification for odd coprime-to-3 seeds p = 1..49
  3. Theorem 8: Exhaustive uniqueness check for odd n <= 500
  4. Theorem 9: Transient termination at n = 5
  5. Theorem 9 Step 3: Explicit GCD calculation

Requirements: Python 3.8+ (no external dependencies)
"""

from math import gcd, isqrt


# --- Fibonacci and Lucas number generators ---

def fibonacci(n):
    """Return the n-th Fibonacci number (F(0)=0, F(1)=1)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    """Return the n-th Lucas number (L(0)=2, L(1)=1)."""
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# --- GCD-Fibonacci sequence ---

def gcd_fibonacci(p, length=25):
    """Compute the GCD-Fibonacci sequence C_p(n) with seeds (1, p)."""
    seq = [0, 1, p]  # 1-indexed: seq[1]=1, seq[2]=p
    for n in range(3, length + 1):
        seq.append(seq[n-1] + seq[n-2] + gcd(seq[n-1], seq[n-2]))
    return seq


# --- Verification 1: Table 1 (Pell solutions) ---

def verify_table1():
    """Verify Pell equation solutions and cofactor orbit validity (Table 1)."""
    print("=" * 70)
    print("VERIFICATION 1: Table 1 --- Pell equation solutions")
    print("=" * 70)
    print(f"{'n':>4} {'(L_2n, F_2n)':>16} {'a=(x-3)/5':>12} {'Int?':>5} {'b':>6} {'gcd':>5} {'Valid':>6}")
    print("-" * 70)

    for n in range(1, 8):
        x = lucas(2 * n)
        y = fibonacci(2 * n)

        # Verify Pell equation
        assert x * x - 5 * y * y == 4, f"Pell equation fails for n={n}"

        a_num = x - 3
        if a_num % 5 == 0:
            a = a_num // 5
            if a <= 0:
                print(f"{n:>4} ({x}, {y}){'':>8} {a:>12} {'---':>5} {'---':>6} {'---':>5} {'---':>6}")
                continue

            k_numer = 3 * a + 1
            k_sq_disc = (5 * a + 1) * (a + 1)
            sq = isqrt(k_sq_disc)
            k = (k_numer + sq) // (2 * a)

            b = a * (k - 1) - 1
            g = gcd(a, b)
            valid = "\u2713" if g == 1 else "\u2717"

            print(f"{n:>4} ({x}, {y}){'':>8} {a:>12} {'Yes':>5} {b:>6} {g:>5} {valid:>6}")
        else:
            print(f"{n:>4} ({x}, {y}){'':>8} {a_num}/5{'':>6} {'No':>5} {'---':>6} {'---':>5} {'---':>6}")

    print()


# --- Verification 2: Table 2 (Lock-in for odd coprime-to-3 seeds) ---

def verify_table2():
    """Verify lock-in at n=5 for odd seeds coprime to 3 (Table 2)."""
    print("=" * 70)
    print("VERIFICATION 2: Table 2 --- Lock-in for odd coprime-to-3 seeds")
    print("=" * 70)
    print(f"{'p':>4} {'C(5)':>10} {'C(6)':>10} {'d=p+2':>8} {'Cofactors':>12} {'Lock-in':>8}")
    print("-" * 70)

    seeds = [p for p in range(1, 50, 2) if gcd(p, 3) == 1]
    all_pass = True

    for p in seeds:
        seq = gcd_fibonacci(p, 10)
        c5, c6 = seq[5], seq[6]
        d = p + 2
        cof_a = c5 // d
        cof_b = c6 // d
        ok = (c5 == 3 * d and c6 == 5 * d and cof_a == 3 and cof_b == 5)
        if not ok:
            all_pass = False
        status = "n=5 \u2713" if ok else "FAIL"
        print(f"{p:>4} {c5:>10} {c6:>10} {d:>8} ({cof_a},{cof_b}){'':>5} {status:>8}")

    print(f"\nAll seeds pass: {all_pass}")
    print()


# --- Verification 3: Theorem 8 uniqueness (extended to n <= 500) ---

def verify_theorem8(max_n=500):
    """Exhaustive uniqueness check for the (3,5) attractor as period-2 orbit."""
    print("=" * 70)
    print(f"VERIFICATION 3: Theorem 8 --- Uniqueness check (odd n \u2264 {max_n})")
    print("=" * 70)
    print("Checking all Pell solutions for coprime period-2 cofactor orbits...")
    print()

    valid_orbits = []
    integer_solutions = []

    for n in range(1, max_n + 1, 2):  # odd n only
        x = lucas(2 * n)
        y = fibonacci(2 * n)

        # Verify Pell equation holds
        assert x * x - 5 * y * y == 4, f"Pell fails at n={n}"

        a_num = x - 3
        if a_num % 5 != 0:
            continue

        a = a_num // 5
        if a < 2:
            continue

        # Compute discriminant and k
        disc = (5 * a + 1) * (a + 1)
        sq = isqrt(disc)
        if sq * sq != disc:
            continue

        # Both roots
        k_plus = (3 * a + 1 + sq) // (2 * a)
        k_minus = (3 * a + 1 - sq) // (2 * a)

        for k in [k_plus, k_minus]:
            if k < 2:
                continue
            b = a * (k - 1) - 1
            if b < 2:
                continue

            # Verify orbit equation: a(k^2 - 3k + 1) = k
            if a * (k * k - 3 * k + 1) != k:
                continue

            g = gcd(a, b)
            integer_solutions.append((n, a, b, k, g))

            if g == 1:
                valid_orbits.append((n, a, b, k))
                print(f"  n={n}: a={a}, b={b}, k={k}, gcd={g} --- VALID coprime period-2 orbit")
            elif n <= 21:
                print(f"  n={n}: a={a}, b={b}, k={k}, gcd={g} --- integer solution, NOT coprime")

    print(f"\nTotal odd n checked: {(max_n + 1) // 2}")
    print(f"Integer solutions satisfying orbit equation: {len(integer_solutions)}")
    print(f"Coprime period-2 orbits found: {len(valid_orbits)}")

    if len(valid_orbits) == 1 and valid_orbits[0] == (3, 3, 5, 3):
        print("CONFIRMED: (3,5) with k=3 is the UNIQUE coprime period-2 orbit.")
    else:
        print("WARNING: Unexpected result --- review solutions above.")

    print()


# --- Verification 4: Theorem 9 transient termination ---

def verify_theorem9():
    """Verify the transient cofactor evolution step by step."""
    print("=" * 70)
    print("VERIFICATION 4: Theorem 9 --- Transient termination")
    print("=" * 70)

    test_seeds = [7, 11, 13, 17, 23, 25, 29, 37, 41, 43, 47]

    for p in test_seeds:
        seq = gcd_fibonacci(p, 10)

        # Check Fibonacci coefficients in transient
        # C(3)=p+2, C(4)=2p+3, C(5)=3(p+2), C(6)=5(p+2)
        assert seq[3] == p + 2, f"p={p}: C(3) mismatch"
        assert seq[4] == 2 * p + 3, f"p={p}: C(4) mismatch"
        assert seq[5] == 3 * (p + 2), f"p={p}: C(5) mismatch"
        assert seq[6] == 5 * (p + 2), f"p={p}: C(6) mismatch"

        # Verify cofactors at n=5
        d = gcd(seq[5], seq[6])
        assert d == p + 2, f"p={p}: scale factor mismatch"
        assert seq[5] // d == 3 and seq[6] // d == 5, f"p={p}: cofactor mismatch"

        # Verify geometric lock-in continues
        assert seq[7] == 9 * (p + 2), f"p={p}: C(7) should be 9(p+2)"
        assert seq[8] == 15 * (p + 2), f"p={p}: C(8) should be 15(p+2) -- actually {seq[8]} vs {15*(p+2)}"

    print(f"  All {len(test_seeds)} test seeds verified: transient terminates at n=5")
    print(f"  Cofactor pair (3,5) reached with scale factor d = p+2")
    print(f"  Geometric lock-in confirmed through n=8")
    print()


# --- Verification 5: Theorem 9 Step 3 explicit GCD ---

def verify_theorem9_step3():
    """Verify the explicit GCD calculation gcd(2p+3, p+2) = gcd(-1, p+2) = 1."""
    print("=" * 70)
    print("VERIFICATION 5: Theorem 9 Step 3 --- Explicit GCD")
    print("=" * 70)

    for p in range(1, 100, 2):
        if gcd(p, 3) != 1:
            continue
        g = gcd(2 * p + 3, p + 2)
        assert g == 1, f"p={p}: gcd(2p+3, p+2) = {g} \u2260 1"

        # Also verify: gcd(2p+3 - 2(p+2), p+2) = gcd(-1, p+2) = 1
        assert gcd(2 * p + 3 - 2 * (p + 2), p + 2) == 1

    print("  gcd(2p+3, p+2) = 1 verified for all odd p coprime to 3, p \u2264 99")
    print("  Intermediate: gcd(2p+3 \u2212 2(p+2), p+2) = gcd(\u22121, p+2) = 1 \u2713")
    print()


# --- Main ---

if __name__ == "__main__":
    print()
    print("Supplementary Verification Code")
    print("AIR-2026-000571 v2: Cofactor Dynamics and Pell Equations")
    print("Author: Mosab Hawarey")
    print()

    verify_table1()
    verify_table2()
    verify_theorem8(max_n=500)
    verify_theorem9()
    verify_theorem9_step3()

    print("=" * 70)
    print("ALL VERIFICATIONS COMPLETE")
    print("=" * 70)
