"""One-time, inventory-pinned retirement of KFM's GitHub Vercel records."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import subprocess
import time
from urllib import error, request

REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix"
ENVIRONMENTS = frozenset({
    "Preview", "Production", "Preview – kfm", "Production – kfm",
    "Preview – usgs", "Production – usgs",
    "Preview – kansas-frontier-matrix-explorer-web",
    "Production – kansas-frontier-matrix-explorer-web",
})
CREATORS = frozenset({"vercel", "vercel[bot]"})
PREFIX = f"/repos/{REPOSITORY}/deployments"


class Stop(RuntimeError):
    pass


class APIError(Stop):
    def __init__(self, status):
        self.status = status
        super().__init__(f"GitHub HTTP {status}; stop and retain the inventory/journal")


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class GitHub:
    def __init__(self, token):
        if not token:
            raise Stop("GH_TOKEN is required; never pass a token as a command argument")
        self.token = token
        self.opener = request.build_opener(NoRedirect)

    def call(self, method, path, body=None):
        if not path.startswith(PREFIX) or method not in {"GET", "POST", "DELETE"}:
            raise Stop("Request outside the fixed repository deployment boundary")
        if method != "GET":
            time.sleep(1)  # Keep mutation traffic below common secondary limits.
        req = request.Request(
            "https://api.github.com" + path,
            data=None if body is None else json.dumps(body).encode(),
            method=method,
            headers={"Authorization": "Bearer " + self.token,
                     "Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2026-03-10",
                     "Content-Type": "application/json"},
        )
        try:
            with self.opener.open(req, timeout=30) as response:
                raw = response.read(8_388_609)
                if len(raw) > 8_388_608:
                    raise Stop("Oversized API response")
                return json.loads(raw) if raw else None
        except error.HTTPError as exc:
            raise APIError(exc.code) from None


class GitHubCLI:
    """Use an operator's existing gh authentication; never create credentials."""
    def call(self, method, path, body=None):
        if not path.startswith(PREFIX) or method not in {"GET", "POST", "DELETE"}:
            raise Stop("Request outside the fixed repository deployment boundary")
        if method != "GET":
            time.sleep(1)
        command = ["gh", "api", "--hostname", "github.com", "--include",
                   "--method", method, "--header", "Accept: application/vnd.github+json",
                   "--header", "X-GitHub-Api-Version: 2026-03-10", path.lstrip("/")]
        if body is not None:
            command += ["--input", "-"]
        try:
            result = subprocess.run(command, input=None if body is None else json.dumps(body).encode(),
                                    capture_output=True, timeout=40, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise Stop("GitHub CLI outcome is unverified; check access and run a fresh inventory") from None
        raw = result.stdout.replace(b"\r\n", b"\n")
        if len(raw) > 8_388_608:
            raise Stop("Oversized GitHub CLI response")
        header, separator, payload = raw.partition(b"\n\n")
        status = re.match(rb"HTTP/\S+ (\d{3})(?: |\n|$)", header)
        if not separator or status is None:
            raise Stop("GitHub CLI did not return HTTP metadata; check existing authentication/network")
        code = int(status.group(1))
        if code >= 300:
            raise APIError(code)
        if result.returncode:
            raise Stop("GitHub CLI failed; no automatic authentication or retry")
        return json.loads(payload) if payload.strip() else None


def inventory(api):
    selected, seen, ignored = [], set(), 0
    for page in range(1, 101):
        rows = api.call("GET", f"{PREFIX}?per_page=100&page={page}")
        if not isinstance(rows, list) or len(rows) > 100:
            raise Stop("Malformed deployment page")
        for row in rows:
            if not isinstance(row, dict):
                raise Stop("Malformed deployment record")
            identity = row.get("id")
            if type(identity) is not int or identity <= 0 or identity in seen:
                raise Stop("Invalid or duplicate deployment ID; inventory is not stable")
            seen.add(identity)
            creator = row.get("creator")
            actor = creator.get("login") if isinstance(creator, dict) else None
            environment = row.get("environment")
            if not isinstance(actor, str) or not isinstance(environment, str):
                raise Stop("Missing provider attribution or environment")
            if actor not in CREATORS or environment not in ENVIRONMENTS:
                ignored += 1
                continue
            sha, ref = row.get("sha"), row.get("ref")
            if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
                raise Stop("Invalid candidate source SHA")
            if not isinstance(ref, str) or not ref:
                raise Stop("Missing candidate source ref")
            selected.append({"id": identity, "sha": sha, "ref": ref,
                             "environment": environment, "creator": actor})
        if len(rows) < 100:
            snapshot = {"repository": REPOSITORY,
                        "deployments": sorted(selected, key=lambda x: x["id"])}
            return snapshot, ignored
    raise Stop("Pagination ceiling reached; inventory is incomplete")


def fingerprint(snapshot):
    return hashlib.sha256(json.dumps(snapshot, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def retire(api, snapshot, expected, journal):
    if not re.fullmatch(r"[0-9a-f]{64}", expected or "") or expected != fingerprint(snapshot):
        raise Stop("Inventory fingerprint mismatch; run a new read-only inventory")
    for item in snapshot["deployments"]:
        path = f"{PREFIX}/{item['id']}"
        journal({"id": item["id"], "action": "delete_attempt"})
        try:
            api.call("DELETE", path)
        except APIError as exc:
            if exc.status != 422:
                raise
            # An active record cannot be deleted. Inspect it before the one
            # bounded inactive-status transition; do not retry an inactive record.
            statuses = api.call("GET", path + "/statuses?per_page=1")
            if (not isinstance(statuses, list) or not statuses
                    or not isinstance(statuses[0], dict)
                    or statuses[0].get("state") not in {
                        "error", "failure", "pending", "in_progress", "queued", "success"}):
                raise Stop("422 without an eligible active status; no automatic retry") from None
            api.call("POST", path + "/statuses", {
                "state": "inactive", "auto_inactive": False,
                "description": "Owner-requested retirement of unused Vercel deployment record",
            })
            journal({"id": item["id"], "action": "marked_inactive"})
            api.call("DELETE", path)
        journal({"id": item["id"], "action": "deleted"})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--expected-digest", default="")
    parser.add_argument("--use-gh", action="store_true",
                        help="Use existing GitHub CLI authentication instead of GH_TOKEN")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.output.exists():
        raise Stop("Output directory already exists; preserve prior inventory/journal")
    api = GitHubCLI() if args.use_gh else GitHub(os.environ.get("GH_TOKEN"))
    snapshot, ignored = inventory(api)
    digest = fingerprint(snapshot)
    args.output.mkdir(parents=True)
    (args.output / "inventory.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (args.output / "sha256.txt").write_text(digest + "\n", encoding="ascii")
    print(json.dumps({"mode": "apply" if args.apply else "inventory", "selected":
                      len(snapshot["deployments"]), "ignored": ignored, "sha256": digest}), flush=True)
    if args.apply:
        with (args.output / "journal.jsonl").open("x", encoding="utf-8") as stream:
            def journal(row):
                stream.write(json.dumps(row) + "\n")
                stream.flush()
            retire(api, snapshot, args.expected_digest, journal)
        remaining, _ = inventory(api)
        if remaining["deployments"]:
            raise Stop("Vercel records remain; inspect before another pinned run")
        print("ELIGIBLE_VERCEL_GITHUB_RECORDS_ABSENT", flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (Stop, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
