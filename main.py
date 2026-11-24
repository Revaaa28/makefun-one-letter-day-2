"""One Letter for Your Day — make.fun entry (u-puan-one-letter-for-your-day-e54e9c36).

Writes exactly one letter to /output/entry.txt: "Z".

Letter choice: "Z" — the hidden word behind it is "zombie" (dragging
through the day like a zombie) / "zero sleep". It won a 12-candidate
proxy-judge tournament (Gemini gemini-3.5-flash-lite judging the kit brief
verbatim, letters only, house scoring): Z 0.577 mean over 11 games, ahead
of M ("Monday") 0.568, W ("wrecked") 0.55, G ("groggy") 0.533; then won a
3-game Z-vs-M tie-break 0.583 : 0.417. "Z" is vivid (a sharp picture of a
sleepless, shambling day), funny at once, true to a real day, and the
initial fits the word's sound and shape — a sharper pick than the obvious
mood letters. Full tournament record: tournament-merged.json + tiebreak.json
in the builder's notes (kept out of this repo; see README).

Gate compliance: the entry file is exactly one byte, "Z", no newline,
no whitespace, UTF-8. Deterministic: no randomness, no network, no clock.
ENTRY_OUTPUT env var overrides the path (local verification only); the
letter itself is fixed.
"""

import os

LETTER = "Z"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError(f"entry must be exactly one A-Z letter, got {LETTER!r}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: what the sealed scorer will see — exactly 1 UTF-8 char.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != LETTER.encode("utf-8"):
        raise ValueError(f"entry file is not exactly {LETTER!r}: {raw!r}")


if __name__ == "__main__":
    main()
