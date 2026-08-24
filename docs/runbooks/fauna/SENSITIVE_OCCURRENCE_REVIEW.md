<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/sensitive-occurrence-review
title: Fauna — Sensitive Occurrence Review Runbook
type: runbook; review-procedure; domain-lane; sensitive-domain; non-authoritative
version: v0.1
prior_version: inventory-generated proposed scaffold
status: draft; repository-grounded; fixture-first; manual-review-handoff; live-policy-and-public-release-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: >-
  Accountable Fauna, taxonomy, source, rights, sensitivity/geoprivacy,
  evidence, policy, review, release, correction, rollback, public-surface,
  and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS
  routing does not create those authorities.
created: 2026-08-24
updated: 2026-08-24
policy_label: restricted-review; fauna; sensitive-occurrence; geoprivacy; fail-closed; no-live-source; no-release-authority; no-publication-authority
current_path: docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md
owning_root: docs/
responsibility: >-
  Document the bounded, fail-closed review procedure for a Fauna occurrence
  candidate whose location, taxon/site context, source terms, steward control,
  or re-identification risk may require withholding or restricted handling,
  while preventing documentation, fixture validation, or a review handoff from
  becoming source admission, policy approval, geoprivacy authority, release,
  deployment, promotion, or publication.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path completion of an existing tracked scaffold; no sibling authority created
path_posture: PLACE
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a
  target_prior_blob: 7ba828b1b70327b08f10e844109b3dbf48c65622
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  occurrence_evidence_contract_blob: f38ae38055d03149471a97b63d38a7b8f7cfbd35
  occurrence_public_contract_blob: d0c1481160b4979445a916915ff96d04d48f7033
  occurrence_restricted_contract_blob: 47f2623c61afde5f198b9b226ffbdd2ef5e3d38e
  occurrence_validator_readme_blob: 6e15662b1256ab0cf6e8ae4e63cdaa593c32246d
  fauna_sensitivity_doc_blob: 58c557cda55362345ac3869502910bc301ef5b8c
  sensitivity_policy_readme_blob: aac9f7b6316b89238d209c7ef4045fbf4df15ea9
  rare_species_policy_stub_blob: a7269d357bb7570fc3680c299486e5d62cb33a68
  redaction_receipt_contract_blob: 94e6efa36b508ca7cfd1fa9bf728b91200cf02c9
  publication_gate_runbook_blob: 3a65acdf9d399c7fac0271657a9ce706350f555c
  no_network_runbook_blob: 4a8772dd1356521b11d4a568ae127acde2b2cc5e
drive_lineage:
  file: KFM_Fauna_Architecture_PDF_Only_Report.pdf
  drive_id: 1mWhhtubyaAtNuWJ3vY7nuDLx50Wig7Bj
  date: 2026-04-21
inspection_boundary: >-
  Current-session GitHub reads of this scaffold, accepted Directory Rules,
  Fauna occurrence contracts, the executable fixture-first OccurrenceEvidence
  validator lane, Fauna sensitivity documentation, policy scaffolds, redaction
  receipt semantics, and current promotion/publication runbooks; plus the
  connected Drive Fauna architecture report as proposal lineage. No live
  wildlife source, protected payload, exact or reconstructable location,
  credential, production policy evaluator, reviewer identity, release service,
  deployed public surface, or lifecycle object was exercised or changed.
related:
  - ../README.md
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./PUBLICATION_GATE_DRY_RUN.md
  - ./EBD_DERIVATIVE_RELEASE.md
  - ./ROLLBACK_RUNBOOK.md
  - ./ROLLBACK_DRILL.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/POLICY.md
  - ../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../contracts/domains/fauna/occurrence_public.md
  - ../../../contracts/domains/fauna/occurrence_restricted.md
  - ../../../contracts/domains/fauna/sensitive_site.md
  - ../../../contracts/domains/fauna/redaction_receipt.md
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_public.schema.json
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_restricted.schema.json
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../policy/domains/fauna/rare_species_redaction.rego
  - ../../../fixtures/domains/fauna/occurrence_evidence/
  - ../../../tests/domains/fauna/test_occurrence_evidence.py
  - ../../../tools/validators/domains/fauna/occurrence/README.md
  - ../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
  - ../../../release/candidates/fauna/README.md
