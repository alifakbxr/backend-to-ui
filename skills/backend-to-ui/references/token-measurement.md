# Token measurement: estimated file budget vs actual AGY usage

**Never claim savings from shorter Markdown alone.** Concise Caveman-style output affects response tokens, not automatically tool results, repository input, reasoning or browser traces. Caveman's runtime/proxy is a separate, optional system; `backend-to-ui` does not install or require it.

## Static size (not billed tokens)

```bash
python3 skills/backend-to-ui/scripts/token_report.py
python3 skills/backend-to-ui/scripts/token_report.py --json
```

The zero-dependency reporter uses **characters / 4** to approximate text tokens. Tokenization, agent caching and loaded references differ. The "all files" estimate is a **worst-case text inventory**, not a normal session; progressive disclosure should load only relevant references.

## Actual loaded skill cost in interactive AGY

Invoke `backend-to-ui` inside `agy`, then run **`/context`**. The Context Usage panel lists Skill files and their **loaded tokens**, as well as model/tool/plugin overhead. Record the skill-file values separately from system prompts and other plugins.

Docs: https://antigravity.google/docs/cli/commands/context

## Actual whole-run AGY usage (consumes model tokens)

```bash
agy -p "Use backend-to-ui to audit this repository read-only; do not edit files." \
  --output-format json > /tmp/agy-run.json
jq '.usage' /tmp/agy-run.json
python3 skills/backend-to-ui/scripts/token_report.py --usage-json /tmp/agy-run.json
```

For `--output-format stream-json`, read the **last** `event == "result"` and its `result.usage`. Do **not** add intermediate step usage again. AGY exposes input, output, thinking, cache-read and total tokens; thinking is contained within output. These counters describe the **entire run**, not only `backend-to-ui`. The reporter prints counters only, never prompts or tool logs.

Docs: https://antigravity.google/docs/cli/headless/

## A/B measurement

For credible savings, hold project SHA, design contract, prompt, model, effort, fixtures and test acceptance constant. Compare fresh-session **skill enabled** vs **skill disabled** runs; record total input/output/cache/thinking, time, tool calls, quality, screenshots and regressions. Repeat to quantify variance. A skipped browser check or unfinished implementation invalidates quality equivalence.

Do not claim Caveman's promotional output-reduction percentage applies to this skill.

References:
- https://github.com/JuliusBrussee/caveman/blob/main/docs/HONEST-NUMBERS.md
- https://github.com/JuliusBrussee/caveman/blob/main/docs/technical/product-model.md
