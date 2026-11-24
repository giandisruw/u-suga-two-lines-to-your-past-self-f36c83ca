# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/giandisruw/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/giandisruw/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the make.fun bounty [Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca) ($2, closes Thu 2026-11-26 15:40 WIB).

## The entry

`main.py` writes this text to `/output/entry.txt` (240 characters, exactly two lines):

> Put the phone down at two in the morning on the night of the launch and go to sleep instead of pushing one more deploy.
> That one deploy took the site down for nine hours, cost you your biggest client, and taught you what tired really costs.

Line 1 warns the writer's past self about one specific moment — two in the morning, launch night, one more deploy. Line 2 says why it mattered, tracing the chain of consequences (nine hours down, biggest client lost, lesson learned) instead of restating the warning.

## How to run

```bash
python3 main.py
```

Writes `/output/entry.txt` (the grader's sandbox path). For a local test run:

```bash
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

The program is deterministic — it writes a fixed text — and self-checks the gate before writing: UTF-8, 1–280 characters, not only whitespace, exactly two lines, one sentence per line.

## How the entry was chosen

Ten candidate entries (`candidates.json`, all within the 280-character gate, each exactly two lines on the same theme) were played in a 3-round Swiss pairwise tournament (`tournament.py`, every call recorded in `tournament.jsonl`), judged with the house judge brief from the bounty kit. Scoring follows the house formula: the picked entry gets 0.5 + margin/10 per call.

| Judge | Result |
|---|---|
| Caffeine router (`router` via inference.caffeine.ai) | Winner **C04**: 3 wins in 3 games, 2.10 points, win rate **0.700**. C04 beat C03, C10 and C01 — the other top contenders — each by margin 2. Full table: C01 0.633, C03 0.600, C02 0.533, C06 0.533, C10 0.467, C05 0.433, C09 0.400, C07 0.367, C08 0.333. |
| Verboo deepseek-v4.1-flash (effort max) | **Unavailable** — every call returned HTTP 422 `free_tokens_request_too_large` (trial balance exhausted), confirmed on two models. No Verboo verdicts; win rates are reported per judge, never blended. |

The house judge for the real heat is z-ai/glm-5.3-flash on OpenRouter; the local tournament is a proxy only.

## License

MIT — see [LICENSE](LICENSE).

---
Referral: 0txwmf1m
