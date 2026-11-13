# Token measurement — estimates vs AGY usage

Use **English for agent-facing reporting**. Never confuse file size, model output, active context, provider usage, or billing.

## What the skill costs

```bash
# From a clone of product-ui
python3 skills/backend-to-ui/scripts/token_report.py
python3 skills/backend-to-ui/scripts/token_report.py --json
```

The standard-library tool reports UTF-8 text characters and a coarse **characters/4 token estimate** for the entrypoint, reference files, and supporting scripts/assets. It does **not** execute AGY or contain a provider tokenizer. This is a static file-budget indicator, not a measured context load, model reasoning cost, or invoice. Files are only included in a prompt if the host loads them. Do **not** add every reference estimate to a normal task when progressive disclosure is in effect.

## Actual AGY measurement: interactive

Launch `agy`, invoke `backend-to-ui`, then run **`/context` inside AGY**. Its Context Usage panel displays loaded Skill-file counts, customization categories, active context and checkpoint metrics. Record the actual loaded `backend-to-ui` tokens from there. It can also show other rules, plugins and tool schema overhead; do not attribute them to this skill.

Documentation: https://antigravity.google/docs/cli/commands/context

## Actual AGY measurement: headless

For a dedicated, authorized experiment with the same prompt and model:

```bash
# CAUTION: this invokes the model and consumes real usage.
agy -p "Use backend-to-ui to audit this repository read-only. Do not edit." \
  --output-format json > /tmp/backend-to-ui-agy-usage.json

# Print only native token counters, not private prompts or messages.
jq '.usage' /tmp/backend-to-ui-agy-usage.json

# Summarize locally, without uploading the conversation
python3 skills/backend-to-ui/scripts/token_report.py \
  --usage-json /tmp/backend-to-ui-agy-usage.json
```

Alternatively, use `--output-format stream-json`; the **terminal** `event=="result"` contains overall `result.usage`. Do **not** sum the intermediate `step_update.usage` with the final result (double-counting risk). Native counters commonly contain `input_tokens`, `output_tokens`, `thinking_tokens`, `cache_read_tokens` and `total_tokens`. Thinking is a **part** of output, not an extra charge to add blindly.

Documentation: https://antigravity.google/docs/cli/headless/

## Real A/B experiment for this skill

Run two separate fresh-session trials from an identical project commit and data fixture, using the same model, effort, prompt, available tools and acceptance rubric.

- A: explicitly activated `backend-to-ui`, with the actual skill file/version recorded.
- B: no skill loaded, but the same functional requirements and user-approved design constraints.
- Record **total input**, cache-read, output, thinking (as an output subset), elapsed time, number of tool calls, screenshots, task success and regressions.
- Repeat runs because agent variance, cache warmup and tooling effects can outweigh a small prompt reduction.
- **Do not compare a fully QA-tested A against a B that omitted browser testing.**
- Report median/dispersion and separate *quality*, *speed*, *total tokens* and *skill-loaded tokens*. A shorter response is not evidence of better quality or lower total tokens.

Do not claim “65% savings” merely because Caveman or another skill advertises it. Caveman distinguishes terse output instructions from an optional local compression runtime; the former does not compress repository or model input. Use external compressors only when present, justified and security-reviewed. Do not automatically install Caveman or convert skill Markdown to images.

Sources:
- https://github.com/JuliusBrussee/caveman/blob/main/docs/HONEST-NUMBERS.md
- https://github.com/JuliusBrussee/caveman/blob/main/docs/technical/product-model.md
- https://antigravity.google/docs/cli/commands/context
- https://antigravity.google/docs/cli/headless/
