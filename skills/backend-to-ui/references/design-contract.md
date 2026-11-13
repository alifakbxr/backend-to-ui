# Design authority and portable project contract

A skill is **a workflow, not a visual preset**. AGY, Gemini, ChatGPT, Claude and Codex should follow the *same project decisions*; they need not produce identical pixels.

## Order of authority

1. Current explicit user direction (including a requested rebrand or removal).
2. Previously **user-approved** `UI_CONTRACT.json` and approved brand guidelines.
3. Existing project tokens, components, logo, content, route flows and screenshots.
4. Product tasks, real data and domain conventions.
5. Provisional design proposals grounded in evidence.
6. Model/host aesthetic defaults: **no authority**.

If a user asks to change a previously approved look, do not resist: the current request wins. Avoid changing things outside the requested scope.

## When to create `UI_CONTRACT.json`

**Always read** an existing one before frontend edits. For read-only audits, do not write anything. For targeted fixes (bug, one component, spacing, form validation), do not force a new contract. For a new design or substantial ongoing redesign, persisting one is useful for repeatable cross-agent work; ask approval if writing it would be outside requested scope. Never place generated design files in an unrelated repository or claim the user approved a direction they have not seen.

The contract is stored in the *target project root*. [Example structure](../assets/UI_CONTRACT.example.json) is **not a UI template**. Do not copy the example's product, user, task or composition.

## Status means something

- `approved`: direction explicitly approved by the current user; must cite a `user:` source. A repo file alone cannot grant approval.
- `observed`: direction extracted from an actual existing project file, with a `file:` source. Preservation default, **not user approval**.
- `provisional`: tentative, source-labeled proposal. `inference:` sources cannot become approved without a user instruction.

Evidence entries may separately include facts and inferred assumptions; *only the direction's source* controls its approval status. Don't prohibit all inference from a reviewed project just because an unrelated statement remains uncertain.

## Design decision procedure

1. Determine the product's **actual user, activity and device**. A landing page and operations console have different tasks even for the same product.
2. Identify existing color tokens, type scales, layout conventions, logo/assets, UI copy and component contracts; list file paths, not invented brand hex codes.
3. If an existing design is established and not being replaced, preserve its recognizable identity and flow.
4. If selecting a **new** direction, compare two *structurally different* compositions. A list/detail view and an immersive full-canvas editor are different; recoloring a generic 3-column card layout is not.
5. Record the selected composition, its **dominant subject**, density, task rationale and **specific provenance**. Avoid invented user approval.
6. Implement in the already authorized stack, then inspect real rendered screenshots and interactions.
7. On negative feedback, diagnose hierarchy and structural fit first; correct the contract direction deliberately when the user requests it.

## Anti-slop diagnosis: tell → why → fix

| Tell | Why it fails | Direction for the fix |
| --- | --- | --- |
| Generic hero + stats + identical cards regardless of product | Imported marketing/dashboard shell hides the real activity | Rebuild hierarchy around the actual user task |
| Charts and KPIs with no authorized backing source | Makes fictitious data look authoritative | Remove, or derive from verified backend contracts with period/units |
| Buttons, pills or icons that never do anything | Simulates completeness without behavior | Wire real actions and meaningful empty/error/mutation states |
| Contradictory brand typography/color/spacing | Agent preferences override actual project identity | Reuse project tokens/assets and record the design source |
| Large vacant viewport around a tiny central task | Incorrect use of canvas and information density | Give the primary work the needed scale and space |
| Same section order across unrelated products | Template selection precedes product understanding | Rethink composition, content sequence and core affordances |

Cards, gradients, dark mode, bright colors, Inter or animations are **not inherently forbidden**. Judge purpose, coherence, execution, accessibility, and brand fit instead of banning a style.

## Contract validation

```bash
python3 <skill-dir>/scripts/check_contract.py --contract ./UI_CONTRACT.json --project-root .
```

The script validates **schema and provenance only**. It cannot measure originality, usability, aesthetics or adherence to brand without real screenshots and judgment. When not available, inspect the contract manually and mark validation as unverified.

## Cross-agent acceptance

Keep project git SHA, skill version, contract SHA, prompt and fixture data constant. Inspect **actual files, screenshots and user flows** from each host. The existing `evals/compare_agents.py` compares reported records and fingerprints but does not authenticate agent activation or screenshots.
