#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


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
        print(not_found.format(path=path), file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(non_utf8.format(path=path), file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(invalid_json.format(path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(unreadable.format(path=path, exc=exc), file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(wrong_type.format(path=path), file=sys.stderr)
        raise SystemExit(2)

    return payload
