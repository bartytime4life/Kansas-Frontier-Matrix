"""No-network configuration checks; these do not build or install artifacts.

The root distribution is a dependency carrier, not a second source root or an
SDK. Keep artifact execution and inventory verification as a separate gate.
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import tomllib
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[2]


def assert_distribution_boundary(manifest: dict[str, Any]) -> None:
    """Check the committed packaging boundary, not Hatchling's implementation."""
    project = manifest.get("project", {})
    assert project.get("name") == "kfm", "root distribution identity changed"
    assert project.get("readme") == {
        "file": "README.md", "content-type": "text/markdown"
    }, "unexpected root metadata source"
    for key in ("scripts", "gui-scripts", "entry-points", "dynamic"):
        assert key not in project, f"root distribution must not declare {key}"

    build_system = manifest.get("build-system", {})
    assert build_system == {
        "requires": ["hatchling"], "build-backend": "hatchling.build"
    }, "backend changes require separate review"

    hatch = manifest.get("tool", {}).get("hatch", {})
    assert set(hatch) == {"build"}, "unexpected Hatch configuration or metadata hook"
    build = hatch["build"]
    assert set(build) == {"targets"}, "global build overrides are not admitted"
    targets = build["targets"]
    assert set(targets) == {"wheel", "sdist"}, "unexpected build target"
    assert targets["wheel"] == {
        "include": ["/pyproject.toml"], "exclude": ["*"]
    }, "wheel must disable discovery and select no project payload"
    assert targets["sdist"] == {
        "include": ["/LICENSE", "/README.md", "/pyproject.toml"]
    }, "source archive must retain the metadata-only file allowlist"


def load_manifest() -> dict[str, Any]:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def test_committed_root_distribution_boundary() -> None:
    assert_distribution_boundary(load_manifest())


def test_no_alternate_root_hatch_configuration() -> None:
    alternate = ROOT / "hatch.toml"
    assert not alternate.exists() and not alternate.is_symlink()


def test_boundary_check_does_not_mutate_the_manifest() -> None:
    manifest = load_manifest()
    original = deepcopy(manifest)
    assert_distribution_boundary(manifest)
    assert manifest == original


# Each fixture changes exactly one boundary. None installs a package, runs a
# hook, opens a network connection, or reads actual lifecycle/secret payloads.
@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("tool", "hatch", "build", "targets", "wheel", "packages"), ["src/kfm"]),
        (("tool", "hatch", "build", "targets", "wheel", "include"), ["**"]),
        (("tool", "hatch", "build", "targets", "wheel", "exclude"), []),
        (("tool", "hatch", "build", "targets", "wheel", "only-include"), ["apps"]),
        (("tool", "hatch", "build", "targets", "wheel", "force-include"), {"data": "data"}),
        (("tool", "hatch", "build", "targets", "wheel", "artifacts"), ["data/**"]),
        (("tool", "hatch", "build", "targets", "wheel", "shared-data"), {"data": "data"}),
        (("tool", "hatch", "build", "targets", "wheel", "shared-scripts"), {"tools": "tools"}),
        (("tool", "hatch", "build", "targets", "wheel", "dev-mode-dirs"), ["."]),
        (("tool", "hatch", "build", "targets", "wheel", "sources"), {"apps": ""}),
        (("tool", "hatch", "build", "targets", "wheel", "hooks"), {"custom": {}}),
        (("tool", "hatch", "build", "targets", "sdist", "include"), ["/**"]),
        (("tool", "hatch", "build", "targets", "sdist", "force-include"), {"data": "data"}),
        (("tool", "hatch", "build", "targets", "sdist", "artifacts"), [".env"]),
        (("tool", "hatch", "build", "targets", "binary"), {}),
        (("tool", "hatch", "build", "hooks"), {"custom": {}}),
        (("tool", "hatch", "build", "force-include"), {"data": "data"}),
        (("tool", "hatch", "metadata"), {"hooks": {"custom": {}}}),
        (("project", "scripts"), {"kfm": "kfm:main"}),
        (("project", "gui-scripts"), {"kfm": "kfm:main"}),
        (("project", "entry-points"), {"example.plugins": {"kfm": "kfm:main"}}),
        (("project", "dynamic"), ["dependencies"]),
        (("project", "readme"), {"file": "data/raw/example.md", "content-type": "text/markdown"}),
        (("build-system", "backend-path"), ["."]),
    ],
    ids=[
        "phantom-src-package", "broad-wheel-include", "removed-wheel-exclusion",
        "application-selection", "forced-lifecycle-payload", "artifact-bypass",
        "shared-payload", "shared-executables", "editable-repo-exposure",
        "source-remapping", "wheel-hook", "broad-source-archive",
        "forced-source-payload", "source-secret-artifact", "extra-build-target",
        "global-hook", "global-forced-payload", "metadata-hook", "cli-export",
        "gui-export", "plugin-export", "dynamic-dependencies", "raw-metadata-source",
        "in-tree-backend",
    ],
)
def test_rejects_distribution_boundary_expansion(
    path: tuple[str, ...], value: Any
) -> None:
    manifest = load_manifest()
    assert_distribution_boundary(manifest)
    mutated = deepcopy(manifest)
    target = mutated
    for component in path[:-1]:
        target = target.setdefault(component, {})
    target[path[-1]] = value
    with pytest.raises(AssertionError):
        assert_distribution_boundary(mutated)
    assert manifest == load_manifest()
