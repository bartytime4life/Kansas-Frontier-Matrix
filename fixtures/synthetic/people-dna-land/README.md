<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-synthetic-people-dna-land-readme
title: fixtures/synthetic/people-dna-land/README.md — People/DNA/Land Synthetic Compatibility Boundary
type: README
version: v0.2
status: draft; repository-grounded; compatibility-boundary; payload-admission-held; domain-routing-required; T4-aware; no-network-default; non-authoritative
owners:
  - "@bartytime4life — CONFIRMED GitHub CODEOWNERS review route for /fixtures/"
  - "OWNER_TBD — People/DNA/Land fixture steward, sensitivity reviewer, consent reviewer, and migration owner"
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, schema, contract, policy, validator, test, workflow, source record, release object, or publication state is superseded
policy_label: repository-facing; fixtures; synthetic; people-dna-land; compatibility; deny-first; T4-aware; no-real-person-data; no-raw-dna; no-private-land-linkage; no-network-default; correction-aware; rollback-aware; non-publisher
owning_root: fixtures/
responsibility: preserve a reviewable compatibility pointer from the broad synthetic fixture tree to the domain-owned People/DNA/Land fixture family without admitting new payloads before consumer, policy, sensitivity, consent, test, and CI coverage are accepted
truth_posture: cite-or-abstain; synthetic naming, fixture placement, validator presence, workflow success, or a future expected output never establishes identity, kinship, DNA support, consent, ownership, title, boundary, evidence closure, policy approval, release readiness, legal sufficiency, or publication
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8e32aa017c6321e9847ffade5ac32e5f69ab2562
  prior_blob: 22625e882b89e30a25da739c2e48bd00283e9322
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  synthetic_parent_readme_blob: aef53253c29073b054542c944ecb3b34cf53d149
  domain_fixture_readme_blob: 8eb10804c587c62edf1eb9750c2c82b5cf237f2a
  domain_doctrine_readme_blob: 19a3ea59bab2d5e04c73f402a35048c1a55ab071
  domain_policy_readme_blob: 571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a
  domain_consent_readme_blob: fa7ea7c95a473a7fd498053536ca0b72b17461f6
  domain_tests_readme_blob: ddd28f6583b66cdbb81df1780e40c057c0c4a287
  domain_validator_readme_blob: 7a78d278aa03d843107d4d66a954c7a670d2ac19
  domain_workflow_blob: bb5626ff3aaba558070f53807027e70b2ba89a6e
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ../../README.md
  - ../README.md
  - ../../domains/people-dna-land/README.md
  - ../../domains/people-dna-land/genealogy/README.md
  - ../../domains/people-dna-land/land-ownership/README.md
  - ../../domains/people-dna-land/valid/README.md
  - ../../domains/people-dna-land/invalid/README.md
  - ../../domains/people-dna-land/golden/README.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../policy/domains/people-dna-land/README.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tools/validators/domains/people-dna-land/README.md
  - ../../../.github/workflows/domain-people-dna-land.yml
  - ../../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no payload, consumer, schema, contract, policy, validator, test, workflow, receipt, proof, release object, or public surface."
  - "The domain-owned fixture root is fixtures/domains/people-dna-land/; this path is retained as a compatibility and migration boundary only."
  - "Bounded repository inspection did not establish an executable consumer or test that reads this compatibility lane."
  - "The current People/DNA/Land workflow explicitly checks the domain-owned fixture root for newly surfaced payloads but does not name this compatibility path; therefore automated payload coverage for this lane is not established."
  - "New payload admission is held here because using this path could create a parallel fixture home and bypass the domain workflow's current payload guard."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/synthetic/people-dna-land/` — People/DNA/Land Synthetic Compatibility Boundary

[![Status: payload admission held](https://img.shields.io/badge/status-payload%20admission%20held-f59e0b?style=flat-square)](#status)
[![Routing: domain-owned lane](https://img.shields.io/badge/routing-domain--owned%20lane-1f6feb?style=flat-square)](#canonical-routing)
[![Sensitivity: deny-first](https://img.shields.io/badge/sensitivity-deny--first-b42318?style=flat-square)](#rights-sensitivity-and-test-data)
[![Authority: compatibility only](https://img.shields.io/badge/authority-compatibility%20only-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** This directory preserves a stable compatibility pointer for People / Genealogy / DNA / Land synthetic fixture work while routing all new or stabilized fixture material to the domain-owned [`fixtures/domains/people-dna-land/`](../../domains/people-dna-land/README.md) family through a reviewed, consumer-bound change.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Routing](#canonical-routing) · [Migration](#migration-and-retirement-posture) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Scenario routing](#scenario-routing-matrix) · [Admission](#fixture-admission-contract) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Verification](#verification-status) · [Rollback](#rollback) · [Last reviewed](#last-reviewed)

> [!IMPORTANT]
> This path is **not the canonical People/DNA/Land fixture family**. The domain-owned home is [`fixtures/domains/people-dna-land/`](../../domains/people-dna-land/README.md). Keep this compatibility lane README-only unless a reviewed migration or compatibility decision explicitly admits a payload and wires every applicable consumer, policy, consent, sensitivity, test, and workflow boundary.

> [!CAUTION]
> The current People/DNA/Land readiness workflow checks the domain-owned fixture root for newly surfaced payloads and intentionally holds executable validation. It does **not** name this compatibility path. A payload placed here could therefore escape the domain workflow's current payload guard. Do not use this directory as a shortcut around domain review.

> [!WARNING]
> “Synthetic” does not mean harmless, anonymous, consented, public-safe, or legally usable. Do not place real or realistic living-person records, raw or derived DNA material, vendor or kit identifiers, private genealogy notes, person–parcel joins, deeds, assessor rows, legal descriptions, precise residences, exact parcel geometry, credentials, or reverse-engineerable combinations here.

---

## Purpose

This README converts an inherited broad staging lane into a bounded compatibility surface.

It exists to:

- preserve stable links while the repository converges on the domain-owned fixture home;
- prevent a second People/DNA/Land fixture authority from forming under `fixtures/synthetic/`;
- route authors to the narrowest accepted domain fixture family;
- make the current lack of executable consumer coverage visible;
- keep living-person, DNA/genomic, genealogy, consent, and private land-link material fail-closed;
- define the evidence needed before any payload can be admitted, migrated, or retired;
- preserve correction and rollback options for documentation and fixture-path changes.

This lane does **not** exist to hold “temporary” sensitive examples. Temporary placement is still placement, and compatibility paths must not become ungoverned data stores.

[Back to top](#top)

---

## Authority level

| Field | Authority |
|---|---|
| **Directory class** | Existing nested compatibility lane under the canonical `fixtures/` root |
| **Current role** | Documentation pointer, routing boundary, migration record, and correction surface |
| **Canonical fixture owner** | [`fixtures/domains/people-dna-land/`](../../domains/people-dna-land/README.md) |
| **May own now** | This README, migration notes approved for this path, and temporary redirect documentation |
| **Must not own now** | Fixture payloads, schemas, policies, consent records, validators, executable tests, source records, real evidence, receipts, proofs, release objects, generated runtime output, or published artifacts |
| **Network posture** | Denied by default |
| **Public-path posture** | DENY direct serving; public clients use governed APIs and released artifacts |
| **Sensitivity posture** | Deny-first; living-person, DNA/genomic, and private person–land material receive the strictest review posture |
| **Truth posture** | A compatibility pointer proves location history only; it proves no person, relationship, DNA, land, consent, policy, review, release, or publication claim |

Directory Rules place files by primary responsibility. The domain-owned fixture family already exists under `fixtures/domains/people-dna-land/`; admitting parallel payloads here would duplicate responsibility and create drift. This documentation-only update preserves the existing path while narrowing it to a reversible compatibility role.

### Responsibility boundary

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| People/DNA/Land doctrine | [`docs/domains/people-dna-land/`](../../../docs/domains/people-dna-land/README.md) | Link only; never restate as machine or policy authority |
| Domain fixture families | [`fixtures/domains/people-dna-land/`](../../domains/people-dna-land/README.md) | Route new and stable synthetic examples |
| Semantic contracts | `contracts/domains/people-dna-land/` or an ADR-selected home | No contract authority |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` or an ADR-selected home | No schema authority |
| Domain policy | [`policy/domains/people-dna-land/`](../../../policy/domains/people-dna-land/README.md) | Current README is a greenfield scaffold; this lane cannot simulate activation |
| Consent policy | [`policy/consent/people-dna-land/`](../../../policy/consent/people-dna-land/README.md) | Use only consumer-bound toy inputs after policy activation and review |
| Executable validation | [`tools/validators/domains/people-dna-land/`](../../../tools/validators/domains/people-dna-land/README.md) | No verified executable consumer currently reads this lane |
| Test-local examples | [`tests/domains/people-dna-land/`](../../../tests/domains/people-dna-land/README.md) and `tests/fixtures/` | Keep one-test-only examples out of this compatibility path |
| Lifecycle data | `data/<phase>/people-dna-land/` | Never store real or promoted data here |
| Review, proof, receipts, and release | governed review surfaces, `data/proofs/`, `data/receipts/`, and `release/` | Never manufacture or store trust authority here |

