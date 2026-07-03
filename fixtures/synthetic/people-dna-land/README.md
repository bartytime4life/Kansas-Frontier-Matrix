# Synthetic People/DNA/Land fixtures

`fixtures/synthetic/people-dna-land/`

Status: draft / synthetic compatibility fixture lane / People-DNA-Land examples.

This directory is a synthetic-only staging lane for small People / Genealogy / DNA / Land fixture examples that are not yet routed to the domain-owned fixture root. Use it for toy examples that exercise bounded genealogy, identity, consent, source-role, evidence, citation, rights, sensitivity, land-context, drawer, Focus Mode, release-readiness, correction, rollback, and expected-output behavior.

These files are examples only. They are not real personal records, genetic records, land-title records, source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, AI authority, or published artifacts.

## Synthetic lane posture

Use this lane only for toy, public-safe, synthetic examples. It may stage broad examples while fixture ownership is still being sorted, but it must not become a parallel authority root beside `fixtures/domains/people-dna-land/`.

The domain-owned People/DNA/Land fixture root is `fixtures/domains/people-dna-land/`. Stable examples should move there once the object family and consumer are clear. That root already carries lanes for genealogy, land ownership, valid examples, invalid examples, and golden expected outputs.

People/DNA/Land remains deny-first even for synthetic examples. Fixtures must not normalize public exposure of living-person outputs, genetic inference, private person-land linkage, title opinions, or unreviewed generated claims. Positive examples must stay public-safe and evidence-referenced. Invalid examples must make the blocked condition explicit and fail closed.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, legal-opinion root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

`fixtures/synthetic/README.md` is currently only a greenfield stub. Until that parent index is expanded, this lane must carry its own boundary statement and must not imply parent-level synthetic fixture maturity.

## Relationship to People/DNA/Land fixture governance

| Lane or document | Relationship |
|---|---|
| `../../domains/people-dna-land/README.md` | Preferred domain-owned People/DNA/Land fixture root. |
| `../../domains/people-dna-land/genealogy/` | Preferred fixture family for synthetic genealogy examples. |
| `../../domains/people-dna-land/land-ownership/` | Preferred lane for land-context and evidence-not-title examples. |
| `../../domains/people-dna-land/valid/` | Preferred broad positive-path People/DNA/Land staging lane. |
| `../../domains/people-dna-land/invalid/` | Preferred broad fail-closed People/DNA/Land staging lane. |
| `../../domains/people-dna-land/golden/` | Preferred expected-output lane for stable synthetic People/DNA/Land inputs. |
| `../README.md` | Synthetic fixture parent; currently only a greenfield stub. |
| `../../README.md` | Root fixture rules and runtime boundary. |
| `../../golden/README.md` | Top-level expected-output lane for cross-domain or runtime-wide outputs. |
| `../../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy historical relationship, identity, consent-state, citation, rights, sensitivity, land-context, drawer, Focus Mode, decision-envelope, correction, rollback, or expected-output examples;
- toy land-context examples that preserve the distinction between evidence, administrative context, mapped context, and title truth;
- positive-path, fail-closed, and expected-output examples that remain synthetic, deterministic, public-safe, and reviewable;
- paired expected outputs in `../../domains/people-dna-land/golden/` or `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real personal, genetic, genealogy, consent, land-title, parcel, source-export, proof, release, or lifecycle material. Do not use it for legal opinions, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy names, toy IDs, toy dates, toy places, toy relationship refs, toy land refs, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy rollback refs, toy hashes, and toy timestamps.
- Prefer generic placeholders such as `PersonA`, `PersonB`, `SyntheticFamily1`, `ToyPlaceRef`, `ToyParcelRef`, `ToyInstrumentRef`, and `SyntheticOwnerA`.
- Make fixture posture explicit: synthetic, valid, invalid, positive, negative, golden, expected output, evidence-backed, evidence-missing, identity-resolved, identity-conflicted, consent-valid, consent-missing, source-role-preserved, source-role-conflicted, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, correction-missing, rollback-ready, rollback-missing, or blocked render.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, citation-ready, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or deterministic expected output.
- Move stable broad examples into the most specific `fixtures/domains/people-dna-land/` family lane once the object family and consumer are clear.
- Keep schema validity, semantic validity, identity resolution, evidence resolution, citation validation, consent posture, rights posture, sensitivity posture, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as identity truth, relationship truth, genetic truth, ownership truth, title truth, boundary truth, legal advice, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected synthetic fixture families

| Scenario family | Preferred lane once stable | Expected posture |
|---|---|---|
| Toy historical relationship assertion | `../../domains/people-dna-land/genealogy/positive/` | Validation pass, review-ready, or bounded `ANSWER`. |
| Missing-evidence genealogy assertion | `../../domains/people-dna-land/genealogy/negative/` | `ABSTAIN`, validation failure, or review-required. |
| Toy public-safe ancestor summary | `../../domains/people-dna-land/genealogy/positive/` | `ANSWER` or review-ready with evidence refs. |
| Toy land ownership interval | `../../domains/people-dna-land/land-ownership/` | Validation pass or review-ready. |
| Administrative land context preserved as context | `../../domains/people-dna-land/land-ownership/` | Validation pass or review-ready. |
| Land context treated as title truth | `../../domains/people-dna-land/invalid/` | `DENY`, validation failure, or blocked render. |
| Private person-land linkage attempt | `../../domains/people-dna-land/invalid/` | `DENY` or review-required. |
| Stable expected output | `../../domains/people-dna-land/golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when `fixtures/synthetic/README.md` is expanded, when payload files are added, or when stable examples move to the domain-owned fixture root.
- Link each stable fixture to the exact validator, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, domain-owned README, and this compatibility lane together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real personal, genetic, land-title, source, proof, consent, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent synthetic README: PARTIALLY VERIFIED as a greenfield stub at `fixtures/synthetic/README.md`.
- Fixture payload inventory: no payload files verified under this synthetic People/DNA/Land lane during this update.
- Exact child-lane inventory under `fixtures/synthetic/people-dna-land/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Domain People/DNA/Land fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/README.md`.
- Domain valid lane alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/valid/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, People/DNA/Land governed-API tests, genealogy checks, land-ownership checks, identity-resolution checks, consent checks, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
