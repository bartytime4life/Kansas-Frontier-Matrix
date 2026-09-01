import re
from collections.abc import Sequence
from urllib.parse import parse_qsl


MAX_QUERY_STRING_LENGTH = 640
MAX_QUERY_FIELDS = 3
MAX_IDENTIFIER_LENGTH = 160

_SAFE_IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$")
_INVALID_PERCENT_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")


class InvalidRequest(ValueError):
    """Signal a bounded request-shape failure without retaining input detail."""


def is_safe_identifier(value: object) -> bool:
    return isinstance(value, str) and _SAFE_IDENTIFIER.fullmatch(value) is not None


def parse_exact_identifier_query(
    query_string: object,
    required_keys: Sequence[str],
) -> dict[str, str]:
    """Parse one closed query shape containing single-valued safe identifiers."""

    if not isinstance(query_string, str):
        raise InvalidRequest("invalid-query")
    if len(query_string) > MAX_QUERY_STRING_LENGTH:
        raise InvalidRequest("invalid-query")
    if any(ord(character) > 127 for character in query_string):
        raise InvalidRequest("invalid-query")

    expected = tuple(required_keys)
    if len(expected) > MAX_QUERY_FIELDS or len(set(expected)) != len(expected):
        raise InvalidRequest("invalid-query")
    if not expected:
        if query_string:
            raise InvalidRequest("invalid-query")
        return {}
    if not query_string or _INVALID_PERCENT_ESCAPE.search(query_string):
        raise InvalidRequest("invalid-query")

    try:
        pairs = parse_qsl(
            query_string,
            keep_blank_values=True,
            strict_parsing=True,
            encoding="utf-8",
            errors="strict",
            max_num_fields=MAX_QUERY_FIELDS,
        )
    except (UnicodeError, ValueError):
        raise InvalidRequest("invalid-query") from None

    if len(pairs) != len(expected):
        raise InvalidRequest("invalid-query")

    parsed: dict[str, str] = {}
    expected_set = set(expected)
    for key, value in pairs:
        if key not in expected_set or key in parsed:
            raise InvalidRequest("invalid-query")
        if len(value) > MAX_IDENTIFIER_LENGTH or not _SAFE_IDENTIFIER.fullmatch(value):
            raise InvalidRequest("invalid-query")
        parsed[key] = value

    if set(parsed) != expected_set:
        raise InvalidRequest("invalid-query")
    return parsed
