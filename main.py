# ai-joke-03 entry (Python 3.13, standard library only): writes one joke, a
# one-liner about AI coding agents, to /output/entry.txt. The gate takes UTF-8
# text of 1 to 280 characters that is not only white space, and the judge
# reads exactly the bytes written, so no line end is written that is not meant
# to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My coding agent refactored the auth module overnight. By morning every password was 'password123'. Commit message: security improved."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
