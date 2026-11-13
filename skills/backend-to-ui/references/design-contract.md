# Project design contract — cross-agent source of truth

**Purpose:** ensure Codex, Claude Code, Gemini CLI, ChatGPT, and Antigravity do not replace a project's identity with model-specific taste. A shared, versioned \`UI_CONTRACT.json\` lives at the **target project's root**, not inside this skill repository. Its contents are project-specific. The bundled example is only a **schema illustration**, never a palette, layout, or UI template.

## Precedence, in order

1. Explicit **current user request** (including deliberate redesign and constraints).
2. Previously **reviewed project contract** that the user has accepted.
3. Real existing brand assets, UI tokens, components and behavior in the project.
4. Evidence from product documents, domain content, workflows and users.
5. Research and established task-specific UX patterns.
6. Agent or model defaults: **never a source of visual authority**.

If sources conflict, explain the conflict and update the contract after the user's explicit direction. Don't silently average two identities together. A project with no established brand can use a **provisional direction**; disclose it and retain the contract so later agents reuse the same recorded decisions. Never label inferred directions "approved".

## Workflow

1. **Read before writing UI code.** Use the existing \`UI_CONTRACT.json\` if one exists. For existing projects without it, inspect component library, tokens, app shell, routes, real data and screenshots; source an initial contract from those observations. This is *adoption*, not an automatic rebrand.
2. **Honor frontend stack choice gate first.** No new UI files or contract writing until the stack is explicitly selected or reuse authorized. Read-only audit may inspect the contract without editing.
3. **Record concise data** matching [example contract](../assets/UI_CONTRACT.example.json):
   - Product: name, surface mode, primary user and task.
   - Frontend: selected stack and confirmation method.
   - Design: status (\`approved\` or \`provisional\`), provenance, the dominant subject, density, composition and precise, project-grounded visual decisions.
   - Preservation: concrete routes, components, state, permission-sensitive flows.
   - Options: two distinct compositions considered when choosing a **new** direction. If an approved composition already exists, reuse it; don't regenerate two alternatives on every turn.
   - Evidence: specific sources for factual and aesthetic decisions (file path, current user instruction, or labeled inference).
4. **Validate** using \`python3 <skill-dir>/scripts/check_contract.py --contract <project>/UI_CONTRACT.json --project-root <project>\`. File-backed references must stay inside the project; \`inference:\` sources require provisional status.
5. **Apply** contract to the target UI. Never treat the example's aesthetics as defaults. Don't replace existing framework or make a parallel app.
6. **Review** desktop/mobile renders and working flows. The JSON validator checks *structure and provenance*, not beauty. A human/browser-based review remains essential.

## Anti-slop decisions that must be justified

- What is the first meaningful user action? Where is it visible?
- Why does this composition fit *this* domain and device?
- What visual material is native to this product? Does art genuinely help?
- Is blank space giving attention or hiding an undersized task?
- Is every number anchored to real data and an actual decision?
- Does content density serve reading, operating, playing, exploring or creating?
- Could a stranger swap the logo and reuse the page as another product? If so, revisit composition.

Use **Tell → Why → Fix** for specific problems. Avoid global "no cards/no gradients/no Inter" rules; these could damage legitimate existing brands.

## Deterministic versus subjective checks

**Machine-checkable:** contract schema, explicit source provenance, missing required fields, unresolved composition, references outside root, and whether a purportedly approved contract cites an inference.

**Requires actual agent/browser QA:** visual originality, usable proportions, interaction clarity, contrast rendering, touch behavior, animation performance and task completion. Never label these passed from a lint result alone.

**Cross-agent repeatability protocol:** reuse the **same git commit + same UI_CONTRACT.json SHA**, same target repo/data fixtures, same prompt and same acceptance criteria across host runs. Compare screenshots and actual diffs; report model-specific deviations instead of hiding them.
