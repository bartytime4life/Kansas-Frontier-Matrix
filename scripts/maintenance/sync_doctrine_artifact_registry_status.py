#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _doctrine_registry import parse_required_entries


def sync(
    registry: Path,
    artifacts_dir: Path,
    output: Path | None = None,
    dry_run: bool = False,
    fail_on_change: bool = False,
) -> int:
    # Validate duplicate filenames / invalid status values before mutation.
    parse_required_entries(registry)
    lines = registry.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    current_filename: str | None = None
    changes: list[dict[str, str]] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- filename:"):
            current_filename = stripped.split(":", 1)[1].strip()
            updated.append(line)
            continue
        if stripped.startswith("status:") and current_filename is not None:
            indent = line[: len(line) - len(line.lstrip())]
            desired = "present" if (artifacts_dir / current_filename).exists() else "missing"
            old = stripped.split(":", 1)[1].strip()
            if old != desired:
                changes.append({"filename": current_filename, "from": old, "to": desired})
            updated.append(f"{indent}status: {desired}")
            continue
        updated.append(line)

    if not dry_run:
        registry.write_text("\n".join(updated) + "\n", encoding="utf-8")

    payload = {
        "check": "sync_doctrine_artifact_registry_status",
        "registry": str(registry),
        "artifacts_dir": str(artifacts_dir),
        "changes": changes,
        "changed_count": len(changes),
        "dry_run": dry_run,
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)

    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    if fail_on_change and changes:
        return 1
    return 0


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=root / "control_plane" / "document_registry_doctrine_required.yaml")
    parser.add_argument("--artifacts-dir", type=Path, default=root / "docs" / "doctrine" / "artifacts")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true", help="Report registry status changes without writing file")
    parser.add_argument("--fail-on-change", action="store_true", help="Return exit code 1 when reconciliation changes are needed")
    args = parser.parse_args()
    try:
        return sync(args.registry, args.artifacts_dir, args.output, dry_run=args.dry_run, fail_on_change=args.fail_on_change)
    except (ValueError, OSError) as exc:
        print(json.dumps({"check": "sync_doctrine_artifact_registry_status", "result": "error", "error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
