from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable, Iterator

from .exceptions import SchemaError, ValidationError


@dataclass(frozen=True)
class _ValidationIssue:
    path: tuple[Any, ...]
    message: str


class Draft202012Validator:
    def __init__(self, schema: dict[str, Any]) -> None:
        if not isinstance(schema, dict):
            raise SchemaError("schema must be a JSON object")
        self._schema = schema

    @staticmethod
    def check_schema(schema: dict[str, Any]) -> None:
        if not isinstance(schema, dict):
            raise SchemaError("schema must be a JSON object")

    def iter_errors(self, instance: Any) -> Iterator[_ValidationIssue]:
        yield from _iter_schema_errors(instance, self._schema, ())


_DEFAULT_DRAFT = Draft202012Validator


def validate(*, instance: Any, schema: dict[str, Any]) -> None:
    validator = _DEFAULT_DRAFT(schema)
    errors = list(validator.iter_errors(instance))
    if errors:
        raise ValidationError(errors[0].message)


def _iter_schema_errors(instance: Any, schema: dict[str, Any], path: tuple[Any, ...]) -> Iterable[_ValidationIssue]:
    schema_type = schema.get("type")
    if schema_type is not None:
        if schema_type == "object" and not isinstance(instance, dict):
            yield _ValidationIssue(path, "is not of type 'object'")
            return
        if schema_type == "array" and not isinstance(instance, list):
            yield _ValidationIssue(path, "is not of type 'array'")
            return
        if schema_type == "string" and not isinstance(instance, str):
            yield _ValidationIssue(path, "is not of type 'string'")
            return
        if schema_type == "boolean" and not isinstance(instance, bool):
            yield _ValidationIssue(path, "is not of type 'boolean'")
            return

    enum_values = schema.get("enum")
    if enum_values is not None and instance not in enum_values:
        yield _ValidationIssue(path, f"{instance!r} is not one of {enum_values}")

    if "const" in schema and instance != schema["const"]:
        yield _ValidationIssue(path, f"{instance!r} was expected to be constant {schema.get('const')!r}")

    if isinstance(instance, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(instance) < min_length:
            yield _ValidationIssue(path, f"is too short (minimum length: {min_length})")

        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.fullmatch(pattern, instance) is None:
            yield _ValidationIssue(path, f"does not match '{pattern}'")

    if isinstance(instance, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(instance) < min_items:
            yield _ValidationIssue(path, f"is too short (minimum size: {min_items})")

        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                yield from _iter_schema_errors(item, item_schema, (*path, index))

    if isinstance(instance, dict):
        required = schema.get("required")
        if isinstance(required, list):
            for key in required:
                if key not in instance:
                    yield _ValidationIssue(path, f"{key!r} is a required property")

        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            for key, subschema in properties.items():
                if key in instance and isinstance(subschema, dict):
                    yield from _iter_schema_errors(instance[key], subschema, (*path, key))

        if schema.get("additionalProperties") is False and isinstance(properties, dict):
            allowed_keys = set(properties)
            for key in instance:
                if key not in allowed_keys:
                    yield _ValidationIssue(path, f"Additional properties are not allowed ({key!r} was unexpected)")

    all_of = schema.get("allOf")
    if isinstance(all_of, list):
        for subschema in all_of:
            if isinstance(subschema, dict):
                yield from _iter_schema_errors(instance, subschema, path)

    if_schema = schema.get("if")
    then_schema = schema.get("then")
    else_schema = schema.get("else")
    if isinstance(if_schema, dict):
        if_matches = not any(_iter_schema_errors(instance, if_schema, path))
        branch = then_schema if if_matches else else_schema
        if isinstance(branch, dict):
            yield from _iter_schema_errors(instance, branch, path)


__all__ = [
    "Draft202012Validator",
    "SchemaError",
    "ValidationError",
    "validate",
]
