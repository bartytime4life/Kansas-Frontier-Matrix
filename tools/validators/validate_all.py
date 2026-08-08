#!/usr/bin/env python3
"""Run KFM validators from a bounded, deterministic registry.

This repository tool computes validation results only. It does not resolve
EvidenceRefs, evaluate policy, authenticate review, approve promotion, release,
or publish. Reports omit timing unless ``--include-timing`` is requested so
identical validator outputs produce identical JSON bytes.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

REGISTRY_SCHEMA_VERSION = "kfm.validator-orchestrator-registry.v1"
REPORT_SCHEMA_VERSION = "kfm.validator-orchestrator-report.v1"
DEFAULT_REGISTRY = Path("tools/validators/validator_registry.json")
EXIT_PASS = 0
EXIT_VALIDATION_FAILURE = 1
EXIT_ORCHESTRATOR_ERROR = 2
MAX_REGISTRY_BYTES = 512 * 1024
MAX_VALIDATORS = 256
MAX_CAPTURE_CHARS = 1_000_000
ID_RE = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
PROFILES = ("focused", "changed-area", "release-dry-run", "full")


class RegistryError(ValueError):
    """Unsafe or malformed orchestrator configuration."""


@dataclass(frozen=True)
class ValidatorSpec:
    validator_id: str
    script: str
    args: tuple[str, ...]
    path_globs: tuple[str, ...]
    timeout_seconds: int
    artifact_refs: tuple[str, ...]


@dataclass(frozen=True)
class Registry:
    registry_id: str
    registry_sha256: str
    profiles: Mapping[str, tuple[str, ...]]
    validators: tuple[ValidatorSpec, ...]

    @property
    def by_id(self) -> dict[str, ValidatorSpec]:
        return {item.validator_id: item for item in self.validators}


def _pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise RegistryError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _finite_constant(value: str) -> object:
    raise RegistryError(f"non-finite JSON number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise RegistryError(f"non-finite JSON number: {value}")
    return parsed


def _digest_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _digest_text(value: str) -> str:
    return _digest_bytes(value.encode("utf-8"))


def _safe_path(value: object, *, field: str, prefix: str | None = None) -> str:
    if not isinstance(value, str) or not value or len(value) > 512 or "\x00" in value:
        raise RegistryError(f"{field}: invalid path")
    if "\\" in value:
        raise RegistryError(f"{field}: backslashes are denied")
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or "." in parsed.parts or ".." in parsed.parts:
        raise RegistryError(f"{field}: path must be normalized and repository-relative")
    normalized = parsed.as_posix()
    if normalized != value or (prefix and not value.startswith(prefix)):
        raise RegistryError(f"{field}: path violates its required location")
    return value


def _strings(value: object, *, field: str, maximum: int) -> tuple[str, ...]:
    if not isinstance(value, list) or len(value) > maximum:
        raise RegistryError(f"{field}: expected a bounded array")
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item or len(item) > 512 or "\x00" in item:
            raise RegistryError(f"{field}[{index}]: expected a bounded non-empty string")
        result.append(item)
    if len(result) != len(set(result)):
        raise RegistryError(f"{field}: duplicate values are denied")
    return tuple(result)


def _load_json(path: Path) -> tuple[dict[str, object], bytes]:
    if path.is_symlink() or not path.is_file():
        raise RegistryError(f"registry file is missing or unsafe: {path}")
    if path.stat().st_size > MAX_REGISTRY_BYTES:
        raise RegistryError("registry file exceeds the size budget")
    raw = path.read_bytes()
    try:
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_finite_constant,
            parse_float=_finite_float,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, RegistryError) as exc:
        raise RegistryError(f"registry JSON is invalid: {type(exc).__name__}") from exc
    if not isinstance(value, dict):
        raise RegistryError("registry root must be an object")
    return value, raw


def load_registry(path: Path, repo_root: Path) -> Registry:
    data, raw = _load_json(path)
    if set(data) != {"schema_version", "registry_id", "profiles", "validators"}:
        raise RegistryError("registry root keys do not match the v1 contract")
    if data["schema_version"] != REGISTRY_SCHEMA_VERSION:
        raise RegistryError("unsupported registry schema_version")
    registry_id = data["registry_id"]
    if not isinstance(registry_id, str) or not registry_id.startswith("kfm://") or len(registry_id) > 256:
        raise RegistryError("registry_id must be a bounded kfm:// identifier")

    raw_validators = data["validators"]
    if not isinstance(raw_validators, list) or not raw_validators or len(raw_validators) > MAX_VALIDATORS:
        raise RegistryError("validators must be a non-empty bounded array")

    root = repo_root.resolve()
    validators: list[ValidatorSpec] = []
    seen: set[str] = set()
    exact_keys = {"id", "description", "script", "args", "path_globs", "timeout_seconds", "artifact_refs"}
    for index, item in enumerate(raw_validators):
        if not isinstance(item, dict) or set(item) != exact_keys:
            raise RegistryError(f"validators[{index}] does not match the v1 contract")
        validator_id = item["id"]
        if not isinstance(validator_id, str) or not ID_RE.fullmatch(validator_id):
            raise RegistryError(f"validators[{index}].id is invalid")
        if validator_id in seen:
            raise RegistryError(f"duplicate validator id: {validator_id}")
        seen.add(validator_id)
        description = item["description"]
        if not isinstance(description, str) or not description.strip() or len(description) > 512:
            raise RegistryError(f"validators[{validator_id}].description is invalid")
        script = _safe_path(item["script"], field=f"validators[{validator_id}].script", prefix="tools/validators/")
        if not script.endswith(".py"):
            raise RegistryError(f"validators[{validator_id}].script must be Python")
        script_path = root / script
        if script_path.is_symlink():
            raise RegistryError(f"validators[{validator_id}].script symlink is denied")
        try:
            script_path.resolve().relative_to(root)
        except ValueError as exc:
            raise RegistryError(f"validators[{validator_id}].script escapes the repository") from exc
        if not script_path.is_file():
            raise RegistryError(f"validators[{validator_id}].script is missing")
        args = _strings(item["args"], field=f"validators[{validator_id}].args", maximum=32)
        raw_globs = item["path_globs"]
        if not isinstance(raw_globs, list) or not raw_globs or len(raw_globs) > 128:
            raise RegistryError(f"validators[{validator_id}].path_globs must be non-empty")
        globs = tuple(
            _safe_path(value, field=f"validators[{validator_id}].path_globs")
            for value in raw_globs
        )
        if len(globs) != len(set(globs)):
            raise RegistryError(f"validators[{validator_id}].path_globs contains duplicates")
        timeout = item["timeout_seconds"]
        if isinstance(timeout, bool) or not isinstance(timeout, int) or not 1 <= timeout <= 600:
            raise RegistryError(f"validators[{validator_id}].timeout_seconds is invalid")
        artifacts = _strings(item["artifact_refs"], field=f"validators[{validator_id}].artifact_refs", maximum=64)
        validators.append(ValidatorSpec(validator_id, script, args, globs, timeout, artifacts))

    raw_profiles = data["profiles"]
    if not isinstance(raw_profiles, dict) or set(raw_profiles) != set(PROFILES):
        raise RegistryError("profiles must contain focused, changed-area, release-dry-run, and full")
    profiles: dict[str, tuple[str, ...]] = {}
    for name in PROFILES:
        ids = _strings(raw_profiles[name], field=f"profiles.{name}", maximum=MAX_VALIDATORS)
        unknown = sorted(set(ids) - seen)
        if unknown:
            raise RegistryError(f"profiles.{name} references unknown validators: {unknown}")
        if name != "changed-area" and not ids:
            raise RegistryError(f"profiles.{name} must be non-empty")
        profiles[name] = ids
    all_ids = tuple(item.validator_id for item in validators)
    if profiles["full"] != all_ids:
        raise RegistryError("profiles.full must list every validator exactly once in registry order")
    return Registry(registry_id, _digest_bytes(raw), profiles, tuple(validators))


def normalize_changed_paths(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(sorted({_safe_path(value.strip(), field="changed_path") for value in values if value.strip()}))


def read_changed_path_file(path: Path) -> tuple[str, ...]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 1024 * 1024:
        raise RegistryError(f"changed-path file is missing, unsafe, or too large: {path}")
    return normalize_changed_paths(path.read_text(encoding="utf-8").splitlines())


def select_validators(
    registry: Registry,
    *,
    profile: str,
    changed_paths: Sequence[str] = (),
    requested_ids: Sequence[str] = (),
) -> tuple[tuple[ValidatorSpec, ...], str]:
    by_id = registry.by_id
    if requested_ids:
        if len(requested_ids) != len(set(requested_ids)):
            raise RegistryError("explicit validator ids contain duplicates")
        unknown = [item for item in requested_ids if item not in by_id]
        if unknown:
            raise RegistryError(f"unknown explicit validator ids: {unknown}")
        return tuple(by_id[item] for item in requested_ids), "explicit"
    if profile not in registry.profiles:
        raise RegistryError(f"unknown profile: {profile}")
    if profile == "changed-area":
        selected = tuple(
            spec
            for spec in registry.validators
            if any(fnmatch.fnmatchcase(path, glob) for path in changed_paths for glob in spec.path_globs)
        )
        return selected, "changed-area"
    return tuple(by_id[item] for item in registry.profiles[profile]), "profile"


def _bounded(value: str) -> str:
    return value if len(value) <= MAX_CAPTURE_CHARS else value[:MAX_CAPTURE_CHARS] + "\n[TRUNCATED]\n"


def _run_one(spec: ValidatorSpec, *, repo_root: Path, include_timing: bool, verbose: bool) -> dict[str, object]:
    command = [sys.executable, str(repo_root / spec.script), *spec.args]
    env = os.environ.copy()
    env.update({
        "KFM_NO_NETWORK": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "PYTHONUNBUFFERED": "1",
        "TZ": "UTC",
    })
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=repo_root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=spec.timeout_seconds,
            check=False,
        )
        stdout, stderr = _bounded(completed.stdout), _bounded(completed.stderr)
        if completed.returncode == 0:
            status, reason = "PASS", "VALIDATOR_PASS"
        elif completed.returncode == 1:
            status, reason = "FAIL", "VALIDATOR_REJECTED"
        else:
            status, reason = "ERROR", "VALIDATOR_ERROR"
        return_code: int | None = completed.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = _bounded(exc.stdout if isinstance(exc.stdout, str) else "")
        stderr = _bounded(exc.stderr if isinstance(exc.stderr, str) else "")
        status, reason, return_code = "ERROR", "VALIDATOR_TIMEOUT", None
    if verbose:
        for channel, value in (("stdout", stdout), ("stderr", stderr)):
            if value:
                print(f"[{spec.validator_id}:{channel}]\n{value}", file=sys.stderr)
    result: dict[str, object] = {
        "validator_id": spec.validator_id,
        "status": status,
        "reason_code": reason,
        "return_code": return_code,
        "artifact_refs": list(spec.artifact_refs),
        "stdout_sha256": _digest_text(stdout),
        "stderr_sha256": _digest_text(stderr),
        "stdout_line_count": len(stdout.splitlines()),
        "stderr_line_count": len(stderr.splitlines()),
    }
    if include_timing:
        result["duration_ms"] = int(round((time.monotonic() - started) * 1000))
    return result


def orchestrate(
    registry: Registry,
    *,
    repo_root: Path,
    profile: str,
    changed_paths: Sequence[str] = (),
    requested_ids: Sequence[str] = (),
    include_timing: bool = False,
    verbose: bool = False,
) -> tuple[int, dict[str, object]]:
    selected, mode = select_validators(
        registry,
        profile=profile,
        changed_paths=changed_paths,
        requested_ids=requested_ids,
    )
    started = time.monotonic()
    base: dict[str, object] = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "registry_id": registry.registry_id,
        "registry_sha256": registry.registry_sha256,
        "profile": profile,
        "selection": {
            "mode": mode,
            "changed_paths": list(changed_paths),
            "requested_validator_ids": list(requested_ids),
        },
        "registered_count": len(registry.validators),
        "selected_count": len(selected),
        "timing_included": include_timing,
    }
    if not selected:
        base.update({
            "outcome": "ABSTAIN",
            "reason_code": "NO_MATCHING_VALIDATORS",
            "exit_code": EXIT_PASS,
            "results": [],
        })
        if include_timing:
            base["total_duration_ms"] = int(round((time.monotonic() - started) * 1000))
        return EXIT_PASS, base

    results = [
        _run_one(item, repo_root=repo_root, include_timing=include_timing, verbose=verbose)
        for item in selected
    ]
    if any(item["status"] == "ERROR" for item in results):
        outcome, reason, code = "ERROR", "ONE_OR_MORE_VALIDATOR_ERRORS", EXIT_ORCHESTRATOR_ERROR
    elif any(item["status"] == "FAIL" for item in results):
        outcome, reason, code = "FAIL", "ONE_OR_MORE_VALIDATORS_REJECTED", EXIT_VALIDATION_FAILURE
    else:
        outcome, reason, code = "PASS", "ALL_SELECTED_VALIDATORS_PASSED", EXIT_PASS
    base.update({"outcome": outcome, "reason_code": reason, "exit_code": code, "results": results})
    if include_timing:
        base["total_duration_ms"] = int(round((time.monotonic() - started) * 1000))
    return code, base


def _write(path: Path, text: str) -> None:
    if path.exists() and path.is_symlink():
        raise RegistryError(f"output symlink is denied: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    if temporary.exists() and temporary.is_symlink():
        raise RegistryError(f"temporary output symlink is denied: {temporary}")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default="full", choices=PROFILES)
    parser.add_argument("--validator", action="append", default=[])
    parser.add_argument("--changed-path", action="append", default=[])
    parser.add_argument("--changed-path-file", type=Path)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--include-timing", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--validate-registry", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo_root = (args.repo_root or Path(__file__).resolve().parents[2]).resolve()
    registry_path = args.registry if args.registry.is_absolute() else repo_root / args.registry
    try:
        registry = load_registry(registry_path, repo_root)
        if args.list:
            print(json.dumps({
                "registry_id": registry.registry_id,
                "registry_sha256": registry.registry_sha256,
                "profiles": {name: list(ids) for name, ids in sorted(registry.profiles.items())},
                "validators": [item.validator_id for item in registry.validators],
            }, indent=2, sort_keys=True))
            return EXIT_PASS
        if args.validate_registry:
            print(json.dumps({
                "outcome": "PASS",
                "reason_code": "REGISTRY_VALID",
                "registry_id": registry.registry_id,
                "registry_sha256": registry.registry_sha256,
                "validator_count": len(registry.validators),
            }, indent=2, sort_keys=True))
            return EXIT_PASS
        changed = list(args.changed_path)
        if args.changed_path_file:
            changed.extend(read_changed_path_file(args.changed_path_file))
        code, report = orchestrate(
            registry,
            repo_root=repo_root,
            profile=args.profile,
            changed_paths=normalize_changed_paths(changed),
            requested_ids=args.validator,
            include_timing=args.include_timing,
            verbose=args.verbose,
        )
        text = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.output:
            _write(args.output, text)
        if not args.quiet:
            print(text, end="")
        return code
    except RegistryError as exc:
        print(json.dumps({
            "schema_version": REPORT_SCHEMA_VERSION,
            "outcome": "ERROR",
            "reason_code": "ORCHESTRATOR_CONFIGURATION_ERROR",
            "exit_code": EXIT_ORCHESTRATOR_ERROR,
            "detail": str(exc),
        }, indent=2, sort_keys=True), file=sys.stderr)
        return EXIT_ORCHESTRATOR_ERROR
    except OSError as exc:
        print(json.dumps({
            "schema_version": REPORT_SCHEMA_VERSION,
            "outcome": "ERROR",
            "reason_code": "ORCHESTRATOR_IO_ERROR",
            "exit_code": EXIT_ORCHESTRATOR_ERROR,
            "detail": type(exc).__name__,
        }, indent=2, sort_keys=True), file=sys.stderr)
        return EXIT_ORCHESTRATOR_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
