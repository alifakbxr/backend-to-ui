# AGY / Antigravity and legacy Gemini CLI — discovery vs activation

**Use the right executable.** Antigravity CLI is `agy`. It does **not** support the shell command `agy skills list --all`; use `/skills` and `/skills reload` **inside interactive AGY**. A missing `gemini` binary does not mean `agy` is broken. Do not install legacy Gemini CLI just to use AGY.

An installer completion message is not proof of agent activation. Four independent stages: **installed on disk → discovered in host → activated for task → instructions followed**. Report the latter stages `unverified` without real host evidence.

## Install (explicit agent target)

```bash
# AGY / Antigravity CLI
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent antigravity-cli -g -y
# Antigravity IDE if used
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent antigravity -g -y
```

AGY and the IDE share the preferred global path:
`~/.gemini/config/skills/backend-to-ui/SKILL.md`

Workspace skills live at `<workspace>/.agents/skills/backend-to-ui/SKILL.md`. AGY also accepts CLI-only locations `~/.gemini/antigravity-cli/skills/` and `~/.gemini/skills/`. The IDE supports `~/.gemini/antigravity/skills/` as a legacy path; don't assume CLI-only locations apply to the IDE.

**The universal `~/.agents/skills/backend-to-ui` global alias is not the documented AGY global path.** A generic installer choosing only that path is not proof of discovery.

## Verify on disk, then inside the host

From a clone of `product-ui`:

```bash
python3 skills/backend-to-ui/scripts/doctor.py --host antigravity-cli --strict
python3 skills/backend-to-ui/scripts/doctor.py --host antigravity --strict
```

Open `agy` and, in the interactive UI, run:

```text
/skills reload
/skills
/backend-to-ui
```

Check the loaded version and content, not just skill name. In Antigravity IDE, inspect Customizations and invoke `/backend-to-ui`. The CLI slash command list may need `/skills reload` after installation.

If absent, confirm explicit `--agent antigravity-cli`, the global path, current workspace, higher-precedence `.agents/skills/` copies and stale metadata. The read-only doctor locates files, compares hashes and flags conflicts; it does not launch AGY or verify activation.

## Optional legacy Gemini CLI

Only if the user actually runs `gemini`, install explicitly:

```bash
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent gemini-cli -g -y
python3 skills/backend-to-ui/scripts/doctor.py --host gemini-cli --strict
```

Gemini CLI recognizes `~/.gemini/skills/` and `~/.agents/skills/` and uses interactive `/skills list` and `/skills reload`. These are separate host commands, not aliases of `agy skills list`.

## Optional swarm/agent parallelism

AGY documents interactive `/swarm <task>` and plan-dependent `/teamwork <task>`. **Do not execute either without explicit opt-in** and first confirm the current AGY session exposes the command. See [parallel-work.md](parallel-work.md) for scope, cost and integration rules. Other hosts may expose different tools or none.

## Diagnostic report semantics

`doctor.py --strict` fails for missing expected files or malformed/stale conflicting copies. It can warn about legacy duplicates. Report separate statuses for `installed_on_disk`, `host_discovered`, `activated` and `instructions_followed`. Unobserved stages are `unverified`.

Sources:
- https://antigravity.google/docs/skills?app=antigravity
- https://antigravity.google/docs/customization-discovery?tab=cli
- https://antigravity.google/docs/cli/reference
- https://geminicli.com/docs/cli/skills/
- https://github.com/vercel-labs/skills/blob/main/docs/agents.md
