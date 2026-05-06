package tests.policy.tiles.pmtiles

import data.tiles.pmtiles.deny

test_valid_manifest_allows if {
  count(deny) with input as {
    "base_archive": {"href": "https://cdn/base.pmtiles", "digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
    "delta_archive": {"href": "https://cdn/delta.pmtiles", "digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "completeness_pct": 0.95},
    "masked_pct": 0.1,
    "attestations": {"steward": "s", "reviewer": "r"},
    "rights": "public",
    "license": "CC-BY-4.0",
    "proof_refs": ["proof://1"],
    "signature_refs": ["sig://1"],
    "geoprivacy": {"sensitive_geometry": false, "redaction_receipt": null}
  } == 0
}

test_reject_high_masked_pct if {
  "masked_pct > 30% is reject" in deny with input as {
    "base_archive": {"href": "https://cdn/base.pmtiles", "digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
    "delta_archive": {"href": "https://cdn/delta.pmtiles", "digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "completeness_pct": 0.95},
    "masked_pct": 0.31,
    "attestations": {"steward": "s", "reviewer": "r"},
    "rights": "public",
    "license": "CC-BY-4.0",
    "proof_refs": ["proof://1"],
    "signature_refs": ["sig://1"],
    "geoprivacy": {"sensitive_geometry": false, "redaction_receipt": null}
  }
}
