# Public-safe settlement fixtures

`fixtures/public_safe/settlement/`

Status: draft / public-safe fixture lane / synthetic settlement examples.

This directory is for small synthetic public-safe settlement fixture examples. Use it for toy settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, map-rendering, drawer, Focus Mode, governed API, source-role, evidence-reference, correction, rollback, and expected-output examples that are safe to show in public documentation or runtime fixture contexts.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, settlement truth, municipal-legal truth, census truth, historic-site truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Fixture lane posture

Use this lane for settlement-side public-safe synthetic examples only. It is a runtime/documentation fixture lane, not a canonical Settlements/Infrastructure domain root. When an example becomes clearly domain-owned, route it to the appropriate `fixtures/domains/settlements-infrastructure/` lane if present or document the needed domain-owned fixture path before adding more payloads here.

The Settlements/Infrastructure file-system plan identifies Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, and ReservationCommunity as settlement-side object families. It also treats infrastructure-side critical asset detail separately and under stricter sensitivity. Public-safe settlement fixtures must preserve that separation: an example about a town, municipal boundary, historic townsite, fort, mission, or reservation community must not leak infrastructure vulnerability, private person-land joins, or restricted source detail.

A fixture may describe intended behavior before the corresponding validator, route, policy bundle, UI surface, release gate, renderer check, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic runtime/checking inputs and public-safe generalized examples. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, public API root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

`fixtures/public_safe/README.md` was not found during this update. Until a parent public-safe fixture README exists, this lane must carry its own boundary statement and must not imply parent-level policy or implementation maturity.

## Relationship to Settlements/Infrastructure governance

| Lane or document | Relationship |
|---|---|
| `../../../docs/domains/settlements-infrastructure/FILE_SYSTEM_PLAN.md` | Settlements/Infrastructure placement and object-family context; this fixture lane supplies examples only. |
| `../../../docs/domains/settlements-infrastructure/MISSING_OR_PLANNED_FILES.md` | Register of planned/expected dossier and cross-root files; fixture paths remain verification-bound. |
| `../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md` | Infrastructure-side object-family dossier; public-safe settlement fixtures must not import infrastructure sensitivity risks. |
| `../../infrastructure-generalized/README.md` | Top-level generalized-infrastructure runtime fixture lane; use that lane for public-safe generalized infrastructure examples. |
| `../../domains/infrastructure-generalized/README.md` | Domain-owned generalized-infrastructure fixture root; infrastructure examples belong there when ownership is clear. |
| `../../hydrology/README.md` | Top-level Hydrology runtime fixture lane; settlement examples may reference water context only as context. |
| `../../invalid/README.md` | Top-level fail-closed fixture lane for broad invalid examples. |
| `../../golden/README.md` | Top-level expected-output fixture lane for stable cross-domain or runtime-wide outputs. |
| `../../../contracts/domains/settlements-infrastructure/` | Contract home if present; fixtures do not define contracts. |
| `../../../schemas/contracts/v1/domains/settlements-infrastructure/` | Schema home if present; fixtures do not define schemas. |
| `../../../policy/domains/settlements-infrastructure/` | Policy home if present; fixtures do not decide policy. |
| `../../../data/registry/sources/settlements-infrastructure/` | Source descriptor home if present; fixtures do not create source authority. |
| `../../../release/manifests/settlements-infrastructure/` | Release home if present; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy public-safe settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, map-rendering, layer, drawer, Focus Mode, governed API, source-role, evidence-ref, citation-ref, correction, rollback, or expected-output examples;
- public-safe generalized geometries and toy attributes for renderer smoke tests, map UI checks, and documentation examples;
- examples that show settlement-side context without claiming municipal legal authority, census authority, historic-site truth, land ownership, infrastructure status, emergency status, or release state;
- paired expected outputs in `../../golden/` or a future domain-specific golden lane when behavior becomes stable.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real municipal/legal records; real census data extracts; real historic-site records; real tribal/community records; real exact sensitive geometry; private person-land joins; ownership/title data; critical infrastructure detail; emergency alerts; lifecycle data; SourceDescriptors; actual EvidenceBundles; actual RunReceipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, generalized, and public-safe.
- Use toy IDs, toy refs, toy dates, toy places, toy geometries, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy reviewer refs, and toy hashes.
- Prefer generalized, coarse, aggregated, or toy geometry; never include sensitive exact geometry.
- Make fixture posture explicit: public-safe, generalized, valid, invalid, negative, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, release-blocked, correction-visible, rollback-visible, or blocked render.
- Keep source role, evidence support, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as settlement truth, municipal-legal truth, census truth, historic-site truth, source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected public-safe settlement fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Toy settlement point or polygon | Public-safe or renderer-safe | Generalized geometry only. |
| Toy municipality example | Validation pass or review-ready | Not legal authority. |
| Toy CensusPlace example | Validation pass or review-ready | Not census authority. |
| Toy townsite or ghost-town example | Public-safe or citation-ready | Historical uncertainty remains visible. |
| Toy fort, mission, or reservation-community example | Review-ready or public-safe | Cultural sensitivity and source role must remain explicit. |
| Settlement drawer or Focus Mode context | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` as governed | Generated text remains interpretive and evidence-bound. |
| Missing evidence, rights, sensitivity, release, correction, or rollback support | `ABSTAIN`, `DENY`, validation failure, or review-required | Cite-or-abstain and deny-by-default remain visible. |
| Stable expected output | `../../golden/` or future domain golden lane | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when parent public-safe fixture documentation, child lanes, payload files, validators, tests, helper scripts, renderer checks, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the renderer check, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, sensitivity check, or documentation example that consumes it.
- Move stable domain-owned examples into an owning `fixtures/domains/settlements-infrastructure/` lane once that lane is verified or created through a governed directory decision.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this lane index together.
- Keep payloads small enough for normal code review unless an explicit large-corpus storage decision exists.
- If a fixture accidentally includes real settlement records, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, private joins, restricted cultural/community detail, infrastructure-sensitive detail, or emergency-authority content, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent `fixtures/public_safe/README.md`: NOT FOUND during this update.
- Fixture payload inventory: no payload files verified under this public-safe settlement lane during this update.
- Exact child-lane inventory under `fixtures/public_safe/settlement/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Settlements/Infrastructure file-system alignment: PARTIALLY VERIFIED against `docs/domains/settlements-infrastructure/FILE_SYSTEM_PLAN.md`.
- Settlements/Infrastructure backlog alignment: PARTIALLY VERIFIED against `docs/domains/settlements-infrastructure/MISSING_OR_PLANNED_FILES.md`.
- Infrastructure sensitivity boundary alignment: PARTIALLY VERIFIED against `docs/domains/settlements-infrastructure/sublanes/infrastructure.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, settlement checks, public-safe fixture checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, evidence-resolver checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
