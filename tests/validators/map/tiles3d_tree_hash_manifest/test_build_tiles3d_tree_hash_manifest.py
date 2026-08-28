from __future__ import annotations
import importlib.util, json, socket, subprocess, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[4]
TOOL=ROOT/'tools/validators/map/tiles3d_tree_hash_manifest/build_tiles3d_tree_hash_manifest.py'
FIXTURES=ROOT/'fixtures/map/tiles3d_tree_hash_manifest'; SCHEMA=ROOT/'schemas/contracts/v1/map/tiles3d_tree_hash_manifest.schema.json'
SPEC=importlib.util.spec_from_file_location('tiles3d_tree_hash_manifest',TOOL); assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=MODULE; SPEC.loader.exec_module(MODULE)
class Tiles3DTreeHashManifestTests(unittest.TestCase):
    def test_schema_closed(self):
        schema=json.loads(SCHEMA.read_text(encoding='utf-8')); Draft202012Validator.check_schema(schema); self.assertFalse(schema['additionalProperties'])
    def test_build_matches_exact_fixture(self):
        result=MODULE.build(FIXTURES/'tree'); self.assertTrue(result.ok,result.findings)
        expected=json.loads((FIXTURES/'expected/valid_manifest.json').read_text(encoding='utf-8')); self.assertEqual(result.manifest,expected)
        self.assertEqual([e['path'] for e in result.manifest['files']],sorted(e['path'] for e in result.manifest['files']))
        self.assertFalse(any(result.manifest['governance'].values()))
    def test_verify_detects_tamper(self):
        result=MODULE.verify(FIXTURES/'tree',FIXTURES/'invalid/invalid_tampered_manifest.json'); self.assertEqual({f.code for f in result.findings},{'MANIFEST_MISMATCH'})
    def test_missing_tileset_fails(self):
        self.assertEqual({f.code for f in MODULE.build(FIXTURES/'invalid_tree_missing_tileset').findings},{'TILESET_MISSING'})
    @unittest.skipUnless(hasattr(Path,'symlink_to'),'symlinks unavailable')
    def test_symlink_denied(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'tileset.json').write_text('{"asset":{"version":"1.1"}}',encoding='utf-8'); target=root/'payload.bin'; target.write_bytes(b'x'); link=root/'link.bin'
            try: link.symlink_to(target)
            except OSError: self.skipTest('symlink creation unavailable')
            self.assertIn('TREE_SYMLINK_DENIED',{f.code for f in MODULE.build(root).findings})
    def test_no_network_and_fixture_cli(self):
        with mock.patch.object(socket,'create_connection',side_effect=AssertionError('network denied')),mock.patch.object(socket,'socket',side_effect=AssertionError('network denied')):
            a=MODULE.build(FIXTURES/'tree'); b=MODULE.build(FIXTURES/'tree')
        self.assertEqual(a,b)
        completed=subprocess.run([sys.executable,str(TOOL),'--fixtures'],cwd=ROOT,capture_output=True,text=True,check=False)
        self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr); self.assertEqual(len(completed.stdout.splitlines()),4); self.assertNotIn('"suite_match":false',completed.stdout)
if __name__=='__main__': unittest.main()
