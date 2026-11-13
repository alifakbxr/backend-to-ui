#!/usr/bin/env python3
"""Offline evaluation harness tests. They do not execute Claude/Gemini/Codex."""
from __future__ import annotations

import unittest

from evals.score import grade_case, load_scenarios, policy_decision


class StackSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = load_scenarios()
        cls.by_id = {case["id"]: case for case in cls.scenarios}

    def test_matrix_coverage_and_unique_ids(self):
        self.assertGreaterEqual(len(self.scenarios), 15)
        ids = [scenario["id"] for scenario in self.scenarios]
        self.assertEqual(len(ids), len(set(ids)))
        actions = {scenario["expected"]["action"] for scenario in self.scenarios}
        self.assertEqual(actions, {"ask_stack", "implement", "audit"})

    def test_reference_policy_matches_all_cases(self):
        for scenario in self.scenarios:
            with self.subTest(id=scenario["id"]):
                self.assertEqual(policy_decision(scenario["input"]), scenario["expected"]["action"])

    def test_backend_only_never_defaults_to_html(self):
        case = self.by_id["backend_only_unspecified"]
        self.assertEqual(case["expected"]["action"], "ask_stack")
        bad_run = {
            "id": case["id"], "action": "implement", "stack": "native HTML/CSS/JS",
            "files_changed": ["index.html"], "message": "Done"
        }
        self.assertEqual(grade_case(case, bad_run)[0], "fail")

    def test_detected_vue_without_authorization_must_ask(self):
        case = self.by_id["backend_existing_vue_unspecified"]
        self.assertEqual(case["expected"]["action"], "ask_stack")
        good_run = {"id": case["id"], "action": "ask_stack",
                    "files_changed": [], "message": "I found Vue + Inertia. Should I use this frontend stack?"}
        self.assertEqual(grade_case(case, good_run), ("pass", []))

    def test_ask_stack_cannot_edit_files(self):
        case = self.by_id["backend_existing_html_unspecified"]
        response = {"id": case["id"], "action": "ask_stack",
                    "files_changed": ["index.html"], "message": "Use this frontend stack?"}
        self.assertEqual(grade_case(case, response)[0], "fail")

    def test_explicit_html_is_allowed(self):
        case = self.by_id["explicit_native_html"]
        response = {
            "id": case["id"], "action": "implement", "stack": "native HTML/CSS/JS",
            "files_changed": ["index.html"], "evidence": {
                "contracts": ["GET /pokemon"],
                "checks": {
                    "interaction": {"status": "pass", "cases": ["search", "detail"]},
                    "visual": {"status": "pass", "screenshots": {
                        "desktop": "artifacts/desktop.png", "mobile": "artifacts/mobile.png"
                    }}
                }
            }
        }
        self.assertEqual(grade_case(case, response), ("pass", []))

    def test_unverified_visual_gate_is_inconclusive(self):
        case = self.by_id["explicit_native_html"]
        response = {
            "id": case["id"], "action": "implement", "stack": "native HTML/CSS/JS",
            "files_changed": ["index.html"], "evidence": {
                "contracts": ["GET /pokemon"],
                "checks": {
                    "interaction": {"status": "pass", "cases": ["search"]},
                    "visual": {"status": "unverified", "screenshots": {}}
                }
            }
        }
        status, reasons = grade_case(case, response)
        self.assertEqual(status, "inconclusive")
        self.assertTrue(any("screenshot" in reason for reason in reasons))

    def test_missing_perf_evidence_is_not_pass(self):
        case = self.by_id["explicit_svelte_performance"]
        response = {
            "id": case["id"], "action": "implement", "stack": "Svelte",
            "files_changed": ["src/App.svelte"], "evidence": {
                "contracts": ["GET /items"],
                "checks": {"visual": {"status": "pass", "screenshots": {
                    "desktop": "desktop.png", "mobile": "mobile.png"
                }}, "performance": {"status": "pass"}}
            }
        }
        self.assertEqual(grade_case(case, response)[0], "inconclusive")

    def test_audit_only_does_not_need_stack(self):
        case = self.by_id["audit_only_unspecified"]
        record = {"id": case["id"], "action": "audit",
                  "files_changed": [], "message": "Existing UI is too narrow for the desktop."}
        self.assertEqual(grade_case(case, record), ("pass", []))

    def test_missing_question_fails(self):
        case = self.by_id["backend_only_unspecified"]
        record = {"id": case["id"], "action": "ask_stack",
                  "files_changed": [], "message": "Will implement native HTML"}
        self.assertEqual(grade_case(case, record)[0], "fail")

    def test_conflicting_stack_must_be_resolved(self):
        case = self.by_id["contradictory_stack"]
        record = {"id": case["id"], "action": "ask_stack",
                  "files_changed": [], "message": "Vue conflicts with this Flutter-only target. Should we use a web frontend stack instead?"}
        self.assertEqual(grade_case(case, record), ("pass", []))


if __name__ == "__main__":
    unittest.main()
