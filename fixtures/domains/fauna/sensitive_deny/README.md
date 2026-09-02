# Fauna sensitive-deny fixtures

`fixtures/domains/fauna/sensitive_deny/`

Status: draft / fixture lane.

This directory is for small synthetic Fauna fixture examples that prove sensitive fauna records fail closed at public or semi-public surfaces. These fixtures exercise `DENY`, `ABSTAIN`, `RESTRICTED_ACCESS`, `GENERALIZED_GEOMETRY`, and related negative states when a request touches sensitive taxa, exact-location exposure, steward-controlled records, unknown rights, missing review state, missing redaction receipts, unreleased evidence, or re-identifying joins.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, policy decisions, sensitivity approvals, rights approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Fauna-domain fixture lane for sensitive-deny examples, not a data lifecycle root, not a policy root, not a source registry, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../layers/README.md`

## Related references

- `../../../../docs/domains/fauna/SENSITIVITY.md`
- `../../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/fauna/POLICY.md`
- `../../../../contracts/domains/fauna/redaction_receipt.md`
- `../../../../contracts/domains/fauna/sensitive_site.md`
- `../../../../policy/sensitivity/fauna/`
- `../../../../policy/domains/fauna/`
- `../../../../schemas/contracts/v1/domains/fauna/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json` examples that represent public-surface requests which must fail closed;
- matching `*.expected.json` examples for expected `DENY`, `ABSTAIN`, `RESTRICTED_ACCESS`, `GENERALIZED_GEOMETRY`, or `DENIED_BY_POLICY` outcomes;
- negative examples for sensitive occurrence, sensitive site, nest, den, roost, hibernaculum, spawning site, observer identity, steward-controlled record, unknown rights, missing review state, missing release state, or missing redaction receipt handling;
- synthetic click-resolution, Evidence Drawer, Focus Mode, renderer, layer-manifest, or governed-API examples that prove sensitive material is denied or generalized before public display;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, nest, den, roost, hibernacula, spawning-site, or sensitive-site records;
- source-system exports, live upstream fetch results, scraped payloads, steward-only records, or restricted agency records;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- EvidenceBundles, proof packs, receipts, release manifests, rollback cards, correction notices, or review records;
- policy rules, policy decisions, sensitivity approvals, rights approvals, or reviewer approvals;
- exact sensitive locations, reconstructive geoprivacy clues, concrete redaction radii, concrete fuzzing parameters, or side-channel hints that could help recover a sensitive site;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Prefer no geometry unless the test explicitly needs a geometry-shaped placeholder.
- When geometry shape is required, use coarse toy geometry that cannot be mistaken for a real fauna occurrence or sensitive site.
- Do not include real observer names, contact details, source-system identifiers, parcel-level hints, timestamps that could re-identify an observation, or taxon-site combinations that imply a real sensitive location.
- Pair each input with an expected denial, abstention, restricted-access, generalized-geometry, or denied-by-policy output when practical.
- Keep source role, evidence state, rights state, review state, sensitivity state, redaction-receipt state, release state, and correction path explicit.
- Treat `schema-valid` and `release-safe` as separate checks. A fixture can be intentionally schema-shaped while still proving that policy denies public exposure.
- Do not treat any fixture as evidence, approval, release state, policy authority, or a published artifact.

## Expected negative-state examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Sensitive occurrence exact-location request | `DENY` or `RESTRICTED_ACCESS` | Exact geometry must not reach public UI or Focus Mode. |
| Sensitive site, nest, den, roost, hibernaculum, or spawning site | `DENY` | Public exact-location exposure fails closed. |
| Missing `RedactionReceipt` for a generalized public derivative | `ABSTAIN` or `DENY` | Public-safe claim cannot be supported without transform evidence. |
| Unknown rights or steward-control status | `DENY` | Rights uncertainty does not degrade into public release. |
| Unreleased EvidenceBundle | `ABSTAIN` | Focus Mode and Evidence Drawer require released evidence. |
| Re-identifying cross-domain join | `DENY` | The joined output is treated as sensitive even if each source looked public alone. |
| Observer identity request for sensitive observation | `DENY` | Privacy and geoprivacy are enforced together. |
| Renderer receives sensitive geometry or forbidden fields | `ERROR` / deny fixture | Raw sensitive payload should never be considered renderable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, or expected-output names are added.
- Link each fixture to the validator, renderer check, governed-API contract, Focus Mode test, or documentation example that consumes it.
- Keep concrete geoprivacy parameters out of public fixture prose; binding values belong in `policy/sensitivity/fauna/` and must be reviewed before use.
- If a fixture needs to demonstrate a redaction receipt, use a synthetic receipt-shaped example rather than a real receipt.
- If a fixture accidentally includes real or reconstructive sensitive detail, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Policy-rule alignment: NEEDS VERIFICATION against `policy/sensitivity/fauna/` once the scaffold is replaced by authoritative content.
- Tests and validators: NOT RUN.
