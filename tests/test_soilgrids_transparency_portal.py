import json
from pathlib import Path
from tools.soilgrids import soilgrids_transparency_portal as m


def _mk_packet(root: Path, packet_id="p1"):
    root.mkdir(parents=True, exist_ok=True)
    (root/"disclosure_packet.json").write_text(json.dumps({"disclosure_packet_id":packet_id,"packet_profile":"public-transparency","audience":"public"}))
    (root/"trust_claim_set.json").write_text(json.dumps({"claims":[{"id":"c1","evidence":["e1"]}]}))
    (root/"redaction_report.json").write_text(json.dumps({"status":"pass"}))


def test_rejects_missing_transparency_log_spec(tmp_path):
    try:
        m.build_transparency_log_and_portal(transparency_log_spec=str(tmp_path/"missing.json"), output_root=str(tmp_path), mode="plan-only")
        assert False
    except m.TransparencyError as e:
        assert e.code == 30


def test_packet_leaf_hash_stable():
    entry={"disclosure_packet_id":"a","disclosure_packet_hash":"b","trust_claim_set_hash":"c","redaction_hash":"d","source_assurance_pack_hash":None,"packet_profile":"p","audience":"x"}
    assert m.compute_packet_leaf_hash(entry)==m.compute_packet_leaf_hash(entry)


def test_merkle_root_two_leaves():
    r=m.compute_merkle_root(["00"*32,"11"*32])
    assert isinstance(r,str) and len(r)==64


def test_inclusion_proof_verifies():
    leaves=["aa"*32,"bb"*32]
    root=m.compute_merkle_root(leaves)
    p=m.build_inclusion_proof(leaves,0)
    assert m.verify_inclusion_proof(leaves[0],p,root)


def test_cli_stdout_only_receipt_path_on_success(tmp_path, capsys):
    spec=tmp_path/"spec.json"
    spec.write_text(Path("transparency/transparency_log_spec_example.json").read_text())
    packet=tmp_path/"packet"; _mk_packet(packet)
    out=tmp_path/"out"
    rc=m.main(["--transparency-log-spec",str(spec),"--output-root",str(out),"--mode","full","--disclosure-packet-root",str(packet)])
    stdout=capsys.readouterr().out.strip()
    assert rc==0 and stdout.endswith("transparency_log_receipt.json")
