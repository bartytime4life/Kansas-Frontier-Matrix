#!/usr/bin/env python3
"""Authenticated read-only GitHub issue inventory probe.

Live mode performs GET requests only and never serializes credentials. Fixture mode is
used by CI so deterministic tests remain no-network.
"""
from __future__ import annotations

import argparse, hashlib, json, os, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://api.github.com"
PROFILE = "PROPOSED_INACTIVE"
VERSION = "1.0.0"


def _canon(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _iso(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _digest(record):
    payload = {k: v for k, v in record.items() if k not in {"receipt_id", "response_digest"}}
    return hashlib.sha256(_canon(payload).encode()).hexdigest()


def build_record(*, repository, repo_payload, ref_payload, issue_payloads, headers, requested_issue_ids, retrieved_at, max_age_seconds=300):
    ids = sorted(set(requested_issue_ids))
    if ids != list(requested_issue_ids) or not ids or any(not isinstance(x, int) or isinstance(x, bool) or x < 1 for x in ids):
        raise ValueError("requested issue ids must be sorted unique positive integers")
    if repo_payload.get("full_name") != repository or not isinstance(repo_payload.get("id"), int):
        raise ValueError("repository binding mismatch")
    branch = repo_payload.get("default_branch")
    ref_name = ref_payload.get("ref")
    sha = (ref_payload.get("object") or {}).get("sha")
    if ref_name != f"refs/heads/{branch}" or not isinstance(sha, str) or len(sha) != 40:
        raise ValueError("default branch ref binding mismatch")
    rows = []
    for issue in issue_payloads:
        if "pull_request" in issue:
            raise ValueError("pull request returned through issue endpoint")
        rows.append({"number": issue["number"], "state": issue["state"].upper(), "updated_at": issue["updated_at"]})
    rows.sort(key=lambda row: row["number"])
    if [row["number"] for row in rows] != ids:
        raise ValueError("issue response set mismatch")
    remaining_raw = headers.get("x-ratelimit-remaining")
    remaining = int(remaining_raw) if remaining_raw is not None else None
    reset_raw = headers.get("x-ratelimit-reset")
    reset_at = _iso(datetime.fromtimestamp(int(reset_raw), tz=timezone.utc)) if reset_raw else None
    stale_at = retrieved_at + timedelta(seconds=max_age_seconds)
    outcome = "HOLD_RATE_LIMIT" if remaining == 0 else "FRESH"
    record = {
        "schema_version": VERSION,
        "profile_state": PROFILE,
        "receipt_id": "",
        "outcome": outcome,
        "repository": repository,
        "repository_id": repo_payload["id"],
        "default_branch": branch,
        "default_branch_head_sha": sha,
        "requested_issue_ids": ids,
        "issues": rows,
        "retrieved_at": _iso(retrieved_at),
        "stale_at": _iso(stale_at),
        "rate_limit_remaining": remaining,
        "rate_limit_reset_at": reset_at,
        "response_digest": "",
        "repository_mutation_allowed": False,
        "authority_created": False,
        "evidence_created": False,
        "release_authorized": False,
        "publication_authorized": False,
        "public_use_allowed": False,
    }
    digest = _digest(record)
    record["response_digest"] = f"sha256:{digest}"
    record["receipt_id"] = f"kfm:github-issue-read:{digest[:24]}"
    return record


def freshness(record, now):
    return "STALE" if now > _parse(record["stale_at"]) else record["outcome"]


def _get_json(path, token):
    req = Request(API + path, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}", "User-Agent": "kfm-read-only-probe", "X-GitHub-Api-Version": "2022-11-28"}, method="GET")
    with urlopen(req, timeout=15) as response:
        return json.loads(response.read().decode("utf-8")), {k.lower(): v for k, v in response.headers.items()}


def read_live(repository, issue_ids, token, now):
    repo, repo_headers = _get_json(f"/repos/{repository}", token)
    branch = repo["default_branch"]
    ref, ref_headers = _get_json(f"/repos/{repository}/git/ref/heads/{branch}", token)
    issues, headers = [], dict(repo_headers)
    headers.update(ref_headers)
    for number in issue_ids:
        issue, issue_headers = _get_json(f"/repos/{repository}/issues/{number}", token)
        issues.append(issue)
        headers.update(issue_headers)
    return build_record(repository=repository, repo_payload=repo, ref_payload=ref, issue_payloads=issues, headers=headers, requested_issue_ids=issue_ids, retrieved_at=now)


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--repository", required=True)
    p.add_argument("--issue", type=int, action="append", required=True)
    p.add_argument("--fixture", type=Path)
    p.add_argument("--now")
    args = p.parse_args(argv)
    issue_ids = sorted(set(args.issue))
    now = _parse(args.now) if args.now else datetime.now(timezone.utc)
    try:
        if args.fixture:
            payload = json.loads(args.fixture.read_text())
            record = build_record(repository=args.repository, repo_payload=payload["repository"], ref_payload=payload["ref"], issue_payloads=payload["issues"], headers=payload.get("headers", {}), requested_issue_ids=issue_ids, retrieved_at=now)
        else:
            token = os.getenv("KFM_GITHUB_READ_TOKEN") or os.getenv("GITHUB_TOKEN")
            if not token:
                print(_canon({"outcome": "HOLD_AUTH", "repository_mutation_allowed": False}), file=sys.stderr)
                return 2
            record = read_live(args.repository, issue_ids, token, now)
        print(_canon(record))
        return 0 if record["outcome"] == "FRESH" else 2
    except (HTTPError, URLError, OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(_canon({"outcome": "ERROR", "error_class": type(exc).__name__, "repository_mutation_allowed": False}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
