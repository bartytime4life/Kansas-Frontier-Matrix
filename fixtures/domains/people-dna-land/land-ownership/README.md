# People/DNA/Land land-ownership fixtures

`fixtures/domains/people-dna-land/land-ownership/`

Status: draft / fixture parent index / land-ownership synthetic examples.

This directory is for small synthetic land-ownership fixtures in the People / Genealogy / DNA / Land domain. Use it for toy cases that exercise land ownership assertions, ownership intervals, deed or title instrument references, assessor/tax context, parcel-version references, legal-description references, chain-of-title reasoning, source-role boundaries, person-to-land joins, decision envelopes, drawer projections, Focus Mode responses, release-readiness checks, correction posture, rollback posture, and expected outputs.

These files are examples only. They are not source records, lifecycle data, real deeds, real title instruments, real assessor records, real tax records, real parcel records, real legal descriptions, real person-to-parcel joins, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, consent records, review approvals, title opinions, release state, public API material, public map material, public tiles, land truth, title truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Land-ownership fixture posture

KFM land ownership is evidence, not title. A land fixture may imitate a deed, title instrument, assessor row, parcel version, legal description, or ownership interval, but it must remain synthetic and cannot certify ownership, marketable title, boundary truth, or legal status.

Two rules are load-bearing for this lane:

- Assessor and tax records are administrative context, not title truth.
- Parcel geometry is not a title boundary.

A positive fixture may show a toy public-safe historical land assertion only when the example is evidence-referenced, source-role-preserved, rights-visible, sensitivity-visible, release-aware, correction-aware, rollback-aware, and synthetic. An invalid or negative fixture should fail closed when evidence, source role, rights, sensitivity, identity resolution, consent, release state, correction posture, or rollback posture is missing or unsafe.

This fixture parent can support future validation and governed-API checks, but examples here do not prove validator implementation, route behavior, policy enforcement, schema enforcement, consent enforcement, EvidenceBundle storage, release integration, UI rendering, title validity, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, title root, legal-opinion root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to People/DNA/Land governance

