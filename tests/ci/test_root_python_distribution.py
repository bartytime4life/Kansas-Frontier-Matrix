"""Root distribution configuration, synthetic archive checks, and opt-in proof.

Default tests are offline. KFM_RUN_ROOT_PYTHON_ARTIFACTS=1 additionally runs
real Hatchling builds and pip installs to temporary targets without dependency
resolution. A skipped real gate is not artifact evidence or release authority.
"""

from __future__ import annotations

import base64
import csv
from email.parser import BytesParser
import hashlib
import importlib.metadata
import io
import json
import os
import stat
import subprocess
import sys
import tarfile
import zipfile

from packaging.requirements import Requirement

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


# The following pure checks inspect synthetic archives by default. Real backend
# and pip execution is opt-in, and missing tools then FAIL rather than skip.


DIST = "kfm-0.0.0.dist-info"
WHEEL_FILES = {f"{DIST}/{name}" for name in (
    "METADATA", "WHEEL", "RECORD", "licenses/LICENSE", "licenses/AUTHORS.md"
)}
# Hatchling 1.32.0 always adds VCS-ignore and default license-family files.
# These exact metadata-support inputs are checked, not arbitrary globs.
INPUT_FILES = ("LICENSE", "README.md", "pyproject.toml", "AUTHORS.md", ".gitignore")
MAX_ARCHIVE_BYTES = 2_000_000


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _assert_wheel(members: dict[str, bytes], *, editable: bool = False) -> None:
    # editables 0.6 omits an empty path file. Absence is not an install failure;
    # a legacy empty _kfm.pth is also harmless, but no path/code may be added.
    expected = WHEEL_FILES | ({"_kfm.pth"} if editable and "_kfm.pth" in members else set())
    assert set(members) == expected, "unexpected wheel member inventory"
    if editable and "_kfm.pth" in members:
        assert not members["_kfm.pth"].strip(), "editable import-path exposure"
    record = f"{DIST}/RECORD"
    rows = list(csv.reader(io.StringIO(members[record].decode("utf-8"))))
    assert all(len(row) == 3 for row in rows), "invalid RECORD row"
    assert len(rows) == len(members), "RECORD count mismatch"
    assert {row[0] for row in rows} == set(members), "RECORD inventory mismatch"
    for name, digest, size in rows:
        if name == record:
            assert (digest, size) == ("", ""), "RECORD self-entry must be empty"
        else:
            expected_hash = base64.urlsafe_b64encode(
                hashlib.sha256(members[name]).digest()
            ).rstrip(b"=").decode("ascii")
            assert digest == f"sha256={expected_hash}", "RECORD hash mismatch"
            assert size == str(len(members[name])), "RECORD size mismatch"


def _read_wheel(path: Path) -> dict[str, bytes]:
    assert 0 < path.stat().st_size <= MAX_ARCHIVE_BYTES, "wheel byte limit"
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        assert len(names) <= 16 and len(names) == len(set(names)), "duplicate/oversize wheel"
        assert sum(info.file_size for info in infos) <= MAX_ARCHIVE_BYTES, "wheel expansion limit"
        for info in infos:
            assert not info.is_dir(), "directory member not admitted"
            assert not stat.S_ISLNK(info.external_attr >> 16), "wheel symlink denied"
        return {name: archive.read(name) for name in names}


def _assert_metadata(raw: bytes, manifest: dict[str, Any]) -> None:
    metadata = BytesParser().parsebytes(raw)
    project = manifest["project"]
    for key, expected in (("Name", project["name"]), ("Version", project["version"]),
                          ("Requires-Python", project["requires-python"]),
                          ("License", project["license"]["text"]),
                          ("Description-Content-Type", "text/markdown")):
        assert metadata.get_all(key) == [expected], f"metadata mismatch: {key}"
    assert sorted(metadata.get_all("License-File", [])) == ["AUTHORS.md", "LICENSE"], "license-file metadata mismatch"
    extras = project.get("optional-dependencies", {})
    assert sorted(metadata.get_all("Provides-Extra", [])) == sorted(extras), "extra mismatch"
    expected_requirements = [Requirement(item) for item in project["dependencies"]]
    for extra, requirements in extras.items():
        # This root's static requirements have no existing environment markers.
        for item in requirements:
            assert Requirement(item).marker is None, "review new requirement markers"
            expected_requirements.append(Requirement(f'{item}; extra == "{extra}"'))
    actual = [Requirement(item) for item in metadata.get_all("Requires-Dist", [])]
    assert len(actual) == len(expected_requirements), "dependency count mismatch"
    assert set(actual) == set(expected_requirements), "dependency metadata mismatch"


