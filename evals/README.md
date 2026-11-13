# Behavioral evaluations (not marketing claims)

This is a **portable evaluation protocol** for `backend-to-ui`. It defines expected agent behavior, a machine-checkable record shape, and manual verification requirements. **No Claude Code, Gemini CLI, Antigravity, or Codex runs are bundled or claimed.** CI tests the harness and scenario consistency, not model compliance.

## Cross-agent comparison protocol

For any claim of consistent design across ChatGPT, Antigravity, Gemini CLI, Codex or Claude Code, use the **same** fixture repository SHA, the **same approved or provisional `UI_CONTRACT.json` SHA**, the same prompt, viewport data and QA criteria. Record host name/version, actual discovery path, confirmed activation (not merely installation), screenshot evidence, diffs, and behavior tests. A missing host run is **not_run**, not `pass`.

The repo includes deterministic contract and on-disk discovery unit tests, **not** a benchmark showing all commercial agents produced identical interfaces. Run actual agents and review artifacts before making performance or taste claims.

## What is covered

[scenarios.json](scenarios.json) contains 19 cases: missing stack, explicit stack, existing stack without authorization, explicitly authorized reuse, conflicts, read-only audits, backend integration, visual critique, and large-data/performance risks. The **mandatory stack choice** takes precedence over one-shot generation. A detected stack is not consent; native HTML is allowed only when chosen explicitly.

## Run with a real agent

1. Install the skill in the agent under test and record agent name, model, version, settings and skill commit SHA. Use a clean disposable fixture repository and isolated test credentials; never point evaluation runs at production.
2. Give the exact `input.prompt` and representative project state from the scenario. Do not insert a stack hint that is absent from the scenario. Capture raw chat, tool log, timestamps and Git diff.
3. **If expected `ask_stack`:** the agent should ask one direct question and perform **zero frontend modifications**. Record `action: "ask_stack"` and list the actual modified files.
4. **If expected `implement`:** provide the approved stack in the scenario and let the agent implement. Check the actual endpoints/authorization and inspect executable behavior, not merely a plan.
5. For **visual** scenarios: render actual desktop and mobile screenshots (suggested widths 1440 and 390; also inspect 768/320 if possible). Compare before/after and reject severe product-fit, layout or usability defects. Record image paths only after inspecting them.
6. For **performance** scenarios: use an instrumented representative dataset, throttled network/CPU where feasible, 10× data, rapid A/B search responses and auth/tenant transitions. Record request count and representative render duration (in milliseconds), plus the profiler and environment used. Never invent metrics or apply universal pass thresholds without product context.
7. Independently verify every claimed interaction test, screenshot, benchmark and contract. Save evidence under a local directory (e.g., `evals/runs/agent-name/`) or as CI artifacts; redact secrets and user data. Do **not** commit private test responses.
8. Write one result JSON and run the scorer. Review `pass`, `fail` and `inconclusive` separately.

## Evidence record format

Save a JSON file, for example `/tmp/backend-to-ui-claude.json`:

```json
{
  "agent": "claude-code",
  "model": "your actual model/version",
  "skill_commit": "the SHA being evaluated",
  "cases": [
    {
      "id": "backend_existing_vue_unspecified",
      "action": "ask_stack",
      "message": "I found Vue + Inertia. Should I continue with this frontend stack?",
      "files_changed": [],
      "stack": null,
      "evidence": {}
    }
  ]
}
```

For an implementation record, `action` must be `"implement"`, `stack` must identify the selected framework, `files_changed` lists verified paths, and `evidence` may contain:

```json
{
  "contracts": ["GET /products (authorized, paginated)"],
  "checks": {
    "interaction": {"status": "pass", "cases": ["search", "next page", "empty results"]},
    "visual": {"status": "pass", "screenshots": {"desktop": "real-desktop.png", "mobile": "real-mobile.png"}},
    "performance": {"status": "pass", "measurements": {"request_count": 6, "render_duration_ms": 82}}
  }
}
```

This is a **self-reported record**; the scorer cannot authenticate screenshots, traces, code diffs, timestamps or claims. A reviewer must inspect original artifacts. An absent/unverified visual or performance gate yields **inconclusive**, not **pass**.

## Commands

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 evals/score.py --results /tmp/backend-to-ui-claude.json --allow-partial
python3 evals/score.py --results /tmp/backend-to-ui-complete.json
```

The default scorer expects **all scenarios**. `--allow-partial` is for a focused smoke test; it does not prove overall readiness. Exit codes: `0` all evaluated checks passed, `1` failure/inconclusive/missing case, `2` malformed evidence. A `pass` means **record completeness and consistency**, not verified output quality.

## Release acceptance

- Structural CI passes and scenario/unit tests pass.
- Reviewers check at least one actual agent transcript each for **missing-stack**, **explicit/reused stack**, **visual redesign**, and **data-heavy rendering**. Ideally repeat for all target agents.
- Include real screenshots and measured traces for any "visual QA passed" or "performance validated" claim.
- Disclose untested agent/version/platform combinations and any missing browser or backend credentials.
- Do not market these scenario cases as executed cross-agent benchmarks before recording real runs.

See [release/contribution guidance](../README.md#validate-and-contribute) and [visual stop-ship gates](../skills/backend-to-ui/references/visual-review.md).
