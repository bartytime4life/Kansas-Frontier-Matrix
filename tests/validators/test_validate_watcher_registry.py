from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / 'tools/validators/validate_watcher_registry.py'
REGISTRY = ROOT / 'control_plane/watcher_registry.json'
SCHEMA = ROOT / 'schemas/contracts/v1/source/watcher_registry.schema.json'
FIXTURES = ROOT / 'fixtures/contracts/v1/source/watcher_registry'
SPEC = importlib.util.spec_from_file_location('validate_watcher_registry', VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = MODULE; SPEC.loader.exec_module(MODULE)

class WatcherRegistryTests(unittest.TestCase):
    def test_schema_closed(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding='utf-8')); Draft202012Validator.check_schema(schema)
        self.assertFalse(schema['additionalProperties'])
    def test_repository_registry_passes(self) -> None:
        result = MODULE.validate(REGISTRY); self.assertTrue(result.ok, result.findings)
    def test_placeholder_cannot_create_authority(self) -> None:
        value = json.loads(REGISTRY.read_text(encoding='utf-8')); watcher = value['watchers'][0]
        self.assertEqual(watcher['state'], 'PLACEHOLDER')
        self.assertFalse(any(watcher['governance'].values()))
        self.assertIsNone(watcher['source_descriptor_ref']); self.assertEqual(watcher['outputs'], [])
    def test_manifest_polarity(self) -> None:
        manifest = json.loads((FIXTURES/'expected_findings_manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest['cases']), 4)
        for case in manifest['cases']:
            with self.subTest(case=case['case_id']):
                result = MODULE.validate(FIXTURES/case['input'])
                self.assertEqual(result.outcome, case['expected_outcome'])
                self.assertEqual(sorted({f.code for f in result.findings}), case['expected_findings'])
    def test_no_network_and_deterministic_cli(self) -> None:
        with mock.patch.object(socket, 'create_connection', side_effect=AssertionError('network denied')), mock.patch.object(socket, 'socket', side_effect=AssertionError('network denied')):
            first = MODULE.validate(REGISTRY); second = MODULE.validate(REGISTRY)
        self.assertEqual(first, second)
        completed = subprocess.run([sys.executable, str(VALIDATOR), '--fixtures'], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 4)
        self.assertNotIn('"suite_match":false', completed.stdout)

if __name__ == '__main__': unittest.main()
