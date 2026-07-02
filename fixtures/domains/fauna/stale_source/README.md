# Fauna stale-source fixtures

`fixtures/domains/fauna/stale_source/`

Status: draft / fixture lane.

This directory is for small synthetic Fauna fixture examples that prove stale source handling behaves correctly at public and semi-public KFM surfaces. These fixtures exercise `SOURCE_STALE`, stale badges, bounded `ABSTAIN` behavior, freshness-window checks, release/correction lineage visibility, and safe fallback behavior when a fauna claim depends on out-of-date, superseded, withdrawn, or freshness-unknown support.

These files are examples only. They are not authoritative project records, source records, EvidenceBundles, source descriptors, source-refresh receipts, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Placement basis

Directory rules and the root fixture README keep fixture material under the `fixtures/` responsibility root. This lane is therefore a Fauna-domain fixture lane for stale-source examples, not a data lifecycle root, not a source registry, not a policy root, not a release root, and not a publication target.

The root fixture README also states that `fixtures/` is for operational rendering inputs rather than validator-only test data, and that fixtures must not contain RAW, WORK, QUARANTINE data, sensitive exact geometry, or canonical truth. This README inherits those boundaries.

## Related fixture lanes

- `../README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../layers/README.md`
- `../sensitive_deny/README.md`

## Related references

- `../../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/fauna/SENSITIVITY.md`
- `../../../../docs/domains/fauna/DATA_LIFECYCLE.md`
- `../../../../docs/domains/fauna/POLICY.md`
- `../../../../data/registry/sources/fauna/`
- `../../../../contracts/domains/fauna/domain_observation.md`
- `../../../../contracts/domains/fauna/domain_validation_report.md`
- `../../../../policy/domains/fauna/`
- `../../../../schemas/contracts/v1/domains/fauna/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json` examples that represent stale, freshness-unknown, withdrawn, superseded, or out-of-window fauna support;
- matching `*.expected.json` examples for expected `SOURCE_STALE`, `ABSTAIN`, `RELEASE_WITHDRAWN`, `CONFLICTED_SUPPORT`, or safe fallback outcomes;
- stale `EvidenceDrawerPayload`-shaped examples that require a stale badge and limit consequential claims;
- stale `LayerManifest`- or layer-state-shaped examples that verify UI trust-visible state behavior;
- Focus Mode examples proving that stale evidence can be summarized only with explicit caveats, or must abstain when the claim is consequential;
- synthetic examples where a source refresh is needed but not yet proven by a receipt or review state;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for:

- authoritative taxon, occurrence, monitoring, mortality, disease, invasive-species, range, or sensitive-site records;
- source-system exports, live upstream fetch results, scraped payloads, steward-only records, or restricted agency records;
- real source-refresh logs, real source descriptors, real update timestamps, or real upstream freshness windows unless they have been intentionally reduced to synthetic examples;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, registry, or release-lifecycle artifacts;
- EvidenceBundles, proof packs, run receipts, source-refresh receipts, release manifests, rollback cards, correction notices, or review records;
- policy rules, policy decisions, freshness policy thresholds, sensitivity approvals, rights approvals, or reviewer approvals;
- exact sensitive locations, reconstructive geoprivacy clues, concrete redaction radii, concrete fuzzing parameters, or side-channel hints;
- connector, pipeline, validator, package, schema, policy, release, or app implementation code;
- public API material, public map material, public tiles, published artifacts, or canonical layer registry entries.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the stale condition explicit: include synthetic retrieval time, observed time, source time, release time, freshness class, or freshness reason as needed by the test.
- Keep the six KFM time concerns distinct where material. Do not collapse observation time, source update time, retrieval time, release time, correction time, and UI request time into one generic timestamp.
- Prefer toy identifiers and toy timestamps that cannot be confused with real source records.
- Pair each input with an expected stale badge, abstention, withdrawn-release notice, conflict notice, or safe fallback output when practical.
- Treat `source available`, `source fresh`, `evidence released`, and `claim safe to answer` as separate checks.
- Do not turn a stale fixture into a source-refresh receipt, release approval, or policy authority.
- Do not use stale data as a fallback for sensitive or exact-location requests. Sensitivity and rights gates still outrank freshness handling.

## Expected stale-source examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Source freshness exceeds configured threshold | `SOURCE_STALE` | UI shows stale badge; consequential claims abstain. |
| Evidence exists but freshness class is unknown | `ABSTAIN` | Missing freshness support blocks confident answer. |
| Layer release is superseded by a newer release | `RELEASE_WITHDRAWN` or superseded state | Surface supersession and point to current release when known. |
| Source retrieval time is fresh but observation time is old | `ANSWER` with caveat or `ABSTAIN` | Depends on claim type; do not collapse retrieval freshness into ecological freshness. |
| Authority source and aggregator source disagree after one goes stale | `CONFLICTED_SUPPORT` / `SOURCE_STALE` | Preserve source roles; do not silently choose the fresher source as truth. |
| Focus Mode asked for a current status using stale evidence | `ABSTAIN` | Cite-or-abstain beats plausible extrapolation. |
| Stale public layer with open correction notice | stale + correction-visible state | Correction state must remain visible at the public surface. |
| Sensitive record is also stale | `DENY` or `RESTRICTED_ACCESS` first | Sensitivity gates still fail closed before freshness display. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, or expected-output names are added.
- Link each fixture to the validator, renderer check, governed-API contract, Focus Mode test, source-refresh check, or documentation example that consumes it.
- Keep concrete operational freshness thresholds in policy or config, not in public fixture prose, unless the value is explicitly synthetic and labeled as such.
- If a fixture needs to demonstrate source-refresh evidence, use a synthetic receipt-shaped example rather than a real receipt.
- If a fixture accidentally includes real source identifiers, real update windows, or real sensitive detail, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Payload inventory: NEEDS VERIFICATION.
- Freshness-policy alignment: NEEDS VERIFICATION against `policy/domains/fauna/`, source descriptors, and any source-refresh runbooks once those are authoritative.
- Tests and validators: NOT RUN.
