#!/usr/bin/env python3
"""Capture repository-control issue comments through strict resource bounds.

The helper reads one GitHub API page at a time, rejects oversized pages or
aggregates before JSON materialization can grow without bound, and writes only
one of two local source states: ``AVAILABLE`` with the complete bounded page
array, or ``UNAVAILABLE`` with an empty comments array. The downstream trusted-
base source validator remains responsible for the blocking classification.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

PER_PAGE = 100
MAX_PAGES = 100
MAX_PAGE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 16 * 1024 * 1024
READ_CHUNK_BYTES = 64 * 1024
REQUEST_TIMEOUT_SECONDS = 20
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


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


def _object_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID")
        result[key] = value
    return result


def _bounded_read(
    response: Any,
    *,
    maximum_bytes: int,
    overflow_reason: str,
) -> bytes:
    """Read at most ``maximum_bytes`` plus one bounded overflow probe."""

    chunks: list[bytes] = []
    size = 0
    while True:
        # Read no more than the remaining allowance plus one byte. That final
        # byte is sufficient to prove overflow without consuming an arbitrary
        # transport chunk beyond the configured boundary.
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

    return b"".join(chunks)


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
    overflow_reason: str,
) -> tuple[list[dict[str, Any]], int]:
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
                overflow_reason=overflow_reason,
            )
    except CaptureError:
        raise
    except (HTTPError, URLError, OSError, TimeoutError) as exc:
        raise CaptureError("CONTROL_SOURCE_FETCH_FAILED") from exc

    try:
        value = json.loads(
            encoded.decode("utf-8"), object_pairs_hook=_object_no_duplicates
        )
    except CaptureError:
        raise
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise CaptureError("CONTROL_SOURCE_PAGE_JSON_INVALID") from exc

    if not isinstance(value, list):
        raise CaptureError("CONTROL_SOURCE_PAGE_SHAPE_INVALID")
    if len(value) > per_page:
        raise CaptureError("CONTROL_SOURCE_PAGE_COUNT_EXCEEDED")
    if any(not isinstance(comment, dict) for comment in value):
        raise CaptureError("CONTROL_SOURCE_PAGE_SHAPE_INVALID")
    return value, len(encoded)


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
    limits = (per_page, max_pages, max_page_bytes, max_total_bytes)
    if any(
        not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0
        for limit in limits
    ):
        raise CaptureError("CONTROL_SOURCE_LIMIT_INVALID")

    pages: list[list[dict[str, Any]]] = []
    comment_count = 0
    transferred_bytes = 0

    # One sentinel page beyond the admitted page count proves completeness when
    # the final admitted page contains exactly ``per_page`` records.
    for page_number in range(1, max_pages + 2):
        remaining_total_bytes = max_total_bytes - transferred_bytes
        if remaining_total_bytes <= 0:
            raise CaptureError("CONTROL_SOURCE_TOTAL_BYTES_EXCEEDED")

        page_budget = min(max_page_bytes, remaining_total_bytes)
        overflow_reason = (
            "CONTROL_SOURCE_PAGE_BYTES_EXCEEDED"
            if max_page_bytes <= remaining_total_bytes
            else "CONTROL_SOURCE_TOTAL_BYTES_EXCEEDED"
        )
        page, page_bytes = _read_page(
            opener=opener,
            api_url=api_url,
            repository=repository,
            control_issue=control_issue,
            page=page_number,
            per_page=per_page,
            token=token,
            maximum_bytes=page_budget,
            overflow_reason=overflow_reason,
        )
        transferred_bytes += page_bytes

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

    serialized = json.dumps(
        pages, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    if len(serialized) > max_total_bytes:
        raise CaptureError("CONTROL_SOURCE_SERIALIZED_BYTES_EXCEEDED")
    return BoundedPages(pages, comment_count, transferred_bytes)


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n",
        encoding="utf-8",
    )
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
    print(json.dumps(result.as_dict(), sort_keys=True, separators=(",", ":")))

    # Source availability is classified by the next trusted-base validator.
    # Returning zero here ensures transport errors are represented by the
    # bounded UNAVAILABLE status instead of bypassing that classification step.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
