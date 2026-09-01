from __future__ import annotations

from typing import Any

from jsonschema import Draft202012Validator


def assert_jsonschema_subset(instance: Any, schema: dict[str, Any]) -> None:
    """Validate that an instance satisfies the provided JSON Schema.

    This helper intentionally treats the schema as a contract check, not a subset
    transformation; the app tests only require that the payload match the target
    response envelope and fail closed when it does not.
    """
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda err: list(err.path))
    if errors:
        details = "; ".join(f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}" for error in errors)
        raise AssertionError(f"JSON schema validation failed: {details}")
