"""Independent mixed-VDW coloring checker.

This file intentionally imports nothing from src/. It directly enumerates
1-based arithmetic progressions and checks the raw bit string.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_bits(path: str) -> str:
    text = Path(path).read_text(encoding="ascii")
    bits = "".join(ch for ch in text if ch in "01")
    if not bits:
        raise ValueError(f"no 0/1 bits found in {path}")
    return bits


def check(bits: str, t: int, limit: int = 20) -> dict:
    n = len(bits)
    bad_zero_3ap: list[list[int]] = []
    bad_one_tap: list[list[int]] = []

    for a in range(1, n + 1):
        max_d = (n - a) // 2
        for d in range(1, max_d + 1):
            ap = (a, a + d, a + 2 * d)
            if bits[ap[0] - 1] == "0" and bits[ap[1] - 1] == "0" and bits[ap[2] - 1] == "0":
                if len(bad_zero_3ap) < limit:
                    bad_zero_3ap.append(list(ap))

    for a in range(1, n + 1):
        max_d = (n - a) // (t - 1)
        for d in range(1, max_d + 1):
            ok = True
            ap: list[int] = []
            for j in range(t):
                pos = a + j * d
                ap.append(pos)
                if bits[pos - 1] != "1":
                    ok = False
                    break
            if ok and len(bad_one_tap) < limit:
                bad_one_tap.append(ap)

    return {
        "ok": not bad_zero_3ap and not bad_one_tap,
        "n": n,
        "t": t,
        "bad_zero_3ap_count_at_least": len(bad_zero_3ap),
        "bad_one_tap_count_at_least": len(bad_one_tap),
        "bad_zero_3ap_examples": bad_zero_3ap,
        "bad_one_tap_examples": bad_one_tap,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = check(read_bits(args.path), args.t)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    elif result["ok"]:
        print(f"INDEPENDENT_OK t={result['t']} n={result['n']}")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
