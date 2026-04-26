#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


RENDER_JOBS = (
    {
        "renderer": "tools/ci/render_promotion_summary.py",
        "inputs": {"--input": "tests/ci/fixtures/promotion_summary/promotion.json"},
        "output": "promotion_summary.md",
    },
    {
        "renderer": "tools/ci/render_diff_summary.py",
        "inputs": {"--input": "tests/ci/fixtures/diff_summary/diff.json"},
        "output": "diff_summary.md",
    },
    {
        "renderer": "tools/ci/render_promotion_bundle_summary.py",
        "inputs": {"--input": "tests/ci/fixtures/promotion_bundle/bundle.json"},
        "output": "promotion_bundle_summary.md",
    },
    {
        "renderer": "tools/ci/render_bundle_diff_policy_summary.py",
        "inputs": {"--input": "tests/ci/fixtures/diff_policy/diff_policy.json"},
        "output": "diff_policy_summary.md",
    },
    {
        "renderer": "tools/ci/render_promotion_review_handoff.py",
        "inputs": {
            "--promotion": "tests/ci/fixtures/review_handoff/promotion.json",
            "--bundle": "tests/ci/fixtures/review_handoff/bundle.json",
            "--diff": "tests/ci/fixtures/review_handoff/diff.json",
            "--diff-policy": "tests/ci/fixtures/review_handoff/diff_policy.json",
        },
        "output": "promotion_review_handoff.md",
    },
)


def sha256_text(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_or_absolute(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path.resolve())


def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic governed CI artifacts from fixed fixtures.")
    parser.add_argument("--root", default=".", help="Repository root path")
    parser.add_argument("--out-dir", default="artifacts/governed", help="Output directory for rendered artifacts")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"build_governed_artifacts: invalid root path: {root}", file=sys.stderr)
        return 2

    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, object] = {"artifacts": []}
    for job in RENDER_JOBS:
        renderer = str(job["renderer"])
        output_name = str(job["output"])
        inputs = dict(job["inputs"])
        renderer_path = root / renderer
        output_path = out_dir / output_name
        command = [sys.executable, str(renderer_path)]
        for flag, rel_path in inputs.items():
            command.extend([flag, str(root / rel_path)])
        command.extend(["--output", str(output_path)])
        subprocess.run(
            command,
            check=True,
        )
        manifest["artifacts"].append(
            {
                "renderer": renderer,
                "inputs": inputs,
                "output": relative_or_absolute(output_path, root),
                "sha256": sha256_text(output_path),
            }
        )

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"build_governed_artifacts: wrote {relative_or_absolute(manifest_path, root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
