#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

__all__ = ["format_message", "read_json_object"]



def format_message(template: object, **kwargs: object) -> str:
    template_text = template if isinstance(template, str) else str(template)
    try:
        return template_text.format(**kwargs)
    except (AttributeError, KeyError, IndexError, TypeError, ValueError):
        return template_text


# Backward-compatible alias for internal callers.
_format_message = format_message


def read_json_object(
    path: str,
    *,
    not_found: object,
    non_utf8: object,
    invalid_json: object,
    unreadable: object,
    wrong_type: object,
) -> dict[str, object]:
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
