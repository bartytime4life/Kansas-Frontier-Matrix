import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators._common.local_resolver import build_registry


def load_validator(schema_path: Path):
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    repo_root = Path(__file__).resolve().parents[3]
    registry = build_registry(repo_root)
    return Draft202012Validator(schema, registry=registry)


def validate_files(validator, files):
    ok = True
    for fp in files:
        try:
            data = json.loads(Path(fp).read_text(encoding="utf-8"))
            errs = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if errs:
                print(f"FAIL {fp}: {errs[0].message}")
                ok = False
            else:
                print(f"OK {fp}")
        except Exception as e:
            print(f"FAIL {fp}: {e}")
            ok = False
    return 0 if ok else 1


def run(schema_path: Path, fixtures_dir: Path | None, argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    ns = parser.parse_args(argv)
    v = load_validator(schema_path)
    if ns.fixtures:
        files = list((fixtures_dir / "valid").glob("*.json")) + list((fixtures_dir / "invalid").glob("*.json"))
        rc = validate_files(v, files)
        if rc == 2:
            return rc
        for f in (fixtures_dir / "valid").glob("*.json"):
            data = json.loads(f.read_text())
            if list(v.iter_errors(data)):
                return 1
        for f in (fixtures_dir / "invalid").glob("*.json"):
            data = json.loads(f.read_text())
            if not list(v.iter_errors(data)):
                return 1
        return 0
    if not ns.files:
        print("No files provided", file=sys.stderr)
        return 2
    return validate_files(v, ns.files)
