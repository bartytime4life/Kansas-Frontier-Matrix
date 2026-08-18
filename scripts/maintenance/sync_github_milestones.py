#!/usr/bin/env python3
"""Safely validate, preview, and apply KFM milestones M13-M24.

``validate`` is offline and is the default. ``plan`` is read-only. ``apply``
requires an environment token plus an exact repository confirmation. The tool
changes GitHub planning metadata only; it creates no KFM evidence, approval,
release, deployment, or publication state.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

API_ROOT = "https://api.github.com"
DEFAULT_MANIFEST = Path(__file__).with_name("github_milestones_m13_m24.json")
EXPECTED_IDS = tuple(f"M{number}" for number in range(13, 25))
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
PREFIX_RE = re.compile(r"^(M(?:1[3-9]|2[0-4]))(?:\s|$)")
MAX_MANIFEST_BYTES = 512 * 1024
MAX_RESPONSE_BYTES = 4 * 1024 * 1024


class ManifestError(ValueError):
    pass


class ApiError(RuntimeError):
    pass


class Hold(RuntimeError):
    pass


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ManifestError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _text(value: Any, field: str, limit: int) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ManifestError(f"{field} must be a non-empty string <= {limit} characters")
    return value


def _ints(value: Any, field: str) -> list[int]:
    if not isinstance(value, list):
        raise ManifestError(f"{field} must be an array")
    if any(isinstance(item, bool) or not isinstance(item, int) or item <= 0 for item in value):
        raise ManifestError(f"{field} must contain positive integers")
    if len(value) != len(set(value)):
        raise ManifestError(f"{field} contains duplicates")
    return value


def load_manifest(path: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    try:
        if not 0 < path.stat().st_size <= MAX_MANIFEST_BYTES:
            raise ManifestError("manifest size is outside the allowed range")
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_strict_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"cannot load manifest {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ManifestError("manifest root must be an object")
    if data.get("schema_version") != "kfm.github-milestones-manifest.v1":
        raise ManifestError("unsupported schema_version")

    repository = _text(data.get("repository"), "repository", 200)
    if not REPOSITORY_RE.fullmatch(repository):
        raise ManifestError("repository must use owner/name syntax")
    generated_at = _text(data.get("generated_at"), "generated_at", 32)
    try:
        date.fromisoformat(generated_at)
    except ValueError as exc:
        raise ManifestError("generated_at must be an ISO calendar date") from exc

    checkpoint = data.get("source_checkpoint")
    if not isinstance(checkpoint, dict) or not SHA_RE.fullmatch(str(checkpoint.get("main_sha", ""))):
        raise ManifestError("source_checkpoint.main_sha must be a lowercase 40-hex SHA")
    open_issues = _ints(checkpoint.get("open_issues"), "source_checkpoint.open_issues")
    _ints(checkpoint.get("open_pull_requests"), "source_checkpoint.open_pull_requests")

    policy = data.get("mutation_policy")
    expected_policy = {
        "create_state": "open",
        "due_on": None,
        "update_existing_descriptions": False,
        "replace_existing_issue_milestones": False,
    }
    if policy != expected_policy:
        raise ManifestError("mutation_policy must match the fail-closed packet policy")

    rows = data.get("milestones")
    if not isinstance(rows, list) or len(rows) != 12:
        raise ManifestError("milestones must contain exactly 12 records")
    mapped: list[int] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ManifestError(f"milestones[{index}] must be an object")
        milestone_id = _text(row.get("id"), f"milestones[{index}].id", 3)
        title = _text(row.get("title"), f"milestones[{index}].title", 255)
        _text(row.get("description"), f"milestones[{index}].description", 1024)
        issues = _ints(row.get("issues"), f"milestones[{index}].issues")
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise ManifestError(f"milestones[{index}].evidence must be non-empty")
        for evidence_index, item in enumerate(evidence):
            _text(item, f"milestones[{index}].evidence[{evidence_index}]", 500)
        if not title.startswith(f"{milestone_id} — "):
            raise ManifestError(f"{milestone_id} title prefix does not match its id")
        mapped.extend(issues)

    ids = tuple(row["id"] for row in rows)
    if ids != EXPECTED_IDS:
        raise ManifestError("milestone ids must be ordered exactly M13 through M24")
    titles = [row["title"] for row in rows]
    if len(titles) != len(set(titles)):
        raise ManifestError("milestone titles must be unique")
    if len(mapped) != len(set(mapped)):
        raise ManifestError("an issue may be mapped to at most one milestone")
    missing = sorted(set(mapped) - set(open_issues))
    if missing:
        raise ManifestError(f"mapped issues absent from checkpoint: {missing}")
    return data


class GitHubClient:
    def __init__(self, token: str | None) -> None:
        self.token = token

    def request(self, method: str, path: str, payload: Mapping[str, Any] | None = None) -> Any:
        if not path.startswith("/") or "//" in path or ".." in path:
            raise ApiError("unsafe GitHub API path")
        body = None if payload is None else json.dumps(payload, separators=(",", ":")).encode()
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "kfm-github-milestone-sync/1",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if body is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(f"{API_ROOT}{path}", data=body, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
                if len(raw) > MAX_RESPONSE_BYTES:
                    raise ApiError("GitHub response exceeded the safety limit")
                return json.loads(raw.decode()) if raw else None
        except urllib.error.HTTPError as exc:
            detail = exc.read(16_384).decode(errors="replace")
            raise ApiError(f"{method} {path} failed with HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise ApiError(f"{method} {path} failed: {exc.reason}") from exc
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise ApiError(f"{method} {path} returned invalid JSON: {exc}") from exc

    @staticmethod
    def repo_path(repository: str) -> str:
        return "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/", 1))

    def milestones(self, repository: str) -> list[dict[str, Any]]:
        repo = self.repo_path(repository)
        result: list[dict[str, Any]] = []
        for page in range(1, 21):
            batch = self.request("GET", f"/repos/{repo}/milestones?state=all&per_page=100&page={page}")
            if not isinstance(batch, list):
                raise ApiError("milestone list was not an array")
            result.extend(item for item in batch if isinstance(item, dict))
            if len(batch) < 100:
                return result
        raise ApiError("milestone pagination exceeded the safety limit")

    def issue(self, repository: str, number: int) -> dict[str, Any]:
        result = self.request("GET", f"/repos/{self.repo_path(repository)}/issues/{number}")
        if not isinstance(result, dict):
            raise ApiError(f"issue #{number} response was not an object")
        return result

    def create_milestone(self, repository: str, row: Mapping[str, Any]) -> dict[str, Any]:
        result = self.request(
            "POST",
            f"/repos/{self.repo_path(repository)}/milestones",
            {"title": row["title"], "description": row["description"], "state": "open"},
        )
        if not isinstance(result, dict):
            raise ApiError("create-milestone response was not an object")
        return result

    def assign(self, repository: str, issue: int, milestone: int) -> None:
        result = self.request(
            "PATCH",
            f"/repos/{self.repo_path(repository)}/issues/{issue}",
            {"milestone": milestone},
        )
        if not isinstance(result, dict):
            raise ApiError(f"issue #{issue} update was not an object")


def issue_milestone_title(issue: Mapping[str, Any]) -> str | None:
    milestone = issue.get("milestone")
    if milestone is None:
        return None
    if not isinstance(milestone, dict) or not isinstance(milestone.get("title"), str):
        raise Hold("issue contains an unreadable milestone binding")
    return milestone["title"]


def build_plan(
    manifest: Mapping[str, Any],
    remote: Sequence[Mapping[str, Any]],
    issues: Mapping[int, Mapping[str, Any]] | None = None,
) -> list[dict[str, str]]:
    by_title: dict[str, Mapping[str, Any]] = {}
    by_prefix: dict[str, list[Mapping[str, Any]]] = {}
    for item in remote:
        title = item.get("title")
        if not isinstance(title, str):
            continue
        if title in by_title:
            raise Hold(f"duplicate remote milestone title: {title}")
        by_title[title] = item
        match = PREFIX_RE.match(title)
        if match:
            by_prefix.setdefault(match.group(1), []).append(item)

    actions: list[dict[str, str]] = []
    for row in manifest["milestones"]:
        conflicts = [item for item in by_prefix.get(row["id"], []) if item.get("title") != row["title"]]
        if conflicts:
            raise Hold(f"{row['id']} already exists with a different title")
        exact = by_title.get(row["title"])
        if exact is None:
            actions.append({"action": "CREATE_MILESTONE", "subject": row["id"], "detail": row["title"]})
        else:
            if exact.get("state") != "open":
                raise Hold(f"existing milestone is not open: {row['title']}")
            detail = "exact title already exists"
            if exact.get("description") != row["description"]:
                detail += "; description drift preserved for review"
            actions.append({"action": "KEEP_MILESTONE", "subject": row["id"], "detail": detail})

    if issues is not None:
        for row in manifest["milestones"]:
            for number in row["issues"]:
                issue = issues.get(number)
                if issue is None:
                    raise Hold(f"issue #{number} was not inspected")
                if "pull_request" in issue or issue.get("state") != "open":
                    raise Hold(f"#{number} is not an open issue")
                current = issue_milestone_title(issue)
                if current is None:
                    actions.append({"action": "ASSIGN_ISSUE", "subject": f"#{number}", "detail": row["title"]})
                elif current == row["title"]:
                    actions.append({"action": "KEEP_ISSUE", "subject": f"#{number}", "detail": current})
                else:
                    raise Hold(f"issue #{number} already belongs to milestone '{current}'")
    return actions


def inspect_issues(client: GitHubClient, manifest: Mapping[str, Any]) -> dict[int, Mapping[str, Any]]:
    numbers = sorted({number for row in manifest["milestones"] for number in row["issues"]})
    return {number: client.issue(manifest["repository"], number) for number in numbers}


def emit(value: Any, as_json: bool) -> None:
    if as_json:
        print(json.dumps(value, indent=2, sort_keys=True))
    elif isinstance(value, list):
        for row in value:
            print(f"{row['action']}: {row['subject']} — {row['detail']}")
    else:
        print(value)


def apply_packet(
    client: GitHubClient,
    manifest: Mapping[str, Any],
    assign_issues: bool,
    as_json: bool,
) -> int:
    repository = manifest["repository"]
    before = client.milestones(repository)
    inspected = inspect_issues(client, manifest) if assign_issues else None
    preflight = build_plan(manifest, before, inspected)
    by_title = {item.get("title"): item for item in before if isinstance(item.get("title"), str)}
    created: list[str] = []
    for row in manifest["milestones"]:
        if row["title"] not in by_title:
            by_title[row["title"]] = client.create_milestone(repository, row)
            created.append(row["title"])

    refreshed = client.milestones(repository)
    by_title = {item.get("title"): item for item in refreshed if isinstance(item.get("title"), str)}
    missing = [row["title"] for row in manifest["milestones"] if row["title"] not in by_title]
    if missing:
        raise ApiError(f"post-create verification failed: {missing}")

    assigned: list[int] = []
    if assign_issues:
        assert inspected is not None
        for row in manifest["milestones"]:
            milestone_number = by_title[row["title"]].get("number")
            if isinstance(milestone_number, bool) or not isinstance(milestone_number, int):
                raise ApiError(f"milestone number missing for {row['title']}")
            for number in row["issues"]:
                if issue_milestone_title(inspected[number]) is None:
                    client.assign(repository, number, milestone_number)
                    assigned.append(number)
        for row in manifest["milestones"]:
            for number in row["issues"]:
                if issue_milestone_title(client.issue(repository, number)) != row["title"]:
                    raise ApiError(f"issue #{number} milestone verification failed")

    result = {
        "outcome": "APPLIED",
        "created_count": len(created),
        "kept_count": 12 - len(created),
        "assigned_count": len(assigned),
        "created_milestones": created,
        "assigned_issues": sorted(assigned),
        "preflight_actions": preflight,
        "due_dates": None,
        "release_or_publication_effect": False,
    }
    emit(result if as_json else f"APPLIED: {len(created)} created, {12-len(created)} kept, {len(assigned)} issues assigned.", as_json)
    return 0


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate, plan, or apply KFM milestones M13-M24.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--json", action="store_true")
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("validate", help="Validate offline; this is the default.")
    plan = commands.add_parser("plan", help="Read GitHub and print intended actions.")
    plan.add_argument("--assign-issues", action="store_true")
    apply_parser = commands.add_parser("apply", help="Create missing milestones and optionally assign issues.")
    apply_parser.add_argument("--confirm-repository", required=True)
    apply_parser.add_argument("--assign-issues", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    command = args.command or "validate"
    try:
        manifest = load_manifest(args.manifest)
        if command == "validate":
            result = {
                "outcome": "VALIDATED",
                "repository": manifest["repository"],
                "milestone_count": 12,
                "mapped_issue_count": sum(len(row["issues"]) for row in manifest["milestones"]),
                "source_main_sha": manifest["source_checkpoint"]["main_sha"],
                "network_used": False,
                "mutation_performed": False,
                "due_dates": None,
            }
            emit(result if args.json else "VALIDATED: 12 milestones, 10 mapped issues, no due dates, no network, no mutation.", args.json)
            return 0

        token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
        if command == "apply" and not token:
            raise ApiError("apply requires GITHUB_TOKEN or GH_TOKEN in the environment")
        if command == "apply" and args.confirm_repository != manifest["repository"]:
            raise Hold("--confirm-repository must exactly match the manifest repository")
        client = GitHubClient(token)
        if command == "plan":
            issue_rows = inspect_issues(client, manifest) if args.assign_issues else None
            emit(build_plan(manifest, client.milestones(manifest["repository"]), issue_rows), args.json)
            return 0
        if command == "apply":
            return apply_packet(client, manifest, args.assign_issues, args.json)
        raise ManifestError(f"unsupported command: {command}")
    except Hold as exc:
        print(f"HOLD: {exc}", file=sys.stderr)
        return 1
    except (ManifestError, ApiError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
