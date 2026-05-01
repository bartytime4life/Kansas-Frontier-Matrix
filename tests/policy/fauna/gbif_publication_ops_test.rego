package fauna.gbif_publication_ops_test
import data.fauna.gbif_publication_ops

test_missing_spec_hash_denied if {
  "missing_spec_hash" in gbif_publication_ops.deny with input as {"release_posture":"public_candidate"}
}
