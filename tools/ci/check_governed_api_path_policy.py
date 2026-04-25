#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CANONICAL_FILES = [
    "apps/governed_api/ecology/evidencebundle_resolver.py",
    "apps/governed_api/ecology/routes.py",
    "apps/governed_api/ecology/fastapi_routes.py",
]

LEGACY_SHIMS = {
    "apps/governed-api/ecology/evidencebundle_resolver.py": "apps.governed_api.ecology.evidencebundle_resolver",
    "apps/governed-api/ecology/routes.py": "apps.governed_api.ecology.routes",
    "apps/governed-api/ecology/fastapi_routes.py": "apps.governed_api.ecology.fastapi_routes",
}


def is_valid_shim(text: str, target: str) -> bool:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) != 2:
        return False
    if lines[0] != "from __future__ import annotations":
        return False
    pattern = rf"^from {re.escape(target)} import \*  # noqa: F401,F403$"
    return bool(re.match(pattern, lines[1]))


def is_shim_only_module(text: str) -> bool:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) != 2:
        return False
    if lines[0] != "from __future__ import annotations":
        return False
    return bool(re.match(r"^from apps\.governed_api\.ecology\..+ import \*  # noqa: F401,F403$", lines[1]))



def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce governed_api canonical path and legacy shim policy.")
    parser.add_argument("--root", default=".", help="Repository root path")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"check_governed_api_path_policy: invalid root path: {root}", file=sys.stderr)
        return 2

    errors: list[str] = []

    for rel in CANONICAL_FILES:
        path = root / rel
        if not path.is_file():
            errors.append(f"missing canonical file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if is_shim_only_module(text):
            # Guardrail against accidental inversion where canonical files become shim-only.
            errors.append(f"canonical file must not be shim-only: {rel}")


    for rel, target in LEGACY_SHIMS.items():
        path = root / rel
        if not path.is_file():
            errors.append(f"missing legacy shim: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if not is_valid_shim(text, target):
            errors.append(f"legacy path must remain shim-only: {rel}")

    if errors:
        print("check_governed_api_path_policy: FAILED", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print("check_governed_api_path_policy: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
