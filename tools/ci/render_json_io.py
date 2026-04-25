#!/usr/bin/env python3
"""Shared JSON I/O helpers for CI renderer entrypoints.

Exports:
- ``MessageTemplate``: accepted template-like message input type.
- ``format_message``: defensive interpolation helper.
- ``read_json_object``: JSON object loader with deterministic CLI failures.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TypeAlias

__all__: tuple[str, str, str] = ("MessageTemplate", "format_message", "read_json_object")
MessageTemplate: TypeAlias = object


def format_message(template: object, **kwargs: object) -> str:
    """Format a message template defensively.

    Falls back to the raw template text if interpolation fails.
    """
    template_text = template if isinstance(template, str) else str(template)
    try:
        return template_text.format(**kwargs)
    except (AttributeError, KeyError, IndexError, TypeError, ValueError):
        return template_text


def read_json_object(
    path: str,
    *,
    not_found: MessageTemplate,
    non_utf8: MessageTemplate,
    invalid_json: MessageTemplate,
    unreadable: MessageTemplate,
    wrong_type: MessageTemplate,
) -> dict[str, object]:
    """Read a JSON file and require a top-level object payload.

    On read/parse/type failures, prints the provided message template to stderr
    and exits with code 2 to preserve renderer CLI contracts.
    """
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(format_message(not_found, path=path), file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(format_message(non_utf8, path=path), file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(format_message(invalid_json, path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(format_message(unreadable, path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(format_message(wrong_type, path=path), file=sys.stderr)
        raise SystemExit(2)

    return payload
