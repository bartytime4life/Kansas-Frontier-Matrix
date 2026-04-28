class ValidationError(Exception):
    """Raised when a JSON instance fails schema validation."""


class SchemaError(Exception):
    """Raised when a provided JSON schema is invalid."""
