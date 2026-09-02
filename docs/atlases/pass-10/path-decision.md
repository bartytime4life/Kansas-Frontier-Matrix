# Path decision - Pass 10 integration carrier

Truth label: CONFIRMED for the adopted responsibility-root and atlas-lane basis; PROPOSED for downstream operationalization families.

```yaml
path_decision:
  artifact: "Pass 10 changed-card integration carrier"
  proposed_path: "docs/atlases/pass-10/"
  artifact_kind: "human atlas plus derived downstream-carrier sidecars"
  authority_owner: "human-readable atlas lineage and integration traceability"
  lifecycle_stage: "not_applicable"
  execution_role: "none"
  scope_kind: "object_family"
  scope_id: "idea-index-category-atlas-pass-10"
  exposure: "internal"
  mutability: "versioned"
  retention: "durable_lineage"
  physical_storage: "Git-compatible workspace"
  evidence:
    - "KFM Pass 10 source PDF sha256:386fce4b5915257a162fa60b871d3e6cd857a94723ab0d120a818ef35ce643af"
    - "docs/doctrine/directory-rules.md sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e"
    - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md status:accepted"
    - "GitHub main inventory confirming docs/atlases/ and absence of docs/atlases/pass-10/"
  rules:
    - "DIR-SCOPE-001"
    - "DIR-DOCS-003"
    - "DIR-CONTROL-001"
    - "DIR-PLACE-005"
    - "DIR-README-001"
    - "DIR-README-005"
  outcome: "PLACE"
  outcome_limit: "Placement covers the non-authoritative carrier only; operational implementation remains HOLD."
```

## Basis

The artifact is a human-readable atlas lineage packet, so `docs/` owns its primary responsibility. Accepted ADR-0029 adopts the exact Directory Rules v2 bytes, which select plural `docs/atlases/` as the canonical collection spelling. The Pass 10 scope is a versioned child, and the packet contains admitted evidence artifacts rather than empty scaffolding.

The embedded and derived JSON sidecars remain downstream carriers colocated with the atlas packet; they are not machine governance registers. They cannot authorize rules, policies, data, release state, or implementation. Exact operational leaf paths remain on HOLD because each composite card still requires current per-family repository evidence, verified owners, consumer mapping, validation, and rollback design.
