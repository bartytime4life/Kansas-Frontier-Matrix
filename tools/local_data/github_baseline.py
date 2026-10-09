#!/usr/bin/env python3
"""Inspect or explicitly download a source-context baseline from GitHub Releases.

No credentials, source admission, service operation, or Site activation. Archives
are verified before a new destination is created; existing paths are never used.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tarfile
import tempfile
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix"
STORAGE_CAP = 80_000_000_000
MAX_ASSET_BYTES = 1_800_000_000
MAX_MANIFEST_BYTES = 8_000_000
MAX_FILES = 1_000_000
CHUNK = 1024 * 1024
STATUS = "source-context-unadmitted"
SAFE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,199}\Z")


class BaselineError(ValueError):
    """A manifest, archive, budget, or destination failed its contract."""


def require(condition, message):
    if not condition:
        raise BaselineError(message)


def integer(value, name, maximum=STORAGE_CAP, minimum=0):
    require(type(value) is int and minimum <= value <= maximum, f"Invalid {name}")
    return value


def relative_path(value):
    require(isinstance(value, str) and 0 < len(value) <= 1024, "Invalid archive path")
    require("\\" not in value and not any(ord(c) < 32 or ord(c) == 127 for c in value), "Unsafe archive path")
    parts = value.split("/")
    require(all(part not in {"", ".", ".."} for part in parts), "Unsafe archive path")
    require(not PurePosixPath(value).is_absolute() and ":" not in value, "Unsafe archive path")
    return parts


def asset_url(tag, name):
    return f"https://github.com/{REPOSITORY}/releases/download/{tag}/{name}"


def load_manifest(path):
    with Path(path).open("rb") as stream:
        raw = stream.read(MAX_MANIFEST_BYTES + 1)
    require(len(raw) <= MAX_MANIFEST_BYTES, "Manifest exceeds byte limit")
    def unique_pairs(pairs):
        value = {}
        for key, item in pairs:
            require(key not in value, "Duplicate manifest key")
            value[key] = item
        return value
    try:
        manifest = json.loads(raw, object_pairs_hook=unique_pairs)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise BaselineError("Manifest is not valid UTF-8 JSON") from error
    validate_manifest(manifest)
    return manifest, hashlib.sha256(raw).hexdigest()


def validate_manifest(manifest):
    require(isinstance(manifest, dict), "Invalid manifest")
    require(type(manifest.get("schema_version")) is int and manifest["schema_version"] == 1, "Unsupported manifest schema")
    require(manifest.get("status") == STATUS, "Unsupported baseline status")
    require(manifest.get("storage_cap_bytes") == STORAGE_CAP, "Unexpected storage cap")
    tag = manifest.get("release_tag")
    require(isinstance(tag, str) and SAFE_NAME.fullmatch(tag), "Invalid release tag")
    require(isinstance(manifest.get("snapshot_utc"), str), "Missing snapshot time")
    try:
        snapshot = datetime.fromisoformat(manifest["snapshot_utc"].replace("Z", "+00:00"))
        require(snapshot.utcoffset() is not None and snapshot.utcoffset().total_seconds() == 0, "Snapshot must use UTC")
    except ValueError as error:
        raise BaselineError("Invalid snapshot time") from error
    require(isinstance(manifest.get("exclusions"), list), "Missing exclusion inventory")
    datasets = manifest.get("datasets")
    require(isinstance(datasets, list) and 1 <= len(datasets) <= 1000, "Invalid dataset inventory")
    ids, names, subdirs = set(), set(), []
    total_assets = total_bytes = 0
    for dataset in datasets:
        require(isinstance(dataset, dict), "Invalid dataset")
        identifier = dataset.get("id")
        require(isinstance(identifier, str) and SAFE_NAME.fullmatch(identifier) and identifier not in ids, "Invalid or duplicate dataset ID")
        ids.add(identifier)
        for field in ("title", "description", "license"):
            require(isinstance(dataset.get(field), str) and bool(dataset[field].strip()), f"Missing dataset {field}")
        sources = dataset.get("source_urls")
        require(isinstance(sources, list) and sources and all(isinstance(url, str) and urlsplit(url).scheme in {"https", "http"} and urlsplit(url).hostname for url in sources), "Missing source provenance")
        subdir = dataset.get("install_subdir")
        relative_path(subdir)
        require(not subdir.startswith("."), "Reserved dataset directory")
        require(all(not (subdir == prior or subdir.startswith(prior + "/") or prior.startswith(subdir + "/")) for prior in subdirs), "Overlapping dataset directories")
        subdirs.append(subdir)
        integer(dataset.get("files"), "dataset file count", MAX_FILES, 1)
        integer(dataset.get("bytes"), "dataset expanded bytes", STORAGE_CAP, 1)
        joins = dataset.get("reassemble", [])
        require(isinstance(joins, list), "Invalid reassembly inventory")
        outputs, parts_used = set(), set()
        for join in joins:
            require(isinstance(join, dict), "Invalid reassembly record")
            path = join.get("path")
            relative_path(path)
            require(path.startswith(subdir + "/") and path not in outputs, "Invalid reassembly output")
            outputs.add(path)
            integer(join.get("bytes"), "reassembly bytes", dataset["bytes"], 1)
            require(isinstance(join.get("sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", join["sha256"]), "Invalid reassembly SHA-256")
            parts = join.get("parts")
            require(isinstance(parts, list) and 2 <= len(parts) <= 1000, "Invalid reassembly parts")
            for part in parts:
                relative_path(part)
                require(part.startswith(subdir + "/") and part not in parts_used, "Invalid or reused reassembly part")
                parts_used.add(part)
        require(not outputs & parts_used, "Reassembly output overlaps input")
        assets = dataset.get("assets")
        require(isinstance(assets, list) and assets, "Dataset has no archives")
        for asset in assets:
            require(isinstance(asset, dict), "Invalid asset")
            name = asset.get("name")
            require(isinstance(name, str) and SAFE_NAME.fullmatch(name) and name.endswith(".tar.gz") and name not in names, "Invalid or duplicate asset name")
            names.add(name)
            total_bytes += integer(asset.get("bytes"), "asset bytes", MAX_ASSET_BYTES - 1, 1)
            require(isinstance(asset.get("sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", asset["sha256"]), "Invalid asset SHA-256")
            require(asset.get("url") == asset_url(tag, name), "Asset URL is outside the exact repository release")
        total_assets += len(assets)
    require(total_assets <= 1000 and total_bytes <= STORAGE_CAP, "Release exceeds asset or storage limit")


def select_datasets(manifest, selected, all_datasets=False, *, explicit=False):
    require(not (selected and all_datasets), "Choose --dataset or --all")
    require(not explicit or selected or all_datasets, "Download requires --dataset or --all")
    wanted = set(selected or [])
    known = {row["id"] for row in manifest["datasets"]}
    require(wanted <= known, "Unknown dataset: " + ", ".join(sorted(wanted - known)))
    return [row for row in manifest["datasets"] if not wanted or row["id"] in wanted]


def plan(manifest, datasets):
    compressed = sum(asset["bytes"] for row in datasets for asset in row["assets"])
    expanded = sum(row["bytes"] for row in datasets)
    join_space = max((item["bytes"] for row in datasets for item in row.get("reassemble", [])), default=0)
    return {"operation": "plan", "release_tag": manifest["release_tag"], "snapshot_utc": manifest["snapshot_utc"],
            "status": STATUS, "network": False, "writes": False,
            "download_bytes": compressed, "expanded_bytes": expanded,
            "reassembly_temporary_bytes": join_space,
            "minimum_free_bytes": compressed + expanded + join_space + 16 * 1024 * 1024,
            "files": sum(row["files"] for row in datasets),
            "datasets": [{key: row[key] for key in ("id", "title", "description", "license", "source_urls", "files", "bytes", "install_subdir")} for row in datasets]}


class ReleaseRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        parsed = urlsplit(newurl)
        require(parsed.scheme == "https" and parsed.hostname == "release-assets.githubusercontent.com"
                and parsed.port in {None, 443} and parsed.username is None and parsed.password is None,
                "Unexpected GitHub asset redirect")
        return super().redirect_request(request, fp, code, msg, headers, newurl)


def fetch_asset(asset, destination):
    digest, size = hashlib.sha256(), 0
    opener = build_opener(ReleaseRedirects())
    request = Request(asset["url"], headers={"User-Agent": "KFM-source-context-baseline/1", "Accept-Encoding": "identity"})
    with opener.open(request, timeout=60) as response, destination.open("xb") as output:
        require(response.status == 200, "Asset request did not return 200")
        require(response.headers.get("Content-Encoding", "identity") == "identity", "Unexpected asset content encoding")
        length = response.headers.get("Content-Length")
        require(length is None or length == str(asset["bytes"]), "Asset Content-Length differs from manifest")
        while chunk := response.read(min(CHUNK, asset["bytes"] - size + 1)):
            size += len(chunk)
            require(size <= asset["bytes"], "Asset exceeds declared bytes")
            digest.update(chunk)
            output.write(chunk)
    require(size == asset["bytes"] and digest.hexdigest() == asset["sha256"], "Asset size or SHA-256 mismatch")


@contextmanager
def parent_directory(destination):
    require(hasattr(os, "O_NOFOLLOW") and os.open in os.supports_dir_fd, "Safe download installation requires POSIX directory descriptors")
    destination = Path(os.path.abspath(destination))
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    descriptor = os.open(destination.anchor, flags)
    try:
        for part in destination.parent.parts[1:]:
            child = os.open(part, flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        info = os.fstat(descriptor)
        require(info.st_uid == os.getuid() and not stat.S_IMODE(info.st_mode) & 0o022, "Destination parent must be owned by you and not writable by others")
        try:
            os.stat(destination.name, dir_fd=descriptor, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise BaselineError("Destination already exists; choose a new directory")
        yield destination, descriptor
    finally:
        os.close(descriptor)


def inspect_archive(path, dataset, seen, totals):
    """Inspect metadata while streaming, without tarfile.extract or path writes."""
    prefix = dataset["install_subdir"]
    with tarfile.open(path, "r|gz") as archive:
        count = 0
        for member in archive:
            count += 1
            require(count <= MAX_FILES * 2, "Archive has too many members")
            name = member.name.rstrip("/") if member.isdir() else member.name
            relative_path(name)
            require(name == prefix or name.startswith(prefix + "/"), "Archive member escapes dataset directory")
            require(member.isdir() or member.isreg(), "Archive contains links or special files")
            require(not member.issparse(), "Sparse archive members are not supported")
            require(not member.isdir() or member.size == 0, "Directory contains unexpected payload")
            for parent in PurePosixPath(name).parents:
                if str(parent) != ".":
                    require(not isinstance(seen.get(str(parent)), int), "Archive ancestor is a file")
                    seen.setdefault(str(parent), None)
            if member.isdir():
                require(not isinstance(seen.get(name), int), "Archive file/directory conflict")
                seen[name] = None
                continue
            require(name != prefix and name not in seen, "Duplicate archive file or directory conflict")
            seen[name] = member.size
            totals[0] += 1
            totals[1] += integer(member.size, "member bytes")
            require(totals[0] <= dataset["files"] and totals[1] <= dataset["bytes"], "Archive exceeds declared expanded size or file count")


def extract_archive(path, root_descriptor):
    """All entries were inspected; descriptor-relative exclusive writes also
    reject a path swapped for a symlink between inspection and extraction.
    """
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    with tarfile.open(path, "r|gz") as archive:
        for member in archive:
            parts = relative_path(member.name.rstrip("/") if member.isdir() else member.name)
            descriptor = os.dup(root_descriptor)
            try:
                for component in parts if member.isdir() else parts[:-1]:
                    try:
                        os.mkdir(component, 0o700, dir_fd=descriptor)
                    except FileExistsError:
                        pass
                    child = os.open(component, flags, dir_fd=descriptor)
                    os.close(descriptor)
                    descriptor = child
                if member.isdir():
                    continue
                require(member.isreg() and not member.issparse(), "Unexpected archive member")
                fd = os.open(parts[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=descriptor)
                with os.fdopen(fd, "wb") as output, archive.extractfile(member) as source:
                    copied = 0
                    while chunk := source.read(CHUNK):
                        copied += len(chunk)
                        require(copied <= member.size, "Member exceeds declared size")
                        output.write(chunk)
                    require(copied == member.size, "Truncated archive member")
            finally:
                os.close(descriptor)


@contextmanager
def existing_parent(root_descriptor, name):
    parts = relative_path(name)
    descriptor = os.dup(root_descriptor)
    try:
        for component in parts[:-1]:
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        yield descriptor, parts[-1]
    finally:
        os.close(descriptor)


def reassemble(dataset, root_descriptor):
    for join in dataset.get("reassemble", []):
        digest, size = hashlib.sha256(), 0
        with existing_parent(root_descriptor, join["path"]) as (parent, name):
            fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=parent)
            with os.fdopen(fd, "wb") as output:
                for part in join["parts"]:
                    with existing_parent(root_descriptor, part) as (part_parent, part_name):
                        source_fd = os.open(part_name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=part_parent)
                        with os.fdopen(source_fd, "rb") as source:
                            require(stat.S_ISREG(os.fstat(source.fileno()).st_mode), "Reassembly input is not a regular file")
                            while chunk := source.read(CHUNK):
                                size += len(chunk)
                                require(size <= join["bytes"], "Reassembly exceeds declared size")
                                digest.update(chunk)
                                output.write(chunk)
        require(size == join["bytes"] and digest.hexdigest() == join["sha256"], "Reassembly size or SHA-256 mismatch")
        # Inputs exist only in this freshly reserved output; retain them on failure.
        for part in join["parts"]:
            with existing_parent(root_descriptor, part) as (parent, name):
                os.unlink(name, dir_fd=parent)


def download(manifest, manifest_digest, datasets, destination, max_bytes):
    integer(max_bytes, "download budget", STORAGE_CAP, 1)
    summary = plan(manifest, datasets)
    require(summary["download_bytes"] <= max_bytes, "Selected archives exceed --max-bytes")
    with parent_directory(destination) as (destination, parent_fd):
        require(shutil.disk_usage(destination.parent).free >= summary["minimum_free_bytes"], "Insufficient disk space for archives and expanded files")
        with tempfile.TemporaryDirectory(prefix=".kfm-baseline-download-", dir=destination.parent) as temporary:
            packages, seen = [], {}
            for dataset in datasets:
                totals = [0, 0]
                for asset in dataset["assets"]:
                    path = Path(temporary) / asset["name"]
                    fetch_asset(asset, path)
                    inspect_archive(path, dataset, seen, totals)
                    packages.append(path)
                require(totals == [dataset["files"], dataset["bytes"]], "Dataset file count or expanded size differs from manifest")
                for join in dataset.get("reassemble", []):
                    require(join["path"] not in seen, "Reassembly output already exists in archive")
                    require(all(isinstance(seen.get(part), int) for part in join["parts"]), "Reassembly input is missing")
                    require(sum(seen[part] for part in join["parts"]) == join["bytes"], "Reassembly part sizes differ from output")
                    require(str(PurePosixPath(join["path"]).parent) in seen, "Reassembly output parent is absent")
            # Exclusive reservation after every download and archive check.
            os.mkdir(destination.name, 0o700, dir_fd=parent_fd)
            root_fd = os.open(destination.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd)
            try:
                marker = os.open(".baseline-incomplete", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600, dir_fd=root_fd)
                os.close(marker)
                for path in packages:
                    extract_archive(path, root_fd)
                for dataset in datasets:
                    reassemble(dataset, root_fd)
                receipt = {"operation": "downloaded", "status": STATUS, "release_tag": manifest["release_tag"],
                           "snapshot_utc": manifest["snapshot_utc"], "manifest_sha256": manifest_digest,
                           "installed_utc": datetime.now(timezone.utc).isoformat(),
                           "datasets": [row["id"] for row in datasets], "download_bytes": summary["download_bytes"],
                           "expanded_bytes": summary["expanded_bytes"], "files": summary["files"],
                           "installed_files": summary["files"] - sum(len(join["parts"]) - 1 for row in datasets for join in row.get("reassemble", [])),
                           "activation": False, "source_admission": False}
                fd = os.open("baseline-install-receipt.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=root_fd)
                with os.fdopen(fd, "w") as output:
                    json.dump(receipt, output, indent=2)
                    output.write("\n")
                os.unlink(".baseline-incomplete", dir_fd=root_fd)
            finally:
                os.close(root_fd)
    return {**receipt, "directory": str(destination)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("plan", "download"), nargs="?", default="plan")
    parser.add_argument("--manifest", required=True, type=Path, help="Local reviewed baseline-manifest.json; never fetched implicitly")
    choices = parser.add_mutually_exclusive_group()
    choices.add_argument("--dataset", action="append", help="Explicit dataset ID; repeat to select several")
    choices.add_argument("--all", action="store_true", dest="all_datasets")
    parser.add_argument("--directory", type=Path, help="New output directory below an existing parent owned by you")
    parser.add_argument("--max-bytes", type=int, help="Mandatory compressed download budget, at most 80000000000")
    args = parser.parse_args(argv)
    try:
        manifest, digest = load_manifest(args.manifest)
        datasets = select_datasets(manifest, args.dataset, args.all_datasets, explicit=args.command == "download")
        if args.command == "plan":
            result = plan(manifest, datasets)
        else:
            require(args.directory is not None and args.max_bytes is not None, "Download requires --directory and --max-bytes")
            result = download(manifest, digest, datasets, args.directory, args.max_bytes)
        print(json.dumps(result, indent=2))
        return 0
    except (BaselineError, OSError, tarfile.TarError, EOFError) as error:
        print(json.dumps({"operation": "failed", "error": str(error), "activation": False}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
