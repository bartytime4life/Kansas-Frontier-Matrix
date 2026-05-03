import hashlib
import json
import sys
from pathlib import Path


def canonical_json_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def compute_hash_for_path(path: Path) -> str:
    obj = json.loads(path.read_text())
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python tools/compute_spec_hash.py <json-file>")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 2
    print(compute_hash_for_path(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
