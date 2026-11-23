#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? - make.fun entry.

Writes the honest count of open browser tabs, digits only, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

COUNT = 47
# Why 47: a real tab-hoarder count. High enough to surprise (nobody
# guesses "forty-seven tabs" for a normal afternoon), odd and non-round
# so it reads as counted, not picked — the kind of number you only get
# from actually looking at the tab bar and sighing. Believable for a
# person who researches in bursts and never closes anything "just in
# case": a few work docs, a dozen half-read articles, shopping tabs,
# videos to watch later, and the three tabs that have been open so long
# nobody remembers what they were for.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(str(COUNT))


if __name__ == "__main__":
    main()
