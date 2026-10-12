from typing import Any


def assert_jsonschema_subset(instance: Any, schema: dict[str, Any]) -> None:
    schema_type = schema.get("type")
    if schema_type == "object":
        assert isinstance(instance, dict), f"expected object, got {type(instance).__name__}"

        required = schema.get("required", [])
        for key in required:
            assert key in instance, f"missing required key: {key}"

        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                assert_jsonschema_subset(value, properties[key])

        additional = schema.get("additionalProperties", True)
        if additional is False:
            extra_keys = set(instance) - set(properties)
            assert not extra_keys, f"unexpected keys: {sorted(extra_keys)}"
        return

    if schema_type == "string":
        assert isinstance(instance, str), f"expected string, got {type(instance).__name__}"
        return

    if schema_type == "array":
        assert isinstance(instance, list), f"expected array, got {type(instance).__name__}"
        item_schema = schema.get("items")
        if item_schema:
            for item in instance:
                assert_jsonschema_subset(item, item_schema)
        return

    if schema_type == "number":
        assert isinstance(instance, (int, float)) and not isinstance(instance, bool), (
            f"expected number, got {type(instance).__name__}"
        )
        return

    if schema_type == "integer":
        assert isinstance(instance, int) and not isinstance(instance, bool), (
            f"expected integer, got {type(instance).__name__}"
        )
        return

    if schema_type == "boolean":
        assert isinstance(instance, bool), f"expected boolean, got {type(instance).__name__}"
        return

    if schema_type is None:
        return

    raise AssertionError(f"unsupported schema type for test validator: {schema_type}")
