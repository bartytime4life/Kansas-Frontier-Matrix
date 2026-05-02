package maps.signed_release_manifest

default decision := "deny"

valid_identity if startswith(input.signer_identity, "spiffe://kfm/signers/")
valid_release if input.release_state == "released"; input.policy_label == "public-safe"
valid_digest if input.signature.signed_digest == input.artifacts[0].digest
valid_bundle if input.signature.bundle
valid_public_href if not contains(lower(input.artifacts[0].href), "raw"); not contains(lower(input.artifacts[0].href), "work"); not contains(lower(input.artifacts[0].href), "quarantine"); not contains(lower(input.artifacts[0].href), "private")
valid_policy if input.policy_label == "public-safe"
allow if valid_identity; valid_release; valid_digest; valid_bundle; valid_public_href; valid_policy

decision := "allow" if allow
