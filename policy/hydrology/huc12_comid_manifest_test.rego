package kfm.hydrology.huc12_comid_manifest

base := {
  "layer_type": "huc12",
  "huc12": "031300010101",
  "snapshot_id": "wbd-2026-01",
  "nhd_snapshot_id": "nhdplushr-2026-01",
  "spec_hash": "sha256:abcdef123456",
  "run_receipt_url": "https://example.org/receipts/r1.json",
  "run_receipt_url_verified": true,
  "valid_from": "2026-01-01T00:00:00Z",
  "valid_to": "2026-12-31T23:59:59Z",
  "comid_crosswalk": "crosswalk.csv",
  "crosswalk_digest": "sha256:111111aa"
}

test_allow_same_manifest {
  input := {"previous": base, "current": base}
  allow with input as input
}

test_deny_changed_nhd_snapshot {
  input := {
    "previous": base,
    "current": object.union(base, {"nhd_snapshot_id": "nhdplushr-2026-02"})
  }
  deny_msg := deny[_] with input as input
  contains(deny_msg, "nhd_snapshot_id changed")
}

test_deny_changed_digest {
  input := {
    "previous": base,
    "current": object.union(base, {"crosswalk_digest": "sha256:999999"})
  }
  deny_msg := deny[_] with input as input
  contains(deny_msg, "crosswalk_digest changed")
}

test_deny_unverified_receipt {
  input := {
    "previous": base,
    "current": object.union(base, {"run_receipt_url_verified": false})
  }
  deny_msg := deny[_] with input as input
  deny_msg == "run_receipt_url_verified must be true"
}

test_deny_missing_previous {
  input := {"current": base}
  deny_msg := deny[_] with input as input
  deny_msg == "missing previous released manifest"
}
