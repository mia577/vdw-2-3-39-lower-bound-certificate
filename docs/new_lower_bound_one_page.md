# One-page Result: t=39 Certified Lower Bound Candidate

## Statement

The attached coloring of `[1,1420]` for `t=39` avoids:

- every 0-colored 3-term arithmetic progression;
- every 1-colored 39-term arithmetic progression.

Therefore:

```text
w(2;3,39) > 1420
w(2;3,39) >= 1421
```

## Certificate

```text
colorings/NEW_t39_n1420.txt
```

Package SHA-256 for certificate:

```text
4223895F890D61077150BDD98FC5C7AFE63A5EE6BF5A48EEDADECEDB2C4BE3CF
```

## Independent verification

Run from this package folder:

```powershell
python checker\independent_checker.py colorings\NEW_t39_n1420.txt --t 39
```

Expected output:

```text
INDEPENDENT_OK t=39 n=1420
```

## Status of the other four certificates

The package also contains independently verified lower-bound certificates for t=32,33,35,36. After the TaSSAT public-table check, these are not currently claimed as public-new records.

## Exact value status

No exact value is claimed. To prove `w(2;3,39)=1421`, one still needs an UNSAT proof for the length-1421 CNF plus independent DRAT/LRAT-class proof verification.

First upper-bound attempt: CaDiCaL 3.0.0 on the plain CNF for `N=1421` timed out after 3600 seconds with result `unknown`. This is not an UNSAT proof.
