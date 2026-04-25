#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def _format_message(template: object, **kwargs: object) -> str:
    template_text = template if isinstance(template, str) else str(template)
    try:
        return template_text.format(**kwargs)
    except (AttributeError, KeyError, IndexError, TypeError, ValueError):
        return template_text


def read_json_object(
    path: str,
    *,
    not_found: str,
    non_utf8: str,
    invalid_json: str,
    unreadable: str,
    wrong_type: str,
) -> dict:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(_format_message(not_found, path=path), file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(_format_message(non_utf8, path=path), file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(_format_message(invalid_json, path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(_format_message(unreadable, path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(_format_message(wrong_type, path=path), file=sys.stderr)
        raise SystemExit(2)

    return payload
