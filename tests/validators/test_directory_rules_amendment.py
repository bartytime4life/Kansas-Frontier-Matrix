"""ADR-0039 proposal-carrier integrity; never adoption or topology enforcement.

The current adopted bytes supply the predecessor, so a shallow checkout works.
Only a disposable Git repository is patched. Candidate metadata stays in ADR-0039;
these tests do not create another registry or activate any proposed obligation.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Callable
import hashlib
import os
from pathlib import Path
import re
import subprocess

import pytest
import yaml

from tools.validators.directory_governance.validate_root_registry import (
    ADOPTED_DOCTRINE_SHA256,
)

ROOT = Path(__file__).resolve().parents[2]
DOCTRINE = "docs/doctrine/directory-rules.md"
ADR = "docs/adr/ADR-0039-directory-build-and-verification-profiles.md"
PATCH = "docs/adr/directory-rules-v2.1.0-draft.1.patch"
PROFILE = "docs/architecture/directory-implementation-profiles.md"
INVENTORY = "docs/architecture/directory-current-state-20260905.md"
WORKFLOW = ".github/workflows/docs-control-plane.yml"
PATCH_ROW = "[Replacement diff](./directory-rules-v2.1.0-draft.1.patch) SHA-256"
MAX_BYTES = 512 * 1024
ADDED_IDS = {
    "DIR-AUTH-005", "DIR-PROFILE-001", "DIR-DEP-004",
    "DIR-BUILD-001", "DIR-BUILD-002", "DIR-BUILD-003",
    "DIR-TEST-001", "DIR-TEST-002", "DIR-TEST-003",
}


def _read(root: Path, name: str) -> bytes:
    if Path(name).is_absolute() or ".." in Path(name).parts:
        raise ValueError("INPUT_PATH_SCOPE")
    path = root / name
    # Reject symlinked ancestors as well as files; never read an escaped input.
    for part in (path, *path.parents):
        if part == root:
            break
        if part.is_symlink():
            raise ValueError("INPUT_SYMLINK")
    if not path.is_file():
        raise ValueError("INPUT_NOT_FILE")
    with path.open("rb") as stream:
        data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("INPUT_TOO_LARGE")
    data.decode("utf-8")
    return data


def _digest_row(adr: str, label: str, width: int = 64) -> str:
    rows = [line.split("|")[2].strip() for line in adr.splitlines()
            if line.startswith(f"| {label} |")]
    if len(rows) != 1:
        raise ValueError("DIGEST_ROW_NOT_UNIQUE")
    values = re.findall(r"`([0-9a-f]{" + str(width) + r"})`", rows[0])
    if len(values) != 1:
        raise ValueError("DIGEST_ROW_INVALID")
    return values[0]


def _bound(data: bytes, expected: str) -> None:
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("DIGEST_MISMATCH")


def _git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def _reconstruct(predecessor: bytes, patch: bytes, work: Path) -> bytes:
    if not patch.endswith(b"\n"):
        raise ValueError("PATCH_FINAL_NEWLINE")
    lines = patch.splitlines()
    if not lines[-1].strip():
        raise ValueError("PATCH_TRAILING_CONTEXT")
    if ([line for line in lines if line.startswith(b"--- ")] !=
            [b"--- a/docs/doctrine/directory-rules.md"] or
            [line for line in lines if line.startswith(b"+++ ")] !=
            [b"+++ b/docs/doctrine/directory-rules.md"]):
        raise ValueError("PATCH_TARGET_SCOPE")
    if any(line.startswith((b"diff --git ", b"GIT binary patch", b"rename ",
                            b"new file mode ", b"deleted file mode ")) for line in lines):
        raise ValueError("PATCH_FORMAT_SCOPE")
    work.mkdir(parents=True, exist_ok=False)
    target = work / DOCTRINE
    target.parent.mkdir(parents=True)
    target.write_bytes(predecessor)
    # No inherited Git directory/index/config may route writes into the source tree.
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
               GIT_TERMINAL_PROMPT="0", GIT_CEILING_DIRECTORIES=str(work.parent))

    def git(*args: str, data: bytes | None = None) -> None:
        result = subprocess.run(["git", *args], input=data, cwd=work, env=env,
                                capture_output=True, timeout=15, check=False)
        if result.returncode:
            raise ValueError("PATCH_GIT_FAILURE: " + result.stderr.decode("utf-8", "replace"))

    git("init", "--quiet")
    git("apply", "--check", "--whitespace=error", "-", data=patch)
    git("apply", "--whitespace=error", "-", data=patch)
    candidate = target.read_bytes()
    git("apply", "--reverse", "--check", "--whitespace=error", "-", data=patch)
    git("apply", "--reverse", "--whitespace=error", "-", data=patch)
    if target.read_bytes() != predecessor:
        raise ValueError("PATCH_ROUNDTRIP")
    return candidate


def _rules(data: bytes) -> dict[str, str]:
    rules: dict[str, str] = {}
    for line in data.decode("utf-8").splitlines():
        match = re.match(r"^`(DIR-[A-Z]+-[0-9]{3})` — ", line)
        if match:
            rule_id = match[1]
            if rule_id in rules:
                raise ValueError("RULE_ID_DUPLICATE")
            rules[rule_id] = line
    return rules


def _preserved(predecessor: bytes, candidate: bytes) -> None:
    before, after = _rules(predecessor), _rules(candidate)
    if len(before) != 94 or any(after.get(key) != value for key, value in before.items()):
        raise ValueError("RETAINED_RULE_CHANGED")
    if set(after) - set(before) != ADDED_IDS:
        raise ValueError("ADDED_RULE_SET_CHANGED")
    old, new = predecessor.decode("utf-8"), candidate.decode("utf-8")
    headings = Counter(line for line in old.splitlines() if line.startswith("#"))
    headings.pop("## Directory Rules v2.0.0-draft.1")
    if headings - Counter(line for line in new.splitlines() if line.startswith("#")):
        raise ValueError("HEADING_REMOVED")
    anchors = set(re.findall(r'<a id="([^"]+)"', old)) | {"directory-rules-v200-draft1"}
    if not anchors.issubset(set(re.findall(r'<a id="([^"]+)"', new))):
        raise ValueError("ANCHOR_REMOVED")


def _validate(root: Path, work: Path) -> bytes:
    predecessor = _read(root, DOCTRINE)
    adr = _read(root, ADR).decode("utf-8")
    if (re.findall(r"^status: (.+)$", adr, re.M) != ["proposed"] or
            re.findall(r"^effective_decision_status: (.+)$", adr, re.M) != ["proposed"]):
        raise ValueError("PROPOSAL_STATUS_REQUIRED")
    _bound(predecessor, ADOPTED_DOCTRINE_SHA256)
    _bound(predecessor, _digest_row(adr, "Predecessor SHA-256"))
    assert _git_blob(predecessor) == _digest_row(adr, "Predecessor Git blob", 40)
    for path, label in ((PATCH, PATCH_ROW), (PROFILE, "Profile SHA-256"),
                        (INVENTORY, "Inventory SHA-256")):
        _bound(_read(root, path), _digest_row(adr, label))
    candidate = _reconstruct(predecessor, _read(root, PATCH), work)
    _bound(candidate, _digest_row(adr, "Candidate SHA-256"))
    assert _git_blob(candidate) == _digest_row(adr, "Candidate Git blob", 40)
    assert b"status: PROPOSED_FOR_ADOPTION\n" in candidate
    _preserved(predecessor, candidate)
    return candidate


def test_repository_candidate_is_byte_bound_reversible_and_non_active(tmp_path: Path) -> None:
    paths = (DOCTRINE, ADR, PATCH, PROFILE, INVENTORY)
    before = {path: _read(ROOT, path) for path in paths}
    candidate = _validate(ROOT, tmp_path / "review")
    assert len(_rules(candidate)) == 103
    assert before == {path: _read(ROOT, path) for path in paths}


@pytest.mark.parametrize("data", [b"changed\n", b"expected\r\n", b"\xef\xbb\xbfexpected\n"])
def test_digest_rejects_content_or_encoding_changes(data: bytes) -> None:
    with pytest.raises(ValueError, match="^DIGEST_MISMATCH$"):
        _bound(data, hashlib.sha256(b"expected\n").hexdigest())


@pytest.mark.parametrize("rows,code", [
    ("", "DIGEST_ROW_NOT_UNIQUE"),
    ("| digest | no digest |", "DIGEST_ROW_INVALID"),
    ("| digest | `bad` |", "DIGEST_ROW_INVALID"),
    (("| digest | `" + "0" * 64 + "` |\n") * 2, "DIGEST_ROW_NOT_UNIQUE"),
])
def test_digest_fields_fail_closed(rows: str, code: str) -> None:
    with pytest.raises(ValueError, match="^" + code + "$"):
        _digest_row(rows, "digest")


@pytest.mark.parametrize("mutation,code", [
    (lambda p: p.replace(b"@@ -3,7 +3,10 @@", b"@@ -3,8 +3,10 @@"), "PATCH_GIT_FAILURE"),
    (lambda p: p.replace(b"+++ b/docs/doctrine/directory-rules.md", b"+++ b/other.md"), "PATCH_TARGET_SCOPE"),
    (lambda p: p + b"--- a/other.md\n+++ b/other.md\n@@ -1 +1 @@\n-a\n+b\n", "PATCH_TARGET_SCOPE"),
    (lambda p: p.replace(b"+updated: 2026-09-05\n", b"+updated: 2026-09-05 \n"), "PATCH_GIT_FAILURE"),
    (lambda p: p + b" \n", "PATCH_TRAILING_CONTEXT"),
    (lambda p: p[:-1], "PATCH_FINAL_NEWLINE"),
    (lambda p: b"", "PATCH_FINAL_NEWLINE"),
    (lambda p: p + b"new file mode 100755\n", "PATCH_FORMAT_SCOPE"),
])
def test_patch_corruption_is_rejected(tmp_path: Path, mutation: Callable[[bytes], bytes], code: str) -> None:
    with pytest.raises(ValueError, match="^" + code):
        _reconstruct(_read(ROOT, DOCTRINE), mutation(_read(ROOT, PATCH)), tmp_path / "bad")


@pytest.mark.parametrize("mutation,code", [
    (lambda c: c.replace("`DIR-AUTH-004` — A change".encode(), "`DIR-AUTH-004` — Any change".encode()), "RETAINED_RULE_CHANGED"),
    (lambda c: c + "\n`DIR-AUTH-004` — duplicate\n".encode(), "RULE_ID_DUPLICATE"),
    (lambda c: c.replace("`DIR-BUILD-001` — ".encode(), "`DIR-BUILD-099` — ".encode()), "ADDED_RULE_SET_CHANGED"),
    (lambda c: c.replace(b"## 4. The responsibility signature", b"## Changed heading"), "HEADING_REMOVED"),
    (lambda c: c.replace(b'<a id="directory-rules-v200-draft1"></a>', b""), "ANCHOR_REMOVED"),
])
def test_retained_rules_and_fragments_cannot_disappear(tmp_path: Path, mutation: Callable[[bytes], bytes], code: str) -> None:
    predecessor = _read(ROOT, DOCTRINE)
    candidate = _reconstruct(predecessor, _read(ROOT, PATCH), tmp_path / "review")
    with pytest.raises(ValueError, match="^" + code + "$"):
        _preserved(predecessor, mutation(candidate))


def test_symlink_inputs_are_rejected(tmp_path: Path) -> None:
    outside = tmp_path / "outside"
    outside.write_text("not proposal content", encoding="utf-8")
    (tmp_path / "link").symlink_to(outside)
    with pytest.raises(ValueError, match="^INPUT_SYMLINK$"):
        _read(tmp_path, "link")


def test_oversized_input_is_rejected(tmp_path: Path) -> None:
    (tmp_path / "large").write_bytes(b"x" * (MAX_BYTES + 1))
    with pytest.raises(ValueError, match="^INPUT_TOO_LARGE$"):
        _read(tmp_path, "large")


def test_existing_ci_job_discovers_the_whole_suite() -> None:
    workflow = yaml.load(_read(ROOT, WORKFLOW), Loader=yaml.BaseLoader)
    assert set(workflow["jobs"]) == {
        "validate-control-plane-yaml", "registers-schema", "adr-index-coherence",
    }
    steps = workflow["jobs"]["adr-index-coherence"]["steps"]
    found = [step for step in steps if "tests/validators/test_directory_rules_amendment.py"
             in step.get("run", "")]
    assert len(found) == 1
    assert "if" not in found[0] and "continue-on-error" not in found[0]
    assert found[0]["run"].split() == [
        "python", "-m", "pytest", "tests/validators/test_directory_rules_amendment.py",
        "-q", "--strict-config", "--strict-markers",
    ]
    assert workflow["permissions"] == {"contents": "read"}


@pytest.mark.parametrize("path", [DOCTRINE, PATCH, PROFILE, INVENTORY])
def test_mutated_repository_artifact_is_not_rebound_implicitly(tmp_path: Path, path: str) -> None:
    root = tmp_path / "inputs"
    for name in (DOCTRINE, ADR, PATCH, PROFILE, INVENTORY):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(_read(ROOT, name))
    target = root / path
    target.write_bytes(target.read_bytes() + b"changed\n")
    with pytest.raises(ValueError, match="^DIGEST_MISMATCH$"):
        _validate(root, tmp_path / "review")


def test_proposed_record_cannot_silently_become_accepted(tmp_path: Path) -> None:
    root = tmp_path / "inputs"
    for name in (DOCTRINE, ADR):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(_read(ROOT, name))
    path = root / ADR
    path.write_bytes(path.read_bytes().replace(b"status: proposed\n", b"status: accepted\n"))
    with pytest.raises(ValueError, match="^PROPOSAL_STATUS_REQUIRED$"):
        _validate(root, tmp_path / "review")


def test_git_environment_cannot_redirect_the_temporary_patch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    outside = tmp_path / "outside"
    outside.mkdir()
    sentinel = outside / "do-not-touch"
    sentinel.write_bytes(b"original")
    monkeypatch.setenv("GIT_DIR", str(outside / ".git"))
    monkeypatch.setenv("GIT_WORK_TREE", str(outside))
    monkeypatch.setenv("GIT_INDEX_FILE", str(outside / "index"))
    _validate(ROOT, tmp_path / "review")
    assert sorted(p.name for p in outside.iterdir()) == ["do-not-touch"]
    assert sentinel.read_bytes() == b"original"


@pytest.mark.parametrize("name", ["../outside", "/outside"])
def test_input_paths_cannot_escape_the_review_root(tmp_path: Path, name: str) -> None:
    with pytest.raises(ValueError, match="^INPUT_PATH_SCOPE$"):
        _read(tmp_path, name)