def _read_sdist(path: Path, inputs: dict[str, bytes]) -> dict[str, bytes]:
    assert 0 < path.stat().st_size <= MAX_ARCHIVE_BYTES, "sdist byte limit"
    expected = {f"kfm-0.0.0/{name}" for name in (*INPUT_FILES, "PKG-INFO")}
    with tarfile.open(path, "r:gz") as archive:
        infos = archive.getmembers()
        assert len(infos) == len(expected), "sdist member count mismatch"
        assert {info.name for info in infos} == expected, "unexpected sdist inventory"
        assert all(info.isfile() for info in infos), "sdist links/non-files denied"
        assert sum(info.size for info in infos) <= MAX_ARCHIVE_BYTES, "sdist expansion limit"
        members = {}
        for info in infos:
            stream = archive.extractfile(info)
            assert stream is not None
            members[info.name.split("/", 1)[1]] = stream.read()
    for name, raw in inputs.items():
        assert members[name] == raw, f"source bytes changed: {name}"
    return members


def _synthetic_wheel(*, editable: bool = False) -> dict[str, bytes]:
    members = {name: b"synthetic metadata\n" for name in WHEEL_FILES}
    if editable:
        members["_kfm.pth"] = b""
    record = f"{DIST}/RECORD"
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    for name, raw in sorted(members.items()):
        digest = base64.urlsafe_b64encode(hashlib.sha256(raw).digest()).rstrip(b"=").decode()
        writer.writerow((name, "", "") if name == record else (name, f"sha256={digest}", len(raw)))
    members[record] = output.getvalue().encode()
    return members


@pytest.mark.parametrize("editable", [False, True])
def test_synthetic_wheel_inventory_and_record(editable: bool) -> None:
    _assert_wheel(_synthetic_wheel(editable=editable), editable=editable)


def test_editable_without_path_file_is_metadata_only() -> None:
    _assert_wheel(_synthetic_wheel(), editable=True)


def test_noneditable_rejects_even_an_empty_path_file() -> None:
    with pytest.raises(AssertionError, match="inventory"):
        _assert_wheel(_synthetic_wheel(editable=True))


@pytest.mark.parametrize("name", [
    "kfm.py", "kfm/__init__.py", "apps/example.py", "data/raw/example.json",
    ".env", "../outside", "/absolute", f"{DIST}/entry_points.txt",
    f"{DIST}/licenses/NOTICE-unreviewed.txt",
])
def test_archive_guard_rejects_additional_payload(name: str) -> None:
    members = _synthetic_wheel()
    members[name] = b"SYNTHETIC ONLY"
    with pytest.raises(AssertionError, match="inventory"):
        _assert_wheel(members)


@pytest.mark.parametrize("payload", [b".\n", b"/tmp/fixture-source\n", b"import fixture_module\n"])
def test_archive_guard_rejects_editable_exposure(payload: bytes) -> None:
    members = _synthetic_wheel(editable=True)
    members["_kfm.pth"] = payload
    with pytest.raises(AssertionError, match="import-path"):
        _assert_wheel(members, editable=True)


def test_archive_guard_rejects_changed_recorded_bytes() -> None:
    members = _synthetic_wheel()
    members[f"{DIST}/METADATA"] += b"changed"
    with pytest.raises(AssertionError, match="hash mismatch"):
        _assert_wheel(members)


@pytest.mark.parametrize("fault", [None, "extra", "symlink", "changed-input", "duplicate"])
def test_source_archive_guard_fixture_polarity(tmp_path: Path, fault: str | None) -> None:
    inputs = {name: b"SYNTHETIC ONLY\n" for name in INPUT_FILES}
    path = tmp_path / "candidate.tar.gz"
    with tarfile.open(path, "w:gz") as archive:
        for name in (*INPUT_FILES, "PKG-INFO"):
            raw = inputs.get(name, b"synthetic metadata")
            info = tarfile.TarInfo(f"kfm-0.0.0/{name}")
            if name == "README.md" and fault == "changed-input":
                raw += b"changed"
            if name == "README.md" and fault == "symlink":
                info.type, info.linkname = tarfile.SYMTYPE, "../../outside"
            else:
                info.size = len(raw)
            archive.addfile(info, io.BytesIO(raw))
        if fault in {"extra", "duplicate"}:
            info = tarfile.TarInfo("../outside" if fault == "extra" else "kfm-0.0.0/README.md")
            archive.addfile(info, io.BytesIO())
    if fault is None:
        assert set(_read_sdist(path, inputs)) == {*INPUT_FILES, "PKG-INFO"}
    else:
        with pytest.raises(AssertionError):
            _read_sdist(path, inputs)


