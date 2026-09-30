"""Deterministic transport tests; no provider requests or source admission."""
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlsplit

import pytest

from connectors_core.captured_json import canonical_bytes, decode_object
from connectors_core.transport import TransportResponse
from connectors.usgs.water_data.pilot_capture import capture, request_plan, safe_page_url

START, END = "2026-09-29T18:00:00Z", "2026-09-30T18:00:00Z"


class Clock:
    seconds = 0

    def monotonic(self):
        return self.seconds

    def now(self):
        return datetime(2026, 9, 30, 18, 1, tzinfo=timezone.utc)

    def sleep(self, seconds):
        self.seconds += seconds


class Transport:
    def __init__(self, responses=()):
        self.responses = list(responses)
        self.calls = []

    def send(self, request, **kwargs):
        self.calls.append((request, kwargs))
        if self.responses:
            result = self.responses.pop(0)
            if isinstance(result, Exception):
                raise result
            return result
        return response()


def response(value=None, status=200, headers=None):
    return TransportResponse(status, headers or {"content-type": "application/geo+json"},
                             (canonical_bytes(value or {"type": "FeatureCollection", "features": [], "links": []}),))


def test_complete_capture_is_bounded_and_replayable():
    transport = Transport()
    first = capture(START, END, transport=transport, clock=Clock())
    second = capture(START, END, transport=Transport(), clock=Clock())
    assert first == second and first.manifest["complete"]
    assert len(first.manifest["pages"]) == len(transport.calls) == 4
    assert first.manifest["source_admission"] == "PENDING"
    assert all(not options["allow_redirects"] and options["timeout_seconds"] <= 25
               for _, options in transport.calls)
    assert all("/v1/" in request.url for request, _ in transport.calls)


@pytest.mark.parametrize("url", [
    "https://evil.invalid/items", "http://api.waterdata.usgs.gov/ogcapi/v1/collections/continuous/items",
    "https://api.waterdata.usgs.gov:444/ogcapi/v1/collections/continuous/items",
    "https://api.waterdata.usgs.gov@evil.invalid/ogcapi/v1/collections/continuous/items",
])
def test_malicious_next_links_never_reach_transport(url):
    transport = Transport([response({"type": "FeatureCollection", "features": [],
                                      "links": [{"rel": "next", "href": url}]})])
    result = capture(START, END, transport=transport, clock=Clock())
    assert not result.manifest["complete"] and len(transport.calls) == 1
    assert len(result.objects) == 1


def test_rate_limit_obeys_bounded_retry_after():
    transport = Transport([response(status=429, headers={"retry-after": "3600"})])
    result = capture(START, END, transport=transport, clock=Clock())
    assert not result.manifest["complete"] and len(transport.calls) == 1
    assert result.manifest["attempts"][0]["outcome"] == "RATE_LIMITED"


def test_timeout_exhaustion_preserves_failure():
    transport = Transport([TimeoutError(), TimeoutError()])
    result = capture(START, END, transport=transport, clock=Clock())
    assert not result.manifest["complete"] and len(transport.calls) == 2
    assert result.manifest["attempts"][-1]["outcome"] == "TIMEOUT"


def test_malformed_bytes_retained_for_quarantine():
    transport = Transport([TransportResponse(200, {"content-type": "application/json"}, (b'{"a":1,"a":2}',))])
    result = capture(START, END, transport=transport, clock=Clock())
    assert not result.manifest["complete"] and len(result.objects) == 1


def test_scope_change_and_loop_rejected():
    request = request_plan(START, END)[0]
    with pytest.raises(ValueError):
        safe_page_url(request["url"] + "&agency_code=OTHER", request)
    value = {"type": "FeatureCollection", "features": [], "links": [{"rel": "next", "href": request["url"]}]}
    transport = Transport([response(value)])
    assert not capture(START, END, transport=transport, clock=Clock()).manifest["complete"]
    assert len(transport.calls) == 1


@pytest.mark.parametrize("raw", [b'{"n":NaN}', b'{"n":1e999}', b'{"n":1,"n":2}', b"[]"])
def test_strict_parser_rejects_ambiguous_content(raw):
    with pytest.raises(ValueError):
        decode_object(raw, limit=100)


def test_interval_scope_rejected_before_network():
    with pytest.raises(ValueError):
        request_plan("2004-01-01T00:00:00Z", END)
    assert all(parse_qs(urlsplit(item["url"]).query)["limit"] == ["1000"]
               for item in request_plan(START, END))
