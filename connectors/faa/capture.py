"""Fixed-product FAA capture. Emits RAW + a held receipt, never a release.

No archive extraction, credentials, discovery scheduler, or public endpoint.
"""
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError
import hashlib
import io
import json
import shutil
import time

from tools.local_data.candidate_capture import atomic_candidate, candidate_path, write_candidate

PRODUCTS = {"2026-10-01": "https://nfdc.faa.gov/webContent/28DaySub/extra/01_Oct_2026_APT_CSV.zip"}
MAX_BYTES = 16 * 1024 * 1024
RESERVE_BYTES = 128 * 1024 * 1024


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def capture(root, edition, *, opener=None, today=None):
    """Retry by rerunning: a verified completed capture is reused unchanged.

    Interrupted downloads restart; HTTP byte-range resume is deliberately absent.
    Root is an operator-selected private RAW directory, never a browser parameter.
    The shared candidate boundary permits only external KFM_DATA_ROOT/data/raw
    destinations or disposable system temporary storage, never this repository.
    """
    today = today or datetime.now(timezone.utc).date()
    if edition not in PRODUCTS or date.fromisoformat(edition) > today:
        raise ValueError("EDITION_NOT_ALLOWED")
    root = Path(root)
    if not root.is_dir() or any(p.is_symlink() for p in [root, *root.parents]):
        raise ValueError("RAW_ROOT_INVALID")
    target = candidate_path(root.absolute() / ("faa-apt-" + edition))
    if target.exists():
        if target.is_symlink() or not target.is_dir():
            raise ValueError("CAPTURE_PATH_INVALID")
        for name in ("archive.zip", "receipt.json"):
            if not (target / name).is_file() or (target / name).is_symlink():
                raise ValueError("INCOMPLETE_CAPTURE")
        receipt = json.loads((target / "receipt.json").read_text())
        body = (target / "archive.zip").read_bytes() if (target / "archive.zip").stat().st_size <= MAX_BYTES else b""
        if not body or receipt.get("sha256") != hashlib.sha256(body).hexdigest() or receipt.get("edition") != edition:
            raise ValueError("CAPTURE_INTEGRITY_FAILED")
        return target
    if shutil.disk_usage(root).free < RESERVE_BYTES + MAX_BYTES:
        raise OSError("DISK_RESERVE_REQUIRED")
    with atomic_candidate(target) as stage:
        digest, length = hashlib.sha256(), 0
        started = time.monotonic()
        request = Request(PRODUCTS[edition], headers={"User-Agent": "KFM-Research-Capture/1", "Accept-Encoding": "identity"})
        try:
            response = (opener or build_opener(NoRedirect())).open(request, timeout=20)
        except HTTPError as error:
            # Caller may retry after provider backoff; no automatic polling or quota bypass.
            if error.code in (429, 503):
                raise OSError("UPSTREAM_BACKOFF_REQUIRED") from None
            raise OSError("UPSTREAM_UNAVAILABLE") from None
        # Keep source acquisition separate from filesystem authority. Memory is
        # bounded by MAX_BYTES; the shared operator writer validates every sink.
        with response, io.BytesIO() as output:
            if response.status != 200 or response.geturl() != PRODUCTS[edition]:
                raise ValueError("UPSTREAM_NOT_ALLOWED")
            declared = response.headers.get("Content-Length")
            if declared and (not declared.isdigit() or int(declared) > MAX_BYTES):
                raise ValueError("RESPONSE_TOO_LARGE")
            while True:
                if time.monotonic() - started > 60:
                    raise TimeoutError("CAPTURE_DEADLINE")
                chunk = response.read(65536)
                if not chunk:
                    break
                length += len(chunk)
                if length > MAX_BYTES or shutil.disk_usage(root).free < RESERVE_BYTES:
                    raise OSError("CAPTURE_BUDGET_EXCEEDED")
                digest.update(chunk)
                output.write(chunk)
            if not length or declared and length != int(declared):
                raise ValueError("INCOMPLETE_CAPTURE")
            write_candidate(stage, "archive.zip", output.getvalue())
        receipt = {"source_id": "faa-nasr-apt", "edition": edition, "url": PRODUCTS[edition],
                   "sha256": digest.hexdigest(), "byte_length": length,
                   "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                   "parser_version": "faa-apt-v1", "lifecycle": "RAW", "release_state": "HELD",
                   "source_publication_time": None, "rights": "REVIEW_REQUIRED"}
        write_candidate(stage, "receipt.json", json.dumps(receipt, sort_keys=True).encode("utf-8"))
    return target


def disabled_observations(provider):
    if provider not in {"opensky", "adsb-lol"}:
        raise ValueError("SOURCE_NOT_ALLOWED")
    return {"outcome": "DENY", "reason_code": "WRITTEN_LICENSE_REQUIRED" if provider == "opensky" else "ADMISSION_REVIEW_REQUIRED",
            "ingestion_enabled": False, "public_display_enabled": False, "evidence_refs": []}
