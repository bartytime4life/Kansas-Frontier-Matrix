from __future__ import annotations

import re

FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")
HTML_COMMENT_OPEN_RE = re.compile(r"^ {0,3}<!--")


def _is_indented_code_line(line: str) -> bool:
    if not line.strip():
        return False
    column = 0
    for character in line:
        if character == " ":
            column += 1
        elif character == "\t":
            column += 4 - (column % 4)
        else:
            return False
        if column >= 4:
            return True
    return False


def visible_line_spans(text: str) -> list[tuple[int, int, str]]:
    """Return non-code Markdown lines with offsets into the original text."""
    visible: list[tuple[int, int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    fence_offset = 0
    html_comment_offset: int | None = None
    offset = 0
    for raw_line in text.splitlines(keepends=True):
        line = raw_line.rstrip("\r\n")
        if html_comment_offset is not None:
            if "-->" in line:
                html_comment_offset = None
        elif fence_char is not None:
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
                info = line[opening.end("fence") :]
                if fence[0] == "`" and "`" in info:
                    raise ValueError(
                        "backtick fence info contains backtick "
                        f"at offset {offset}"
                    )
                fence_char = fence[0]
                fence_length = len(fence)
                fence_offset = offset
            elif _is_indented_code_line(line):
                pass
            elif HTML_COMMENT_OPEN_RE.match(line) is not None:
                if "-->" not in line:
                    html_comment_offset = offset
            else:
                visible.append((offset, offset + len(line), line))
        offset += len(raw_line)
    if fence_char is not None:
        fence = fence_char * fence_length
        raise ValueError(
            f"unterminated Markdown fence {fence!r} at offset {fence_offset}"
        )
    if html_comment_offset is not None:
        raise ValueError(
            f"unterminated Markdown HTML comment at offset {html_comment_offset}"
        )
    return visible
