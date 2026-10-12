from __future__ import annotations
import importlib.util,json,socket,subprocess,sys,unittest
from pathlib import Path
from unittest import mock
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];VALIDATOR=ROOT/'tools/validators/validate_earth_observation_harvest_authority_matrix.py';MATRIX=ROOT/'control_plane/earth_observation_harvest_authority_matrix.json';SCHEMA=ROOT/'schemas/contracts/v1/source/earth_observation_harvest_authority_matrix.schema.json';FIXTURES=ROOT/'fixtures/contracts/v1/source/earth_observation_harvest_authority_matrix'
SPEC=importlib.util.spec_from_file_location('validate_eo_matrix',VALIDATOR);assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC);sys.modules[SPEC.name]=MODULE;SPEC.loader.exec_module(MODULE)
class EarthObservationHarvestAuthorityMatrixTests(unittest.TestCase):
    def test_schema_closed(self):
        schema=json.loads(SCHEMA.read_text(encoding='utf-8'));Draft202012Validator.check_schema(schema);self.assertFalse(schema['additionalProperties'])
    def test_repository_matrix_passes_and_is_inactive(self):
        result=MODULE.validate(MATRIX);self.assertTrue(result.ok,result.findings)
        value=json.loads(MATRIX.read_text(encoding='utf-8'));self.assertFalse(any(value['governance'].values()))
        self.assertTrue(all(not e['harvest']['network_authorized'] for e in value['entries']))
        self.assertTrue(all(e['harvest']['state']=='DOCUMENTED_ONLY' for e in value['entries']))
    def test_access_surface_relationship(self):
        value=json.loads(MATRIX.read_text(encoding='utf-8'));by_id={e['authority_id']:e for e in value['entries']};ref=by_id['kfm.eo.nasa.hls_product']['access_surface_ref'];self.assertEqual(by_id[ref]['authority_role'],'ACCESS_SURFACE')
    def test_manifest_polarity(self):
        manifest=json.loads((FIXTURES/'expected_findings_manifest.json').read_text(encoding='utf-8'));self.assertEqual(len(manifest['cases']),5)
        for case in manifest['cases']:
            with self.subTest(case=case['case_id']):
                result=MODULE.validate(FIXTURES/case['input']);self.assertEqual(result.outcome,case['expected_outcome']);self.assertEqual(sorted({f.code for f in result.findings}),case['expected_findings'])
    def test_no_network_and_deterministic_cli(self):
        with mock.patch.object(socket,'create_connection',side_effect=AssertionError('network denied')),mock.patch.object(socket,'socket',side_effect=AssertionError('network denied')):
            a=MODULE.validate(MATRIX);b=MODULE.validate(MATRIX)
        self.assertEqual(a,b)
        completed=subprocess.run([sys.executable,str(VALIDATOR),'--fixtures'],cwd=ROOT,capture_output=True,text=True,check=False);self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr);self.assertEqual(len(completed.stdout.splitlines()),5);self.assertNotIn('"suite_match":false',completed.stdout)
if __name__=='__main__':unittest.main()
