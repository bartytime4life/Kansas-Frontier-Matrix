import json, hashlib, subprocess, sys
from pathlib import Path
import pytest

from soilgrids_disclosure_packet import compute_disclosure_spec_hash, validate_disclosure_spec


def _mk_pack(root: Path):
    (root / "assessment").mkdir(parents=True)
    manifest = {"schema":"AssurancePackManifest.v1","assurance_pack_id":"pack1","assurance_pack_hash":"abc"}
    receipt = {"schema":"AssurancePackReceipt.v1","status":"success"}
    gate = {"schema":"AssuranceGateReport.v1","status":"pass"}
    (root / "assurance_pack_manifest.json").write_text(json.dumps(manifest))
    (root / "assurance_pack_receipt.json").write_text(json.dumps(receipt))
    (root / "assessment/assurance_gate_report.json").write_text(json.dumps(gate))
    h1 = hashlib.sha256((root / "assurance_pack_manifest.json").read_bytes()).hexdigest()
    h2 = hashlib.sha256((root / "assurance_pack_receipt.json").read_bytes()).hexdigest()
    h3 = hashlib.sha256((root / "assessment/assurance_gate_report.json").read_bytes()).hexdigest()
    (root / "checksums.sha256").write_text(f"{h1}  assurance_pack_manifest.json\n{h2}  assurance_pack_receipt.json\n{h3}  assessment/assurance_gate_report.json\n")


def _mk_spec(path: Path):
    spec={"schema":"DisclosureSpec.v1","disclosure_id":"d1","dataset_id":"soilgrids-v2","audience":"auditor","packet_profile":"auditor-full","source":{"assurance_pack_root":"x"},"redaction":{"redaction_marker":"[REDACTED]"}}
    path.write_text(json.dumps(spec)); return spec


def test_rejects_missing_disclosure_spec(tmp_path):
    p = subprocess.run([sys.executable, "soilgrids_disclosure_packet.py", "--output-root", str(tmp_path / "o"), "--mode", "auditor-full", "--disclosure-spec", str(tmp_path / "none.json"), "--assurance-pack-root", str(tmp_path / "pack")], capture_output=True, text=True)
    assert p.returncode != 0


def test_disclosure_spec_hash_stable(tmp_path):
    s = _mk_spec(tmp_path / "spec.json")
    assert compute_disclosure_spec_hash(s) == compute_disclosure_spec_hash(dict(s))


def test_rejects_unsupported_schema():
    with pytest.raises(Exception):
        validate_disclosure_spec({"schema":"X","disclosure_id":"1","audience":"public","packet_profile":"public-transparency","source":{"assurance_pack_root":"a"}})


def test_validates_source_assurance_checksums(tmp_path):
    pack = tmp_path / "pack"; _mk_pack(pack)
    spec = tmp_path / "spec.json"; _mk_spec(spec)
    out = tmp_path / "out"
    p = subprocess.run([sys.executable, "soilgrids_disclosure_packet.py", "--disclosure-spec", str(spec), "--assurance-pack-root", str(pack), "--output-root", str(out), "--mode", "auditor-full"], capture_output=True, text=True)
    assert p.returncode == 0
    r = Path(p.stdout.strip())
    assert r.exists()


def test_rejects_source_checksum_mismatch(tmp_path):
    pack = tmp_path / "pack"; _mk_pack(pack)
    (pack / "assessment/assurance_gate_report.json").write_text("{}")
    spec = tmp_path / "spec.json"; _mk_spec(spec)
    p = subprocess.run([sys.executable, "soilgrids_disclosure_packet.py", "--disclosure-spec", str(spec), "--assurance-pack-root", str(pack), "--output-root", str(tmp_path / "out"), "--mode", "auditor-full"], capture_output=True, text=True)
    assert p.returncode == 40
