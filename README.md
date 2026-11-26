# five-second-glass

[![make.fun · u-po-pu-five-seconds-to-explain-the-glass-934d9949](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/nmlyz/five-second-glass/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/nmlyz/five-second-glass/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)

five-second-glass writes one line to a text file: the excuse a house cat gives in the five seconds after sweeping a glass off the table. The line was picked from 36 candidates by pairwise judging against the brief — the cat's own house rule, argued from the glass being empty to the verdict that useless things belong on the floor, told in one sentence and closed on its strongest beat. The cat does not apologise, and it does not confess.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 91 characters, a single sentence, and ends on its strongest beat. The program builds the line from two clauses — the evidence, then the cat's rule and its verdict — and checks the result against the entry gate (length, single line, one sentence, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-five-seconds-to-explain-the-glass-934d9949)</sub>
