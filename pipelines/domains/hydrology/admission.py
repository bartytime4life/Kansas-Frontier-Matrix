"""Read the admitted USGS water SourceDescriptor for package preparation.

Admission supplies the rights and sensitivity statements a package carries.
It grants no release: serving still requires a trusted release decision that
passes ``policy_runtime.serving_gate``.
"""
from pathlib import Path

from hashing import load_json_file

DESCRIPTOR = Path(__file__).resolve().parents[3] / "data/registry/sources/hydrology/usgs_nwis.yaml"
SOURCE_REF = "kfm://source/usgs-nwis"


def load_admission(path: Path = DESCRIPTOR) -> dict:
    """Return the admitted rights and sensitivity, or raise SOURCE_NOT_ADMITTED."""
    descriptor = load_json_file(path)
    try:
        admitted = (descriptor["object_type"] == "SourceDescriptor"
                    and descriptor["source_id"] == SOURCE_REF
                    and descriptor["review_state"] == "approved"
                    and descriptor["lifecycle"]["registry_state"] == "active"
                    and descriptor["rights"]["rights_status"] == "verified_open"
                    and descriptor["sensitivity_default"] == "public"
                    and descriptor["public_release"]["allowed"] is True)
        license_text = descriptor["rights"]["license_or_terms"]
        admitted_at = descriptor["rights"]["last_verified_at"]
    except (KeyError, TypeError):
        raise ValueError("SOURCE_NOT_ADMITTED") from None
    if not admitted or not isinstance(license_text, str) or not license_text:
        raise ValueError("SOURCE_NOT_ADMITTED")
    return {"source_ref": SOURCE_REF, "license": license_text, "admitted_at": admitted_at}
