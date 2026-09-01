"""Compatibility helpers for Draft 2020-12 validator construction."""

from __future__ import annotations

import inspect
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

try:  # jsonschema >= 4.18
    from jsonschema.validators import RefResolver
except ImportError:  # pragma: no cover - older jsonschema layouts
    from jsonschema import RefResolver  # type: ignore[no-redef]


@lru_cache(maxsize=None)
def _schema_store(schema_root: str) -> dict[str, dict[str, Any]]:
    root = Path(schema_root)
    store: dict[str, dict[str, Any]] = {}
    for schema_path in sorted(root.rglob("*.schema.json")):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            store[schema_id] = schema
    return store


def load_draft202012_validator(
    schema: dict[str, Any],
    schema_root: Path,
    *,
    check_formats: bool = False,
) -> Draft202012Validator:
    kwargs: dict[str, Any] = {}
    if check_formats:
        kwargs["format_checker"] = FormatChecker()

    if "registry" in inspect.signature(Draft202012Validator).parameters:
        from referencing import Registry, Resource

        resources = (
            (schema_id, Resource.from_contents(contents))
            for schema_id, contents in _schema_store(str(schema_root)).items()
        )
        return Draft202012Validator(schema, registry=Registry().with_resources(resources), **kwargs)

    resolver = RefResolver.from_schema(schema, store=_schema_store(str(schema_root)))
    return Draft202012Validator(schema, resolver=resolver, **kwargs)
