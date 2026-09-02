from __future__ import annotations

import re

FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")


def visible_line_spans(text: str) -> list[tuple[int, int, str]]:
    """Return non-fenced Markdown lines with offsets into the original text."""
    visible: list[tuple[int, int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    fence_offset = 0
    offset = 0
    for raw_line in text.splitlines(keepends=True):
        line = raw_line.rstrip("\r\n")
        if fence_char is not None:
            closing = re.fullmatch(
                rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*",
                line,
            )
            if closing is not None:
                fence_char = None
                fence_length = 0
        else:
            opening = FENCE_OPEN_RE.match(line)
            if opening is not None:
                fence = opening.group("fence")
                fence_char = fence[0]
                fence_length = len(fence)
                fence_offset = offset
            else:
                visible.append((offset, offset + len(line), line))
        offset += len(raw_line)
    if fence_char is not None:
        fence = fence_char * fence_length
        raise ValueError(
            f"unterminated Markdown fence {fence!r} at offset {fence_offset}"
        )
    return visible
