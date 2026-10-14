"""Explicit KSHS land-sales exports and bounded official document acquisition."""
from urllib.request import HTTPRedirectHandler, Request, build_opener
import time
from people_dna_land.land_capture import capture_export
from people_dna_land.land_records import MAX_BYTES, source_url


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch_document(url, *, max_bytes=2 * 1024 * 1024):
    source_url("kshs-land-sales", url)
    if type(max_bytes) is not int or not 1 <= max_bytes <= MAX_BYTES:
        raise ValueError("DOCUMENT_LIMIT_INVALID")
    with build_opener(NoRedirect).open(Request(url, headers={"Accept-Encoding": "identity", "User-Agent": "KFM bounded Kansas historical land-record capture"}), timeout=30) as response:
        if response.status != 200 or response.geturl() != url:
            raise ValueError("DOCUMENT_RESPONSE_INVALID")
        length = response.headers.get("Content-Length")
        if length is not None and (not length.isdigit() or int(length) > max_bytes):
            raise ValueError("DOCUMENT_SIZE_LIMIT")
        chunks, count, deadline = [], 0, time.monotonic() + 60
        while True:
            if time.monotonic() >= deadline:
                raise ValueError("DOCUMENT_DEADLINE")
            chunk = response.read1(min(65536, max_bytes - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > max_bytes:
                raise ValueError("DOCUMENT_SIZE_LIMIT")
            chunks.append(chunk)
        raw = b"".join(chunks)
        if not raw or len(raw) > max_bytes or length is not None and len(raw) != int(length):
            raise ValueError("DOCUMENT_SIZE_LIMIT")
        return raw


def capture(raw, *, url, retrieved_at, documents):
    if not documents:
        raise ValueError("ARCHIVAL_ORIGINAL_REQUIRED")
    return capture_export("kshs-land-sales", raw, url=url, retrieved_at=retrieved_at, format="mapped-csv", documents=documents)
