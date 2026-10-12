#!/usr/bin/env python3
"""Build a water catalog preview from validated input into isolated output.

The pilot WORK preview is not a processed catalog admission. General production
catalog generation remains held until a processed-input admission profile exists.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from catalog.core import water_catalog
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from pipelines.domains.hydrology.validate import validate_candidate
from tools.local_data.file_io import read_regular, write_new


def build(candidate_path: Path, output: Path):
    if output.resolve().is_relative_to(ROOT) or output.exists() or output.is_symlink():
        raise ValueError("ISOLATED_NEW_OUTPUT_REQUIRED")
    candidate = decode_object(read_regular(candidate_path, 8*1024*1024), limit=8*1024*1024)
    catalog = water_catalog(candidate, validate_candidate(candidate))
    raw = canonical_bytes(catalog)
    write_new(output, raw)
    return {"outcome": "PASS", "catalog_digest": digest_bytes(raw), "entries": len(catalog["entries"]), "authority": "candidate_only", "published": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True); parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        result = build(Path(args.candidate), Path(args.output))
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"FAIL","reason_code":"CATALOG_CANDIDATE_INVALID"}'); return 1
    print(json.dumps(result)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
