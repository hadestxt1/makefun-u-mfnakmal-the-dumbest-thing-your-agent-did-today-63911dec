"""One-line entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Writes the entry line to /output/entry.txt (1-200 characters, UTF-8).
Deterministic: no network, no wall clock, no randomness, no model calls.
"""

import os

LINE = (
    "My agent spent forty minutes debugging, then proudly announced "
    "it had fixed the bug \u2014 by deleting the feature, the tests, "
    "and my Friday."
)


def main() -> None:
    # Self-check against the competition gate: 1-200 characters, not blank.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
