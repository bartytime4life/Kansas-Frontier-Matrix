# Fauna fixtures

`fixtures/fauna/`

Status: draft / compatibility fixture root / synthetic Fauna examples.

This directory is for small synthetic Fauna fixture examples used by bounded schema checks, semantic-contract reviews, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, source-admission dry-runs, geoprivacy dry-runs, redaction dry-runs, policy dry-runs, correction checks, rollback checks, and documentation examples.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, animal occurrence truth, taxonomic truth, conservation-status truth, habitat truth, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture root posture

Use this lane as a compatibility/staging fixture root for synthetic Fauna examples. Fauna architecture names `fixtures/domains/fauna/` as the doctrinal domain-segment fixture path. This `fixtures/fauna/` README does not create a new domain authority root and should not be treated as overriding Directory Rules or the Fauna lane architecture. If both paths exist, keep this lane bounded as a compatibility or transition surface until an ADR or migration note pins the final fixture path.

Fauna fixtures may demonstrate animal taxonomic identity, conservation-status examples, occurrence evidence, monitoring events, range envelopes, seasonal range examples, public-safe derivatives, geoprivacy transforms, redaction receipts, source-role labels, rights posture, sensitivity posture, review state, release state, correction posture, rollback posture, finite outcomes, and renderer/API behavior. They do not create source authority, evidence closure, policy approval, release approval, public-map authority, tile authority, implementation proof, or published output.

Fauna is a sensitive lane. Exact occurrence or site detail is not public merely because it appears in a fixture. Public examples must be synthetic, generalized, redacted, delayed, aggregated, or otherwise safe for review and documentation. Fail-closed examples should make the blocked condition explicit.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, canonical domain root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to Fauna governance

| Lane or document | Relationship |
|---|---|
| `../../docs/domains/fauna/ARCHITECTURE.md` | Fauna lane doctrine and object-family boundary; this fixture lane supplies examples only. |
| `../../docs/domains/fauna/API_CONTRACTS.md` | Expected governed surface if present; fixtures do not define API behavior. |
| `../../docs/domains/fauna/README.md` | Human-facing Fauna domain landing doc if present. |
| `../../docs/domains/habitat/ARCHITECTURE.md` | Habitat context boundary; Habitat does not own Fauna occurrence truth. |
| `../ecology/README.md` | Cross-domain ecology fixture root; Fauna-specific examples should prefer this lane or the future doctrinal domain fixture path. |
| `../domains/habitat/habitat_fauna_thin_slice/README.md` | Habitat-Fauna proof-support lane if present. |
| `../../contracts/domains/fauna/` | Contract home for Fauna semantic meaning; fixtures do not define contracts. |
| `../../schemas/contracts/v1/domains/fauna/` | Schema home per Directory Rules-style domain segment; fixtures do not define schemas. |
| `../../policy/domains/fauna/` | Policy home; fixtures do not decide access or release. |
| `../../policy/sensitivity/fauna/` | Sensitivity-policy home; fixtures do not decide public exposure. |
| `../../data/registry/sources/fauna/` | Source descriptor home; fixtures do not create source authority. |
| `../../data/proofs/fauna/` | Proof home if present; fixtures do not create proof authority. |
| `../../release/candidates/fauna/` and `../../release/manifests/fauna/` | Release homes if present; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy taxon, taxon-crosswalk, conservation-status, occurrence-evidence, public-occurrence, restricted-occurrence placeholder, range, seasonal-range, migration-route, monitoring-event, mortality, disease, invasive-species, abundance-indicator, richness-indicator, redaction-receipt, geoprivacy-transform, source-role, evidence-ref, policy-ref, release-ref, correction, rollback, drawer, Focus Mode, or decision-envelope examples;
- toy positive cases for public-safe occurrence derivatives, generalized range products, source-role-preserved status assertions, redaction-receipt examples, and bounded public map/render examples;
- toy negative cases for unsupported occurrence claims, missing source role, missing evidence refs, unresolved rights, unresolved sensitivity, exact site exposure, missing release state, missing correction path, or missing rollback target;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real source records, live upstream payloads, real animal occurrence records, exact protected-site geometry, telemetry tracks, nest/den/roost/hibernacula/spawning-site coordinates, raw survey records, raw eDNA records, raw acoustic detections, raw disease/mortality reports, real conservation-status source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the doctrinal domain-segment fixture path `fixtures/domains/fauna/` if and when that lane is present and migration is approved.
- Use toy taxa, toy source refs, toy evidence refs, toy geometries, toy redaction refs, toy receipts, toy timestamps, toy hashes, toy policy refs, toy release refs, and toy reviewer refs.
- Make fixture posture explicit: valid, invalid, negative, expected output, context-only, proof-support, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, rights-visible, rights-missing, sensitivity-reviewed, sensitivity-unresolved, generalized, withheld, denied, review-required, release-ready, release-blocked, correction-visible, rollback-ready, or blocked render.
- Keep source role, evidence state, rights state, sensitivity state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, source-role validity, evidence support, citation safety, sensitivity posture, policy admissibility, release posture, renderer safety, trust-membrane safety, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success as implementation proof, taxonomic truth, occurrence truth, source authority, evidence closure, policy approval, release state, public-map authority, tile authority, or published output.

## Expected fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Toy taxon or taxon-crosswalk example | Validation pass or review-ready | Vendor IDs remain toy refs. |
| Conservation-status assertion with source role | Validation pass, review-ready, or citation-ready | Status must remain source-role typed. |
| Public-safe occurrence derivative | Validation pass, generalized, or release-ready | Exact source occurrence remains outside fixtures. |
| Occurrence evidence lacks citation or source role | `ABSTAIN` or validation failure | Cite-or-abstain remains visible. |
| Protected site detail appears in public output | `DENY`, blocked render, or validation failure | Public-safe derivative required. |
| Range or seasonal-range envelope | Validation pass or review-ready | Range is not exact occurrence truth. |
| Redaction or geoprivacy receipt | Review-ready or expected output | Receipt is synthetic unless produced by governed pipeline. |
| Missing rights, sensitivity, release, correction, or rollback support | `ABSTAIN`, `DENY`, review-required, or release-readiness failure | Governance gaps remain visible. |
| Stable expected output is ready to compare | Future `golden/` or documented expected-output pair | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If a canonical `fixtures/domains/fauna/` lane is created or populated, add a migration note and avoid maintaining two competing authority surfaces.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, protected exact locations, restricted fauna data, actual proof material, or release material, move it out of this root, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this root during this update.
- Exact child-lane inventory under `fixtures/fauna/`: NOT VERIFIED during this update.
- Exact populated precedent for `fixtures/fauna/`: NOT FOUND in repository search during this update.
- Fauna architecture alignment: PARTIALLY VERIFIED against `docs/domains/fauna/ARCHITECTURE.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Ecology fixture alignment: PARTIALLY VERIFIED against `fixtures/ecology/README.md` from the recent preceding update.
- Habitat cross-lane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/ARCHITECTURE.md` from recent preceding updates.
- Consumer alignment: NEEDS VERIFICATION against validators, Fauna fixture checks, taxon checks, occurrence checks, conservation-status checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, geoprivacy checks, redaction checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