| Lane or document | Relationship |
|---|---|
| `../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md` | Land ownership model and title/parcel boundary; this fixture lane supplies examples only. |
| `../../../../docs/domains/people-dna-land/sublanes/land.md` | Land sublane doctrine; fixtures do not create a sublane authority root. |
| `../../../../docs/domains/people-dna-land/API_CONTRACTS.md` | Governed surface and finite outcome posture; fixtures do not define API behavior. |
| `../../../../docs/domains/people-dna-land/IDENTITY_MODEL.md` | Identity model and publication constraints; fixtures do not create canonical people or parcel identities. |
| `../genealogy/README.md` | Genealogy fixtures may reference land links, but genealogy does not decide title. |
| `../invalid/README.md` | Whole-domain invalid fixture index; land-link failures may be routed there when broader than this lane. |
| `../golden/README.md` | Stable expected outputs for land-ownership inputs may be paired there. |
| `../../../../contracts/domains/people-dna-land/` | Contract home for domain object meaning; fixtures do not define contracts. |
| `../../../../schemas/contracts/v1/domains/people-dna-land/` | Schema home if present; fixtures do not define schemas. |
| `../../../../policy/domains/people-dna-land/` | Policy home; fixtures do not decide access or release. |
| `../../../../data/registry/sources/people-dna-land/` | Source registry home if present; fixtures do not create source authority. |
| `../../../../data/proofs/people-dna-land/` | Proof home if present; fixtures do not create proof authority. |
| `../../../../release/candidates/people-dna-land/` and `../../../../release/manifests/people-dna-land/` | Release homes if present; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.positive.json`, `*.valid.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy land ownership assertions, ownership intervals, deed instrument refs, title instrument refs, LandInstrument refs, assessor-record refs, tax-record refs, legal-description refs, parcel-version refs, chain-of-title notes, source-role cases, rights cases, sensitivity cases, policy refs, release refs, correction refs, rollback refs, drawer contexts, Focus Mode contexts, or decision-envelope examples;
- toy positive cases for evidence-backed historical ownership intervals, cited instrument chains, source-role-preserved assessor context, parcel-version context, public-safe land-link summaries, correction-visible claim display, and rollback-ready outputs;
- toy negative cases for assessor-as-title misuse, parcel-geometry-as-boundary misuse, unsupported chain-of-title inference, private person-to-parcel exposure, missing evidence, unknown rights, unresolved sensitivity, missing release, missing correction path, or missing rollback target;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real deeds, real title instruments, real assessor records, real tax records, real parcel records, real legal descriptions, real person-to-parcel joins, real land records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, consent records, proof packs, release manifests, implementation code, title opinions, legal advice, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy parcel IDs, toy legal descriptions, toy instrument refs, toy person refs, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy rollback refs, toy hashes, toy timestamps, and toy places.
- Prefer placeholders such as `ToyParcelRef`, `ToyInstrumentRef`, `SyntheticOwnerA`, `SyntheticRecorderRef`, `ToyLegalDescription`, and `SyntheticCountyRef`; do not use real people, real parcels, real coordinates, real instrument numbers, or real title records.
- Make source role explicit: deed/title instrument evidence, assessor/tax administrative context, parcel geometry context, modeled chain-of-title interval, candidate assertion, or synthetic fixture.
- Make the fixture posture explicit: positive, negative, valid, invalid, evidence-backed, evidence-missing, chain-supported, chain-gapped, assessor-context-only, geometry-context-only, title-unsupported, rights-visible, rights-unknown, sensitivity-reviewed, sensitivity-unresolved, release-ready, release-missing, correction-visible, correction-missing, rollback-ready, rollback-missing, or expected output.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-ready, review-required, evidence-resolved, citation-ready, blocked render, correction-required, rollback-required, release-ready, release-readiness failure, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, source role, identity resolution, evidence resolution, citation validation, consent posture where relevant, rights posture, sensitivity posture, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as ownership truth, title truth, boundary truth, legal advice, consent proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Evidence-backed toy historical ownership interval | Validation pass or review-ready | Remains an assertion with cited instrument evidence. |
| Toy deed or title instrument chain with visible gap | Review-ready or `ABSTAIN` for the gap | Chain gaps must be surfaced, not smoothed. |
| Assessor record used as administrative context | Validation pass or review-ready | Assessor context remains administrative and not title truth. |
| Parcel geometry used as spatial context | Validation pass or review-ready | Geometry remains context and not a legal boundary. |
| Assessor row treated as title truth | `DENY` or validation failure | Administrative records cannot certify ownership. |
| Parcel polygon treated as title boundary | `DENY` or validation failure | Geometry cannot become legal boundary truth. |
| Private person-to-parcel join without release and sensitivity review | `DENY` or release-readiness failure | Private land links must fail closed. |
| Missing evidence, rights, sensitivity, correction, or rollback support | `ABSTAIN`, `DENY`, review-required, or release-readiness failure | Governance gaps remain visible. |
| Stable expected output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real person data, land records, parcel records, title records, source exports, precise sensitive geography, or release material, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Land ownership model alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/LAND_OWNERSHIP.md`.
- Land sublane alignment: PARTIALLY VERIFIED against `docs/domains/people-dna-land/sublanes/land.md`.
- Genealogy fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/genealogy/README.md` from recent preceding updates.
- Invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/invalid/README.md` from recent preceding updates.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/golden/README.md` from recent preceding updates.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Parent People/DNA/Land fixture alignment: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, land-ownership checks, chain-of-title checks, source-role checks, identity-resolution checks, consent checks, evidence-bundle checks, citation-validation checks, rights checks, sensitivity checks, person-land-link checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and CI implementation.
- Tests and validators: NOT RUN.
