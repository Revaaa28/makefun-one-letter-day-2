# One Letter for Your Day — `Z`

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36?ref=25wtkm1p)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](main.py)

A [make.fun](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36?ref=25wtkm1p) bounty entry: send exactly one letter, A–Z, standing for the word that describes your day. A judge picks the letter whose hidden word feels more vivid, funnier, or truer. Free to enter, $5 shared by the top letters.

## The entry

**`Z`** — the hidden word behind it is **"zombie"** (dragging through the day like a zombie) / **"zero sleep"**.

`main.py` writes exactly one byte, `Z`, to `/output/entry.txt` — no newline, no whitespace, deterministic.

## Why Z

The letter was picked by a proxy-judge tournament, not by gut feel. Twelve candidate letters were judged pairwise by Gemini `gemini-3.5-flash-lite` against the kit's published judge brief verbatim (letters only — the judge never sees the hidden words), with house scoring (picked entry gets `0.5 + margin/10` per call, both orders per game):

| Letter | Hidden word | Mean score | Games |
| ------ | ----------- | ---------- | ----- |
| **Z** | zombie / zero sleep | **0.577** | 11 |
| M | Monday | 0.568 | 11 |
| W | wrecked | 0.550 | 5 |
| G | groggy | 0.533 | 6 |
| F | Friday-feeling | 0.525 | 4 |
| J | jittery | 0.521 | 14 |
| K | knackered | 0.492 | 6 |
| P | procrastinating | 0.490 | 5 |
| N | nope | 0.468 | 11 |
| H | hangover | 0.441 | 11 |
| D | doomscrolling | 0.433 | 6 |
| Q | queasy | 0.342 | 6 |

Z and M were a hair apart (0.577 vs 0.568, head-to-head 0.5 : 0.5), so a 3-game tie-break rematch was run: **Z 0.583 : 0.417 M**. Honest caveat: only 3 of the 6 tie-break calls returned a verdict (the rest failed and scored 0.5 : 0.5), and both successful calls had Z in position A — so the tie-break margin is thin and noisy. Z is the best-supported pick on the larger 48-game sample, not a runaway winner.

Why Z reads strongest to the brief: vivid (a sharp picture of a sleepless, shambling day), funny at once, true to a real day, and the initial fits the word's sound and shape — sharper than the obvious mood letters.

## Run

```sh
python3 main.py            # writes Z to /output/entry.txt
ENTRY_OUTPUT=/tmp/e.txt python3 main.py   # local check
```

Verified: output is exactly 1 byte (`Z`), identical across runs.

## Competition

- Bounty: [One Letter for Your Day](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36?ref=25wtkm1p)
- Pot: $5 (1st $2 / 2nd $2 / 3rd $1) · entries close 2026-11-24T21:25Z
- Judge: `z-ai/glm-5.3-flash` pairwise on the published brief; blind rounds

## License

MIT — see [LICENSE](LICENSE).
