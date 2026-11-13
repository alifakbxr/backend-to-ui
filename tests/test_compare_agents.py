from __future__ import annotations
from copy import deepcopy
import unittest
from evals.compare_agents import compare

SHA = "a" * 40
DIGEST = "b" * 64

class CrossAgentComparisonTests(unittest.TestCase):
    def runs(self):
        base = {
            "repo_commit": SHA, "skill_commit": SHA,
            "contract_sha256": DIGEST, "prompt_sha256": DIGEST,
            "cases": [{"id": "backend_only_unspecified", "action": "ask_stack",
                       "message": "Which frontend stack should I use?",
                       "files_changed": []}]
        }
        return [dict(deepcopy(base), agent="gemini-cli"), dict(deepcopy(base), agent="antigravity")]

    def test_matching_recorded_inputs(self):
        result = compare(self.runs())
        self.assertEqual(result["status"], "pass")
        self.assertTrue(result["comparable"])
        self.assertIn("Self-reported", result["limitation"])

    def test_mismatched_contract_invalidates_comparison(self):
        runs = self.runs()
        runs[1]["contract_sha256"] = "c" * 64
        result = compare(runs)
        self.assertEqual(result["status"], "invalid")
        self.assertTrue(any("contract_sha256" in e for e in result["problems"]))

    def test_different_scenarios_invalidates_comparison(self):
        runs = self.runs()
        runs[1]["cases"][0]["id"] = "backend_existing_vue_unspecified"
        self.assertEqual(compare(runs)["status"], "invalid")

    def test_incomplete_agent_record_is_not_pass(self):
        runs = self.runs()
        runs[1]["cases"][0]["message"] = "Here is your frontend"
        self.assertEqual(compare(runs)["status"], "fail")

    def test_no_results_is_not_pass(self):
        self.assertEqual(compare([])["status"], "invalid")
