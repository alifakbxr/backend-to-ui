# Install and use

## Requirements

- A repository containing the backend and related source, or accessible API contracts.
- A coding agent that can read and edit those files.
- Node.js 22.20+ and `npx` for the optional [skills CLI](https://skills.sh/docs/cli) installation flow. The skill itself has no runtime dependency.
- Browser/device tools and test credentials when realistic end-to-end verification is required; otherwise the agent must report that those checks were not run.

## Install from the published repository

From the repository where you want to build a frontend:

```bash
npx skills add alifakbxr/backend-to-ui --list
npx skills add alifakbxr/backend-to-ui --skill backend-to-ui
```

Use `-g` for a global, user-level installation. Select the agent when prompted. To target four supported coding agents explicitly:

```bash
npx skills add alifakbxr/backend-to-ui --skill backend-to-ui -g -a claude-code -a gemini-cli -a antigravity -a codex
```

The CLI supports these agent IDs according to [its agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md). If the repository owner differs from `alifakbxr`, replace it.

## Try before publishing

From the extracted repo root, run:

```bash
python3 tests/validate.py
npx skills add . --list
```

The `--list` command confirms discovery of `backend-to-ui` without installing it. To install the local version, run `npx skills add . --skill backend-to-ui`. No network is needed to read the local skill, though `npx` may need to fetch the CLI first.

## One-shot usage

Minimal:

> Use backend-to-ui to build the frontend for this backend.

Add only *real* constraints when necessary:

> Use backend-to-ui for this repository. The product serves shop cashiers on touchscreens. Keep the current design language and payment flows. Implement the checkout UI against existing backend operations, profile rendering and data requests, and test the flows.

For an existing frontend:

> Use backend-to-ui to audit and improve the current frontend. Do not change the backend contract or replace the stack. Fix the real user flows and performance bottlenecks, then verify behavior and visual quality.

## What to expect

The agent should report the backend contracts it discovered; pages and flows implemented; how permissions, loading and failures work; data/pagination/cache decisions; what was actually tested; and remaining limitations. It should not claim a Lighthouse score or live API verification without measurements.

A skill is instruction, not a guarantee of a polished application. It cannot automatically obtain credentials, synthesize missing business rules, or grant an agent capabilities absent from the environment.

## Troubleshooting

| Issue | Check |
| --- | --- |
| Skill not discovered | Verify `skills/backend-to-ui/SKILL.md`, run `npx skills add . --list`, restart or reload the agent's skill registry |
| Agent ignores the skill | Explicitly mention `backend-to-ui` in the prompt; make sure skill files are in the selected agent's search path |
| UI invents features | Require a route/permission-to-action map and reject elements without supported operations |
| UI is slow | Capture a real network trace and rendering profile; inspect `references/performance.md` before optimizing |
| Design looks generic | Identify the specific user's main task and follow the critique checklist in `references/design.md` |
| Tests require login | Provide a safe test account/fixture; do not place real credentials in the skill or repository |

## Maintenance

- Check installed versions: `npx skills list` or `npx skills ls -g`.
- Check/update: `npx skills check` and `npx skills update`.
- Source releases should be tagged and documented in `CHANGELOG.md` for reproducibility.
