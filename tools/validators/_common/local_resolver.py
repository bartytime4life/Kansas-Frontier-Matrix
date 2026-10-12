import json
from pathlib import Path

from referencing import Registry, Resource


def build_registry(repo_root: Path) -> Registry:
    schema_root = repo_root / "schemas" / "contracts" / "v1"
    if not schema_root.exists():
        raise FileNotFoundError(f"Schema root not found: {schema_root}")

    resources = {}
    for schema_path in sorted(schema_root.rglob("*.schema.json")):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_id = schema.get("$id")
        if not schema_id:
            continue
        if schema_id in resources:
            raise ValueError(f"Duplicate schema $id detected: {schema_id}")
        resources[schema_id] = Resource.from_contents(schema)

    return Registry().with_resources(resources.items())
