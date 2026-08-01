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


def _validate_fixture_files(validator, files, *, expect_valid: bool):
    ok = True
    for fp in files:
        try:
            data = json.loads(Path(fp).read_text(encoding="utf-8"))
            errs = sorted(validator.iter_errors(data), key=lambda e: e.path)
        except Exception as e:
            print(f"FAIL {fp}: {e}")
            ok = False
            continue

        if expect_valid:
            if errs:
                print(f"FAIL {fp}: {errs[0].message}")
                ok = False
            else:
                print(f"OK {fp}")
        elif errs:
            print(f"EXPECTED_FAIL {fp}: {errs[0].message}")
        else:
            print(f"FAIL {fp}: expected schema rejection")
            ok = False

    return ok


def run(schema_path: Path, fixtures_dir: Path | None, argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    ns = parser.parse_args(argv)
    if not ns.fixtures and not ns.files:
        print("No files provided", file=sys.stderr)
        return 2

    v = load_validator(schema_path)
    if ns.fixtures:
        if fixtures_dir is None:
            print("FAIL fixture configuration: no fixture directory configured")
            return 1

        valid_dir = fixtures_dir / "valid"
        invalid_dir = fixtures_dir / "invalid"
        valid_files = sorted(valid_dir.glob("*.json"))
        invalid_files = sorted(invalid_dir.glob("*.json"))

        ok = True
        if not valid_files:
            print(f"FAIL {valid_dir}: no JSON fixtures found")
            ok = False
        else:
            ok = _validate_fixture_files(v, valid_files, expect_valid=True) and ok

        if not invalid_files:
            print(f"FAIL {invalid_dir}: no JSON fixtures found")
            ok = False
        else:
            ok = _validate_fixture_files(v, invalid_files, expect_valid=False) and ok

        return 0 if ok else 1

    return validate_files(v, ns.files)
