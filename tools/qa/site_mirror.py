#!/usr/bin/env python3
"""Read-only file comparison and reviewed receipt checks; never copy or delete."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "data/receipts/generated/site-disaster-blm-knowledge-soil-mirror-20260930.json"
DESTINATION = ROOT / "apps/site/source"


def sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def files(root):
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True, timeout=30)
    return sorted(p for p in result.stdout.decode().split("\0") if p)


def safe(root, name):
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or str(p) != name or "\\" in name:
        raise ValueError("UNSAFE_MIRROR_PATH")
    path = root.joinpath(*p.parts)
    if any(part.is_symlink() for part in (path, *path.parents)) or not path.is_file():
        raise ValueError("MIRROR_FILE_UNAVAILABLE")
    return path


def compare(source):
    names = files(source)
    changes = []
    for name in names:
        raw = safe(source, name).read_bytes()
        target = DESTINATION/name
        before = sha(safe(DESTINATION, name).read_bytes()) if target.exists() else None
        after = sha(raw)
        if before != after:
            changes.append({"path": name, "before": before, "after": after})
    mirrored = {p.removeprefix("apps/site/source/") for p in files(ROOT) if p.startswith("apps/site/source/")}
    return {"profile":"kfm.site-mirror-comparison/v1", "source_commit": subprocess.check_output(["git","rev-parse","HEAD"],cwd=source,text=True).strip(), "source_dirty": bool(subprocess.check_output(["git","status","--porcelain"],cwd=source)), "changes":changes,"unexpected_deletions": sorted(mirrored-set(names)),"authority":"REVIEW_ONLY"}


def check():
    receipt = json.loads(RECEIPT.read_text())
    if receipt["profile"] != "kfm.site-mirror-receipt/v1" or receipt["destination"] != "apps/site/source":
        raise ValueError("MIRROR_RECEIPT_PROFILE_DRIFT")
    if receipt["counts"].get("missing", 0) or receipt["counts"].get("unexpected_difference", 0):
        raise ValueError("MIRROR_RECEIPT_INCOMPLETE")
    allowed = {"identical", "inherited_repository_overlay", "merged_water_overlay", "repository_only_water_overlay"}
    comparison = receipt["comparison"]
    if not comparison or any(entry.get("state") not in allowed for entry in comparison.values()):
        raise ValueError("MIRROR_RECEIPT_STATE_INVALID")
    actual_counts = {state: sum(entry["state"] == state for entry in comparison.values()) for state in allowed}
    if any(receipt["counts"].get(state, 0) != count for state, count in actual_counts.items()):
        raise ValueError("MIRROR_RECEIPT_COUNTS_DRIFT")
    expected = {}
    for name, entry in comparison.items():
        digest = entry["mirror_sha256"]
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise ValueError("MIRROR_DIGEST_INVALID")
        if entry["state"] == "identical" and entry.get("site_sha256") != digest:
            raise ValueError("MIRROR_IDENTICAL_MISMATCH")
        expected[name] = "sha256:" + digest
    names = {p.removeprefix("apps/site/source/") for p in files(ROOT) if p.startswith("apps/site/source/")}
    if names != set(expected):
        raise ValueError("MIRROR_FILE_SET_DRIFT")
    for name, digest in expected.items():
        if sha(safe(DESTINATION,name).read_bytes()) != digest:
            raise ValueError("MIRROR_CONTENT_DRIFT:"+name)
    return {"outcome":"PASS","files":len(expected),"source_commit":receipt["site_candidate_commit"],"hosted_equivalence":False,"authority":"CONTENT_PARITY_ONLY"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--source",type=Path);group.add_argument("--check",action="store_true")
    args=parser.parse_args()
    try:
        result=check() if args.check else compare(args.source)
    except (OSError,ValueError,KeyError,subprocess.SubprocessError):
        print('{"outcome":"FAIL","reason_code":"MIRROR_REVIEW_REQUIRED"}')
        return 1
    print(json.dumps(result,sort_keys=True));return 0


if __name__=="__main__":
    raise SystemExit(main())
