#!/usr/bin/env python3
"""Offline language, specificity and token-budget regressions. No agent runs."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/backend-to-ui"


def load_script(name: str):
    p = SKILL / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], p)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


tokens = load_script("token_report.py")


class LanguageAndQualityTests(unittest.TestCase):
    def text(self, path: str) -> str:
        return (SKILL / path).read_text(encoding="utf-8")

    def test_all_skill_prompts_in_english(self):
        core = self.text("SKILL.md")
        parallel = self.text("references/parallel-work.md")
        for value in ("Mau saya", "Gunakan subagent", "atau tetap satu agent", "agar beberapa pekerjaan"):
            self.assertNotIn(value, core + parallel)
        self.assertIn("English for all", core)
        self.assertIn("application ui's locale", core.lower())

    def test_no_concurrent_questions(self):
        core = self.text("SKILL.md").lower()
        parallel = self.text("references/parallel-work.md").lower()
        self.assertIn("never display it alongside", core)
        self.assertIn("do not", parallel)
        self.assertIn("the same turn", parallel)

    def test_no_unjustified_framework_bundle(self):
        core = self.text("SKILL.md")
        selection = self.text("references/stack-selection.md")
        self.assertIn("Next.js", core)
        self.assertIn("CSS", selection)
        self.assertIn("Three.js", selection)
        self.assertIn("minimum viable stack", selection.lower())

    def test_domain_specific_3d_card_qa(self):
        cases = self.text("references/cases.md").lower()
        review = self.text("references/visual-review.md").lower()
        for val in ("3d trading card", "physical trading card", "reduced-motion"):
            self.assertIn(val, cases)
        self.assertIn("product specificity check", review)

    def test_no_mandatory_caveman_install(self):
        lean = self.text("references/lean-workflow.md").lower()
        self.assertIn("do not install caveman", lean)
        self.assertIn("shorter replies", lean)


class BudgetTests(unittest.TestCase):
    def test_char_based_estimate_is_labeled(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("abcdefgh")
            (root / "references").mkdir()
            (root / "references/demo.md").write_text("abcd")
            report = tokens.file_report(root)
            self.assertEqual(report["core"]["estimated_tokens_chars_div_4"], 2)
            self.assertEqual(report["references"]["estimated_tokens_chars_div_4"], 1)
            self.assertIn("NOT", report["warning"])

    def test_accurate_agy_terminal_fields_without_double_counting(self):
        data = {
            "event": "result",
            "result": {"status": "SUCCESS", "usage": {
                "input_tokens": 100, "output_tokens": 60, "thinking_tokens": 35,
                "cache_read_tokens": 70, "total_tokens": 160,
            }},
        }
        out = tokens.usage_from_agy(json.dumps(data))
        self.assertEqual(out["usage"]["total_tokens"], 160)
        self.assertEqual(out["usage"]["output_tokens"], 60)
        self.assertIn("NOT", out["warning"])

    def test_ndjson_only_terminal_result(self):
        step = {"event": "step_update", "step_update": {
            "usage": {"input_tokens": 999, "output_tokens": 999}}}
        result = {"event": "result", "result": {"usage": {
            "input_tokens": 25, "output_tokens": 10, "thinking_tokens": 5,
            "cache_read_tokens": 2, "total_tokens": 35}}}
        out = tokens.usage_from_agy(json.dumps(step) + "\n" + json.dumps(result))
        self.assertEqual(out["usage"]["total_tokens"], 35)

    def test_missing_usage_is_rejected(self):
        with self.assertRaises(ValueError):
            tokens.usage_from_agy('{"event":"result","result":{"status":"SUCCESS"}}')

    def test_static_skill_stats_have_all_buckets(self):
        data = tokens.file_report(SKILL)
        self.assertGreater(data["core"]["characters"], 1000)
        self.assertGreater(data["references"]["files"], 8)
        self.assertGreater(data["all_skill_text"]["characters"], data["core"]["characters"])


if __name__ == "__main__":
    unittest.main()
