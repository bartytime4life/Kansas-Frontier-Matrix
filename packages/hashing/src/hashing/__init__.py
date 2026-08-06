"""Public API for deterministic KFM content hashing."""

from .core import (
    CANONICALIZATION_PROFILE,
    HASH_ALGORITHM,
    SPEC_HASH_PREFIX,
    CanonicalizationFailure,
    JsonInputError,
    SpecHashError,
    SpecHashFormatError,
    VerificationResult,
    canonicalize_json,
    compute_spec_hash,
    is_valid_spec_hash,
    load_json_file,
    verify_spec_hash,
)

__all__ = [
    "CANONICALIZATION_PROFILE",
    "HASH_ALGORITHM",
    "SPEC_HASH_PREFIX",
    "CanonicalizationFailure",
    "JsonInputError",
    "SpecHashError",
    "SpecHashFormatError",
    "VerificationResult",
    "canonicalize_json",
    "compute_spec_hash",
    "is_valid_spec_hash",
    "load_json_file",
    "verify_spec_hash",
]
