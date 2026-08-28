from __future__ import annotations
import copy, unittest
from tools.validators.common.validate_station_spatial_assignment_assessment import FIXTURE_PATH, bind_candidate, load_json_object, materialize_fixture_case, point_relation, validate_candidate, validate_fixture_manifest
class StationSpatialAssignmentAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest,findings=load_json_object(FIXTURE_PATH); assert manifest is not None, findings
        cls.by_name={e["name"]:materialize_fixture_case(manifest,e) for e in manifest["cases"]}
    def test_all_fixture_expectations(self):
        results=validate_fixture_manifest(); self.assertGreaterEqual(len(results),14); self.assertTrue(all(r["ok"] for r in results),results)
    def test_positive_assignment_passes(self): self.assertEqual(validate_candidate(self.by_name["valid_assignment"]).outcome,"PASS")
    def test_boundary_and_outside_abstain(self):
        for name in ("county_boundary","outside_huc12","unresolved_snapshot"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome,"ABSTAIN")
    def test_overlap_and_context_contradictions_deny(self):
        for name in ("overlapping_counties","declared_county_mismatch","state_county_prefix_mismatch"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome,"DENY")
    def test_geometry_and_relation_errors_deny(self):
        for name in ("relation_mismatch","open_polygon_ring","assignments_not_canonical"):
            with self.subTest(name=name): self.assertEqual(validate_candidate(self.by_name[name]).outcome,"DENY")
    def test_closed_ring_classifier(self):
        self.assertEqual(point_relation([0.5,0.5],[[0,0],[1,0],[1,1],[0,1],[0,0]]),"CONTAINS")
        self.assertEqual(point_relation([0,0.5],[[0,0],[1,0],[1,1],[0,1],[0,0]]),"BOUNDARY")
        self.assertEqual(point_relation([2,2],[[0,0],[1,0],[1,1],[0,1],[0,0]]),"OUTSIDE")
    def test_authority_overclaim_is_error(self): self.assertEqual(validate_candidate(self.by_name["authority_overclaim"]).outcome,"ERROR")
    def test_rebinding_after_observation_change(self):
        c=copy.deepcopy(self.by_name["valid_assignment"]); c["observed_at"]="2026-08-11T20:01:00Z"; c=bind_candidate(c); self.assertEqual(validate_candidate(c).outcome,"PASS")
if __name__=="__main__": unittest.main()
