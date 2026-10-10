#!/usr/bin/env python3
"""Read-only recorded-content parity checks; review and deployment are separate."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import html
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "data/receipts/generated/site-v219-cutaway-textures-20261010.json"
DESTINATION = ROOT / "apps/site/source"


def sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def files(root):
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True, timeout=30)
    return sorted(p for p in result.stdout.decode().split("\0") if p)


def safe(root, name):
    valid_name(name)
    p = PurePosixPath(name)
    path = root.joinpath(*p.parts)
    if any(part.is_symlink() for part in (path, *path.parents)) or not path.is_file():
        raise ValueError("MIRROR_FILE_UNAVAILABLE")
    return path


def valid_name(name):
    if not isinstance(name, str):
        raise ValueError("UNSAFE_MIRROR_PATH")
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or str(p) != name or "\\" in name:
        raise ValueError("UNSAFE_MIRROR_PATH")
    return name


def compare(source):
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain"], cwd=source):
        raise ValueError("SOURCE_WORKTREE_DIRTY")
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
    if (subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip() != source_commit
            or subprocess.check_output(["git", "status", "--porcelain"], cwd=source)):
        raise ValueError("SOURCE_WORKTREE_CHANGED")
    return {"profile":"kfm.site-mirror-comparison/v1", "source_commit": source_commit, "source_dirty": False, "changes":changes,"unexpected_deletions": sorted(mirrored-set(names)),"authority":"REVIEW_ONLY"}


def reviewed_receipt():
    """Validate recorded content, retaining the historical function name.

    Receipt review declarations and external owner dispositions are not evaluated
    by this content-parity validator.
    """
    receipt = json.loads(RECEIPT.read_text())
    if receipt["profile"] != "kfm.site-mirror-receipt/v1" or receipt["destination"] != "apps/site/source":
        raise ValueError("MIRROR_RECEIPT_PROFILE_DRIFT")
    if receipt["counts"].get("missing", 0) or receipt["counts"].get("unexpected_difference", 0):
        raise ValueError("MIRROR_RECEIPT_INCOMPLETE")
    allowed = {"identical", "inherited_repository_overlay", "merged_water_overlay", "repository_only_water_overlay",
               "repository_only_overlay"}
    comparison = receipt["comparison"]
    if not comparison or any(entry.get("state") not in allowed for entry in comparison.values()):
        raise ValueError("MIRROR_RECEIPT_STATE_INVALID")
    actual_counts = {state: sum(entry["state"] == state for entry in comparison.values()) for state in allowed}
    if any(receipt["counts"].get(state, 0) != count for state, count in actual_counts.items()):
        raise ValueError("MIRROR_RECEIPT_COUNTS_DRIFT")
    expected = {}
    for name, entry in comparison.items():
        valid_name(name)
        digest = entry["mirror_sha256"]
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise ValueError("MIRROR_DIGEST_INVALID")
        if entry["state"] == "identical" and entry.get("site_sha256") != digest:
            raise ValueError("MIRROR_IDENTICAL_MISMATCH")
        expected[name] = "sha256:" + digest
    return receipt, expected


def check():
    receipt, expected = reviewed_receipt()
    names = {p.removeprefix("apps/site/source/") for p in files(ROOT) if p.startswith("apps/site/source/")}
    if names != set(expected):
        raise ValueError("MIRROR_FILE_SET_DRIFT")
    for name, digest in expected.items():
        if sha(safe(DESTINATION,name).read_bytes()) != digest:
            raise ValueError("MIRROR_CONTENT_DRIFT:"+name)
    states = sorted({entry["state"] for entry in receipt["comparison"].values()})
    file_states = {state: sum(entry["state"] == state for entry in receipt["comparison"].values())
                   for state in states}
    review = receipt.get("review")
    review = review if isinstance(review, dict) else {}
    return {"outcome":"PASS","files":len(expected),"source_commit":receipt["site_candidate_commit"],
            "hosted_equivalence":False,"authority":"CONTENT_PARITY_ONLY",
            "receipt_file": RECEIPT.name, "file_states": file_states,
            "repository_overlay_files": sum(count for state, count in file_states.items() if state != "identical"),
            "review_acceptance": {
                "outcome": "NOT_EVALUATED", "authority": "RECEIPT_DECLARATION_ONLY",
                "receipt_status": receipt.get("status"),
                "source_and_overlay_review": review.get("source_and_overlay_review"),
                "blocking_checks": review.get("blocking_checks"),
            }}


def markdown_report(result):
    """Render CI evidence without converting parity PASS into review acceptance."""
    review = result.get("review_acceptance", {})
    rows = [
        ("Recorded content parity", result["outcome"]),
        ("Parity authority", result.get("authority", "CONTENT_PARITY_ONLY")),
        ("Receipt file", result.get("receipt_file")),
        ("Recorded file states", result.get("file_states")),
        ("Repository overlay files", result.get("repository_overlay_files")),
        ("Review acceptance evaluated by this check", review.get("outcome", "NOT_EVALUATED")),
        ("Review reporting authority", review.get("authority", "RECEIPT_DECLARATION_ONLY")),
        ("Declared receipt status", review.get("receipt_status")),
        ("Declared source and overlay review", review.get("source_and_overlay_review")),
        ("Declared blocking checks", review.get("blocking_checks")),
        ("Hosted equivalence established by this check", result.get("hosted_equivalence", False)),
    ]
    if "reason_code" in result:
        rows.append(("Parity failure reason", result["reason_code"]))
    table = ["### Site mirror: content parity and review state", "", "| Dimension | Recorded result |",
             "|---|---|"]
    for label, value in rows:
        rendered = html.escape(json.dumps(value, sort_keys=True), quote=False).replace("|", "&#124;")
        table.append(f"| {label} | <code>{rendered}</code> |")
    table.extend(["", "A content-parity PASS verifies recorded repository bytes only. "
                  "It does not establish review acceptance, overlay deployment, or hosted equivalence. "
                  "Owner PR dispositions and pending receipt declarations require separate reconciliation. "
                  "Missing declarations are shown as null."])
    return "\n".join(table)


def diagnose():
    """Report current working-tree drift; this never approves a replacement receipt."""
    receipt, expected = reviewed_receipt()
    names = {p.removeprefix("apps/site/source/") for p in files(ROOT) if p.startswith("apps/site/source/")}
    changed = []
    for name in sorted(names & expected.keys()):
        current = sha(safe(DESTINATION, name).read_bytes())
        if current != expected[name]:
            changed.append({"path": name, "receipt_state": receipt["comparison"][name]["state"],
                            "recorded_sha256": expected[name], "working_tree_sha256": current})
    return {"outcome": "REVIEW_REQUIRED" if changed or names != set(expected) else "RECORDED_BYTES_MATCH",
            "authority": "REVIEW_ONLY", "byte_source": "working_tree",
            "repository_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
            "repository_dirty": bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT)),
            "site_candidate_commit_in_receipt": receipt["site_candidate_commit"],
            "changed": changed, "unrecorded_mirror_paths": sorted(names - expected.keys()),
            "missing_mirror_paths": sorted(expected.keys() - names)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--source",type=Path);group.add_argument("--check",action="store_true");group.add_argument("--diagnose",action="store_true")
    parser.add_argument("--format", choices=("json", "markdown"), default="json",
                        help="Markdown renders the content-parity check for a CI step summary.")
    args=parser.parse_args()
    if args.format == "markdown" and not args.check:
        parser.error("--format markdown requires --check")
    try:
        result=check() if args.check else diagnose() if args.diagnose else compare(args.source)
        code = 1 if args.diagnose and result["outcome"] == "REVIEW_REQUIRED" else 0
    except (OSError,ValueError,KeyError,subprocess.SubprocessError):
        result = {"outcome":"FAIL","reason_code":"MIRROR_REVIEW_REQUIRED"}
        code = 1
    print(markdown_report(result) if args.format == "markdown" else json.dumps(result,sort_keys=True))
    return code


if __name__=="__main__":
    raise SystemExit(main())
