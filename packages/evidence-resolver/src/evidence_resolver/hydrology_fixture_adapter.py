"""Read-only Hydrology fixture lookup for the first #2975 packet.

This module is an internal test adapter, not an evidence repository.  It reads
one closed manifest and one allowlisted synthetic Hydrology EvidenceBundle,
binds the complete parsed object to the manifest digest, and then delegates to
the existing candidate evaluator and conservative runtime projection.

No public ``ANSWER``, production lookup, source activation, model call,
persistence, release, deployment, or publication behavior is provided here.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
from typing import Mapping

from .core import (
    BoundedJSONError,
    CandidateInputError,
    MAX_INPUT_BYTES,
    MAX_STRING_LENGTH,
    PROFILE,
    ResolutionCandidate,
    ResolutionIssue,
    _validate_evidence_bundle,
    evaluate_resolution_candidate,
    loads_bounded,
)
from .runtime_projection import RuntimePosture, project_runtime_posture


ADAPTER_PROFILE = "kfm/hydrology-evidence-bundle-fixture-adapter/v1alpha1"
DIGEST_PROFILE = "kfm/evidence-bundle-fixture-digest/v1alpha1"

_REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
_MANIFEST_RELATIVE_PATH = PurePosixPath(
    "fixtures/packages/evidence_resolver/v1alpha1/repository/"
    "hydrology_bundle_manifest.json"
)
_ALLOWED_FIXTURE_ROOT = PurePosixPath(
    "fixtures/domains/hydrology/evidence_bundle/valid"
)
_ALLOWED_FIXTURE_PATH = _ALLOWED_FIXTURE_ROOT / "valid_1.json"
_MANIFEST_FIELDS = frozenset(
    {
        "adapter_profile",
        "bundle_id",
        "fixture_path",
        "digest_profile",
        "expected_digest",
    }
)
_BUNDLE_ID = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_DIGEST = re.compile(r"^sha256:[a-f0-9]{64}$")


class FixtureAdapterError(ValueError):
    """Safe internal adapter failure with no reflected input values."""

    def __init__(self, code: str, checks: tuple[str, ...]) -> None:
        super().__init__(code)
        self.code = code
        self.checks = checks


@dataclass(frozen=True)
class HydrologyFixtureResolution:
    """Candidate result paired with its non-renderable runtime posture."""

    candidate: ResolutionCandidate
    runtime: RuntimePosture


@dataclass(frozen=True)
class _ManifestEntry:
    bundle_id: str
    fixture_path: PurePosixPath
    expected_digest: str


def _raise(code: str, checks: list[str]) -> None:
    raise FixtureAdapterError(code, tuple(checks))


def _adapter_error(issue: FixtureAdapterError) -> ResolutionCandidate:
    return ResolutionCandidate(
        profile=PROFILE,
        status="ERROR",
        bundle_id=None,
        checks_performed=issue.checks,
        issues=(ResolutionIssue(issue.code, "fixture_adapter"),),
    )


def _decorate(
    result: ResolutionCandidate, adapter_checks: list[str]
) -> ResolutionCandidate:
    return ResolutionCandidate(
        profile=result.profile,
        status=result.status,
        bundle_id=result.bundle_id,
        checks_performed=tuple(
            dict.fromkeys((*adapter_checks, *result.checks_performed))
        ),
        issues=result.issues,
    )


def _parse_failure_code(kind: str, issue: BoundedJSONError) -> str:
    suffix = issue.code.removeprefix("input/").replace("/", "-")
    return f"fixture-adapter/{kind}-{suffix}"


def _reject_symlink_components(
    repository_root: Path,
    target: Path,
    *,
    checks: list[str],
    unreadable_code: str,
) -> None:
    try:
        relative = target.relative_to(repository_root)
    except ValueError:
        _raise("fixture-adapter/path-outside-root", checks)

    current = repository_root
    for component in relative.parts:
        current = current / component
        try:
            mode = current.lstat().st_mode
        except OSError:
            _raise(unreadable_code, checks)
        if stat.S_ISLNK(mode):
            _raise("fixture-adapter/path-symlink", checks)


def _read_repository_file(
    relative_path: PurePosixPath,
    *,
    checks: list[str],
    unreadable_code: str,
    allowed_root: PurePosixPath | None = None,
) -> bytes:
    repository_root = _REPOSITORY_ROOT.absolute()
    target = repository_root.joinpath(*relative_path.parts)
    _reject_symlink_components(
        repository_root,
        target,
        checks=checks,
        unreadable_code=unreadable_code,
    )

    try:
        resolved_target = target.resolve(strict=True)
        resolved_repository_root = repository_root.resolve(strict=True)
    except OSError:
        _raise(unreadable_code, checks)
    if not resolved_target.is_relative_to(resolved_repository_root):
        _raise("fixture-adapter/path-outside-root", checks)

    if allowed_root is not None:
        allowlisted = repository_root.joinpath(*allowed_root.parts)
        try:
            resolved_allowlisted = allowlisted.resolve(strict=True)
        except OSError:
            _raise(unreadable_code, checks)
        if not resolved_target.is_relative_to(resolved_allowlisted):
            _raise("fixture-adapter/path-outside-root", checks)

    try:
        if not resolved_target.is_file():
            _raise(unreadable_code, checks)
        if resolved_target.stat().st_size > MAX_INPUT_BYTES:
            _raise(f"{unreadable_code}-too-large", checks)
        with resolved_target.open("rb") as handle:
            payload = handle.read(MAX_INPUT_BYTES + 1)
    except FixtureAdapterError:
        raise
    except OSError:
        _raise(unreadable_code, checks)
    if len(payload) > MAX_INPUT_BYTES:
        _raise(f"{unreadable_code}-too-large", checks)
    return payload


def _manifest_entry(value: object, checks: list[str]) -> _ManifestEntry:
    if not isinstance(value, Mapping) or set(value) != _MANIFEST_FIELDS:
        _raise("fixture-adapter/manifest-entry-invalid", checks)
    if value["adapter_profile"] != ADAPTER_PROFILE:
        _raise("fixture-adapter/adapter-profile-unsupported", checks)
    if value["digest_profile"] != DIGEST_PROFILE:
        _raise("fixture-adapter/digest-profile-unsupported", checks)

    bundle_id = value["bundle_id"]
    if (
        not isinstance(bundle_id, str)
        or len(bundle_id) > MAX_STRING_LENGTH
        or not _BUNDLE_ID.fullmatch(bundle_id)
    ):
        _raise("fixture-adapter/manifest-bundle-id-invalid", checks)

    expected_digest = value["expected_digest"]
    if not isinstance(expected_digest, str) or not _DIGEST.fullmatch(
        expected_digest
    ):
        _raise("fixture-adapter/expected-digest-invalid", checks)

    fixture_path = value["fixture_path"]
    if not isinstance(fixture_path, str) or len(fixture_path) > MAX_STRING_LENGTH:
        _raise("fixture-adapter/path-invalid", checks)
    if fixture_path.startswith("/") or PurePosixPath(fixture_path).is_absolute():
        _raise("fixture-adapter/path-absolute", checks)
    if "\\" in fixture_path:
        _raise("fixture-adapter/path-invalid", checks)
    raw_components = fixture_path.split("/")
    if ".." in raw_components:
        _raise("fixture-adapter/path-traversal", checks)
    if any(component in {"", "."} for component in raw_components):
        _raise("fixture-adapter/path-invalid", checks)

    pure_path = PurePosixPath(fixture_path)
    try:
        pure_path.relative_to(_ALLOWED_FIXTURE_ROOT)
    except ValueError:
        _raise("fixture-adapter/path-outside-root", checks)
    if pure_path != _ALLOWED_FIXTURE_PATH:
        _raise("fixture-adapter/path-not-allowlisted", checks)

    return _ManifestEntry(
        bundle_id=bundle_id,
        fixture_path=pure_path,
        expected_digest=expected_digest,
    )


def _load_manifest(checks: list[str]) -> _ManifestEntry:
    payload = _read_repository_file(
        _MANIFEST_RELATIVE_PATH,
        checks=checks,
        unreadable_code="fixture-adapter/manifest-unreadable",
    )
    checks.append("fixture_manifest_bounded_read")
    try:
        manifest = loads_bounded(payload)
    except BoundedJSONError as exc:
        _raise(_parse_failure_code("manifest", exc), checks)
    if not isinstance(manifest, Mapping) or set(manifest) != {"entries"}:
        _raise("fixture-adapter/manifest-shape-invalid", checks)
    entries = manifest["entries"]
    if not isinstance(entries, list) or not entries:
        _raise("fixture-adapter/manifest-shape-invalid", checks)

    parsed_entries = [_manifest_entry(entry, checks) for entry in entries]
    identities = [entry.bundle_id for entry in parsed_entries]
    if len(identities) != len(set(identities)):
        _raise("fixture-adapter/duplicate-id", checks)
    if len(parsed_entries) != 1:
        _raise("fixture-adapter/manifest-entry-count", checks)
    checks.append("fixture_manifest_closed_shape")
    return parsed_entries[0]


def _canonical_digest(value: object) -> str:
    canonical = json.dumps(
        value,
        ensure_ascii=True,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _load_candidate(
    requested_bundle_id: str,
    entry: _ManifestEntry,
    checks: list[str],
) -> object | None:
    checks.append("fixture_manifest_identity_lookup")
    if requested_bundle_id != entry.bundle_id:
        return None

    payload = _read_repository_file(
        entry.fixture_path,
        checks=checks,
        unreadable_code="fixture-adapter/bundle-unreadable",
        allowed_root=_ALLOWED_FIXTURE_ROOT,
    )
    checks.append("fixture_bundle_bounded_read")
    try:
        candidate = loads_bounded(payload)
    except BoundedJSONError as exc:
        _raise(_parse_failure_code("bundle", exc), checks)
    checks.append("fixture_bundle_bounded_parse")

    if _canonical_digest(candidate) != entry.expected_digest:
        _raise("fixture-adapter/digest-mismatch", checks)
    checks.append("fixture_bundle_digest_binding")

    if not isinstance(candidate, Mapping):
        _raise("fixture-adapter/bundle-identity-invalid", checks)
    candidate_bundle_id = candidate.get("bundle_id")
    if (
        candidate_bundle_id != requested_bundle_id
        or candidate_bundle_id != entry.bundle_id
    ):
        _raise("fixture-adapter/bundle-id-mismatch", checks)
    checks.append("fixture_bundle_identity_binding")

    try:
        _validate_evidence_bundle(candidate)
    except CandidateInputError as exc:
        _raise(exc.code, checks)
    checks.append("shared_hydrology_evidence_bundle_shape")
    return candidate


def _request_with_lookup(
    request: object,
    *,
    candidate: object | None,
    resolved_bundle_id: str | None,
    checks: list[str],
) -> object:
    if not isinstance(request, Mapping):
        _raise("fixture-adapter/request-invalid", checks)
    if request.get("bundle_candidate") is not None:
        _raise("fixture-adapter/caller-bundle-forbidden", checks)

    prepared = dict(request)
    prepared["bundle_candidate"] = candidate
    lookup = prepared.get("lookup_context")
    if isinstance(lookup, Mapping):
        prepared_lookup = dict(lookup)
        prepared_lookup["bundle_id"] = resolved_bundle_id
        prepared["lookup_context"] = prepared_lookup
    return prepared


def resolve_hydrology_fixture(
    bundle_id: str, request: object
) -> HydrologyFixtureResolution:
    """Resolve one stable ID through the fixed fixture manifest.

    The function accepts no filesystem path.  A manifest miss is delegated to
    the existing evaluator as an unresolved candidate.  Adapter integrity or
    configuration failures become finite ``ERROR`` results.  Every result is
    immediately projected through the existing non-authoritative runtime map.
    """

    checks: list[str] = ["fixture_adapter_profile"]
    try:
        if (
            not isinstance(bundle_id, str)
            or len(bundle_id) > MAX_STRING_LENGTH
            or not _BUNDLE_ID.fullmatch(bundle_id)
        ):
            _raise("fixture-adapter/bundle-id-invalid", checks)
        if not isinstance(request, Mapping):
            _raise("fixture-adapter/request-invalid", checks)
        if request.get("bundle_candidate") is not None:
            _raise("fixture-adapter/caller-bundle-forbidden", checks)
        entry = _load_manifest(checks)
        candidate = _load_candidate(bundle_id, entry, checks)
        prepared = _request_with_lookup(
            request,
            candidate=candidate,
            resolved_bundle_id=entry.bundle_id if candidate is not None else None,
            checks=checks,
        )
        evaluated = evaluate_resolution_candidate(prepared)
        result = _decorate(evaluated, checks)
    except FixtureAdapterError as exc:
        result = _adapter_error(exc)

    return HydrologyFixtureResolution(
        candidate=result,
        runtime=project_runtime_posture(result),
    )
