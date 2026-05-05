from __future__ import annotations

import socket
import urllib.error
import urllib.request
from pathlib import Path
from typing import Mapping

from .models import ProbeResult
from .utils import ensure_parent, sha256_prefixed_bytes


def _request(url: str, headers: Mapping[str, str] | None = None, method: str = "GET") -> urllib.request.Request:
    return urllib.request.Request(url, headers=dict(headers or {}), method=method)


def head_probe(url: str, headers: Mapping[str, str] | None = None, timeout: float = 20.0) -> ProbeResult:
    try:
        with urllib.request.urlopen(_request(url, headers, "HEAD"), timeout=timeout) as response:
            content_length = response.headers.get("Content-Length")
            return ProbeResult(
                status=int(response.getcode() or 0),
                etag=response.headers.get("ETag"),
                last_modified=response.headers.get("Last-Modified"),
                content_length=int(content_length) if content_length and content_length.isdigit() else None,
                content_type=response.headers.get("Content-Type"),
            )
    except urllib.error.HTTPError as exc:
        content_length = exc.headers.get("Content-Length") if exc.headers else None
        return ProbeResult(
            status=int(exc.code),
            etag=exc.headers.get("ETag") if exc.headers else None,
            last_modified=exc.headers.get("Last-Modified") if exc.headers else None,
            content_length=int(content_length) if content_length and content_length.isdigit() else None,
            content_type=exc.headers.get("Content-Type") if exc.headers else None,
            error=f"http_error:{exc.code}",
        )
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        return ProbeResult(status=0, error=f"network_error:{exc.__class__.__name__}:{exc}")


def download_to_file(
    url: str,
    headers: Mapping[str, str] | None,
    dest: str | Path,
    max_bytes: int,
    timeout: float = 60.0,
) -> dict[str, object]:
    dest = Path(dest)
    ensure_parent(dest)
    try:
        with urllib.request.urlopen(_request(url, headers, "GET"), timeout=timeout) as response:
            status = int(response.getcode() or 0)
            if status >= 500:
                raise RuntimeError(f"fail_closed_http_status:{status}")
            if status < 200 or status >= 300:
                raise RuntimeError(f"unexpected_http_status:{status}")
            declared = response.headers.get("Content-Length")
            if declared and declared.isdigit() and int(declared) > max_bytes:
                raise RuntimeError(f"max_download_bytes_exceeded:declared={declared}:limit={max_bytes}")
            total = 0
            import hashlib

            h = hashlib.sha256()
            with dest.open("wb") as out:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > max_bytes:
                        raise RuntimeError(f"max_download_bytes_exceeded:actual={total}:limit={max_bytes}")
                    h.update(chunk)
                    out.write(chunk)
            return {
                "status": status,
                "bytes": total,
                "sha256": "sha256-" + h.hexdigest(),
                "content_type": response.headers.get("Content-Type"),
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
            }
    except urllib.error.HTTPError as exc:
        if exc.code >= 500:
            raise RuntimeError(f"fail_closed_http_status:{exc.code}") from exc
        raise RuntimeError(f"unexpected_http_status:{exc.code}") from exc
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise RuntimeError(f"fail_closed_network_error:{exc.__class__.__name__}:{exc}") from exc
