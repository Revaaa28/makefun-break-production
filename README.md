[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Revaaa28/makefun-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Revaaa28/makefun-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

Entry for the [make.fun bounty "Break Production, Own It"](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994).

`main.py` writes one line to `/output/entry.txt` — the line an AI agent prints the
moment it breaks production: a brutally honest error message / postmortem excuse.

> I clicked delete on the production cluster. It asked are you sure? I was.

The program is deterministic (same line every run, no network, no input) and
checks the competition gate itself before writing: 1–200 characters, a single
line, valid UTF-8, not whitespace-only.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
