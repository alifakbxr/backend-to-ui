#!/usr/bin/env python3
"""Offline portability tests: no Gemini/Antigravity execution is claimed."""
from __future__ import annotations
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/backend-to-ui"

def load(filename: str):
    path = SKILL / "scripts" / filename
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module

contract = load("check_contract.py")
doctor = load("doctor.py")

class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads((SKILL / "assets/UI_CONTRACT.example.json").read_text())

    def fixture(self) -> dict:
        value = deepcopy(self.example)
        value["product"]["name"] = "Warehouse Dispatch"
        value["direction"]["source"] = "user:approved product concept"
        value["direction"]["status"] = "approved"
        value["evidence"] = [{"claim": "user chose task-first design", "source": "user:task-first request"}]
        return value

    def test_valid_explicit_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(contract.validate(self.fixture(), Path(tmp)), [])

    def test_model_inference_cannot_be_approved(self):
        value = self.fixture()
        value["direction"]["source"] = "inference:agent taste"
        with tempfile.TemporaryDirectory() as tmp:
            errors = contract.validate(value, Path(tmp))
        self.assertTrue(any("approved" in error for error in errors))

    def test_reject_example_as_real_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(contract.validate(self.example, Path(tmp)))

    def test_two_options_not_color_swaps(self):
        value = self.fixture()
        value["composition"]["alternatives"][1]["description"] = value["composition"]["alternatives"][0]["description"]
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("duplicate" in e for e in contract.validate(value, Path(tmp))))

    def test_unknown_selected_composition(self):
        value = self.fixture()
        value["composition"]["selected"] = "does-not-exist"
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("selected" in e for e in contract.validate(value, Path(tmp))))

    def test_observed_direction_reuses_existing_project_brand(self):
        value = self.fixture()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "brand.css").write_text(":root { --brand: #123456 }")
            value["direction"]["status"] = "observed"
            value["direction"]["source"] = "file:brand.css"
            value["composition"]["alternatives"] = []
            self.assertEqual(contract.validate(value, root), [])

    def test_observed_direction_cannot_be_from_agent_guess(self):
        value = self.fixture()
        with tempfile.TemporaryDirectory() as tmp:
            value["direction"]["status"] = "observed"
            value["direction"]["source"] = "inference:generic theme"
            self.assertTrue(any("observed" in e for e in contract.validate(value, Path(tmp))))

    def test_approved_direction_can_contain_separate_uncertain_fact(self):
        value = self.fixture()
        value["evidence"].append({"claim": "assumed device", "source": "inference:mobile likely"})
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(contract.validate(value, Path(tmp)))

    def test_source_cannot_escape_project(self):
        value = self.fixture()
        value["direction"]["source"] = "file:../private/token.txt"
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("escapes" in e for e in contract.validate(value, Path(tmp))))

    def test_file_source_must_exist(self):
        value = self.fixture()
        value["direction"]["source"] = "file:src/tokens.css"
        value["direction"]["status"] = "observed"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertTrue(any("does not exist" in e for e in contract.validate(value, root)))
            (root / "src").mkdir()
            (root / "src/tokens.css").write_text(":root {}")
            self.assertFalse(contract.validate(value, root))

class HostDiscoveryTests(unittest.TestCase):
    def install(self, folder: Path, *, alternate=False):
        folder.mkdir(parents=True, exist_ok=True)
        body = (SKILL / "SKILL.md").read_text()
        if alternate:
            body += "\n# Unapproved copy\n"
        (folder / "SKILL.md").write_text(body)

    def test_missing_is_not_host_activation(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = doctor.inspect("antigravity", Path(tmp), None, SKILL / "SKILL.md")
            self.assertFalse(result["filesystem_discovery_ok"])
            self.assertEqual(result["activated"], "unverified")

    def test_antigravity_ide_shared_global_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            self.install(home / ".gemini/config/skills/backend-to-ui")
            result = doctor.inspect("antigravity", home, None, SKILL / "SKILL.md")
            self.assertTrue(result["filesystem_discovery_ok"])
            self.assertEqual(result["host_discovered"], "unverified")

    def test_gemini_cli_alias_is_supported(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            self.install(home / ".agents/skills/backend-to-ui")
            result = doctor.inspect("gemini-cli", home, None, SKILL / "SKILL.md")
            self.assertTrue(result["filesystem_discovery_ok"])

    def test_stale_duplicate_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            self.install(home / ".gemini/skills/backend-to-ui")
            self.install(home / ".agents/skills/backend-to-ui", alternate=True)
            result = doctor.inspect("gemini-cli", home, None, SKILL / "SKILL.md")
            self.assertFalse(result["filesystem_discovery_ok"])
            self.assertTrue(result["problems"])

    def test_workspace_override_not_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            home, workspace = Path(tmp) / "home", Path(tmp) / "project"
            self.install(home / ".gemini/config/skills/backend-to-ui")
            self.install(workspace / ".agents/skills/backend-to-ui", alternate=True)
            result = doctor.inspect("antigravity", home, workspace, SKILL / "SKILL.md")
            self.assertFalse(result["filesystem_discovery_ok"])

if __name__ == "__main__":
    unittest.main()
