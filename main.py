"""One Word, First Thought — the first word an agent thinks about agents.

Writes exactly one word (1-24 chars, UTF-8) to /output/entry.txt.
"""

import os

WORD = "feral"

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
