#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


CANONICAL = [
    "apps/governed_api/ecology/evidencebundle_resolver.py",
    "apps/governed_api/ecology/routes.py",
    "apps/governed_api/ecology/fastapi_routes.py",
]

SHIMS = {
    "apps/governed-api/ecology/evidencebundle_resolver.py": "apps.governed_api.ecology.evidencebundle_resolver",
    "apps/governed-api/ecology/routes.py": "apps.governed_api.ecology.routes",
    "apps/governed-api/ecology/fastapi_routes.py": "apps.governed_api.ecology.fastapi_routes",
}


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _setup_valid_tree(root: Path) -> None:
    for rel in CANONICAL:
        _write(root / rel, "x = 1\n")

    for rel, target in SHIMS.items():
        _write(
            root / rel,
            "from __future__ import annotations\n\n"
            f"from {target} import *  # noqa: F401,F403\n",
        )


def test_governed_api_path_policy_passes(tmp_path: Path) -> None:
    _setup_valid_tree(tmp_path)

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_governed_api_path_policy.py",
            "--root",
            str(tmp_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 0
    assert "check_governed_api_path_policy: ok" in proc.stdout


def test_governed_api_path_policy_fails_when_shim_is_not_shim_only(tmp_path: Path) -> None:
    _setup_valid_tree(tmp_path)

    _write(
        tmp_path / "apps/governed-api/ecology/routes.py",
        "from __future__ import annotations\n\n"
        "def real_code():\n"
        "    return 1\n",
    )

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_governed_api_path_policy.py",
            "--root",
            str(tmp_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    assert "legacy path must remain shim-only" in proc.stderr


def test_governed_api_path_policy_fails_when_canonical_missing(tmp_path: Path) -> None:
    _setup_valid_tree(tmp_path)
    (tmp_path / "apps/governed_api/ecology/routes.py").unlink()

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_governed_api_path_policy.py",
            "--root",
            str(tmp_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    assert "missing canonical file" in proc.stderr


def test_governed_api_path_policy_fails_when_canonical_is_shim_only(tmp_path: Path) -> None:
    _setup_valid_tree(tmp_path)
    _write(
        tmp_path / "apps/governed_api/ecology/routes.py",
        "from __future__ import annotations\n\n"
        "from apps.governed_api.ecology.fastapi_routes import *  # noqa: F401,F403\n",
    )

    proc = subprocess.run(
        [
            "python3",
            "tools/ci/check_governed_api_path_policy.py",
            "--root",
            str(tmp_path),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    assert "canonical file must not be shim-only" in proc.stderr
