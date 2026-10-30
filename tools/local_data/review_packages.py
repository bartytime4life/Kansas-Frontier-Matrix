"""Explicit pinned WORK-package reader for private owner review, never promotion.

No store walk, arbitrary browser paths, archive extraction or network. Operators
select exact manifests; each selected member is hashed before it is returned.
The existing file_io ancestor checks are not a sandbox against a hostile owner.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import threading

from tools.local_data.file_io import read_regular
from tools.local_data.review_images import image_metadata

ID = re.compile(r"[a-f0-9]{64}\Z")
MANIFEST_LIMIT = 256 * 1024
MEMBER_LIMIT = 16 * 1024 * 1024
PACKAGE_LIMIT = 256 * 1024 * 1024
TEXT_LIMIT = 64 * 1024
ROW_LIMIT = 40
PROFILES = {
    "kfm-historical-geology-review/v1": "Historical Kansas geology map",
    "kfm-historical-climate-normals-review/v1": "Historical NOAA climate normals",
    "kfm-historical-water-review/v1": "Historical USGS water observations",
    "kfm-map-document-review/v1": "Historical map document review",
    "kfm-water-metadata-availability-review/v1": "Water series availability",
}
SUFFIXES = {".md", ".txt", ".csv", ".tsv", ".json", ".geojson", ".png", ".jpg", ".jpeg"}
AUTHORITY = {"admission": False, "activation": False, "release": False, "publication": False}


def relative(value):
    if (not isinstance(value, str) or len(value) > 400 or not value or "\\" in value
            or any(ord(c) < 32 or ord(c) == 127 for c in value)):
        raise ValueError("REVIEW_PATH_INVALID")
    path = PurePosixPath(value)
    if path.is_absolute() or str(path) != value or any(p.startswith(".") or p in {"credentials", "secrets"} for p in path.parts):
        raise ValueError("REVIEW_PATH_INVALID")
    return path


def member_id(row):
    return hashlib.sha256((row["file"] + "\0" + row["sha256"]).encode()).hexdigest()


class ReviewPackages:
    def __init__(self, root: Path, bindings=()):
        self.root = root
        self.bindings = {}
        self.slots = threading.BoundedSemaphore(2)
        if len(bindings) > 16:
            raise ValueError("REVIEW_PACKAGE_LIMIT")
        for binding in bindings:
            if not isinstance(binding, str) or binding.count("@") != 1:
                raise ValueError("REVIEW_BINDING_INVALID")
            location, digest = binding.split("@")
            path = relative(location)
            if (not ID.fullmatch(digest) or path.parts[:2] != ("data", "work") or len(path.parts) < 5
                    or path.name != "review-manifest.json" or digest in self.bindings):
                raise ValueError("REVIEW_BINDING_INVALID")
            self.bindings[digest] = path
            self._manifest(digest)  # fail startup rather than offer an unbound selection

    def _manifest(self, identity):
        if not isinstance(identity, str) or identity not in self.bindings:
            raise ValueError("REVIEW_PACKAGE_UNKNOWN")
        path = self.root / self.bindings[identity]
        raw = read_regular(path, MANIFEST_LIMIT)
        if hashlib.sha256(raw).hexdigest() != identity:
            raise ValueError("REVIEW_MANIFEST_CHANGED")
        value = json.loads(raw)
        if (not isinstance(value, dict) or value.get("profile") not in PROFILES
                or value.get("released") is not False or value.get("published") is not False
                or value.get("review_state") != "PENDING"):
            raise ValueError("REVIEW_STATE_UNSUPPORTED")
        rows = value.get("outputs")
        if not isinstance(rows, list) or not 1 <= len(rows) <= 1000:
            raise ValueError("REVIEW_MEMBER_LIMIT")
        seen, total = set(), 0
        for row in rows:
            if not isinstance(row, dict) or set(row) != {"file", "bytes", "sha256"}:
                raise ValueError("REVIEW_MEMBER_INVALID")
            member = relative(row["file"])
            if (member.suffix not in SUFFIXES or row["file"] in seen or member.name == "review-manifest.json"
                    or not isinstance(row["sha256"], str) or not ID.fullmatch(row["sha256"])
                    or type(row["bytes"]) is not int or not 0 < row["bytes"] <= MEMBER_LIMIT):
                raise ValueError("REVIEW_MEMBER_INVALID")
            seen.add(row["file"])
            total += row["bytes"]
        if total > PACKAGE_LIMIT or total != value.get("output_bytes"):
            raise ValueError("REVIEW_PACKAGE_BYTE_LIMIT")
        return path.parent, value

    def _read(self, directory, row):
        raw = read_regular(directory / relative(row["file"]), MEMBER_LIMIT)
        if len(raw) != row["bytes"] or hashlib.sha256(raw).hexdigest() != row["sha256"]:
            raise ValueError("REVIEW_MEMBER_CHANGED")
        return raw

    def catalog(self):
        packages = []
        for identity in self.bindings:
            directory, manifest = self._manifest(identity)
            labels = {}
            index_row = next((r for r in manifest["outputs"] if r["file"] == "map-document-index.json"), None)
            if index_row:
                if index_row["bytes"] > 1024 * 1024:
                    raise ValueError("REVIEW_INDEX_LIMIT")
                index = json.loads(self._read(directory, index_row))
                records = index.get("records", []) if isinstance(index, dict) else []
                if not isinstance(records, list) or len(records) > 1000:
                    raise ValueError("REVIEW_INDEX_LIMIT")
                for row in records:
                    if not isinstance(row, dict):
                        raise ValueError("REVIEW_INDEX_INVALID")
                    label = str(row.get("source_path", "")).rsplit("/", 1)[-1][:120]
                    if row.get("filename_conflict") is True:
                        label += " (filename conflict)"
                    digest = row.get("sha256", "")
                    record = row.get("record_relative_path", "")
                    labels[record] = label + " — details"
                    if isinstance(digest, str) and ID.fullmatch(digest):
                        labels.setdefault("renders/" + digest[:20] + ".png", label + " — page image")
                        labels.setdefault("ocr/" + digest[:20] + ".tsv", label + " — OCR candidates")
            packages.append({
                "id": identity, "title": PROFILES[manifest["profile"]], "profile": manifest["profile"],
                "reviewState": "PENDING", "bytes": manifest["output_bytes"], "authority": dict(AUTHORITY),
                "sourceRole": str(manifest.get("source_role", "Private review"))[:600],
                "rights": str(manifest.get("rights", "UNKNOWN"))[:200],
                "members": [{"id": member_id(r), "name": r["file"], "label": labels.get(r["file"], r["file"]),
                             "bytes": r["bytes"], "kind": "image" if Path(r["file"]).suffix in {".png", ".jpg", ".jpeg"} else "text"}
                            for r in manifest["outputs"]],
            })
        return {"schema": "kfm-private-review-packages/v1", "packages": packages, "authority": dict(AUTHORITY),
                "note": "Operator-selected private WORK packages. Manifest integrity is checked here; individual bytes are checked when opened. No release or promotion."}

    def preview(self, identity, member, *, text=""):
        if not isinstance(member, str) or not ID.fullmatch(member) or not isinstance(text, str) or len(text) > 100:
            raise ValueError("REVIEW_REQUEST_INVALID")
        if not self.slots.acquire(blocking=False):
            raise ValueError("REVIEW_BUSY")
        try:
            directory, manifest = self._manifest(identity)
            row = next((r for r in manifest["outputs"] if member_id(r) == member), None)
            if row is None:
                raise ValueError("REVIEW_MEMBER_UNKNOWN")
            raw = self._read(directory, row)
            if Path(row["file"]).suffix in {".png", ".jpg", ".jpeg"}:
                if text:
                    raise ValueError("REVIEW_IMAGE_INVALID")
                metadata = image_metadata(raw, Path(row["file"]).suffix)
                return raw, metadata["media_type"]
            content = raw.decode("utf-8", errors="strict")
            matched, shown = None, None
            if text:
                try:
                    parsed = json.loads(content)
                except json.JSONDecodeError:
                    parsed = None
                rows = (parsed.get("rows", parsed.get("records")) if isinstance(parsed, dict) else parsed)
                if isinstance(rows, list):
                    selected, matched = [], 0
                    for item in rows:
                        if text.casefold() in json.dumps(item, ensure_ascii=False).casefold():
                            matched += 1
                            if len(selected) < ROW_LIMIT:
                                selected.append(item)
                    shown = len(selected)
                    content = json.dumps(selected, indent=2, ensure_ascii=False)
                else:
                    lines = [line for line in content.splitlines() if text.casefold() in line.casefold()]
                    matched, shown = len(lines), min(ROW_LIMIT, len(lines))
                    content = "\n".join(lines[:ROW_LIMIT])
            encoded = content.encode()
            return {"schema": "kfm-private-review-preview/v1", "name": row["file"], "sha256": row["sha256"],
                    "bytes": row["bytes"], "integrity": "EXACT_MEMBER_DIGEST_VERIFIED", "reviewState": "PENDING",
                    "text": encoded[:TEXT_LIMIT].decode("utf-8", errors="ignore"), "matchedRows": matched,
                    "shownRows": shown, "truncated": len(encoded) > TEXT_LIMIT or (matched is not None and matched > shown),
                    "authority": dict(AUTHORITY)}, "application/json"
        finally:
            self.slots.release()
