"""Independent shape, documented example, and process-receipt contract checks."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
import pytest


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas/contracts/v1/source/local_data_manifest.schema.json").read_text())
EXAMPLE = json.loads((ROOT / "configs/examples/local-data-manifest.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def test_example_binds_the_documented_bytes():
    Draft202012Validator.check_schema(SCHEMA)
    VALIDATOR.validate(EXAMPLE)
    item = EXAMPLE["items"][0]
    payload = (ROOT / "fixtures/source/local_data" / item["relative_path"]).read_bytes()
    assert item["sha256"] == hashlib.sha256(payload).hexdigest()
    assert item["size_bytes"] == len(payload)
    assert item["rights"]["redistribution"] == "unknown"
    assert item["sensitivity"] == "unknown"


@pytest.mark.parametrize("field,value", [
    ("sha256", "0" * 64),
    ("sha256", "A" * 64),
    ("size_bytes", True),
    ("size_bytes", 0),
    ("source_id", "../elsewhere"),
    ("version", "../../overwrite"),
    ("source_uri", "http://untrusted.example/file"),
    ("sensitivity", "approved"),
    ("rights", {"redistribution": "allowed"}),
    ("captured_at", "2026-02-30T00:00:00Z"),
    ("captured_at", "2026-09-17T00:00:00+00:00"),
    ("media_type", "text/plain\nInjected"),
])
def test_manifest_rejects_invalid_assertions(field, value):
    candidate = deepcopy(EXAMPLE)
    candidate["items"][0][field] = value
    assert list(VALIDATOR.iter_errors(candidate))


def test_empty_and_extra_fields_do_not_silently_pass():
    for candidate in ({"schema_version": "1", "items": []},
                      {**EXAMPLE, "publish": True},
                      {"schema_version": "2", "items": EXAMPLE["items"]}):
        assert list(VALIDATOR.iter_errors(candidate))
    candidate = deepcopy(EXAMPLE)
    candidate["items"][0]["admitted"] = True
    assert list(VALIDATOR.iter_errors(candidate))


def test_readme_source_download_instructions_have_real_entrypoints():
    # Source ZIPs must contain the entrypoints and example, not just wheel metadata.
    for name in ("tools/local_data/doctor.py", "tools/local_data/manage.py",
                 "docs/runbooks/local-pc-data-store.md",
                 "connectors/local_upload/src/local_upload/fetch.py"):
        assert (ROOT / name).is_file(), name
