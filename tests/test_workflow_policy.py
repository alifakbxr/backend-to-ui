#!/usr/bin/env python3
"""Static workflow-contract tests; do not claim a subagent/browser was executed."""
from __future__ import annotations
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/backend-to-ui"
def read(path): return (SKILL / path).read_text(encoding="utf-8").lower()

class LeanWorkflowPolicyTests(unittest.TestCase):
    def test_skill_is_progressively_disclosed(self):
        skill = read("SKILL.md")
        self.assertLess(len(skill), 9000)
        for name in ("lean-workflow.md", "parallel-work.md", "live-browser.md"):
            self.assertIn(name, skill)
        self.assertIn("progressive disclosure", skill)

    def test_subagents_require_explicit_user_opt_in(self):
        skill = read("SKILL.md")
        policy = read("references/parallel-work.md")
        self.assertIn("explicit opt-in", skill)
        self.assertIn("never invoke a subagent", policy)
        self.assertIn("increase total tokens", policy)
        self.assertIn("if declined", skill)
        self.assertIn("single-agent", policy)
        self.assertIn("main agent integrates and owns qa", policy)
        self.assertIn("at least", policy)

    def test_live_browser_qa_has_real_execution_contract(self):
        skill = read("SKILL.md")
        protocol = read("references/live-browser.md")
        for required in ("playwright", "devtools", "console", "network", "mobile", "unverified"):
            self.assertIn(required, skill + protocol)
        self.assertIn("actual live browser", skill)
        self.assertIn("real browser", protocol)
        self.assertIn("not call an interface", protocol)
        self.assertIn("no browser tool is available", protocol)

    def test_small_fixes_do_not_force_json(self):
        skill = read("SKILL.md")
        contract = read("references/design-contract.md")
        lean = read("references/lean-workflow.md")
        self.assertIn("small fix", skill)
        self.assertIn("do not force", contract)
        self.assertIn("targeted fix", lean)
        self.assertIn("focus", lean)

    def test_no_claimed_cross_agent_validation(self):
        host = read("references/host-compatibility.md")
        self.assertIn("does not", host)
        self.assertIn("agy", host)
        self.assertIn("antigravity-cli", host)

if __name__ == "__main__":
    unittest.main()
