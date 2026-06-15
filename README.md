# Machine-checkable lower-bound certificate for `w(2;3,39) >= 1421`

This repository contains a machine-checkable certificate for the mixed van der
Waerden number `w(2;3,39)`.

The main result certified here is:

```text
w(2;3,39) > 1420
w(2;3,39) >= 1421
```

No exact value is claimed.

## What is included

- `colorings/NEW_t39_n1420.txt`  
  A 0/1 coloring of `[1,1420]`.
- `checker/independent_checker.py`  
  A small independent Python checker that directly enumerates arithmetic
  progressions.
- `docs/`  
  Verification notes, public-record notes, and exact-value status notes.

The repository also includes four additional verified certificates for
`t = 32, 33, 35, 36`; these are included for reproducibility and comparison, not
as claimed public-new records.

## Verify the main certificate

Use Python 3.10 or newer.

```powershell
python checker\independent_checker.py colorings\NEW_t39_n1420.txt --t 39
```

Expected output:

```text
INDEPENDENT_OK t=39 n=1420
```

On macOS or Linux:

```bash
python3 checker/independent_checker.py colorings/NEW_t39_n1420.txt --t 39
```

## Verify all included certificates

```powershell
python checker\independent_checker.py colorings\NEW_t32_n1011.txt --t 32
python checker\independent_checker.py colorings\NEW_t33_n1069.txt --t 33
python checker\independent_checker.py colorings\NEW_t35_n1205.txt --t 35
python checker\independent_checker.py colorings\NEW_t36_n1259.txt --t 36
python checker\independent_checker.py colorings\NEW_t39_n1420.txt --t 39
```

## Certificate hash

SHA-256 for the main certificate:

```text
4223895F890D61077150BDD98FC5C7AFE63A5EE6BF5A48EEDADECEDB2C4BE3CF
```

## Claim discipline

This project proves only a lower bound. To prove the exact value
`w(2;3,39) = 1421`, one would also need an independently verified UNSAT proof
for the corresponding `N = 1421` instance.

## References

- B. L. van der Waerden, *Beweis einer Baudetschen Vermutung*, Nieuw Arch.
  Wiskd. 15 (1927), 212--216.
- TaSSAT TACAS-24 solve-details repository:
  <https://github.com/solimul/TACAS-24-solve_details>

