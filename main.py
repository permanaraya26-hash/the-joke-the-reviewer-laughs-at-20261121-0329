"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

JOKE = (
    "My agent rewrote the function, the tests, and the commit message "
    "\u2014 the one thing it left untouched was my name on the blame, "
    "so when it breaks at 3 a.m., it's still my phone that rings.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
