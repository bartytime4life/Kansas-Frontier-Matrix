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
from .geojson import (
    DEFAULT_COORDINATE_PRECISION,
    GEOJSON_DIGEST_PROFILE,
    GeoJSONDigestError,
    GeoJSONFeatureDigests,
    compute_geojson_feature_digests,
    compute_geojson_geometry_hash,
    normalize_geojson_geometry,
)

__all__ = [
    "CANONICALIZATION_PROFILE",
    "DEFAULT_COORDINATE_PRECISION",
    "GEOJSON_DIGEST_PROFILE",
    "HASH_ALGORITHM",
    "SPEC_HASH_PREFIX",
    "CanonicalizationFailure",
    "GeoJSONDigestError",
    "GeoJSONFeatureDigests",
    "JsonInputError",
    "SpecHashError",
    "SpecHashFormatError",
    "VerificationResult",
    "canonicalize_json",
    "compute_geojson_feature_digests",
    "compute_geojson_geometry_hash",
    "compute_spec_hash",
    "is_valid_spec_hash",
    "load_json_file",
    "normalize_geojson_geometry",
    "verify_spec_hash",
]
