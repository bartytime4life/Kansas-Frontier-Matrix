"""Public boundary for the KFM local schema-registry helper package."""

from schema_registry.core import (
    LookupOutcome,
    LookupResult,
    RegistryErrorCode,
    RegistrySnapshot,
    SchemaRecord,
    SchemaRegistryError,
    SkippedSchema,
    build_referencing_registry,
    build_registry_snapshot,
)

__all__ = [
    "LookupOutcome",
    "LookupResult",
    "RegistryErrorCode",
    "RegistrySnapshot",
    "SchemaRecord",
    "SchemaRegistryError",
    "SkippedSchema",
    "build_referencing_registry",
    "build_registry_snapshot",
]

__version__ = "0.1.0"
