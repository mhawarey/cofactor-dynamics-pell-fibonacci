# CofactorDynamics-Pell-Fibonacci

**Supplementary Verification Code** for the paper:

> **Cofactor Dynamics and Pell Equations in GCD-Augmented Fibonacci Recurrences: The Algebraic Structure of Geometric Stabilization**
>
> Mosab Hawarey
>
> *AIR Journal of Mathematics and Computational Sciences*, Vol. 2026
>
> Article ID: AIRMCS2026571 &nbsp;|&nbsp; DOI: [10.65737/AIRMCS2026571](https://doi.org/10.65737/AIRMCS2026571)

## Overview

This repository contains a self-contained Python script that independently verifies all computational claims in the paper:

| Verification | Description |
|---|---|
| **Table 1** | Pell equation solutions (x² − 5y² = 4) and cofactor orbit validity |
| **Table 2** | Lock-in at n = 5 for odd seeds coprime to 3 (p = 1, 5, 7, …, 49) |
| **Theorem 8** | Exhaustive uniqueness of the (3, 5) coprime period-2 orbit for all odd n ≤ 500 |
| **Theorem 9** | Transient termination — cofactor pair (3, 5) reached by step n = 5 |
| **Theorem 9, Step 3** | Explicit GCD: gcd(2p + 3, p + 2) = 1 for all valid seeds |

## Requirements

- **Python 3.8+**
- No external dependencies (uses only `math.gcd` and `math.isqrt`)

## Usage

```bash
python verify_cofactor_dynamics.py
```

All five verification suites run automatically and print `ALL VERIFICATIONS COMPLETE` on success.

## Paper Abstract

We investigate the algebraic structure underlying geometric stabilization in GCD-augmented Fibonacci recurrences C_p(n) = C_p(n−1) + C_p(n−2) + gcd(C_p(n−1), C_p(n−2)), resolving Open Problem 4 from Hawarey (2026). The binary operation f(a, b) = a + b + gcd(a, b) admits the cofactor factorization f(a, b) = gcd(a, b) · (α + β + 1), decomposing the recurrence into scale factor dynamics and a cofactor map T(α, β) = (β, α + β + 1). We prove that the cofactor pair (3, 5) is the unique coprime period-2 orbit by reducing the existence question to the generalized Pell equation x² − 5y² = 4, whose solutions are parameterized by Lucas and Fibonacci numbers.

## Citation

```bibtex
@article{hawarey2026cofactor,
  title   = {Cofactor Dynamics and Pell Equations in GCD-Augmented Fibonacci Recurrences:
             The Algebraic Structure of Geometric Stabilization},
  author  = {Hawarey, Mosab},
  journal = {AIR Journal of Mathematics and Computational Sciences},
  year    = {2026},
  doi     = {10.65737/AIRMCS2026571}
}
```

## License

This code is released under the [MIT License](LICENSE).

## Author

**Mosab Hawarey** — [GitHub](https://github.com/mhawarey) · [Geospatial Research](mailto:director@geospatial.ch)
