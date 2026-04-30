package flora.usda_plants_static_deployment

test_pass_clean_input if { count(deny with input as {"deployment_approval":{"approved_by":"a","approval_actor_type":"human"},"refs":["published/flora/usda_plants/2026-01-01/release_manifest.json"],"claims":{"external_basemap":false,"long_lived_secrets":false,"auto_merge":false},"hashes":["sha256:abc"],"attribution":"USDA PLANTS and county geometry authority"}) == 0 }
