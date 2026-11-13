# Host activation and discovery — not just installed files

A successful \`npx skills add\` or \`npx skills list -g\` **does not prove** the app/CLI loaded or activated \`backend-to-ui\`. Treat these as separate checks:

1. **Installed on disk:** required \`SKILL.md\` and references are present.
2. **Discovered by the host:** it appears in the host's skill inventory, from the expected folder, without a stale higher-priority copy.
3. **Activated for the task:** invocation was accepted and the agent reads the correct \`SKILL.md\`. An observed design alone cannot prove this.
4. **Followed correctly:** the agent used the project contract, obeyed stack selection and produced verifiable implementation+QA evidence.

## Verified host locations

| Host | Global skill path | Host-side verification |
| --- | --- | --- |
| Antigravity App / IDE | \`~/.gemini/config/skills/backend-to-ui/SKILL.md\` | Customizations → Installed; \`/backend-to-ui\` |
| Antigravity CLI | Same shared global path (plus CLI-only alternate directories) | \`/skills\` then \`/skills reload\`, invoke \`/backend-to-ui\` |
| Gemini CLI | \`~/.gemini/skills/backend-to-ui/SKILL.md\` or \`~/.agents/skills/backend-to-ui/SKILL.md\` | \`/skills list\`, \`/skills reload\`, enable if disabled |
| Codex | \`~/.agents/skills/backend-to-ui/SKILL.md\` | Confirm skill inventory/invocation in current Codex session |
| Workspace (Antigravity/Gemini) | \`<project>/.agents/skills/backend-to-ui/SKILL.md\` | Check workspace trust, current directory, reload and precedence |

These paths and commands follow official host docs and can change. Workspace/extension skills can override user-level skills with the same name. Antigravity App **does not** read all Antigravity CLI-only folders; place a shared skill in \`~/.gemini/config/skills/\`.

## Install explicitly per host

\`\`\`bash
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent antigravity -g
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent gemini-cli -g
\`\`\`

Use \`npx skills add alifakbxr/product-ui --list\` to confirm source discovery.

After install, **diagnose** on disk using the repository's zero-dependency script:

\`\`\`bash
python3 skills/backend-to-ui/scripts/doctor.py --host all
python3 skills/backend-to-ui/scripts/doctor.py --host antigravity --strict
python3 skills/backend-to-ui/scripts/doctor.py --host gemini-cli --strict --json
\`\`\`

The checker compares all known candidate copies (including workspace and legacy locations), file metadata and optional comparison to the repository source. It detects stale duplicates and missing preferred paths. It **never invokes a proprietary host**, never changes your HOME, and never asserts that host activation happened. The \`--strict\` status only means **filesystem discovery checks passed**.

## If skill doesn't appear

- **Antigravity IDE/App:** verify \`~/.gemini/config/skills/backend-to-ui/SKILL.md\`, then Customizations → Installed. Other global paths may be ignored in the IDE.
- **Antigravity CLI:** run \`/skills reload\`. Run \`/skills\` to inspect the actual path and its loaded instructions.
- **Gemini CLI:** run \`/skills reload\`, then \`/skills list\`. If disabled, \`/skills enable backend-to-ui\`. Workspace skills require a trusted workspace; check \`/trust\`.
- **Multiple copies:** inspect them via \`doctor.py\`. Remove or reconcile duplicates *manually*; no automatic deletion.
- **Activates but ignores rules:** capture the exact agent/version, path, skill SHA, user prompt, contract SHA and actual diff. Report which step was omitted. Do not infer compliance from visual resemblance.

## Acceptance

Report a matrix with \`installed\`, \`host_discovered\`, \`activated\`, \`contract_used\`, and \`QA_evidence\` for each host. Mark values \`unverified\` unless actually observed. Passing \`doctor.py\` is **not** passing this full matrix.

Sources:
- https://antigravity.google/docs/skills?app=antigravity
- https://antigravity.google/docs/customization-discovery/
- https://geminicli.com/docs/cli/skills/
- https://github.com/vercel-labs/skills/blob/main/docs/agents.md
