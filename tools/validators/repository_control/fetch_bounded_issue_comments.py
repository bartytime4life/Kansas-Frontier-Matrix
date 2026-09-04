#!/usr/bin/env python3
"""Capture repository-control issue comments through strict resource bounds.

The helper reads one GitHub API page at a time, rejects oversized or structurally
unsafe pages before they can become control input, and writes only one of two
local source states: ``AVAILABLE`` with a complete bounded page array, or
``UNAVAILABLE`` with an empty comments array. The downstream trusted-base source
validator remains responsible for the blocking classification.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
from dataclasses import dataclass
from http.client import HTTPException
from pathlib import Path
from typing import Any, Callable, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

PER_PAGE = 100
MAX_PAGES = 100
MAX_PAGE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 16 * 1024 * 1024
MAX_JSON_DEPTH = 32
MAX_PAGE_NODES = 100_000
MAX_TOTAL_NODES = 1_000_000
MAX_INTEGER_DIGITS = 128
MAX_FLOAT_TOKEN_CHARS = 128
READ_CHUNK_BYTES = 64 * 1024
REQUEST_TIMEOUT_SECONDS = 20
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CONTENT_LENGTH_PATTERN = re.compile(r"^[0-9]+$")


class CaptureError(ValueError):
    """Raised when the remote source cannot be captured within its bounds."""

    def __init__(self, reason_code: str) -> None:
        super().__init__(reason_code)
        self.reason_code = reason_code


@dataclass(frozen=True)
class CaptureResult:
    status: str
    reason_code: str
    pages: int
    comments: int
    transferred_bytes: int

    def as_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "reason_code": self.reason_code,
            "pages": self.pages,
            "comments": self.comments,
            "transferred_bytes": self.transferred_bytes,
        }


@dataclass(frozen=True)
class BoundedPages:
    value: list[list[dict[str, Any]]]
    comment_count: int
    transferred_bytes: int
    node_count: int


def _object_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")
        result[key] = value
    return result


def _reject_constant(_value: str) -> Any:
    raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")


def _parse_int(value: str) -> int:
    digits = value[1:] if value.startswith("-") else value
    if not digits or len(digits) > MAX_INTEGER_DIGITS:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")
    try:
        return int(value)
    except (ValueError, OverflowError) as exc:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID") from exc


def _parse_float(value: str) -> float:
    if len(value) > MAX_FLOAT_TOKEN_CHARS:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")
    try:
        parsed = float(value)
    except (ValueError, OverflowError) as exc:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID") from exc
    if not math.isfinite(parsed):
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")
    return parsed


def _strict_json_text(value: object) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError, RecursionError) as exc:
        raise CaptureError("CONTROL_SOURCE_SERIALIZATION_INVALID") from exc


def _header_text(value: object) -> str:
    """Return one textual header value or reject the response shape."""

    if not isinstance(value, str):
        raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID")
    return value


def _header_values(response: Any, name: str) -> list[str]:
    """Return all visible textual values for one response header."""

    headers = getattr(response, "headers", None)
    if headers is not None:
        get_all = getattr(headers, "get_all", None)
        if callable(get_all):
            values = get_all(name)
            if values is not None:
                if isinstance(values, str):
                    return [values]
                if not isinstance(values, (list, tuple)):
                    raise CaptureError(
                        "CONTROL_SOURCE_CONTENT_LENGTH_INVALID"
                    )
                return [_header_text(value) for value in values]

        get = getattr(headers, "get", None)
        if callable(get):
            value = get(name)
            if value is not None:
                return [_header_text(value)]

    getheader = getattr(response, "getheader", None)
    if callable(getheader):
        value = getheader(name)
        if value is not None:
            return [_header_text(value)]

    return []

def _declared_content_length(response: Any) -> int | None:
    """Return one strict Content-Length value or fail on ambiguity/malformed input."""

    raw_values = _header_values(response, "Content-Length")
    if not raw_values:
        return None

    tokens: list[str] = []
    for raw_value in raw_values:
        if not isinstance(raw_value, str):
            raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID")
        tokens.extend(part.strip() for part in raw_value.split(","))

    if not tokens:
        raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID")

    parsed_values: set[int] = set()
    for token in tokens:
        if (
            not token
            or len(token) > MAX_INTEGER_DIGITS
            or CONTENT_LENGTH_PATTERN.fullmatch(token) is None
        ):
            raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID")
        try:
            parsed_values.add(int(token))
        except (ValueError, OverflowError) as exc:
            raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID") from exc

    if len(parsed_values) != 1:
        raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_INVALID")
    return parsed_values.pop()


def _bounded_read(
    response: Any,
    *,
    maximum_bytes: int,
    overflow_reason: str,
) -> bytes:
    """Read one complete response under a byte limit and verify declared length."""

    declared_length = _declared_content_length(response)
    if declared_length is not None and declared_length > maximum_bytes:
        raise CaptureError(overflow_reason)

    chunks: list[bytes] = []
    size = 0
    while True:
        # Read no more than the remaining allowance plus one byte. That final
        # byte proves overflow without consuming an arbitrary transport chunk.
        read_size = min(READ_CHUNK_BYTES, maximum_bytes - size + 1)
        if read_size <= 0:  # pragma: no cover - defensive.
            raise CaptureError(overflow_reason)

        chunk = response.read(read_size)
        if not chunk:
            break
        if not isinstance(chunk, bytes) or len(chunk) > read_size:
            raise CaptureError("CONTROL_SOURCE_PAGE_READ_INVALID")

        size += len(chunk)
        if size > maximum_bytes:
            raise CaptureError(overflow_reason)
        chunks.append(chunk)

    if declared_length is not None and size != declared_length:
        raise CaptureError("CONTROL_SOURCE_CONTENT_LENGTH_MISMATCH")

    return b"".join(chunks)


def _measure_structure(
    value: object,
    *,
    maximum_depth: int,
    maximum_nodes: int,
    node_overflow_reason: str,
) -> int:
    """Measure an already byte-bounded JSON value without recursive traversal."""

    stack: list[tuple[object, int]] = [(value, 1)]
    nodes = 0
    while stack:
        current, depth = stack.pop()
        if depth > maximum_depth:
            raise CaptureError("CONTROL_SOURCE_PAGE_DEPTH_EXCEEDED")

        nodes += 1
        if nodes > maximum_nodes:
            raise CaptureError(node_overflow_reason)

        if isinstance(current, dict):
            stack.extend((child, depth + 1) for child in current.values())
        elif isinstance(current, list):
            stack.extend((child, depth + 1) for child in current)

    return nodes


def _page_url(
    *, api_url: str, repository: str, control_issue: int, page: int, per_page: int
) -> str:
    owner, name = repository.split("/", 1)
    return (
        f"{api_url.rstrip('/')}/repos/{quote(owner, safe='')}/"
        f"{quote(name, safe='')}/issues/{control_issue}/comments"
        f"?per_page={per_page}&page={page}"
    )


def _read_page(
    *,
    opener: Callable[..., Any],
    api_url: str,
    repository: str,
    control_issue: int,
    page: int,
    per_page: int,
    token: str,
    maximum_bytes: int,
    byte_overflow_reason: str,
    maximum_depth: int,
    maximum_nodes: int,
    node_overflow_reason: str,
) -> tuple[list[dict[str, Any]], int, int]:
    request = Request(
        _page_url(
            api_url=api_url,
            repository=repository,
            control_issue=control_issue,
            page=page,
            per_page=per_page,
        ),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "kfm-repository-control-bounded-capture",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="GET",
    )
    try:
        with opener(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            if getattr(response, "status", 200) != 200:
                raise CaptureError("CONTROL_SOURCE_FETCH_FAILED")
            encoded = _bounded_read(
                response,
                maximum_bytes=maximum_bytes,
                overflow_reason=byte_overflow_reason,
            )
    except CaptureError:
        raise
    except (
        HTTPError,
        URLError,
        HTTPException,
        OSError,
        TimeoutError,
    ) as exc:
        raise CaptureError("CONTROL_SOURCE_FETCH_FAILED") from exc

    try:
        value = json.loads(
            encoded.decode("utf-8"),
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_constant,
            parse_float=_parse_float,
            parse_int=_parse_int,
        )
    except CaptureError:
        raise
    except (
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        OverflowError,
        RecursionError,
    ) as exc:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID") from exc

    node_count = _measure_structure(
        value,
        maximum_depth=maximum_depth,
        maximum_nodes=maximum_nodes,
        node_overflow_reason=node_overflow_reason,
    )

    if not isinstance(value, list):
        raise CaptureError("CONTROL_SOURCE_PAGE_SHAPE_INVALID")
    if len(value) > per_page:
        raise CaptureError("CONTROL_SOURCE_PAGE_COUNT_EXCEEDED")
    if any(not isinstance(comment, dict) for comment in value):
        raise CaptureError("CONTROL_SOURCE_PAGE_SHAPE_INVALID")
    return value, len(encoded), node_count


def fetch_bounded_pages(
    *,
    repository: str,
    control_issue: int,
    token: str,
    api_url: str = "https://api.github.com",
    opener: Callable[..., Any] = urlopen,
    per_page: int = PER_PAGE,
    max_pages: int = MAX_PAGES,
    max_page_bytes: int = MAX_PAGE_BYTES,
    max_total_bytes: int = MAX_TOTAL_BYTES,
    max_json_depth: int = MAX_JSON_DEPTH,
    max_page_nodes: int = MAX_PAGE_NODES,
    max_total_nodes: int = MAX_TOTAL_NODES,
) -> BoundedPages:
    """Return a complete page array or fail before exceeding resource limits."""

    if REPOSITORY_PATTERN.fullmatch(repository) is None:
        raise CaptureError("CONTROL_SOURCE_REPOSITORY_INVALID")
    if (
        not isinstance(control_issue, int)
        or isinstance(control_issue, bool)
        or control_issue <= 0
    ):
        raise CaptureError("CONTROL_SOURCE_ISSUE_INVALID")
    if not token:
        raise CaptureError("CONTROL_SOURCE_TOKEN_UNAVAILABLE")
    if not api_url.startswith("https://"):
        raise CaptureError("CONTROL_SOURCE_API_URL_INVALID")
    limits = (
        per_page,
        max_pages,
        max_page_bytes,
        max_total_bytes,
        max_json_depth,
        max_page_nodes,
        max_total_nodes,
    )
    if any(
        not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0
        for limit in limits
    ):
        raise CaptureError("CONTROL_SOURCE_LIMIT_INVALID")

    pages: list[list[dict[str, Any]]] = []
    comment_count = 0
    transferred_bytes = 0
    total_nodes = 0

    # One sentinel page beyond the admitted page count proves completeness when
    # the final admitted page contains exactly ``per_page`` records.
    for page_number in range(1, max_pages + 2):
        remaining_total_bytes = max_total_bytes - transferred_bytes
        if remaining_total_bytes <= 0:
            raise CaptureError("CONTROL_SOURCE_TOTAL_BYTES_EXCEEDED")

        page_byte_budget = min(max_page_bytes, remaining_total_bytes)
        byte_overflow_reason = (
            "CONTROL_SOURCE_PAGE_BYTES_EXCEEDED"
            if max_page_bytes <= remaining_total_bytes
            else "CONTROL_SOURCE_TOTAL_BYTES_EXCEEDED"
        )

        remaining_total_nodes = max_total_nodes - total_nodes
        if remaining_total_nodes <= 0:
            raise CaptureError("CONTROL_SOURCE_TOTAL_NODES_EXCEEDED")
        page_node_budget = min(max_page_nodes, remaining_total_nodes)
        node_overflow_reason = (
            "CONTROL_SOURCE_PAGE_NODES_EXCEEDED"
            if max_page_nodes <= remaining_total_nodes
            else "CONTROL_SOURCE_TOTAL_NODES_EXCEEDED"
        )

        page, page_bytes, page_nodes = _read_page(
            opener=opener,
            api_url=api_url,
            repository=repository,
            control_issue=control_issue,
            page=page_number,
            per_page=per_page,
            token=token,
            maximum_bytes=page_byte_budget,
            byte_overflow_reason=byte_overflow_reason,
            maximum_depth=max_json_depth,
            maximum_nodes=page_node_budget,
            node_overflow_reason=node_overflow_reason,
        )
        transferred_bytes += page_bytes
        total_nodes += page_nodes

        if page_number > max_pages:
            if page:
                raise CaptureError("CONTROL_SOURCE_PAGE_LIMIT_EXCEEDED")
            break
        if not page:
            break

        comment_count += len(page)
        if comment_count > per_page * max_pages:
            raise CaptureError("CONTROL_SOURCE_COMMENT_LIMIT_EXCEEDED")
        pages.append(page)
        if len(page) < per_page:
            break
    else:  # pragma: no cover - defensive; the finite loop always terminates.
        raise CaptureError("CONTROL_SOURCE_PAGE_LIMIT_EXCEEDED")

    try:
        serialized = _strict_json_text(pages).encode("ascii")
    except (UnicodeError, CaptureError) as exc:
        if isinstance(exc, CaptureError):
            raise
        raise CaptureError("CONTROL_SOURCE_SERIALIZATION_INVALID") from exc
    if len(serialized) > max_total_bytes:
        raise CaptureError("CONTROL_SOURCE_SERIALIZED_BYTES_EXCEEDED")
    return BoundedPages(pages, comment_count, transferred_bytes, total_nodes)


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(_strict_json_text(value) + "\n", encoding="utf-8")
    temporary.replace(path)


def capture_to_files(
    *,
    repository: str,
    control_issue: int,
    token: str,
    comments_output: Path,
    status_output: Path,
    api_url: str = "https://api.github.com",
    opener: Callable[..., Any] = urlopen,
    per_page: int = PER_PAGE,
    max_pages: int = MAX_PAGES,
    max_page_bytes: int = MAX_PAGE_BYTES,
    max_total_bytes: int = MAX_TOTAL_BYTES,
    max_json_depth: int = MAX_JSON_DEPTH,
    max_page_nodes: int = MAX_PAGE_NODES,
    max_total_nodes: int = MAX_TOTAL_NODES,
) -> CaptureResult:
    """Write strict source files while keeping transport failures fail-closed."""

    try:
        bounded = fetch_bounded_pages(
            repository=repository,
            control_issue=control_issue,
            token=token,
            api_url=api_url,
            opener=opener,
            per_page=per_page,
            max_pages=max_pages,
            max_page_bytes=max_page_bytes,
            max_total_bytes=max_total_bytes,
            max_json_depth=max_json_depth,
            max_page_nodes=max_page_nodes,
            max_total_nodes=max_total_nodes,
        )
    except CaptureError as exc:
        _write_json(comments_output, [])
        _write_json(
            status_output,
            {
                "schema_version": "1.0.0",
                "repository": repository,
                "control_issue": control_issue,
                "status": "UNAVAILABLE",
            },
        )
        return CaptureResult("UNAVAILABLE", exc.reason_code, 0, 0, 0)

    _write_json(comments_output, bounded.value)
    _write_json(
        status_output,
        {
            "schema_version": "1.0.0",
            "repository": repository,
            "control_issue": control_issue,
            "status": "AVAILABLE",
        },
    )
    return CaptureResult(
        "AVAILABLE",
        "CONTROL_SOURCE_CAPTURE_BOUNDED",
        len(bounded.value),
        bounded.comment_count,
        bounded.transferred_bytes,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--control-issue", required=True, type=int)
    parser.add_argument("--comments-output", required=True, type=Path)
    parser.add_argument("--status-output", required=True, type=Path)
    parser.add_argument(
        "--api-url", default=os.environ.get("GITHUB_API_URL", "https://api.github.com")
    )
    args = parser.parse_args(argv)

    result = capture_to_files(
        repository=args.repository,
        control_issue=args.control_issue,
        token=os.environ.get("GH_TOKEN", ""),
        comments_output=args.comments_output,
        status_output=args.status_output,
        api_url=args.api_url,
    )
    print(_strict_json_text(result.as_dict()))

    # Source availability is classified by the next trusted-base validator.
    # Returning zero ensures transport/parser errors are represented by the
    # bounded UNAVAILABLE status instead of bypassing that classification step.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
