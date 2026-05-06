"""Build a fixture-backed habitat layer candidate bundle."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from pipelines.habitat_layer_build.emit.write_catalog_refs import write_catalog_refs
from pipelines.habitat_layer_build.emit.write_layer_manifest import write_layer_manifest
from pipelines.habitat_layer_build.emit.write_run_receipt import write_run_receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    candidate = json.loads(args.fixture.read_text(encoding="utf-8"))
    args.out.mkdir(parents=True, exist_ok=True)

    write_layer_manifest(args.out / "layer_manifest.candidate.json", candidate)
    write_catalog_refs(args.out / "catalog_refs.candidate.json", candidate)
    write_run_receipt(args.out / "run_receipt.json", candidate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
