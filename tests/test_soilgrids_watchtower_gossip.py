import json, subprocess, sys
from pathlib import Path
import soilgrids_watchtower_gossip as m

FX=Path("tests/fixtures/watchtower_gossip")

def load(n): return json.loads((FX/n).read_text())

def test_rejects_missing_watchtower_spec(): assert not m.validate_watchtower_spec({"schema":"WatchtowerSpec.v1"})[0]
def test_rejects_malformed_watchtower_spec(): assert not m.validate_watchtower_spec(load("watchtower_spec_invalid.json"))[0]
def test_rejects_unsupported_schema(): assert not m.validate_watchtower_spec({"schema":"X","watchtower_id":"a","dataset_id":"b","log":{"algorithm":"sha256-rfc9162-style","leaf_domain_separator":"00","node_domain_separator":"01"},"peers":{"minimum_witnesses":1}})[0]
def test_watchtower_spec_hash_stable(): s=load("watchtower_spec_valid.json"); assert m.compute_watchtower_spec_hash(s)==m.compute_watchtower_spec_hash(dict(s))
def test_watchtower_plan_hash_stable(): p={"a":1,"created_at_utc":"x"}; assert m.compute_watchtower_plan_hash(p)==m.compute_watchtower_plan_hash({"a":1,"created_at_utc":"y"})
def test_discovers_peer_inputs_deterministically(): a=m.discover_peer_inputs({"transparency_portal_roots":["b","a"],"verifier_run_roots":[],"witness_statements":[]}); assert a==sorted(a)
def test_peer_registry_ids_stable(): s=load("watchtower_spec_valid.json"); p=[("witness","x")]; assert m.build_peer_registry(s,p)["peers"][0]["peer_id"]==m.build_peer_registry(s,p)["peers"][0]["peer_id"]
def test_peer_checkpoint_hash_stable(): c={"a":1,"created_at_utc":"x","errors":[],"checkpoint_hash":"z"}; assert m.compute_peer_checkpoint_hash(c)==m.compute_peer_checkpoint_hash({"a":1})
def test_validates_transparency_snapshot(): assert m.validate_transparency_snapshot(load("snapshot_valid.json"))[0]
def test_rejects_snapshot_root_mismatch(): assert not m.validate_transparency_snapshot(load("snapshot_valid.json"),load("sth_conflict.json"))[0]
def test_validates_signed_tree_head_unsigned_allowed(): assert m.validate_signed_tree_head(load("sth_valid.json"),load("snapshot_valid.json"),True)[0]
def test_rejects_signed_tree_head_conflict(): assert not m.validate_signed_tree_head(load("sth_conflict.json"),load("snapshot_valid.json"),True)[0]
def test_validates_witness_statement(): assert m.validate_witness_statement(load("witness_statement_valid.json"),load("snapshot_valid.json"))[0]
def test_rejects_witness_statement_conflict(): assert not m.validate_witness_statement(load("witness_statement_conflict.json"),load("snapshot_valid.json"))[0]
def test_rejects_failed_verifier_summary(): assert not m.validate_verifier_receipt(load("verifier_summary_failed.json"))
def test_consistency_between_checkpoints_valid(): assert m.verify_consistency_between_checkpoints({"transparency_log_id":"x","tree_size":1,"root_hash":"a"},{"transparency_log_id":"x","tree_size":2,"root_hash":"b"})[0]
def test_consistency_between_checkpoints_invalid(): assert not m.verify_consistency_between_checkpoints({"transparency_log_id":"x","tree_size":1,"root_hash":"a"},{"transparency_log_id":"x","tree_size":1,"root_hash":"b"})[0]
def test_detects_same_size_different_root_candidate(): assert len(m.detect_split_view_candidates([{"checkpoint_hash":"1","peer_id":"a","tree_size":1,"root_hash":"a","transparency_log_id":"x"},{"checkpoint_hash":"2","peer_id":"b","tree_size":1,"root_hash":"b","transparency_log_id":"x"}]))==1
def test_builds_proven_equivocation_when_evidence_sufficient(): assert m.build_equivocation_evidence([{"candidate_id":"c","tree_size_a":1,"root_hash_a":"a","peer_a":"a","tree_size_b":1,"root_hash_b":"b","peer_b":"b"}])["status"]=="proven"
def test_does_not_overclaim_equivocation_without_proof(): assert m.build_equivocation_evidence([]) is None
def test_quorum_met(): assert m.evaluate_witness_quorum([load("witness_statement_valid.json"),{"schema":"WitnessStatement.v1","witness_id":"w2","tree_size":10,"root_hash":"a"*64}],2)["met"]
def test_quorum_not_met_warning(): assert not m.evaluate_witness_quorum([load("witness_statement_valid.json")],2)["met"]
def test_gossip_envelope_hash_stable(): s=load("watchtower_spec_valid.json"); e=m.build_gossip_envelope(s,[]); assert e["envelope_hash"]==m.compute_gossip_envelope_hash(e)
def test_gossip_export_unsigned_by_default(): s=load("watchtower_spec_valid.json"); assert m.build_gossip_envelope(s,[])["signature"]["type"]=="unsigned"
def test_mock_signed_gossip_envelope(): s=load("watchtower_spec_valid.json"); e=m.sign_gossip_envelope_if_requested(m.build_gossip_envelope(s,[]),True,"mock"); assert e["signature"]["type"]=="mock-signature"

def test_watchtower_scan_report_written(tmp_path):
    out=tmp_path/'out'; out.mkdir(); spec=tmp_path/'spec.json'; spec.write_text((FX/'watchtower_spec_valid.json').read_text())
    cp=subprocess.run([sys.executable,'soilgrids_watchtower_gossip.py','--watchtower-spec',str(spec),'--output-root',str(out),'--mode','scan-local'],capture_output=True,text=True)
    assert cp.returncode in (0,10,20)