notes:
  - "The prior file was an inventory-generated scaffold. This revision fills the same path and creates no new authority surface."
  - "The current repository can deterministically validate draft OccurrenceEvidence shape, identity, role anti-collapse, rights/sensitivity consistency, and fixture polarity. It cannot currently prove production sensitivity policy, geoprivacy transformation, accountable review, or public release."
  - "OccurrencePublic and OccurrenceRestricted have substantive semantic contracts but their paired machine schemas remain permissive scaffolds at this snapshot."
  - "The Fauna sensitivity policy README remains a scaffold and rare_species_redaction.rego remains a no-op greenfield stub; no sensitive occurrence may be treated as production-policy-cleared from those files."
  - "The Fauna RedactionReceipt semantic contract is placement-CONFLICTED and its paired schema is not a closed production authority. This runbook never exposes transform parameters or relies on that conflict as permission."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — Sensitive Occurrence Review Runbook

> **Review a potentially sensitive Fauna occurrence without exposing protected location detail, inventing a safe transform, or converting a fixture pass into policy or release authority.** The maximum result of this procedure is a bounded, public-safe review handoff.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![OccurrenceEvidence validator: executable](https://img.shields.io/badge/OccurrenceEvidence%20validator-executable-1f883d?style=flat-square)](#current-repository-posture)
[![Production sensitivity policy: HOLD](https://img.shields.io/badge/production%20sensitivity%20policy-HOLD-d4a72c?style=flat-square)](#current-repository-posture)
[![Exact locations: do not expose](https://img.shields.io/badge/exact%20locations-do%20not%20expose-b42318?style=flat-square)](#safety-and-information-minimization)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **A sensitive-occurrence review is not a publication decision.** A schema-valid record, CLI `PASS`, green workflow, public-safe-looking geometry, human-readable conclusion, or merged pull request cannot admit a source, choose a geoprivacy transform, resolve rights, approve a reviewer, release a derivative, or authorize public display.

> [!WARNING]
> **Do not copy exact or reverse-engineerable wildlife locations into this runbook or its handoff artifacts.** Keep exact coordinates, nest/den/roost/hibernacula/breeding/spawning locations, telemetry tracks, private-land clues, observer-linked details, steward-controlled identifiers, restricted source payloads, and geoprivacy parameters out of public issues, pull requests, logs, screenshots, workflow summaries, generated text, and review notes.

> [!CAUTION]
> **Current production sensitivity policy is not established by the inspected files.** `policy/sensitivity/fauna/README.md` is a proposed scaffold, and `policy/domains/fauna/rare_species_redaction.rego` is a greenfield stub with no real rules. This procedure therefore fails closed and stops before public release whenever a material sensitivity decision is required.

**Quick navigation:** [Purpose](#purpose-and-terminal-boundary) · [Authority](#authority-and-negative-authority) · [Posture](#current-repository-posture) · [Inputs](#allowed-inputs-and-prohibited-content) · [Safety](#safety-and-information-minimization) · [Preflight](#preflight-and-stop-conditions) · [Procedure](#review-procedure) · [State separation](#state-separation-and-finite-results) · [Handoff](#public-safe-review-handoff) · [Validation](#validation-evidence-and-limitations) · [Maintenance](#maintenance-and-correction-triggers) · [Open work](#open-verification-backlog) · [Related](#related-surfaces) · [Rollback](#document-change-rollback)

---

## Purpose and terminal boundary

Use this runbook when a Fauna occurrence candidate may be sensitive because of location precision, taxon/site context, source terms, steward control, private-land or observer linkage, embargo, or a combination of otherwise public attributes that could reconstruct protected detail.

The procedure is intentionally narrower than a release workflow. It may:

1. freeze a repository revision and candidate identity;
2. verify that the candidate is represented by the current draft `OccurrenceEvidence` profile when that profile applies;
3. run or cite the bounded no-network validator and exact fixture evidence;
4. classify unresolved rights, sensitivity, evidence, taxonomy, source-role, and review dependencies;
5. determine whether the candidate must remain held/restricted, must be denied, or has enough non-sensitive metadata for accountable review; and
6. emit a public-safe handoff containing references, digests, state labels, reason codes, and unresolved items only.

It may **not**:

- retrieve a live occurrence or protected source payload;
- admit or activate a source;
- choose, parameterize, or execute a production geoprivacy transform;
- infer a taxon's sensitivity status from prose, a name match, or model output;
- expose restricted geometry or values to prove that they were withheld;
- convert `OccurrenceEvidence` directly into an authoritative `OccurrencePublic` record;
- authenticate a rights holder, steward, reviewer, or release authority;
- create an EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, PromotionDecision, correction, withdrawal, or rollback record by documentation alone; or
- release, deploy, promote, publish, or update a public map/API/search/AI surface.

The maximum result is **review handoff**. Public state remains outside this document.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [`Directory Rules`](../../doctrine/directory-rules.md) place human operational procedures under `docs/runbooks/`. This same-path update therefore belongs here. It does not change semantic, policy, evidence, review, release, or data authority.

| Concern | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Occurrence meaning | `contracts/domains/fauna/occurrence_evidence.md`, public/restricted sibling contracts | cite the current meaning and boundary | redefine the occurrence object family |
| Machine shape | `schemas/contracts/v1/domains/fauna/` | identify which shapes are closed versus scaffolded | treat a permissive scaffold as production enforcement |
| Source identity and rights | admitted source records and source-governance authorities | require a resolvable source/rights posture | admit a source or infer rights from public availability |
| Taxonomic authority | admitted/version-pinned taxonomy authority plus accountable review | require resolved identity where consequential | turn string matching into taxonomic authority |
| Sensitivity/geoprivacy | `policy/sensitivity/fauna/`, `policy/domains/fauna/`, accountable sensitivity review | preserve fail-closed posture and stop conditions | invent policy or transform parameters |
| Evidence | `EvidenceRef`, `EvidenceBundle`, receipts, proofs | require support and cite references | manufacture evidence or treat occurrence fields as citations |
| Review | accountable human/institutional review records | prepare a bounded review packet | self-approve or infer reviewer authority from CODEOWNERS |
| Release/correction/rollback | `release/` and linked accountability objects | identify required downstream closure | release, publish, invalidate, or roll back public state |
| This Markdown file | `docs/runbooks/fauna/` | explain the safe procedure | become a policy, registry, schema, source, proof, or publisher |

The draft [`ADR-0010`](../../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) is relevant design lineage but remains `draft` at the inspected revision. Do not cite it as an accepted decision. The operational hold here follows from current missing policy/review closure and the explicit public-safety boundaries of the implemented draft occurrence profile, not from pretending that draft ADR acceptance has occurred.

[Back to top](#top)

---

## Current repository posture

The following observations are pinned to `main@df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a`.

| Surface | CONFIRMED current evidence | Safe conclusion |
|---|---|---|
| `OccurrenceEvidence` semantic contract | Draft v0.3; source-bound pre-sensitivity-split object | Suitable for bounded candidate representation, not public authority |
| `OccurrenceEvidence` machine schema and validator | Closed Draft 2020-12 draft schema; deterministic local validator; no-network fixtures and focused tests | Can prove internal draft-profile consistency and exact fixture polarity |
| Candidate finite state | `pass`, `quarantine`, `deny`, `error` are represented inside the draft occurrence profile | A schema-valid `quarantine` may still produce CLI `PASS`; that is correct and remains held |
| `OccurrencePublic` contract | Substantive semantic contract | Paired schema is still empty/permissive; public conversion is not machine-proved |
| `OccurrenceRestricted` contract | Substantive semantic contract | Paired schema is still empty/permissive; restricted-access behavior is not machine-proved |
| Fauna sensitivity documentation | Substantive explanatory draft; explicitly avoids publishing transform parameters | Useful safety orientation; policy still owns decisions |
| `policy/sensitivity/fauna/README.md` | Proposed scaffold | No production sensitivity policy is established here |
| `rare_species_redaction.rego` | Greenfield stub; no real rules | Must not be used as public-release clearance |
| Fauna `RedactionReceipt` contract | Substantive domain semantics | Placement is `CONFLICTED`; paired schema remains a scaffold; not final receipt authority |
| Fauna publication gate runbook | Shared synthetic denial rehearsal exists; Fauna candidate-specific release remains `HOLD` | This review cannot skip candidate/evidence/policy/review/release closure |
| Live source, reviewer, release, deployed public behavior | Not established by the inspected files | `UNKNOWN` / `HOLD` unless proven by owning surfaces |

This is a useful but deliberately incomplete boundary: the repository can prove that a held sensitive occurrence is represented consistently without proving that the occurrence is safe to publish.

[Back to top](#top)

---

## Allowed inputs and prohibited content

### Allowed inputs

Use only the minimum information needed to classify the review state:

- exact repository revision;
- candidate path or opaque candidate ID when repository-local and approved for the review context;
- content/spec digest;
- source descriptor reference and source-role value, when already present;
- `EvidenceRef` identifiers, never evidence payload excerpts unless separately authorized;
- rights/sensitivity/review state labels and reason codes;
- public-safe geometry **only if it is already an approved public-safe representation** from the owning process;
- validator profile/version and exact result;
- correction/supersession references and rollback target identifiers when they already exist; and
- unresolved dependencies and accountable-review route.

### Prohibited content in public review artifacts

Do not include:

- raw latitude/longitude or precise geometry for a sensitive occurrence;
- raw `OccurrenceRestricted` payload values;
- sensitive-site identifiers or combinations of place/time/taxon clues that make a location reconstructable;
- telemetry paths, trap/station coordinates, private parcel joins, observer identity, access codes, credentials, or source tokens;
- hidden geoprivacy seeds, radii, jitter rules, suppression thresholds, or other transform parameters;
- screenshots of restricted maps or tables;
- source excerpts whose license or steward terms do not permit redistribution; or
- AI-generated guesses about what a hidden value probably contains.

When a reviewer must inspect restricted material, that inspection belongs in an approved restricted system and must be represented here only by an opaque review reference and public-safe result.

[Back to top](#top)

---

## Safety and information minimization

A sensitive occurrence is a compositional-risk problem as well as a single-field problem. A public-safe point can become unsafe when combined with time, taxon, parcel, habitat, trail, imagery, observer, or infrastructure detail.

Apply these rules throughout the procedure:

1. **Preserve source role.** An aggregate, model, regulatory record, administrative record, candidate, or synthetic record never becomes a direct observation because it is spatially precise.
2. **Separate evidence from exposure.** Strong evidence can support a claim and still be unsafe to expose publicly.
3. **Separate existence from location.** A review may allow a statement that evidence exists while continuing to withhold location detail.
4. **Treat re-identifying joins as sensitive.** Do not approve a candidate because each field is individually public-safe when their combination reconstructs restricted information.
5. **Do not improvise transforms.** Generalization, aggregation, withholding, delay, masking, or other geoprivacy action requires the owning policy/review path. This runbook intentionally contains no transform parameters.
6. **Preserve correction lineage.** A corrected, superseded, withdrawn, or stale record must not silently return to public eligibility because its geometry looks generalized.
7. **Prefer the least revealing review artifact.** Use identifiers, hashes, reason codes, and opaque review references instead of sensitive values.

[Back to top](#top)

---

## Preflight and stop conditions

Before review begins, freeze:

- current repository SHA;
- candidate identity and digest;
- exact validator/profile version if validation is in scope;
- source descriptor and source-role reference;
- evidence references;
- rights and sensitivity posture;
- review requirement and expected accountable reviewer class; and
- downstream public/restricted representation being proposed, if any.

Stop immediately with `HOLD`, `DENY`, `ABSTAIN`, or `ERROR` as appropriate when any of these applies:

| Condition | Required posture |
|---|---|
| Candidate or source identity cannot be pinned | `HOLD` |
| Input contains sensitive values in an inappropriate/public review surface | `DENY` and contain the exposure; do not copy the value into the finding |
| JSON/schema/identity validation is malformed or inconsistent | `ERROR` |
| Source role or basis-of-record is being substituted to make evidence look stronger | `DENY` or `HOLD` |
| Rights or redistribution posture is unresolved for the proposed exposure | `HOLD` / `ABSTAIN` |
| Sensitivity is unresolved and public exposure is proposed | `HOLD` / `ABSTAIN` |
| Required steward/sensitivity review is absent | `HOLD` |
| A join or contextual combination can reconstruct restricted location detail | `DENY` for that public representation |
| Public/restricted conversion depends on the current permissive sibling schemas as if they were closed production gates | `HOLD` |
| Proposed release depends on the current Fauna sensitivity-policy scaffold or no-op Rego stub as clearance | `DENY` / `HOLD` |
| Redaction/receipt placement conflict is material to the proposed release and unresolved | `HOLD` |
| Evidence-dependent public claim lacks resolvable governed support | `ABSTAIN` |

A held candidate is not a failed review. `HOLD` is the correct fail-closed result when required authority or evidence is incomplete.

[Back to top](#top)

---

## Review procedure

### Step 1 — Freeze the review subject

Record the exact revision, opaque candidate identity, content/spec digest, source role, schema/profile version, and review purpose. Do not begin from a screenshot, map click, filename, common name, or copied coordinate alone.

### Step 2 — Run the bounded occurrence conformance check when applicable

Use the repository's current `OccurrenceEvidence` validator lane and its documented no-network entry points. The validator checks draft schema closure, deterministic identity, source-role/basis consistency, provenance, rights/sensitivity consistency, and declared finite state.

Interpret results narrowly:

- CLI `PASS` means no inconsistency was found by that bounded validator.
- A candidate may legitimately declare `quarantine` and still yield CLI `PASS`.
- CLI `PASS` does **not** mean source admitted, EvidenceBundle resolved, policy allowed, reviewer approved, geoprivacy transformed, release ready, or public safe.
- CLI `ERROR` or findings stop the candidate until corrected or explicitly dispositioned.

Do not reroute around a failing check by copying fields into a new permissive object.

### Step 3 — Preserve source, taxonomy, rights, and evidence boundaries

Confirm that the candidate does not borrow authority from an aggregator, map layer, model, administrative record, or generated summary. Taxonomy, source role, rights, and evidence closure are independent review dimensions.

If any consequential identity or support question is unresolved, retain the candidate as held and route it to the appropriate owner. Do not use model language to settle the gap.

### Step 4 — Classify sensitivity without exposing the protected value

Use only approved sensitivity labels, policy references, and reviewer results. Do not inspect or reproduce exact location detail in a public handoff to prove that it exists.

If a candidate is already classified as sensitive, restricted, generalized, withheld, embargoed, or review-required, preserve that state. A new public representation requires a separate approved policy/review/transform path.

### Step 5 — Check compositional and re-identification risk

Review the proposed public representation as a combination of fields and context. Consider whether taxon, date/time, place label, parcel, habitat, access route, imagery, observer information, or cross-domain joins make a protected location inferable.

If yes, deny that representation or hold it for a stronger upstream transform/review. Do not publish a near-exact workaround.

### Step 6 — Separate restricted retention from public eligibility

A restricted or quarantined occurrence can be legitimate KFM evidence while remaining ineligible for normal public clients. Preserve the restricted state and evidence lineage instead of forcing a public derivative to exist.

`OccurrencePublic` and `OccurrenceRestricted` currently provide semantic guidance, but their machine schemas remain permissive scaffolds. Do not claim machine-enforced conversion or restricted-access behavior until those surfaces are closed and tested.

### Step 7 — Prepare the review handoff

Emit only a public-safe handoff containing:

- repository SHA;
- candidate opaque ID and digest;
- source descriptor/reference and canonical source role;
- validator profile and bounded result;
- evidence reference IDs and evidence-closure state;
- rights, sensitivity, and review state labels;
- proposed disposition (`HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or ready for accountable review);
- exact reason codes or unresolved items;
- correction/supersession references where present; and
- downstream action owner/class required next.

Do not include the protected values that motivated the review.

### Step 8 — Stop before release

A successful handoff does not create a public occurrence, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, public layer, API payload, map feature, export, Focus Mode answer, or AI permission. Continue only through the owning downstream process after its prerequisites independently close.

[Back to top](#top)

---

## State separation and finite results

Three distinct state layers are visible in the current repository and must not be collapsed.

| Layer | Values | Meaning |
|---|---|---|
| Occurrence validator wrapper | `PASS`, `ERROR` | Whether the supplied draft record or fixture manifest is internally consistent with the validator profile |
| Draft `OccurrenceEvidence.validation.validator_result` | `pass`, `quarantine`, `deny`, `error` | Candidate's internal draft validation state; a consistent `quarantine` is still held |
| This human procedure | `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or review handoff | Operational documentation disposition only; never publication authority |

Use the terms as follows:

- **`HOLD`** — authority, rights, sensitivity, policy, review, schema closure, or downstream release support is incomplete.
- **`ABSTAIN`** — a requested claim or public conclusion outruns the available evidence or safe public support.
- **`DENY`** — the proposed public representation or handling path is incompatible with an applicable safety/rights boundary or would expose protected detail.
- **`ERROR`** — machine shape, identity, parser, validator, or review-packet consistency failed.
- **review handoff** — bounded checks are complete enough for the accountable reviewer to consider the candidate; it is not approval.

Do not introduce a new machine enum from these prose labels. The owning contracts and policy vocabularies remain authoritative for their own result shapes.

[Back to top](#top)

---

## Public-safe review handoff

A compact handoff should answer these questions without leaking the occurrence:

| Question | Required evidence |
|---|---|
| What exact repository state was reviewed? | commit SHA |
| What candidate was reviewed? | opaque ID + digest, not protected value |
| What kind of source support is it? | SourceDescriptor/reference + canonical `source_role` |
| Did the bounded occurrence validator pass? | profile/version + exact wrapper outcome and finding codes |
| What is the candidate's internal state? | `pass` / `quarantine` / `deny` / `error` as declared and validated |
| Are rights resolved for the proposed use? | state/reference only |
| Is sensitivity resolved? | state/reference only; no hidden value or transform parameter |
| Is accountable review complete? | review reference/state, not inferred from a GitHub username alone |
| Is evidence closure adequate for the requested claim? | EvidenceRef/EvidenceBundle state |
| Is a public representation actually authorized? | owning policy/review/release references; otherwise `HOLD` |
| What changes next? | named responsibility class and unresolved items |
| How would a later public state be corrected? | correction/supersession/rollback references if they already exist |

If a handoff cannot answer those questions without disclosing protected detail, redesign the handoff rather than weakening the safety boundary.

[Back to top](#top)

---

## Validation evidence and limitations

### What is executable now

The repository contains a deterministic, no-network, fixture-first `OccurrenceEvidence` validation lane. Its current documentation records:

- a closed Draft 2020-12 draft schema;
- deterministic JCS + SHA-256 identity checking;
- source-role/basis anti-collapse;
- rights and sensitivity consistency checks;
- public-safe versus internal geometry separation;
- three valid and five exact-negative synthetic cases;
- eight focused no-network tests; and
- a dedicated workflow.

That evidence is useful for this review procedure because it can prove that **held sensitive state is represented consistently**.

### What remains unproved

The inspected repository does not establish, through this lane:

- production source admission or live occurrence retrieval;
- authoritative sensitivity classification for a real record;
- production geoprivacy transformation;
- a closed machine `OccurrencePublic` or `OccurrenceRestricted` conversion profile;
- binding Fauna sensitivity policy execution;
- accountable reviewer identity or separation of duties;
- final RedactionReceipt schema/home;
- proof-pack or candidate-specific release closure;
- operational restricted-access enforcement;
- deployment or public invalidation behavior; or
- publication authority.

Therefore a review result cannot be promoted beyond its bounded evidence.

[Back to top](#top)

---

## Maintenance and correction triggers

Re-review this runbook when any of the following changes:

- `OccurrenceEvidence`, `OccurrencePublic`, `OccurrenceRestricted`, or `SensitiveSite` contract/schema status;
- source-role vocabulary or source-admission rules;
- Fauna sensitivity/geoprivacy policy or its executable implementation;
- taxonomy-resolution authority or review requirements;
- RedactionReceipt placement/schema decision;
- rights/redistribution policy;
- occurrence validator result grammar or fixture inventory;
- review/separation-of-duty controls;
- public API, map, export, search, or Focus Mode exposure path;
- release/correction/withdrawal/rollback requirements; or
- a newly discovered re-identification path.

Corrections must preserve historical evidence and prior review results. Do not rewrite a prior decision or fixture result to look as though the newer policy existed at the earlier time.

[Back to top](#top)

---

## Open verification backlog

The strongest remaining dependency-closed work is outside this documentation file:

1. **Sensitivity policy:** replace the Fauna sensitivity-policy scaffold and no-op rare-species Rego stub only through an explicitly reviewed policy implementation slice with safe synthetic fixtures and negative tests.
2. **Public/restricted machine shapes:** close and test the `OccurrencePublic` and `OccurrenceRestricted` schemas before claiming enforced conversion behavior.
3. **Redaction receipt authority:** resolve the current domain-versus-cross-domain placement conflict before relying on a Fauna-specific receipt schema for release closure.
4. **Accountable review:** identify the Fauna/sensitivity/rights reviewer route and required separation of duties.
5. **Restricted access:** prove that restricted occurrences cannot leak through map, API, search, graph, export, logs, or AI composition.
6. **Candidate-specific release proof:** keep Fauna publication on `HOLD` until a real candidate has source, evidence, rights, sensitivity, policy, review, correction, rollback, and public-carrier closure.
7. **Runbook navigation:** populate `docs/runbooks/fauna/README.md` so this procedure and the now-substantive neighboring runbooks have one local boundary and routing index.

No item above should be inferred complete from this documentation update.

[Back to top](#top)

---

## Related surfaces

| Need | Surface |
|---|---|
| Run the current synthetic Fauna safety checks | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) |
| Prepare an admitted-source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) |
| Resolve taxonomy ambiguity | [`TAXONOMY_RESOLUTION_RUNBOOK.md`](./TAXONOMY_RESOLUTION_RUNBOOK.md) |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) |
| Rehearse publication denial | [`PUBLICATION_GATE_DRY_RUN.md`](./PUBLICATION_GATE_DRY_RUN.md) |
| Handle EBD derivative rights/release review | [`EBD_DERIVATIVE_RELEASE.md`](./EBD_DERIVATIVE_RELEASE.md) |
| Prepare rollback or recovery review | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md), [`ROLLBACK_DRILL.md`](./ROLLBACK_DRILL.md) |
| Understand occurrence meaning | [`OccurrenceEvidence`](../../../contracts/domains/fauna/occurrence_evidence.md), [`OccurrencePublic`](../../../contracts/domains/fauna/occurrence_public.md), [`OccurrenceRestricted`](../../../contracts/domains/fauna/occurrence_restricted.md) |
| Understand current sensitivity doctrine | [`docs/domains/fauna/SENSITIVITY.md`](../../domains/fauna/SENSITIVITY.md) |
| Inspect executable occurrence validation | [`tools/validators/domains/fauna/occurrence/`](../../../tools/validators/domains/fauna/occurrence/README.md) |

[Back to top](#top)

---

## Document change rollback

This change modifies documentation only.

Before merge, close the draft pull request and abandon the branch to roll back the proposal. After an authorized merge, revert this file to its predecessor through normal Git history if the procedure proves inaccurate or conflicts with a higher authority. Do not delete occurrence evidence, rewrite historical receipts, alter source records, expose restricted values, weaken policy, or change release/public state as part of a documentation rollback.

**Non-effects:** this runbook does not admit a source, retrieve a payload, create or transform occurrence data, decide sensitivity, resolve rights, approve taxonomy, create evidence, evaluate production policy, authenticate review, change lifecycle state, release, deploy, promote, publish, or modify repository settings.

[Back to top](#top)
