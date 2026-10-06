#!/usr/bin/env python3
"""Explicit zero-cost downloads into a private, replaceable transport cache.

This operator is not a source registry, connector admission decision or release.
Provider originals stay remote; verified cache files can enter the existing
local-upload quarantine workflow only through a separately reviewed manifest.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))
from tools.local_data.file_io import (  # noqa: E402
    check_directory, fsync_directory, hash_regular, read_regular, write_new,
)
from tools.local_data.manage import (  # noqa: E402
    canonical, external_root, initialized, parse_json, utc_now,
)

CACHE_LIMIT = 500_000_000_000  # Owner-selected decimal 500 GB, about 465.7 GiB.
METADATA_RESERVE = 1024**2
CHUNK = 1024**2
MAX_PLAN = 2 * 1024**2
MAX_JOBS = 500
SCHEMA = "kfm-acquisition-inventory-v1"
SLUG = re.compile(r"[a-z][a-z0-9._-]{0,63}\Z")
SHA = re.compile(r"[0-9a-f]{64}\Z")
# Transport endpoints only: this is not an authoritative source registry.
# In particular, neither usgs-lidar (Requester Pays) nor any arbitrary S3
# bucket is admitted by a suffix wildcard.
PUBLIC_ENDPOINTS = {
    "usgs-lidar-public.s3.amazonaws.com": ("/",),
    "usgs-lidar-public.s3-us-west-2.amazonaws.com": ("/",),
    "prd-tnm.s3.amazonaws.com": ("/StagedProducts/",),
    "rockyweb.usgs.gov": ("/vdelivery/",),
    "www.ncei.noaa.gov": ("/pub/data/ghcn/daily/",),
    "data.nass.usda.gov": ("/Research_and_Science/Cropland/Release/",),
}
JOB_FIELDS = {"source_id", "dataset_id", "label", "source_url", "scope",
              "expected_bytes", "approved_max_bytes", "sha256", "temporal_start",
              "temporal_end", "estimate_basis", "rights_url"}


def validate_url(value: object) -> str:
    if (not isinstance(value, str) or len(value) > 2048
            or any(ord(c) <= 32 or ord(c) == 127 for c in value)
            or "\\" in value or "%" in value):
        raise ValueError("URL_NOT_ALLOWLISTED")
    url = urlsplit(value)
    if (url.scheme != "https" or url.username or url.password or url.port
            or url.query or url.fragment or url.hostname not in PUBLIC_ENDPOINTS
            or any(p in {".", ".."} for p in url.path.split("/"))
            or not any(url.path.startswith(p) for p in PUBLIC_ENDPOINTS[url.hostname])):
        raise ValueError("URL_NOT_ALLOWLISTED")
    return value


def validate_job(job: object) -> dict:
    if not isinstance(job, dict) or set(job) != JOB_FIELDS:
        raise ValueError("JOB_SHAPE_INVALID")
    for field in ("source_id", "dataset_id"):
        if not isinstance(job[field], str) or not SLUG.fullmatch(job[field]):
            raise ValueError("JOB_IDENTIFIER_INVALID")
    if (not isinstance(job["label"], str) or not 1 <= len(job["label"]) <= 160
            or any(ord(c) < 32 for c in job["label"])):
        raise ValueError("JOB_LABEL_INVALID")
    validate_url(job["source_url"])
    if job["scope"] not in {"kansas", "global"}:
        raise ValueError("SCOPE_INVALID")
    if job["estimate_basis"] not in {"provider", "calculated", "unknown"}:
        raise ValueError("ESTIMATE_BASIS_INVALID")
    for field in ("expected_bytes", "approved_max_bytes"):
        if job[field] is not None and (type(job[field]) is not int or not 1 <= job[field] <= CACHE_LIMIT):
            raise ValueError("BYTE_BOUND_INVALID")
    if (job["expected_bytes"] is not None and job["approved_max_bytes"] is not None
            and job["expected_bytes"] > job["approved_max_bytes"]):
        raise ValueError("BYTE_BOUND_CONFLICT")
    if job["sha256"] is not None and (not isinstance(job["sha256"], str) or not SHA.fullmatch(job["sha256"])):
        raise ValueError("CHECKSUM_INVALID")
    times = {}
    for field in ("temporal_start", "temporal_end"):
        if job[field] is not None and (not isinstance(job[field], str)
                or not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2}))?", job[field])):
            raise ValueError("TEMPORAL_VALUE_INVALID")
        if job[field] is not None:
            try:
                value = datetime.fromisoformat(job[field].replace("Z", "+00:00"))
                times[field] = value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value
            except ValueError:
                raise ValueError("TEMPORAL_VALUE_INVALID") from None
    if len(times) == 2 and times["temporal_start"] > times["temporal_end"]:
        raise ValueError("TEMPORAL_RANGE_REVERSED")
    if job["rights_url"] is not None:
        u = urlsplit(job["rights_url"])
        if (u.scheme != "https" or not u.hostname or u.username or u.password
                or u.query or u.fragment or len(job["rights_url"]) > 2048):
            raise ValueError("RIGHTS_URL_INVALID")
    return job


def load_plan(path: Path) -> list[dict]:
    value = parse_json(read_regular(path, MAX_PLAN))
    if (not isinstance(value, dict) or set(value) != {"schema_version", "jobs"}
            or value["schema_version"] != "kfm-acquisition-plan-v1"
            or not isinstance(value["jobs"], list) or not 1 <= len(value["jobs"]) <= MAX_JOBS):
        raise ValueError("PLAN_SHAPE_INVALID")
    jobs = [validate_job(job) for job in value["jobs"]]
    if len({job_id(job) for job in jobs}) != len(jobs):
        raise ValueError("DUPLICATE_JOB")
    return jobs


def job_id(job: dict) -> str:
    return hashlib.sha256(canonical(job)).hexdigest()


def block_reason(job: dict) -> str | None:
    if job["sha256"] is None:
        return "EXPECTED_CHECKSUM_REQUIRED"
    if job["expected_bytes"] is None and job["approved_max_bytes"] is None:
        return "SIZE_SELECTION_REQUIRED"
    return None


def project(job: dict, state: dict | None = None) -> dict:
    state = state or {}
    reason = state.get("reason") or block_reason(job)
    return {"job_id": job_id(job), "source_id": job["source_id"],
            "dataset_id": job["dataset_id"], "label": job["label"],
            "state": state.get("state", "blocked" if reason else "planned"),
            "reason": reason, "scope": job["scope"],
            "expected_bytes": job["expected_bytes"],
            "approved_max_bytes": job["approved_max_bytes"],
            "downloaded_bytes": state.get("downloaded_bytes", 0),
            "sha256": job["sha256"], "checksum_verified": state.get("checksum_verified", False),
            "temporal_start": job["temporal_start"], "temporal_end": job["temporal_end"],
            "estimate_basis": job["estimate_basis"], "rights_url": job["rights_url"],
            "storage": "local-replaceable-cache" if state.get("downloaded_bytes", 0) else "provider-remote",
            "source_url": job["source_url"], "updated_at": state.get("updated_at", utc_now()),
            "protected": state.get("protected", False)}


def cache_root(root: Path) -> Path:
    return root / "data/work/acquisition-cache"


def validate_root(root: Path) -> None:
    if external_root(str(root)) != root:
        raise ValueError("STORE_PATH_NOT_CANONICAL")
    if not initialized(root):
        raise ValueError("STORE_NOT_INITIALIZED")
    if root.stat().st_uid != os.getuid() or stat.S_IMODE(root.stat().st_mode) & 0o077:
        raise ValueError("STORE_NOT_OWNER_PRIVATE")


def usage(root: Path) -> dict:
    """Count every regular cache file, including unrecognized files; never evict them."""
    base = cache_root(root)
    result = {"limit_bytes": CACHE_LIMIT, "used_bytes": 0,
              "temporary_bytes": 0, "replaceable_bytes": 0, "inspected": True}
    if not base.exists() and not base.is_symlink():
        return result
    check_directory(base)
    if base.stat().st_uid != os.getuid() or stat.S_IMODE(base.stat().st_mode) & 0o077:
        raise ValueError("CACHE_NOT_OWNER_PRIVATE")
    def walk(path: Path) -> None:
        for entry in path.iterdir():
            info = entry.lstat()
            if not stat.S_ISDIR(info.st_mode) and (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1):
                raise ValueError("CACHE_SYMLINK_HARDLINK_OR_SPECIAL")
            if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
                raise ValueError("CACHE_NOT_OWNER_PRIVATE")
            if stat.S_ISDIR(info.st_mode):
                walk(entry)
            elif stat.S_ISREG(info.st_mode) and info.st_nlink == 1:
                result["used_bytes"] += info.st_size
                if entry.name == "payload.part":
                    result["temporary_bytes"] += info.st_size
                elif entry.name == "payload":
                    metadata = entry.parent / "state.json"
                    saved = parse_json(read_regular(metadata, MAX_PLAN)) if metadata.exists() else {}
                    saved_job = saved.get("job")
                    recognized = False
                    if isinstance(saved_job, dict):
                        try:
                            validate_job(saved_job)
                            recognized = (job_id(saved_job) == entry.parent.name
                                          and isinstance(saved_job["sha256"], str)
                                          and SHA.fullmatch(saved_job["sha256"]) is not None)
                        except ValueError:
                            pass
                    if (recognized and saved.get("protected") is False
                            and saved.get("checksum_verified") is True and saved.get("state") == "complete"):
                        result["replaceable_bytes"] += info.st_size
            else:
                raise ValueError("CACHE_SYMLINK_HARDLINK_OR_SPECIAL")
    walk(base)
    return result


@contextmanager
def locked(root: Path):
    validate_root(root)
    path = root / ".acquisition.lock"
    fd = os.open(path, os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        info = os.fstat(fd)
        if (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_uid != os.getuid()
                or stat.S_IMODE(info.st_mode) & 0o077):
            raise ValueError("LOCK_UNSAFE")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("WORKER_BUSY") from None
        yield
    finally:
        os.close(fd)


def save_state(path: Path, value: dict) -> None:
    check_directory(path.parent, create=True)
    if path.exists() or path.is_symlink():
        read_regular(path, MAX_PLAN)
    fd, name = tempfile.mkstemp(prefix=".state-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(canonical(value))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("REDIRECT_DENIED")


def request(url: str, method: str, headers: dict):
    validate_url(url)
    return build_opener(ProxyHandler({}), NoRedirect()).open(
        Request(url, method=method, headers={"User-Agent": "KFM-candidate-acquisition/1",
                                           "Accept-Encoding": "identity", **headers}), timeout=30)


def strong_etag(headers) -> str | None:
    value = headers.get("ETag")
    return value if isinstance(value, str) and re.fullmatch(r'"[\x21\x23-\x7e]{1,512}"', value) else None


def content_length(headers) -> int | None:
    value = headers.get("Content-Length")
    if value is None:
        return None
    if not re.fullmatch(r"[0-9]{1,16}", value):
        raise ValueError("CONTENT_LENGTH_INVALID")
    return int(value)


def acquire(root: Path, job: dict, *, transport=request) -> dict:
    """Run one explicitly selected job. No automatic restarts or paid fallbacks."""
    validate_job(job)
    with locked(root):
        base = cache_root(root) / job_id(job)
        state_path, partial, payload = base / "state.json", base / "payload.part", base / "payload"
        current_usage = usage(root)
        if current_usage["used_bytes"] + METADATA_RESERVE > CACHE_LIMIT:
            raise ValueError("CACHE_CAP_REACHED")
        old = parse_json(read_regular(state_path, MAX_PLAN)) if state_path.exists() else {}
        if old and old.get("job") != job:
            raise ValueError("JOB_STATE_CONFLICT")
        state = {**old, "job": job, "state": "blocked", "reason": None,
                 "checksum_verified": False, "updated_at": utc_now(),
                 "protected": old.get("protected", False)}
        def persist(status: str, reason: str | None, count: int):
            state.update(state=status, reason=reason, downloaded_bytes=count, updated_at=utc_now())
            save_state(state_path, state)
            receipt = {"schema_version": SCHEMA, "generated_at": utc_now(),
                       "lifecycle": "candidate-only", "cache": usage(root), "jobs": [project(job, state)]}
            digest = hashlib.sha256(canonical(receipt)).hexdigest()
            path = root / "data/receipts/ingest/acquisition" / job_id(job) / (digest + ".json")
            if not path.exists():
                write_new(path, canonical(receipt))
            return receipt
        count = partial.stat().st_size if partial.exists() else 0
        reason = block_reason(job)
        if reason:
            return persist("blocked", reason, count)
        limit = job["expected_bytes"] or job["approved_max_bytes"]
        try:
            if payload.exists():
                digest, count = hash_regular(payload, limit, expected_size=job["expected_bytes"])
                if digest != job["sha256"]:
                    raise ValueError("CACHE_CHECKSUM_MISMATCH")
                state["checksum_verified"] = True
                return persist("complete", None, count)
            if current_usage["used_bytes"] + max(0, limit - count) + METADATA_RESERVE > CACHE_LIMIT:
                raise ValueError("CACHE_CAP_REACHED")
            if shutil.disk_usage(root).free < max(0, limit - count) + METADATA_RESERVE:
                raise ValueError("DISK_CAPACITY_INSUFFICIENT")
            with transport(job["source_url"], "HEAD", {}) as response:
                if response.status != 200:
                    raise ValueError("HEAD_STATUS_INVALID")
                length = content_length(response.headers)
                etag = strong_etag(response.headers)
                if response.headers.get("Content-Encoding", "identity") != "identity":
                    raise ValueError("CONTENT_ENCODING_DENIED")
                if length is not None and (length > limit or (job["expected_bytes"] is not None and length != limit)):
                    raise ValueError("REMOTE_SIZE_CHANGED_OR_LIMIT")
                if count and (not etag or etag != old.get("etag")):
                    raise ValueError("RESUME_VALIDATOR_CHANGED_OR_MISSING")
            if count and (count >= limit or count == length):
                # A prior process can have died after receiving all bytes.
                digest, actual = hash_regular(partial, limit, expected_size=job["expected_bytes"])
                if digest != job["sha256"]:
                    raise ValueError("CHECKSUM_MISMATCH")
            else:
                state["etag"] = etag
                persist("running", None, count)
                headers = {"If-Match": etag} if etag else {}
                if count:
                    headers.update({"Range": f"bytes={count}-", "If-Range": etag})
                with transport(job["source_url"], "GET", headers) as response:
                    if response.headers.get("Content-Encoding", "identity") != "identity":
                        raise ValueError("CONTENT_ENCODING_DENIED")
                    if (etag and strong_etag(response.headers) != etag) or (count and response.status != 206):
                        raise ValueError("RESUME_RESPONSE_INVALID")
                    if not count and response.status != 200:
                        raise ValueError("GET_STATUS_INVALID")
                    if count:
                        content_range = response.headers.get("Content-Range", "")
                        match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", content_range)
                        if (not match or int(match[1]) != count or int(match[2]) + 1 != int(match[3])
                                or int(match[3]) > limit or (length is not None and int(match[3]) != length)):
                            raise ValueError("CONTENT_RANGE_INVALID")
                    remaining = content_length(response.headers)
                    if remaining is not None and remaining + count > limit:
                        raise ValueError("TRANSFER_BYTE_LIMIT")
                    if remaining is not None and length is not None and remaining + count != length:
                        raise ValueError("HEADER_SIZE_CONFLICT")
                    flags = os.O_WRONLY | getattr(os, "O_NOFOLLOW", 0)
                    flags |= os.O_APPEND if partial.exists() else os.O_CREAT | os.O_EXCL
                    fd = os.open(partial, flags, 0o600)
                    with os.fdopen(fd, "ab") as output:
                        while True:
                            chunk = response.read(min(CHUNK, limit - count + 1))
                            if not chunk:
                                break
                            if len(chunk) + count > limit:
                                raise ValueError("TRANSFER_BYTE_LIMIT")
                            output.write(chunk)
                            count += len(chunk)
                        output.flush()
                        os.fsync(output.fileno())
                digest, actual = hash_regular(partial, limit, expected_size=job["expected_bytes"])
                if length is not None and actual != length:
                    raise ValueError("REMOTE_SIZE_CHANGED_OR_LIMIT")
                if digest != job["sha256"]:
                    raise ValueError("CHECKSUM_MISMATCH")
            # Commit without replacing a pre-existing original, matching the
            # existing local capture primitive's atomic no-overwrite boundary.
            os.link(partial, payload)
            partial.unlink()
            fsync_directory(base)
            state["checksum_verified"] = True
            return persist("complete", None, actual)
        except (OSError, ValueError, HTTPError, URLError) as error:
            reason = str(error) if isinstance(error, ValueError) and re.fullmatch(r"[A-Z_]+", str(error)) else "TRANSPORT_INTERRUPTED"
            if isinstance(error, HTTPError) and error.code in {429, 503}:
                reason = "PROVIDER_RATE_LIMITED"
            count = partial.stat().st_size if partial.exists() else 0
            return persist("blocked" if reason != "CHECKSUM_MISMATCH" else "failed", reason, count)


def inventory(root: Path, jobs: list[dict] = ()) -> dict:
    with locked(root):
        result = {job_id(job): project(job) for job in jobs}
        cache = usage(root)
        base = cache_root(root)
        if base.exists():
            for folder in sorted(base.iterdir()):
                if folder.is_dir() and SHA.fullmatch(folder.name) and (folder / "state.json").exists():
                    state = parse_json(read_regular(folder / "state.json", MAX_PLAN))
                    job = validate_job(state["job"])
                    if job_id(job) != folder.name:
                        raise ValueError("JOB_STATE_CONFLICT")
                    if state["state"] == "running":
                        state = {**state, "state": "blocked", "reason": "INTERRUPTED_RESUME_REQUIRED"}
                    if (folder / "payload.part").exists():
                        state["downloaded_bytes"] = (folder / "payload.part").stat().st_size
                    if state["state"] == "complete":
                        try:
                            digest, count = hash_regular(folder / "payload", CACHE_LIMIT, expected_size=job["expected_bytes"])
                        except (OSError, ValueError):
                            digest, count = None, 0
                        if digest != job["sha256"]:
                            state = {**state, "state": "failed", "reason": "CACHE_CHECKSUM_MISMATCH", "checksum_verified": False}
                        state["downloaded_bytes"] = count
                    result[folder.name] = project(job, state)
        return {"schema_version": SCHEMA, "generated_at": utc_now(), "lifecycle": "candidate-only",
                "cache": cache, "jobs": list(result.values())}


def cache_action(root: Path, identifier: str, *, protect: bool = False) -> dict:
    if not SHA.fullmatch(identifier):
        raise ValueError("JOB_IDENTIFIER_INVALID")
    with locked(root):
        usage(root)
        for folder in cache_root(root).iterdir():
            if (not folder.is_dir() or not SHA.fullmatch(folder.name)
                    or not (folder / "state.json").is_file()
                    or any(p.name not in {"state.json", "payload", "payload.part"} for p in folder.iterdir())):
                raise ValueError("UNKNOWN_CACHE_FILES_BLOCK_EVICTION")
        base = cache_root(root) / identifier
        state = parse_json(read_regular(base / "state.json", MAX_PLAN))
        if job_id(validate_job(state["job"])) != identifier:
            raise ValueError("JOB_STATE_CONFLICT")
        if protect:
            state["protected"] = True
        else:
            if state.get("protected"):
                raise ValueError("PROTECTED_CACHE_CANNOT_EVICT")
            # Only these two worker-owned payload names can be deleted; never
            # recurse, touch originals, or remove unfamiliar files.
            for name in ("payload", "payload.part"):
                path = base / name
                if path.exists():
                    path.unlink()
            state.update(state="planned", reason="CACHE_EVICTED", downloaded_bytes=0, checksum_verified=False)
        state["updated_at"] = utc_now()
        save_state(base / "state.json", state)
    return inventory(root)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.environ.get("KFM_DATA_ROOT"))
    sub = parser.add_subparsers(dest="operation", required=True)
    for operation in ("plan", "acquire"):
        command = sub.add_parser(operation)
        command.add_argument("--manifest", type=Path, required=True)
        if operation == "acquire":
            command.add_argument("--select", required=True, help="Exact job_id emitted by plan; one job per run")
    sub.add_parser("inventory")
    for operation in ("protect", "evict"):
        command = sub.add_parser(operation)
        command.add_argument("--select", required=True)
    args = parser.parse_args(argv)
    try:
        if args.operation == "plan":
            jobs = load_plan(args.manifest)
            result = {"schema_version": SCHEMA, "generated_at": utc_now(), "lifecycle": "candidate-only",
                      "cache": {"limit_bytes": CACHE_LIMIT, "used_bytes": 0, "temporary_bytes": 0,
                                "replaceable_bytes": 0, "inspected": False}, "jobs": [project(job) for job in jobs]}
        else:
            root = external_root(args.root)
            if args.operation == "inventory":
                result = inventory(root)
            elif args.operation in {"protect", "evict"}:
                result = cache_action(root, args.select, protect=args.operation == "protect")
            else:
                jobs = {job_id(job): job for job in load_plan(args.manifest)}
                if args.select not in jobs:
                    raise ValueError("SELECTED_JOB_NOT_IN_PLAN")
                result = acquire(root, jobs[args.select])
        print(canonical(result).decode().strip())
        return 0 if all(job["state"] not in {"failed", "blocked"} for job in result["jobs"]) else 2
    except (OSError, ValueError, KeyError, TypeError):
        print('{"outcome":"ERROR","reason":"ACQUISITION_INPUT_OR_STORE_INVALID"}')
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