def _run(args: list[str], *, cwd: Path, env: dict[str, str]) -> str:
    result = subprocess.run(args, cwd=cwd, env=env, shell=False, check=False,
                            capture_output=True, text=True, timeout=90)
    assert result.returncode == 0, (
        f"command failed ({result.returncode}): {args!r}\n"
        f"{result.stdout[-12000:]}\n{result.stderr[-12000:]}"
    )
    return result.stdout.strip()


def _build(kind: str, source: Path, destination: Path, env: dict[str, str]) -> Path:
    assert kind in {"wheel", "sdist", "editable"}
    destination.mkdir()
    code = ("import sys; from hatchling import build; "
            f"print(build.build_{kind}(sys.argv[1]))")
    name = _run([sys.executable, "-I", "-c", code, str(destination)], cwd=source, env=env)
    assert name == Path(name).name, "unexpected backend artifact name"
    path = destination / name
    assert path.is_file() and not path.is_symlink(), "missing/unsafe artifact"
    return path


def _verify_installed(target: Path, manifest: dict[str, Any], env: dict[str, str]) -> None:
    for path in target.rglob("*"):
        assert not path.is_symlink(), "installed symlink denied"
        if path.is_file():
            relative = path.relative_to(target)
            assert relative.parts[0] == DIST or relative.as_posix() == "_kfm.pth", "installed payload"
            if path.suffix == ".pth":
                assert not path.read_bytes().strip(), "installed import-path exposure"
    _assert_metadata((target / DIST / "METADATA").read_bytes(), manifest)
    # -I -S omits the working directory, PYTHONPATH, and automatic site loading.
    # Processing just the checked target must add only that target, not the repo.
    code = ("import importlib.util,json,site,sys; before=list(sys.path); "
            "site.addsitedir(sys.argv[1]); "
            "print(json.dumps({'added':[p for p in sys.path if p not in before],"
            "'kfm':importlib.util.find_spec('kfm') is not None}))")
    result = json.loads(_run([sys.executable, "-I", "-S", "-c", code, str(target)],
                             cwd=target, env=env))
    assert result == {"added": [str(target)], "kfm": False}, "installed import boundary changed"


@pytest.mark.skipif(os.environ.get("KFM_RUN_ROOT_PYTHON_ARTIFACTS") != "1",
                    reason="real build/install gate not requested; NOT artifact evidence")
