from __future__ import annotations

import re

FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")
RAW_HTML_BLOCK_SPECS = (
    (
        re.compile(r"^ {0,3}<!--"),
        re.compile(r"--!?>"),
        "Markdown HTML comment",
    ),
    (
        re.compile(
            r"^ {0,3}<(?:pre|script|style|textarea)(?=[ \t>]|$)",
            re.IGNORECASE,
        ),
        re.compile(r"</(?:pre|script|style|textarea)>", re.IGNORECASE),
        "Markdown raw HTML element block",
    ),
    (
        re.compile(r"^ {0,3}<\?"),
        re.compile(r"\?>"),
        "Markdown HTML processing instruction",
    ),
    (
        re.compile(r"^ {0,3}<!\[CDATA\["),
        re.compile(r"\]\]>"),
        "Markdown CDATA block",
    ),
    (
        re.compile(r"^ {0,3}<![A-Za-z]"),
        re.compile(r">"),
        "Markdown HTML declaration",
    ),
)


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
    """Return rendered inventory lines with offsets into the original text."""
    visible: list[tuple[int, int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    fence_offset = 0
    raw_html_end: re.Pattern[str] | None = None
    raw_html_name: str | None = None
    raw_html_offset = 0
    offset = 0
    for raw_line in text.splitlines(keepends=True):
        line = raw_line.rstrip("\r\n")
        if raw_html_end is not None:
            if raw_html_end.search(line) is not None:
                raw_html_end = None
                raw_html_name = None
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
            else:
                for opening, ending, name in RAW_HTML_BLOCK_SPECS:
                    if opening.match(line) is None:
                        continue
                    if ending.search(line) is None:
                        raw_html_end = ending
                        raw_html_name = name
                        raw_html_offset = offset
                    break
                else:
                    visible.append((offset, offset + len(line), line))
        offset += len(raw_line)
    if fence_char is not None:
        fence = fence_char * fence_length
        raise ValueError(
            f"unterminated Markdown fence {fence!r} at offset {fence_offset}"
        )
    if raw_html_end is not None:
        raise ValueError(f"unterminated {raw_html_name} at offset {raw_html_offset}")
    return visible
