"""The real transport's process and filesystem boundaries, with no network."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from connectors_core.bounded_curl import BoundedCurlTransport
from connectors_core.transport import TransportProfile, TransportRequest, TransportMethod


def request(url="https://api.waterdata.usgs.gov/ogcapi/v1/collections/continuous/items"):
    return TransportRequest(method=TransportMethod.GET, url=url)


def transport():
    return BoundedCurlTransport(TransportProfile(
        profile_id="synthetic-transport", allowed_hosts=frozenset({"api.waterdata.usgs.gov"}),
        allowed_media_types=frozenset({"application/json"}),
    ), path_prefix="/ogcapi/v1/collections/")


def test_process_is_bounded_and_writes_only_temporary_response_files():
    destinations = []
    def run(command, **options):
        assert options == {"capture_output": True, "timeout": 4, "check": False}
        assert command[1] == "--disable" and command[command.index("--max-redirs") + 1] == "0"
        assert command[command.index("--max-filesize") + 1] == "64"
        assert command[command.index("--proto") + 1] == "=https"
        for flag, content in (("--output", b"{}"), ("--dump-header", b"HTTP/2 200\r\nContent-Type: application/json\r\nSet-Cookie: private\r\n")):
            p = Path(command[command.index(flag) + 1]); destinations.append(p); p.write_bytes(content)
        return SimpleNamespace(returncode=0, stdout=b"200")
    with patch("connectors_core.bounded_curl.subprocess.run", side_effect=run):
        result = transport().send(request(), timeout_seconds=3, max_response_bytes=64, allow_redirects=False)
    assert result.status_code == 200
    assert "set-cookie" not in result.headers
    assert all(not p.exists() for p in destinations)


@pytest.mark.parametrize("url, redirects", [("https://evil.invalid/ogcapi/v1/collections/items", False), ("https://api.waterdata.usgs.gov/admin", False), ("https://api.waterdata.usgs.gov/ogcapi/v1/collections/items", True)])
def test_unadmitted_destination_or_redirect_cannot_start_a_process(url, redirects):
    with patch("connectors_core.bounded_curl.subprocess.run") as run:
        with pytest.raises(ValueError):
            transport().send(request(url), timeout_seconds=3, max_response_bytes=64, allow_redirects=redirects)
    run.assert_not_called()