def test_real_root_build_rebuild_and_install(tmp_path: Path) -> None:
    manifest = load_manifest()
    assert_distribution_boundary(manifest)
    assert not (ROOT / "hatch.toml").exists() and not (ROOT / "hatch.toml").is_symlink()
    # Missing tools on an explicitly requested gate are a test failure.
    versions = {name: importlib.metadata.version(name)
                for name in ("hatchling", "editables", "pytest", "packaging", "pip")}
    inputs = {}
    for name in INPUT_FILES:
        path = ROOT / name
        assert path.is_file() and not path.is_symlink(), "unsafe packaging input"
        inputs[name] = path.read_bytes()
    env = {key: os.environ[key] for key in ("PATH", "SYSTEMROOT", "WINDIR", "LANG") if key in os.environ}
    home = tmp_path / "home"
    home.mkdir()
    env.update(HOME=str(home), TMPDIR=str(tmp_path), TEMP=str(tmp_path), TMP=str(tmp_path),
               PIP_CONFIG_FILE=os.devnull, PIP_NO_INDEX="1", PIP_NO_INPUT="1",
               PIP_DISABLE_PIP_VERSION_CHECK="1", PYTHONDONTWRITEBYTECODE="1",
               PYTHONHASHSEED="0", SOURCE_DATE_EPOCH="1700000000")
    wheel = _build("wheel", ROOT, tmp_path / "wheel", env)
    repeated = _build("wheel", ROOT, tmp_path / "repeat", env)
    sdist = _build("sdist", ROOT, tmp_path / "sdist", env)
    repeated_sdist = _build("sdist", ROOT, tmp_path / "repeat-sdist", env)
    editable = _build("editable", ROOT, tmp_path / "editable", env)
    assert wheel.read_bytes() == repeated.read_bytes(), "wheel not reproducible"
    assert sdist.read_bytes() == repeated_sdist.read_bytes(), "sdist not reproducible"
    source_members = _read_sdist(sdist, inputs)
    _assert_metadata(source_members["PKG-INFO"], manifest)
    source = tmp_path / "source"
    source.mkdir()
    # Only already-checked exact members are written. No generic archive extraction.
    for name, raw in source_members.items():
        (source / name).write_bytes(raw)
    rebuilt = _build("wheel", source, tmp_path / "rebuilt", env)
    assert wheel.read_bytes() == rebuilt.read_bytes(), "wheel-from-sdist differs"
    # Synthetic future module, package, data, and secret-shaped files stay outside
    # both distributions. These are fixtures in a temporary source tree only.
    for name in ("kfm.py", "kfm/__init__.py", "src/kfm/__init__.py", "data/quarantine/example.json", ".env"):
        path = source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# SYNTHETIC EXCLUSION CANARY\n")
    guarded = _build("wheel", source, tmp_path / "guarded", env)
    guarded_sdist = _build("sdist", source, tmp_path / "guarded-sdist", env)
    assert guarded.read_bytes() == wheel.read_bytes(), "future source payload leaked"
    _read_sdist(guarded_sdist, inputs)
    inventories = {}
    for label, artifact, is_editable in (("wheel", wheel, False), ("rebuilt", rebuilt, False),
                                         ("editable", editable, True), ("guarded", guarded, False)):
        members = _read_wheel(artifact)
        _assert_wheel(members, editable=is_editable)
        _assert_metadata(members[f"{DIST}/METADATA"], manifest)
        for name in ("LICENSE", "AUTHORS.md"):
            assert members[f"{DIST}/licenses/{name}"] == inputs[name]
        wheel_metadata = BytesParser().parsebytes(members[f"{DIST}/WHEEL"])
        assert wheel_metadata.get_all("Root-Is-Purelib") == ["true"]
        assert wheel_metadata.get_all("Tag") == ["py3-none-any"]
        inventories[label] = {"sha256": _digest(artifact.read_bytes()), "members": sorted(members)}
    pip = [sys.executable, "-I", "-m", "pip", "--isolated", "install",
           "--no-index", "--no-deps", "--no-cache-dir", "--ignore-installed",
           "--disable-pip-version-check", "--no-input"]
    ordinary_target, editable_target = tmp_path / "installed-wheel", tmp_path / "installed-editable"
    _run([*pip, "--target", str(ordinary_target), str(wheel)], cwd=tmp_path, env=env)
    _run([*pip, "--no-build-isolation", "--target", str(editable_target), "--editable", str(ROOT)],
         cwd=tmp_path, env=env)
    for target in (ordinary_target, editable_target):
        _verify_installed(target, manifest, env)
    direct = json.loads((editable_target / DIST / "direct_url.json").read_text())
    assert direct.get("dir_info", {}).get("editable") is True, "pip editable install not recorded"
    assert all((ROOT / name).read_bytes() == raw for name, raw in inputs.items()), "packaging mutated inputs"
    report = {"status": "PASS", "python": sys.version.split()[0], "tools": versions,
              "source_commit": _run(["git", "rev-parse", "HEAD"], cwd=ROOT, env=env),
              "input_sha256": {name: _digest(raw) for name, raw in inputs.items()},
              "artifacts": inventories, "sdist_sha256": _digest(sdist.read_bytes()),
              "sdist_members": sorted(source_members), "ordinary_and_editable_target_installs": "PASS",
              "network_boundary": "locked bootstrap precedes tests; build/install has no dependency resolution; not OS egress proof",
              "non_effects": "no SDK, CLI, source admission, approval, release, deployment, or publication"}
    print("\nKFM_ROOT_PYTHON_ARTIFACT_VERIFICATION=" + json.dumps(report, sort_keys=True))


