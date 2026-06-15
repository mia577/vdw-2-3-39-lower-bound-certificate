# TaSSAT-aware Public Record Check

Checked date: 2026-05-24

## New source found

- TaSSAT paper/details repository: https://github.com/solimul/TACAS-24-solve_details
- The repository contains `vdw_solve_details/` with TaSSAT-LiWeT and TaSSAT-ProbSAT-LiWeT runs.
- The public directory lists SAT certificates/results for t=31..39, including entries such as:
  - `passat-Green-31-952-SAT`
  - `passat-Green-32-1010-SAT`
  - `passat-Green-33-1070-SAT`
  - `passat-Green-35-1207...`
  - `passat-Green-36-1260...`
  - `passat-Green-37-1340-SAT`
  - `passat-Green-38-1379-SAT`
  - `passat-Green-39-1418-SAT`

## Effect on our five certificates

All five local certificates remain valid lower-bound certificates because independent checking passed.

Public-new status after the TaSSAT check:

| t | our certified n | TaSSAT public table status | public-new status |
|---:|---:|---|---|
| 32 | 1011 | TaSSAT has an updated result in the 31-39 block; compare exact convention/table before claiming. | not claimed |
| 33 | 1069 | TaSSAT table appears to reach 1070. | covered / not claimed |
| 35 | 1205 | TaSSAT table appears to reach 1207. | covered / not claimed |
| 36 | 1259 | TaSSAT table appears to reach 1260. | covered / not claimed |
| 39 | 1420 | TaSSAT table appears to list 1418. | candidate public improvement |

## Conservative conclusion

- Keep all five as machine-verified lower-bound certificates.
- For public-new/result-page wording, feature only t=39 for now:
  - `w(2;3,39) > 1420`, hence `w(2;3,39) >= 1421`.
- Do not claim exact value without an UNSAT proof for N=1421 and independent proof verification.
