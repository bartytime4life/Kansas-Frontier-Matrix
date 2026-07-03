# Synthetic fixtures

`fixtures/synthetic/`

Status: draft / synthetic fixture parent index / toy examples only.

This directory is the parent lane for small synthetic fixture examples used for documentation, smoke checks, governed API dry-runs, Evidence Drawer examples, Focus Mode examples, source-role examples, correction examples, rollback examples, and expected-output comparisons when a more specific fixture owner has not yet been selected.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Synthetic fixture posture

Synthetic fixtures are toy examples. They should be compact, deterministic, public-safe, and easy to review. They may imitate governed object shapes, runtime envelopes, drawer payloads, Focus Mode contexts, source-role states, evidence references, policy references, correction posture, rollback posture, and expected outputs.

Synthetic does not mean authoritative, released, evidence-backed, policy-approved, or implementation-proven. A synthetic fixture must never become canonical truth, source authority, release state, public-map authority, tile authority, legal authority, emergency authority, or public API authority.

A fixture can describe desired behavior before validators, governed API routes, renderer checks, policy bundles, schema checks, release integration, or CI coverage exist. Fixture success or failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic runtime/checking inputs and documentation examples. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, public API root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, proof stores, source-registry records, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `people-dna-land/` | Synthetic compatibility lane for People / Genealogy / DNA / Land toy examples not yet routed to the domain-owned fixture root. | Synthetic, valid, invalid, positive, negative, expected output, evidence-backed, evidence-missing, identity-resolved, identity-conflicted, consent-valid, consent-missing, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, rollback-visible, or blocked render. |

## Relationship to sibling fixture lanes

| Lane | Relationship |
|---|---|
| `../slim/` | Preferred home for small runtime fixtures when the example is not specifically a synthetic compatibility fixture. |
| `../heavy/` | Heavy runtime stress lane; use only when a synthetic fixture is intentionally stress-sized and storage is approved. |
| `../golden/` | Top-level expected-output lane for stable synthetic outputs. |
| `../invalid/` | Top-level fail-closed lane for broad invalid examples. |
| `../public_safe/` | Parent lane for public-safe documentation/runtime examples. |
| `../release/` | Synthetic release-governance fixture lane. |
| `../domains/` | Preferred root for domain-owned fixtures once the object family and consumer are clear. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Accepted material

This parent lane and its child lanes may contain small synthetic `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples; toy governed-object shapes; toy runtime envelopes; toy drawer payloads; toy Focus Mode contexts; toy source-role states; toy evidence refs; toy policy refs; toy release refs; toy correction refs; toy rollback refs; and paired expected outputs.

## Exclusions

Do not use this lane for real source records, restricted material, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer a domain-specific fixture lane when the object family or policy context has a clear owner.
- Use toy names, toy IDs, toy dates, toy places, toy refs, toy evidence refs, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Make fixture posture explicit: synthetic, valid, invalid, positive, negative, golden, expected output, evidence-backed, evidence-missing, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, correction-missing, rollback-ready, rollback-missing, or blocked render.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, citation-ready, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or deterministic expected output.
- Move stable broad examples into the most specific `fixtures/domains/` lane once the object family and consumer are clear.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as truth, source admission, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or published output.

## Expected synthetic fixture families

| Scenario family | Preferred lane once stable | Expected posture |
|---|---|---|
| People/DNA/Land synthetic compatibility example | `people-dna-land/` or `../domains/people-dna-land/` | Public-safe, fail-closed, or bounded expected output. |
| Synthetic expected output | `../golden/` or domain-specific golden lane | Deterministic expected output, not release. |
| Synthetic fail-closed example | `../invalid/` or domain-specific invalid lane | `ABSTAIN`, `DENY`, validation failure, or review-required. |
| Synthetic runtime smoke example | `../slim/` unless domain-owned | Renderer-safe, drawer-safe, Focus-safe, or bounded output. |
| Synthetic example becomes domain-owned | `../domains/<domain>/` | Preserve ownership, policy, evidence, and sensitivity context. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the exact validator, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- Move stable domain-owned examples into the owning `fixtures/domains/` lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, private material, or restricted material, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Child README inventory: PARTIALLY VERIFIED against populated `people-dna-land/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this synthetic parent during this update.
- Exact child-lane inventory under `fixtures/synthetic/`: PARTIALLY VERIFIED by fetching `people-dna-land/README.md`; no exhaustive tree listing was performed.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Synthetic People/DNA/Land alignment: PARTIALLY VERIFIED against `fixtures/synthetic/people-dna-land/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, governed-API tests, renderer checks, Evidence Drawer tests, Focus Mode tests, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