def _assert_workflow(workflow: dict[str, Any]) -> None:
    assert set(workflow) == {"name", "on", "permissions", "concurrency", "jobs"}
    assert workflow["permissions"] == {"contents": "read"}
    assert set(workflow["on"]) == {"push", "pull_request"}
    push = workflow["on"]["push"]
    assert push["branches"] == ["main", "agent/kfm-python-distribution-boundary-20260911"]
    assert set(push["paths"]) == set(workflow["on"]["pull_request"]["paths"])
    assert {"pyproject.toml", "README.md", "LICENSE", ".gitignore", "hatch.toml",
            "AUTHORS*", "LICEN[CS]E*", "COPYING*", "NOTICE*", ".hgignore", "hatch_build.py",
            "tests/ci/test_root_python_distribution.py", "tools/ci/install_python_ci.py",
            "tools/ci/python-test.lock", ".github/workflows/root-python-distribution.yml"} == set(push["paths"])
    assert set(workflow["jobs"]) == {"artifacts"}
    job = workflow["jobs"]["artifacts"]
    assert set(job) == {"name", "runs-on", "timeout-minutes", "strategy", "env", "steps"}
    assert job["runs-on"] == "ubuntu-24.04" and job["timeout-minutes"] == 10
    assert job["strategy"] == {"fail-fast": False, "matrix": {"python-version": ["3.11", "3.12"]}}
    steps = job["steps"]
    assert len(steps) == 7
    assert set(steps[0]) == {"name", "uses", "with"}
    assert steps[0]["uses"] == "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1"
    assert steps[0]["with"] == {"persist-credentials": False, "fetch-depth": 0}
    assert set(steps[1]) == {"name", "uses", "with"}
    assert steps[1]["uses"] == "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97"
    assert steps[1]["with"] == {"python-version": "${{ matrix.python-version }}"}
    assert set(steps[2]) == {"name", "id", "run"}
    assert steps[2]["id"] == "bootstrap"
    assert steps[2]["run"] == ('python -m venv "$RUNNER_TEMP/kfm-root-python"\n'
                               '. "$RUNNER_TEMP/kfm-root-python/bin/activate"\n'
                               'python tools/ci/install_python_ci.py test-dependencies\n')
    assert set(steps[3]) == {"name", "run", "env"}
    assert steps[3]["env"] == {"KFM_RUN_ROOT_PYTHON_ARTIFACTS": "1", "PIP_NO_INDEX": "1"}
    assert steps[3]["run"] == ('. "$RUNNER_TEMP/kfm-root-python/bin/activate"\n'
                               'python -m pytest -q -s -p no:cacheprovider --strict-config --strict-markers tests/ci/test_root_python_distribution.py\n'
                               )
    # These checks remain independent after a successful bootstrap. An installer
    # failure must not hide security results or turn the overall job green.
    guard = "${{ !cancelled() && steps.bootstrap.outcome == 'success' }}"
    activate = '. "$RUNNER_TEMP/kfm-root-python/bin/activate"\n'
    assert steps[4:] == [
        {"name": "Verify existing installer contracts", "if": guard,
         "run": activate + "python -m unittest tests/ci/test_install_python_ci.py -v\n"},
        {"name": "Verify native workflow security", "if": guard,
         "run": activate + "make workflow-security\n"},
        {"name": "Verify tracked tree remains unchanged", "if": guard,
         "run": "git diff --exit-code"},
    ]


def _load_workflow() -> dict[str, Any]:
    import yaml

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader: Any, node: Any) -> dict[str, Any]:
        keys = [loader.construct_object(key, deep=True) for key, _ in node.value]
        assert len(keys) == len(set(keys)), "duplicate workflow key"
        return dict(zip(keys, [loader.construct_object(value, deep=True) for _, value in node.value]))

    UniqueLoader.add_constructor("tag:yaml.org,2002:map", mapping)
    return yaml.load((ROOT / ".github/workflows/root-python-distribution.yml").read_text(), Loader=UniqueLoader)


def test_artifact_workflow_requires_real_gate_and_read_only_permissions() -> None:
    _assert_workflow(_load_workflow())


@pytest.mark.parametrize("fault", ["write", "credentials", "skip-gate", "masked-job", "masked-step",
                                  "skip-installer-checks", "skip-workflow-security",
                                  "skip-security-after-failure", "masked-security", "skip-clean-tree",
                                  "missing-history", "shallow-history"])
def test_artifact_workflow_rejects_weakened_gate(fault: str) -> None:
    workflow = _load_workflow()
    job = workflow["jobs"]["artifacts"]
    if fault == "write":
        workflow["permissions"]["contents"] = "write"
    elif fault == "credentials":
        job["steps"][0]["with"]["persist-credentials"] = True
    elif fault == "missing-history":
        job["steps"][0]["with"].pop("fetch-depth")
    elif fault == "shallow-history":
        job["steps"][0]["with"]["fetch-depth"] = 1
    elif fault == "skip-gate":
        job["steps"][3]["env"].pop("KFM_RUN_ROOT_PYTHON_ARTIFACTS")
    elif fault == "masked-job":
        job["if"] = False
    elif fault in {"skip-installer-checks", "skip-workflow-security", "skip-clean-tree"}:
        index = {"skip-installer-checks": 4, "skip-workflow-security": 5, "skip-clean-tree": 6}[fault]
        job["steps"][index]["run"] = "true"
    elif fault == "skip-security-after-failure":
        job["steps"][5].pop("if")
    elif fault == "masked-security":
        job["steps"][5]["continue-on-error"] = True
    else:
        job["steps"][3]["continue-on-error"] = True
    with pytest.raises(AssertionError):
        _assert_workflow(workflow)
