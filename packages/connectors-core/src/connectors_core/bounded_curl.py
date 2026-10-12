"""Bounded live transport; caller supplies an admitted fixed-host profile.

Transport owns temporary response files, never repository lifecycle writes.
No shell, redirects, curl config files, or caller-supplied command flags.
"""
from pathlib import Path
import shutil
import subprocess
import tempfile
from urllib.parse import urlsplit
from .transport import TransportResponse


class BoundedCurlTransport:
    """A fixed-host implementation of the existing caller-owned transport."""

    def __init__(self, profile, *, path_prefix):
        self.profile = profile
        self.path_prefix = path_prefix
        self.executable = shutil.which("curl")
        if not self.executable:
            raise ValueError("CURL_UNAVAILABLE")

    def send(self, request, *, timeout_seconds, max_response_bytes, allow_redirects):
        self.profile.validate_request(request)
        if allow_redirects or request.method.value != "GET" or request.headers:
            raise ValueError("UNSUPPORTED_TRANSPORT_REQUEST")
        parsed = urlsplit(request.url)
        if not parsed.path.startswith(self.path_prefix):
            raise ValueError("UNSUPPORTED_PROVIDER_PATH")
        with tempfile.TemporaryDirectory(prefix="kfm-usgs-") as directory:
            payload = Path(directory) / "body"
            headers = Path(directory) / "headers"
            command = [
                self.executable, "--disable", "--silent", "--show-error",
                "--proto", "=https", "--max-redirs", "0", "--max-time", str(timeout_seconds),
                "--connect-timeout", str(min(5, timeout_seconds)),
                "--max-filesize", str(max_response_bytes), "--header", "Accept: application/geo+json",
                "--header", "Accept-Encoding: identity", "--output", str(payload),
                "--dump-header", str(headers), "--write-out", "%{http_code}", "--url", request.url,
            ]
            try:
                result = subprocess.run(command, capture_output=True, timeout=timeout_seconds + 1, check=False)
            except subprocess.TimeoutExpired as exc:
                raise TimeoutError("REQUEST_DEADLINE") from exc
            if result.returncode == 28:
                raise TimeoutError("REQUEST_DEADLINE")
            if result.returncode:
                # Never expose provider body, URL, or subprocess stderr in errors.
                raise OSError("PROVIDER_TRANSPORT_FAILED")
            if not payload.is_file() or payload.stat().st_size > max_response_bytes:
                raise ValueError("RESPONSE_BYTE_LIMIT")
            if not headers.is_file() or headers.stat().st_size > 65536:
                raise ValueError("RESPONSE_HEADER_LIMIT")
            safe = {}
            for line in headers.read_text(encoding="iso-8859-1").splitlines():
                if line.startswith("HTTP/"):
                    safe = {}
                if ":" in line:
                    key, value = line.split(":", 1)
                    if key.lower() in {"content-type", "content-length", "etag", "last-modified", "retry-after", "date"}:
                        safe[key.lower()] = value.strip()
            return TransportResponse(int(result.stdout), safe, (payload.read_bytes(),), request.url)
