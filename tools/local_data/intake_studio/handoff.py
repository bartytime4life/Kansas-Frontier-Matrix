"""Explicit, retryable Studio capture into the private Working Data catalog."""
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import os
from pathlib import Path
import re
import tempfile

from tools.local_data import intake, intake_review, manage
from tools.local_data.acquisition import validate_root
from tools.local_data.file_io import capture_file, check_directory, read_regular, write_new

MAX_BYTES = 25 * 1024 * 1024
MAX_REVIEW_BYTES = 4 * 1024 * 1024


def immutable(path, content):
    if path.exists() or path.is_symlink():
        if read_regular(path, max(len(content), 1)) != content:
            raise ValueError("A saved handoff file changed. Restore it before retrying.")
    else:
        write_new(path, content)


@contextmanager
def pipeline_lock(path):
    if path is None:
        yield
        return
    check_directory(path.parent)
    fd = os.open(path, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("KFM is processing another job. Try Send to KFM again when it finishes.") from None
        yield
    finally:
        os.close(fd)


def capture(studio, record):
    """Use the established capture, profiler, router and index; retain sharing holds."""
    root = manage.external_root(str(studio.kfm_root))
    validate_root(root)
    if root == studio.root or root in studio.root.parents or studio.root in root.parents:
        raise ValueError("Studio preparation storage must be separate from Working Data.")
    snapshot = {"kind": "KFM_STUDIO_CAPTURE_REVIEW", "schemaVersion": 1,
                **{k: record[k] for k in ("id", "version", "name", "mime", "size", "sha256",
                                         "uploadedAt", "review", "analysis", "history")}}
    content = manage.canonical(snapshot)
    if len(content) > MAX_REVIEW_BYTES:
        raise ValueError("Review history exceeds the handoff limit. Export this record for separate review.")
    key = hashlib.sha256(content).hexdigest()
    source = f"studio-{record['id']}-{key[:16]}"
    suffix = {"application/pdf": ".pdf", "image/png": ".png", "image/jpeg": ".jpg",
              "image/webp": ".webp", "image/tiff": ".tif"}[record["mime"]]
    stem = re.sub(r"[^A-Za-z0-9 _.-]", "_", Path(record["name"]).stem).strip(" .")[:100]
    filename = "source-" + (stem or record["id"]) + suffix
    captured_at = datetime.fromisoformat(record["uploadedAt"]).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    item = {"source_id": source, "dataset_id": "studio-original", "domain": record["review"]["domain"],
            "version": "review-" + key[:32], "relative_path": filename,
            "source_uri": f"file-ref:intake-studio/{record['id']}/{key}", "media_type": record["mime"],
            # Sending to a private catalog is not an approval for redistribution.
            "rights": {"license_id": None, "redistribution": "unknown"}, "sensitivity": "public",
            "sha256": record["sha256"], "size_bytes": record["size"], "captured_at": captured_at}
    args = manage.parser().parse_args(["sync", "--root", str(root), "--manifest", "unused",
                                      "--downloads", str(studio.root), "--max-file-bytes", str(MAX_BYTES)])
    manifest = manage.validate_manifest({"schema_version": "1", "items": [item]}, args)
    obj = studio.objects / record["sha256"]
    metadata = root / "data/work/intake-studio" / record["id"] / key
    with pipeline_lock(studio.pipeline_lock), intake.writer_lock(root):
        with intake.open_index(root) as conn:
            # A fresh empty catalog may be initialized here; a populated legacy
            # catalog is refused by open_index and still requires full reanalysis.
            empty = not conn.execute("SELECT 1 FROM items WHERE lane='quarantine' LIMIT 1").fetchone()
            with tempfile.TemporaryDirectory(prefix="handoff-", dir=studio.root) as temp:
                downloads = Path(temp)
                capture_file(obj / "original", downloads / filename, sha256=record["sha256"],
                             size_bytes=record["size"], max_bytes=MAX_BYTES)
                immutable(metadata / "review.json", content)
                immutable(metadata / "extracted-text.txt", record["analysis"]["text"].encode("utf-8"))
                if record["preview"]:
                    immutable(metadata / "preview.png", read_regular(obj / "preview.png", 8 * 1024 * 1024))
                immutable(metadata / "capture-manifest.json", manage.canonical(manifest))
                result = manage.sync_store(root, manifest, downloads, args)
            manage.inspect_objects(root, manifest, None, args)
            manage.check_snapshots(root, manifest, required=True)
            target = manage.payload_path(root, item)
            relative = target.relative_to(root / "data/quarantine").as_posix()
            # Reuse discovery's source-and-digest binding semantics. Only this
            # captured file is profiled; other items and runs are left intact.
            found = next((f for f in intake.discover(root, max_files=intake.MAX_CONFIGURED_FILES)
                          if f["lane"] == "quarantine" and f["relative_path"] == relative), None)
            if found is None or found["declared"] is None:
                raise ValueError("Capture could not be located in Working Data. Retry this handoff.")
            profile = intake.profile_file(target, display_path=filename, declared=found["declared"])
            indexed = {"id": intake.item_id("quarantine", relative), "lane": "quarantine",
                       "relative_path": relative, "store_path": str(target.relative_to(root)),
                       "sha256": record["sha256"], "size_bytes": record["size"], "declared": found["declared"]}
            decision = intake_review.decision(conn, indexed, profile, intake.intake_route.load_budget())
            intake._upsert(conn, indexed, found["stat"], profile, decision, "studio-" + key[:24])
            if empty:
                conn.execute("INSERT INTO meta(key,value) VALUES ('quarantine_binding_version',?) "
                             "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (intake.QUARANTINE_BINDING_VERSION,))
        receipt = {"state": "CAPTURED_IN_WORKING_DATA", "reviewVersion": record["version"],
                   "reviewSha256": key, "sourceId": source, "itemId": indexed["id"],
                   "originalSha256": record["sha256"], "captureRunId": result["run_id"],
                   "reviewPath": str(metadata.relative_to(root) / "review.json"),
                   "manifestPath": str(metadata.relative_to(root) / "capture-manifest.json"),
                   "indexed": True, "authority": dict(manage.AUTHORITY)}
        immutable(metadata / "receipt.json", manage.canonical(receipt))
    return receipt
