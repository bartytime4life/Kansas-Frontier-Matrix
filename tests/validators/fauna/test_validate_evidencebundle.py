from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

from packages.evidence.evidencebundle_hash import compute_spec_hash

SCRIPT = Path("tools/validators/fauna/validate_evidencebundle.py")


def _bundle() -> dict[str, object]:
    doc: dict[str, object] = {
        "schema_version": "v1",
        "object_type": "EvidenceBundle",
        "domain": "fauna",
        "source": "ebird",
        "source_uri": "https://example.org/ebird.csv",
        "query_predicate": "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10",
        "aggregate": "huc12",
        "suppression_min_n": 10,
        "mapping": {
            "sampling_event_identifier": "kfm:dataset_key",
            "observation_date": "occurrenceDate",
            "latitude": "decimalLatitude",
            "longitude": "decimalLongitude",
            "observation_count": "individualCount",
            "species_taxon_id": "taxonKey",
            "basisOfRecord": "HumanObservation",
        },
    }
    doc["kfm:spec_hash"] = compute_spec_hash(doc)
    return doc


def _run(doc: dict[str, object]) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "bundle.json"
        path.write_text(json.dumps(doc), encoding="utf-8")
        return subprocess.run(["python3", str(SCRIPT), str(path)], check=False, capture_output=True, text=True)


def test_valid_evidencebundle_validates() -> None:
    proc = _run(_bundle())
    assert proc.returncode == 0


def test_hash_mismatch_fails() -> None:
    doc = _bundle()
    doc["kfm:spec_hash"] = "sha256:" + "0" * 64
    proc = _run(doc)
    assert proc.returncode == 1
    assert "does not match" in proc.stderr


def test_missing_source_uri_fails() -> None:
    doc = _bundle()
    doc.pop("source_uri")
    proc = _run(doc)
    assert proc.returncode == 1


def test_missing_query_predicate_fails() -> None:
    doc = _bundle()
    doc.pop("query_predicate")
    proc = _run(doc)
    assert proc.returncode == 1


def test_malformed_spec_hash_fails() -> None:
    doc = _bundle()
    doc["kfm:spec_hash"] = "abc"
    proc = _run(doc)
    assert proc.returncode == 1