[Back to top](#top)

---

## Status

Snapshot: `main@8e32aa017c6321e9847ffade5ac32e5f69ab2562`, inspected on 2026-07-24.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `22625e882b89e30a25da739c2e48bd00283e9322` | Existing documentation is modernized in place |
| Parent synthetic README | **CONFIRMED** at [`../README.md`](../README.md) | Parent describes a broad synthetic family, but does not establish consumers or payload maturity |
| Canonical reusable fixture root | **CONFIRMED** at [`../../README.md`](../../README.md) | Reusable fixtures are non-authoritative and distinct from test-local and lifecycle material |
| Domain-owned fixture root | **CONFIRMED** at [`../../domains/people-dna-land/README.md`](../../domains/people-dna-land/README.md) | Preferred People/DNA/Land fixture family and child-lane index exists |
| People/DNA/Land domain doctrine | **CONFIRMED DRAFT** | Living-person, DNA-derived, and private person–parcel outputs are deny-by-default; person assertions remain evidence, not facts |
| Domain policy | **CONFIRMED GREENFIELD SCAFFOLD** | Presence is not executable policy |
| Restricted-domain consent policy | **CONFIRMED README-ONLY / activation unproved** | Consent is necessary where applicable but never sufficient; executable rules and production enforcement are not established |
| Domain tests | **CONFIRMED GREENFIELD STUB** | No test coverage is established by the README |
| Domain validator index | **CONFIRMED INDEX / executables unverified** | No accepted executable validator for this lane is established |
| Domain readiness workflow | **CONFIRMED** at [`.github/workflows/domain-people-dna-land.yml`](../../../.github/workflows/domain-people-dna-land.yml) | Performs structural maturity checks and records explicit holds |
| Domain fixture payload guard | **CONFIRMED** | Workflow refuses newly surfaced payloads under `fixtures/domains/people-dna-land/` until reviewed |
| Compatibility-lane payload guard | **NOT ESTABLISHED** | Workflow does not name `fixtures/synthetic/people-dna-land/` |
| Direct consumer of this path | **NOT SURFACED IN BOUNDED SEARCH** | Treat as no verified consumer, not proof of permanent absence |
| Exact payload inventory | **UNKNOWN / not exhaustively listed** | No payload presence or absence claim is made beyond inspected files |
| Identity, genealogy, DNA, consent, title, or release validation | **NOT ESTABLISHED** | Current repository evidence supports readiness holds, not executable domain validation |
| Public or release state | **DENIED as inference** | Fixture or workflow presence cannot establish public safety, legal sufficiency, release, or publication |

### Material corrections in this revision

- Reclassifies this path from a general staging lane to a compatibility and migration boundary.
- Makes the domain-owned fixture root the explicit destination for new and stabilized work.
- Records that no direct consumer of this compatibility path was established.
- Records that the domain workflow guards payloads in the domain-owned root but not this path.
- Denies new payload admission here until coverage and migration decisions are reviewed.
- Separates synthetic appearance from public safety, consent, rights, sensitivity, evidence, title, and release claims.
- Replaces broad implemented-consumer language with evidence-bounded routing and activation criteria.
- Adds migration, retirement, review, validation, correction, and rollback rules.

[Back to top](#top)

---

## Canonical routing

Use the narrowest verified owner.

| Scenario | Preferred home | Current posture |
|---|---|---|
| Positive historical genealogy assertion or ancestor summary | `fixtures/domains/people-dna-land/genealogy/positive/` | Admit only with a named consumer and public-safe synthetic data |
| Missing-evidence, identity-conflict, living-person, raw-source, DNA-derived, or private land-link genealogy case | `fixtures/domains/people-dna-land/genealogy/negative/` or `invalid/` | Fail closed; expected result must be consumer-bound |
| Land ownership assertion, interval, instrument, assessor/tax context, parcel-version context | `fixtures/domains/people-dna-land/land-ownership/` | Preserve evidence-not-title and geometry-not-boundary distinctions |
| Broad positive case awaiting narrower classification | `fixtures/domains/people-dna-land/valid/` | Temporary domain-owned staging only |
| Broad invalid or deny-first case awaiting narrower classification | `fixtures/domains/people-dna-land/invalid/` | Temporary domain-owned fail-closed staging only |
| Stable expected output | `fixtures/domains/people-dna-land/golden/` | Deterministic output, never truth or release authority |
| Test-local example used by one test area | `tests/domains/people-dna-land/` or `tests/fixtures/` | Keep local to executable assertions |
| Real source, person, DNA, land, consent, evidence, proof, or release material | Governed responsibility root and lifecycle | Never a fixture |
| Compatibility or migration note for this historical path | This README | Allowed while path remains present |

### Why not stage here?

This path is outside the payload guard currently implemented by the domain readiness workflow. New payloads here would create a parallel fixture home and weaken inspectability. The smallest sound change is to keep the path as a documentation-only redirect until a deliberate migration or retirement closes the seam.

[Back to top](#top)

---

## Migration and retirement posture

No payload is moved, deleted, or created by this README update.

### Preferred next state

**PROPOSED:** retire this directory after an exhaustive tree and reference scan confirms that it contains no required payloads and no external or internal consumer depends on the path.

### Required migration sequence

Before moving or retiring any material:

1. inventory all tracked, ignored, generated, and externally stored content associated with this path;
2. identify every consumer, documentation link, workflow path filter, script reference, issue, and release note;
3. classify each item by object family, sensitivity, rights, consent, and expected outcome;
4. choose the narrow domain-owned or test-local destination;
5. verify contracts, schemas, policy, validators, tests, and expected outputs together;
6. update the domain workflow so it safely inspects the admitted fixture family without opening restricted material;
7. preserve deterministic identity or record the identity migration;
8. repair all references and add a migration or deprecation note;
9. validate the destination and rollback path;
10. remove this compatibility directory only in a separately reviewed change.

Do not copy payloads into both homes. Duplication creates divergent fixtures and ambiguous authority.

[Back to top](#top)

---

## What belongs here

Until migration or retirement is accepted, this lane may contain only:

- this README;
- a reviewed compatibility pointer or deprecation note;
- a migration manifest that contains **paths and hashes only**, with no sensitive payload content;
- a rollback note identifying the prior documentation or path state;
- link-repair guidance during an approved migration.

Any additional file is **NEEDS VERIFICATION** and should be denied by default until its necessity, sensitivity, consumer, and destination are reviewed.

[Back to top](#top)

---

## What does not belong here

Do not place any of the following in this compatibility lane:

- real or realistic living-person data;
- names, aliases, dates of birth, contact details, residence histories, private notes, or family secrets;
- GEDCOM exports, family trees, vital records, obituaries, directories, correspondence, or source scans;
- raw DNA, genotypes, segments, triangulation results, haplogroup details, vendor IDs, kit IDs, tokens, credentials, or derived relationship scores;
- person–parcel, person–address, person–household, or person–infrastructure joins;
- deeds, title instruments, assessor or tax records, parcel records, legal descriptions, exact boundaries, or title opinions;
- real or plausibly real Kansas addresses, parcel identifiers, coordinates, legal descriptions, or precise geometries;
- SourceDescriptors, EvidenceBundles, PolicyDecisions, ConsentRecords, ReviewRecords, receipts, proofs, release manifests, correction records, or rollback records;
- schemas, policy rules, validator code, test code, runtime code, generated QA output, model output, public API responses, public maps, tiles, or published artifacts;
- “temporary” copies of material awaiting review;
- payloads duplicated from the domain-owned fixture root.

[Back to top](#top)

---

## Scenario routing matrix

| Scenario | This path? | Correct posture |
|---|---:|---|
| README redirect to domain fixture family | Yes | Compatibility documentation only |
| Migration manifest with path, digest, destination, and status | Conditional | No payload content; reviewed and reversible |
| Clearly fictional historical relationship input | No | Route to domain genealogy positive/negative lane after consumer review |
| Living-person disclosure attempt | No | Domain negative/invalid lane; expected `DENY` or review-required only when a consumer exists |
| Raw or derived DNA fixture | No | Default deny; require dedicated policy, consent, sensitivity, schema, validator, test, and public-safe transformation review |
| Toy consent token or revocation case | No | Domain-owned/test-local lane only after accepted consent contract and consumer |
| Assessor context represented as administrative evidence | No | Domain land-ownership lane; never title truth |
| Parcel geometry represented as legal boundary | No | Domain invalid lane; fail closed |
| Stable expected output | No | Domain golden lane |
| One-test-only fixture | No | Test-local fixture home |
| Real data redacted into a “synthetic” example | No | Quarantine and review; redaction alone does not establish safe synthetic status |
| Payload added solely because this directory already exists | No | Existing path is not admission evidence |

[Back to top](#top)

---

## Fixture admission contract

A future payload may be admitted only through a coordinated change that proves all applicable requirements.

### Required identity and ownership

- named object family;
- canonical destination;
- deterministic fixture ID and digest;
- accepted semantic owner;
- accepted policy, consent, and sensitivity reviewers;
- named executable consumer;
- explicit valid, invalid, deny, abstain, error, or expected-output posture.

### Required data-safety evidence

- generated from first principles or demonstrably public-safe source material;
- no real person, DNA, land, title, consent, or private linkage data;
- no realistic combination that could be matched to a person or property;
- no raw DNA-like sequence, kit/vendor identifier, or relationship inference;
- no exact address, coordinate, parcel identifier, legal description, or protected location;
- rights and generation method documented;
- sensitivity and re-identification review recorded;
- network denied unless a separately governed integration workflow is approved.

### Required consumer evidence

- contract or explicit semantic rule;
- schema where shape validation applies;
- policy bundle or explicit policy mock where admissibility is tested;
- deterministic validator or test;
- finite expected result;
- negative-state coverage;
- output location;
- correction and rollback behavior;
- CI or local command that actually reads the fixture;
- proof limits documented.

### Required workflow change

Because the current domain workflow refuses newly surfaced domain fixture payloads and does not inspect this compatibility path, payload activation must update the workflow in the same reviewed change or an explicitly ordered prerequisite change.

A README claim, filename, or directory presence is not sufficient admission evidence.

[Back to top](#top)

---

## Inputs

This compatibility lane currently accepts no runtime or validation payload input.

Permitted documentation inputs are limited to:

- pinned repository paths and blob/commit identifiers;
- migration destinations;
- consumer references;
- sensitivity, consent, rights, and review decisions;
- compatibility status;
- rollback targets.

Do not embed example person, DNA, land, or consent objects in this README unless they are strictly schematic field-name fragments with no values. Prefer linking to the accepted domain fixture contract after it exists.

[Back to top](#top)

---

## Outputs

This lane produces documentation only:

- routing guidance;
- compatibility status;
- migration decisions;
- correction notes;
- rollback instructions.

It does not produce:

- validated identities or relationships;
- genealogy findings;
- DNA/genomic support;
- consent decisions;
- ownership or title findings;
- public-safe derivatives;
- EvidenceBundles;
- receipts or proofs;
- release candidates;
- public API/UI/map/AI output.

Generated reports, if a future migration tool exists, belong in an accepted QA artifact location and must not contain sensitive payloads.

[Back to top](#top)

---

## Validation

### Documentation preflight

```bash
git diff --check
git diff -- fixtures/synthetic/people-dna-land/README.md
```

### Repository-state checks

```bash
test -f fixtures/synthetic/people-dna-land/README.md
test -f fixtures/domains/people-dna-land/README.md
test -f .github/workflows/domain-people-dna-land.yml
```

### Compatibility-lane payload check

A local reviewer with an executable checkout should verify that no substantive payload is present:

```bash
find fixtures/synthetic/people-dna-land \
  -type f \
  ! -name 'README.md' \
  ! -name '.gitkeep' \
  -print
```

Expected current result: **no output**. This expectation is **NEEDS VERIFICATION** until run against an executable checkout; remote file reads did not provide a byte-complete recursive listing.

### Domain readiness workflow

The current workflow:

- verifies required People/DNA/Land boundary files;
- detects newly executable domain tests and validators;
- refuses to open newly surfaced payloads under `fixtures/domains/people-dna-land/`;
- confirms current policy scaffolding;
- records `WORKFLOW_HOLD` for validation, proof, and release readiness.

It does not establish coverage of this compatibility path, and a green held workflow is not domain validation.

### What passing proves

A documentation check can prove only that:

- the README is structurally valid;
- links and paths resolve in the checked revision;
- the compatibility routing is internally consistent;
- no unapproved payload was found by the executed inventory command.

It cannot prove identity, relationship, DNA, consent, ownership, title, boundary, policy, evidence, release, legal sufficiency, or publication.

[Back to top](#top)

---

## Failure interpretation

| Failure | Interpretation | Required response |
|---|---|---|
| Payload found in this compatibility lane | Potential parallel-home and sensitivity breach | Stop; do not open sensitive content automatically; classify and route through reviewed migration |
| Domain workflow fails because a fixture payload surfaced | Guard detected unreviewed activation | Review contracts, policy, consent, sensitivity, validators, tests, expected outcomes, and safe inspection |
| README link points to a missing destination | Migration/routing drift | Repair the link or mark the destination `NEEDS VERIFICATION`; do not invent a path |
| Fixture appears synthetic but contains realistic identifiers | Re-identification and rights risk | Quarantine; require sensitivity and consent review |
| Positive result lacks EvidenceRef/EvidenceBundle or policy context | Unsupported claim posture | `ABSTAIN`, `DENY`, or review-required in the owning consumer |
| Land fixture collapses assessor data into title or geometry into boundary | Semantic and legal-risk failure | Fail closed and route to land-ownership negative coverage |
| DNA fixture exposes raw or reverse-engineerable material | T4 sensitivity failure | Deny, quarantine, and remove from repository history through the accepted security process when required |
| No consumer reads a fixture | Orphaned fixture | Do not admit; document as proposed or remove through reviewed migration |
| CI is green only because a workflow records a hold | Maturity remains unproved | Preserve the hold; do not claim enforcement or release readiness |

[Back to top](#top)

---

## Rights, sensitivity, and test data

People/DNA/Land is a deny-first domain.

### Synthetic-data minimum

Use opaque placeholders rather than realistic personal or land values:

- `PersonA`, `PersonB`, `HistoricalPersonExample`;
- `SyntheticRelationship1`;
- `ToySourceRef`;
- `ToyEvidenceRef`;
- `ToyPlaceRef`;
- `ToyParcelRef`;
- `ToyInstrumentRef`;
- `ConsentStateExample`;
- `SyntheticOwnerA`.

Even these placeholders belong in the domain-owned lane after admission, not here.

### Prohibited realism

Do not use:

- real surnames combined with real towns, dates, cemeteries, obituaries, or family structures;
- plausible full dates of birth for living or recently deceased people;
- real streets, rural routes, legal descriptions, parcel numbers, or exact map coordinates;
- DNA sequences, centimorgan values, segment coordinates, kit IDs, vendor formats, or triangulation patterns that resemble actual data;
- realistic consent tokens, credentials, signatures, or revocation identifiers;
- realistic person–land linkages that could be reverse searched.

### Doctrine boundaries

- Person assertions are evidence, not settled facts.
- Relationship hypotheses are not kinship truth.
- DNA-derived hints do not become public relationships.
- Consent is scoped, revocable, and never a general publication license.
- Assessor and tax records are administrative context, not title truth.
- Parcel geometry is not legal-boundary proof.
- Public release requires independent evidence, policy, rights, sensitivity, review, correction, rollback, and release controls.

When safety is uncertain, abstain from creating the fixture and escalate to the domain, consent, sensitivity, and rights reviewers.

[Back to top](#top)

---

## Review burden

Any change to this path requires:

1. documentation review for routing and links;
2. fixture-root review through `/fixtures/` CODEOWNERS routing;
3. People/DNA/Land domain review;
4. sensitivity review;
5. consent/privacy review when living-person, relationship, DNA, or person-linked material is implicated;
6. rights and legal-risk review when land instruments, administrative records, or title-adjacent context is implicated;
7. validator/test review when a consumer is added;
8. release review when any output is described as candidate, public-safe, or publishable.

Required CODEOWNERS routing is not the same as required-review enforcement, independent approval, or semantic stewardship. Those controls remain `NEEDS VERIFICATION`.

No author should self-approve a payload activation that introduces living-person, DNA/genomic, private linkage, consent, or title-adjacent risk.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../../README.md`](../../README.md) | Canonical reusable fixture-root contract |
| [`../README.md`](../README.md) | Synthetic fixture parent; inherited broad staging language remains documentation debt |
| [`../../domains/people-dna-land/README.md`](../../domains/people-dna-land/README.md) | Canonical domain-owned fixture family |
| [`../../domains/people-dna-land/genealogy/README.md`](../../domains/people-dna-land/genealogy/README.md) | Genealogy fixture family |
| [`../../domains/people-dna-land/land-ownership/README.md`](../../domains/people-dna-land/land-ownership/README.md) | Evidence-not-title land fixture family |
| [`../../domains/people-dna-land/valid/README.md`](../../domains/people-dna-land/valid/README.md) | Broad positive domain-owned staging |
| [`../../domains/people-dna-land/invalid/README.md`](../../domains/people-dna-land/invalid/README.md) | Broad fail-closed domain-owned staging |
| [`../../domains/people-dna-land/golden/README.md`](../../domains/people-dna-land/golden/README.md) | Stable domain expected outputs |
| [`../../../docs/domains/people-dna-land/README.md`](../../../docs/domains/people-dna-land/README.md) | Domain doctrine and T4 deny-by-default posture |
| [`../../../policy/domains/people-dna-land/README.md`](../../../policy/domains/people-dna-land/README.md) | Current domain policy scaffold |
| [`../../../policy/consent/people-dna-land/README.md`](../../../policy/consent/people-dna-land/README.md) | Restricted-domain consent boundary; activation unproved |
| [`../../../tests/domains/people-dna-land/README.md`](../../../tests/domains/people-dna-land/README.md) | Current greenfield test stub |
| [`../../../tools/validators/domains/people-dna-land/README.md`](../../../tools/validators/domains/people-dna-land/README.md) | Proposed validator index; executable coverage unproved |
| [`../../../.github/workflows/domain-people-dna-land.yml`](../../../.github/workflows/domain-people-dna-land.yml) | Readiness and hold workflow |
| [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md) | Placement doctrine |
| `../../../data/` | Governed lifecycle data, evidence, receipts, and proofs |
| `../../../release/` | Release, correction, withdrawal, and rollback authority |

[Back to top](#top)

---

## ADRs

No ADR is required for this same-path documentation correction. It adds no payload, root, authority, consumer, migration, or runtime behavior.

An ADR or explicit migration note may be required when a future change:

- retires this compatibility path;
- establishes an alias or redirect convention for fixture paths;
- changes the canonical People/DNA/Land segment;
- creates a new schema, contract, policy, consent, or sensitivity placement;
- permits fixtures outside `fixtures/domains/people-dna-land/`;
- defines a machine-readable fixture manifest or identity contract;
- activates executable People/DNA/Land validators, policy, consent, or CI;
- changes the split between reusable and test-local fixtures;
- introduces a public or restricted runtime fixture tier;
- changes review separation or release duties.

A payload addition does not automatically require an ADR, but it does require the admission, workflow, policy, consent, sensitivity, and consumer evidence in this README.

[Back to top](#top)

---

## Verification status

| Check | Result |
|---|---|
| Target path and prior bytes | **CONFIRMED** at `main@8e32aa017c6321e9847ffade5ac32e5f69ab2562`, blob `22625e882b89e30a25da739c2e48bd00283e9322` |
| Same-path documentation update | **PASS** — no sibling README or path move |
| Root fixture contract | **CONFIRMED** at blob `911c20c86d9322f38b1f59db66b922a94fd027eb` |
| Synthetic parent README | **CONFIRMED** at blob `aef53253c29073b054542c944ecb3b34cf53d149` |
| Domain fixture root | **CONFIRMED** at blob `8eb10804c587c62edf1eb9750c2c82b5cf237f2a` |
| Domain doctrine | **CONFIRMED DRAFT** at blob `19a3ea59bab2d5e04c73f402a35048c1a55ab071` |
| Domain policy | **CONFIRMED GREENFIELD SCAFFOLD** at blob `571a4a6d5c8ba7cf6c1fa9fcdd63da88bc05eb2a` |
| Restricted-domain consent README | **CONFIRMED README-ONLY / activation unproved** at blob `fa7ea7c95a473a7fd498053536ca0b72b17461f6` |
| Domain test README | **CONFIRMED GREENFIELD STUB** at blob `ddd28f6583b66cdbb81df1780e40c057c0c4a287` |
| Domain validator index | **CONFIRMED / executable coverage unproved** at blob `7a78d278aa03d843107d4d66a954c7a670d2ac19` |
| Domain readiness workflow | **CONFIRMED** at blob `bb5626ff3aaba558070f53807027e70b2ba89a6e` |
| Workflow guard for domain fixture payloads | **CONFIRMED** |
| Workflow guard for this compatibility path | **NOT ESTABLISHED** |
| Direct compatibility-lane consumer | **NOT SURFACED IN BOUNDED SEARCH** |
| Exhaustive payload inventory | **UNKNOWN / not performed** |
| Local compatibility payload scan | **NOT RUN** — no executable checkout mounted |
| Tests, validators, policy, and consent execution | **NOT RUN / not established** |
| Markdown lint, docs build, and link checker | **NOT RUN locally** |
| Required-review and branch-protection enforcement | **NEEDS VERIFICATION** |
| Identity, genealogy, DNA, consent, ownership, title, release, or publication result | **NOT CLAIMED** |

Remote repository reads establish specific bytes, paths, and workflow source. They do not substitute for a recursive tree inventory, local test run, policy evaluation, consent verification, sensitivity review, release dry-run, or legal review.

[Back to top](#top)

---

## Rollback

This is a documentation-only, same-path update.

Rollback options:

1. revert the update commit created for this README; or
2. restore prior blob `22625e882b89e30a25da739c2e48bd00283e9322` at `fixtures/synthetic/people-dna-land/README.md`.

Rollback changes documentation only. It does not add, remove, move, approve, validate, quarantine, release, correct, or publish a fixture payload, person record, DNA record, land record, consent record, evidence object, policy decision, proof, receipt, or release object because none are changed by this update.

[Back to top](#top)

---

## Last reviewed

**2026-07-24** — repository-grounded documentation review against `main@8e32aa017c6321e9847ffade5ac32e5f69ab2562`.

Review again when:

- any non-README file appears in this directory;
- the parent synthetic README changes its compatibility posture;
- the domain-owned fixture root admits its first payload;
- a People/DNA/Land validator, test, policy bundle, consent evaluator, or schema becomes executable;
- the domain workflow begins safely inspecting fixture payloads;
- a migration or retirement proposal is opened;
- the `people` versus `people-dna-land` placement conflict is resolved;
- ownership, required review, or branch-protection rules change;
- six months pass without review.

[Back to top](#top)
