# t=39, N=1421 Upper-Bound Proof Status

Current mathematical status:

```text
Lower bound certificate verified:
w(2;3,39) >= 1421

Upper bound proof:
not yet certified
```

To upgrade to an exact value, the CNF below must be proved UNSAT and the proof must be independently verified:

```text
exact_attempt/t39_n1421.cnf
variables: 1421
clauses: 529963
```

Installed local tools:

```text
tools_windows/bin/cadical.exe
tools_windows/bin/drat-trim.exe
tools_windows/bin/lrat-check.exe
```

Tool self-test passed on a tiny UNSAT CNF:

```text
solver_exit=20
verifier_exit=0
s VERIFIED
```

Formal attempt completed:

```text
solver: CaDiCaL 3.0.0
input:  t39_n1421.cnf
log:    t39_n1421_cadical.log
mode:   plain CNF, no symmetry breaking
time limit: 3600 seconds
result: timeout / unknown
solver exit code: 0
conflicts: 22689557
decisions: 26616029
real time: 3600.05 seconds
max resident set size: 249.71 MB
```

The partial DRAT trace produced during the timed-out run was deleted because it is not a complete proof and cannot certify anything.

Claim discipline:

```text
If CaDiCaL returns SAT:
  no upper bound; the model should be converted into a new coloring certificate.

If CaDiCaL returns UNSAT and drat-trim verifies the proof:
  CERTIFIED UPPER BOUND: w(2;3,39) <= 1421
  Combined with the lower bound: w(2;3,39) = 1421

If CaDiCaL times out or proof verification fails:
  no exact value is claimed.
```
