#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_cmd(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=root / "control_plane" / "document_registry_doctrine_required.yaml")
    parser.add_argument("--artifacts-dir", type=Path, default=root / "docs" / "doctrine" / "artifacts")
    parser.add_argument("--output-dir", type=Path, default=root / "receipts" / "doctrine_artifacts")
    parser.add_argument(
        "--stable-filenames",
        action="store_true",
        help="Use stable receipt filename instead of UTC timestamp suffix",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero when required doctrine artifacts are missing (check returncode 1)",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    suffix = "" if args.stable_filenames else f".{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    check_receipt = args.output_dir / f"check_required_doctrine_artifacts{suffix}.json"

    check_cmd = [
        sys.executable,
        str(root / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--registry",
        str(args.registry),
        "--artifacts-dir",
        str(args.artifacts_dir),
        "--output",
        str(check_receipt),
    ]
    check_res = run_cmd(check_cmd, root)

    if check_res.returncode == 2:
        render_res = subprocess.CompletedProcess(args=[], returncode=2, stdout="", stderr="skipped_due_to_check_error")
    else:
        render_cmd = [
            sys.executable,
            str(root / "scripts" / "maintenance" / "render_doctrine_presence_input.py"),
            str(check_receipt),
        ]
        render_res = run_cmd(render_cmd, root)

    summary = {
        "check_returncode": check_res.returncode,
        "check_stderr": check_res.stderr.strip(),
        "render_returncode": render_res.returncode,
        "render_stderr": render_res.stderr.strip(),
        "check_receipt": str(check_receipt),
        "presence_input": json.loads(render_res.stdout) if render_res.returncode == 0 else None,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

    if render_res.returncode != 0 or check_res.returncode == 2:
        return 2
    if args.strict and check_res.returncode == 1:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
