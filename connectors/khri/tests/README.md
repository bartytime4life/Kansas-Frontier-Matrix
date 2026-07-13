<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-khri-tests-readme
title: connectors/khri/tests/ — KHRI Greenfield Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · Kansas/KHRI source steward · KSHS/SHPO liaison · Archaeology steward · Settlements steward · People/privacy reviewer · Rights reviewer · Sensitivity/cultural-review steward · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-tests; compatibility-path; canonical-family-conflict; source-admission; historic-resource-anti-collapse; rights-fail-closed; cultural-sensitivity-fail-closed; private-location-fail-closed; no-network; negative-first; no-activation; no-publication
current_path: connectors/khri/tests/README.md
truth_posture: CONFIRMED documentation-only local test lane beside a 0.0.0 package scaffold with merged v0.2 source and package boundaries, empty initializer, comment-only fetch/admit modules, and a nonconforming four-field descriptor; conventional conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, and tests/fixtures/README.md were not found at current named probes / CONFLICTED final package and test paths, compatibility class, SourceDescriptor authority, narrative-to-machine role mapping, product topology, fixture routing, registry activation, and public sensitivity floor / PROPOSED negative-first KHRI test contract / UNKNOWN differently named tests, test collection, coverage, package buildability, runtime behavior, live source access, current rights and terms, endpoint/source-head state, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 2e8225eac2d244ac073bee3c2655f84de6f688cc
related:
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/khri/README.md
  - ../src/khri/__init__.py
  - ../src/khri/fetch.py
  - ../src/khri/admit.py
  - ../src/khri/descriptor.yaml
  - ../../README.md
  - ../../kansas/README.md
  - ../../../CONTRIBUTING.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/kansas/khri.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/README.md
  - ../../../fixtures/README.md
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../release/
tags: [kfm, connectors, khri, kshs, shpo, kansas, historic-resources, archaeology, settlements, cultural-resources, tests, python, greenfield, compatibility, source-admission, source-role, rights, sensitivity, privacy, geometry, fixtures, no-network, negative-first, raw, quarantine, no-publication]
notes:
  - "The current local test lane contains this README; conventional files named conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, and tests/fixtures/README.md returned Not Found at current main probes."
  - "The package under test is version 0.0.0 with an empty __init__.py, comment-only fetch.py and admit.py, and a nonconforming descriptor.yaml placeholder."
  - "The merged v0.2 source-layout and package READMEs document exact package files, absent richer helper modules, unresolved Kansas-family migration, role-vocabulary conflict, and cultural-resource fail-closed boundaries."
  - "The parent connectors/khri/README.md remains v0.1 and contains an overconfident canonicality claim; this test README follows current verified child evidence and does not ratify that claim."
  - "The KHRI source dossier states connectors/kansas/khri/ is the correct connector path, but exact current probes in the merged package evidence did not establish that child lane. Final test routing remains governed and unresolved."
  - "The source dossier and archaeology guide use narrative role administrative, while the current populated SourceDescriptor machine enum does not. Tests must reject convenience mapping until an accepted crosswalk exists."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green completion cannot prove imports, test collection, descriptor conformance, rights review, cultural-sensitivity enforcement, or release readiness."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, executable test, workflow, contract, schema, policy, source payload, credential, activation decision, lifecycle artifact, evidence object, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KHRI Greenfield Connector Test Boundary

> Repository-grounded test contract for `connectors/khri/tests/`. The adjacent package is a non-operational `0.0.0` scaffold. This README defines what future tests must prove; it does not claim that executable tests, fixtures, collection, coverage, source access, or substantive CI enforcement already exist.

**Document lifecycle:** `draft v0.2`  
**Current maturity:** `CONFIRMED` README-only local test lane beside a greenfield package scaffold  
**Owner:** `OWNER_TBD`  
**Authority:** test-boundary documentation only; tests prove behavior but do not own source identity, contracts, schemas, policy, lifecycle state, evidence, release, or publication  
**Default posture:** synthetic fixtures · no network · no credentials · no lifecycle writes · no public output

> [!IMPORTANT]
> The package currently supplies no supported fetch, parse, normalize, or admission behavior to test. An empty initializer, comment-only modules, a placeholder descriptor, this README, a pull request, a merge, or a green workflow does not establish test discovery, coverage, source authority, activation, or readiness.

> [!CAUTION]
> KHRI material may include archaeological or culturally restricted locations, historic-resource geometry, private-property details, historical or living-person associations, eligibility and designation evaluations, photographs, survey attachments, and collection-security information. Test fixtures, logs, snapshots, traces, failure messages, and generated artifacts must not become an accidental disclosure channel. Unknown rights, product identity, source role, cultural review, sensitivity, geometry precision, or public-release posture fails closed.

**Quick links:** [Purpose](#purpose) · [Current test lane](#current-test-lane) · [Repository fit](#repository-fit) · [Test authority](#test-authority-boundary) · [Package under test](#package-under-test) · [Surface identity](#khri-and-kshs-surface-identity) · [Record meanings](#khri-record-and-claim-boundaries) · [Fixture safety](#fixture-safety) · [Required families](#required-test-families) · [No-network contract](#no-network-and-side-effect-contract) · [Descriptor tests](#descriptor-role-and-activation-tests) · [Rights and sensitivity](#rights-cultural-sensitivity-privacy-and-geometry-tests) · [Identity and time](#identity-time-correction-and-crosswalk-tests) · [Lifecycle tests](#lifecycle-and-output-boundary-tests) · [Migration tests](#migration-and-routing-tests) · [Failure contract](#failure-contract) · [Validation matrix](#validation-matrix) · [CI limits](#ci-and-observability) · [Evidence](#evidence-basis) · [Review](#review-burden) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

This README turns the local KHRI test directory into an explicit, fail-closed verification boundary.

It exists to:

- distinguish documented expectations from executable proof;
- bind future tests to the actual `0.0.0` package scaffold and unresolved migration posture;
- require KHRI/KSHS surface, product, source-role, rights, cultural-sensitivity, privacy, identity, time, geometry, attachment, and lifecycle checks before source access is considered;
- keep default tests deterministic, synthetic, no-network, credential-free, and side-effect-free;
- prevent fixtures, snapshots, logs, traces, reports, screenshots, and CI artifacts from exposing sensitive cultural-resource or private-location information;
- define finite negative outcomes for incomplete, ambiguous, restricted, or unsafe candidates;
- make zero-test discovery, skipped negative cases, TODO-only workflows, and permissive placeholders visible failures rather than false confidence.

This lane does not activate a source, approve terms, establish a canonical connector path, create a `SourceDescriptor`, select a source-role crosswalk, decide public precision, close an `EvidenceBundle`, authorize release, or prove that a KHRI record or interpretation is true.

[Back to top](#top)

---

## Current test lane

The directly evidenced local test surface is:

```text
connectors/khri/tests/
└── README.md                         # this test-boundary document
```

Current exact probes returned `Not Found` for:

```text
connectors/khri/tests/conftest.py
connectors/khri/tests/test_fetch.py
connectors/khri/tests/test_admit.py
connectors/khri/tests/test_descriptor.py
connectors/khri/tests/fixtures/README.md
```

These statements are bounded to the named paths and reviewed `main` state. Differently named, generated, unindexed, ignored, or concurrently added files remain `UNKNOWN` until directly read and collected at the commit under review.

### Current maturity

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| This README | Documentation contract exists. | Test intent is documented; no executable proof follows from documentation alone. |
| Local executable tests | Not established at the current named probes. | Collection count, pass/fail state, skips, xfails, coverage, and negative-case enforcement are `UNKNOWN`. |
| Local test fixtures | No `tests/fixtures/README.md` at the named probe. | Fixture location, provenance, rights review, sensitivity review, and safety receipts are unresolved. |
| Package | `kfm-connector-khri` version `0.0.0`. | Greenfield placeholder; build and import support are not established. |
| Package modules | Empty `__init__.py`; comment-only `fetch.py` and `admit.py`. | No supported network, parse, normalization, admission, quarantine, or handoff behavior exists. |
| Local descriptor | Four-field placeholder with unresolved role and rights plus `sensitivity_floor: public`. | Invalid as activation, cultural-sensitivity clearance, public-location clearance, or release evidence. |
| Source/package docs | v0.2 and merged. | Current verified documentation of package/layout boundaries; still not executable proof. |
| Parent connector README | v0.1 and stale relative to child evidence. | Its canonicality wording must not be used as migration proof. |
| Connector workflows | TODO echo steps in the inspected workflow definitions. | Green completion proves workflow execution only, not KHRI behavior or test coverage. |

[Back to top](#top)

---

## Repository fit

Directory Rules assign one primary responsibility to each root:

| Responsibility | Owning surface | Test-lane relationship |
|---|---|---|
| Source-specific fetch, probe, preservation, parsing, packaging, and admission mechanics | `connectors/` | Local tests may verify connector mechanics without becoming source authority. |
| Object meaning | `contracts/` | Tests consume accepted meaning; they do not redefine it. |
| Machine shape | `schemas/` | Tests validate against accepted schemas; fixtures and snapshots do not become schema authority. |
| Allow, deny, restrict, redact, abstain, or hold decisions | `policy/` | Tests exercise policy with safe fixtures; they do not mint policy. |
| Source identity, role, rights, sensitivity, cadence, access, and activation | accepted registry/control-plane surfaces | Tests resolve or mock reviewed records; local YAML cannot activate a source. |
| Cultural, sovereignty, steward, and privacy review | accepted governance and policy surfaces | Tests prove enforcement; they do not replace reviewer decisions. |
| Canonical enforceability proof | root `tests/` and accepted validator lanes | Connector-local tests provide narrow package proof; final routing remains `CONFLICTED / NEEDS VERIFICATION`. |
| Golden and negative samples | accepted `fixtures/` or deliberately scoped `tests/fixtures/` lanes | Local test data must follow the accepted fixture-home decision; do not create a parallel fixture authority. |
| Lifecycle material | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Default tests must not write to live lifecycle roots. |
| Evidence and process memory | proof and receipt lanes | Test reports are not EvidenceBundles, source receipts, cultural-review records, or release proofs. |
| Promotion, release, correction, withdrawal, and rollback | `release/` and governed lifecycle surfaces | A passing connector test cannot publish anything. |

The local test directory is useful only when it proves narrow implementation behavior and routes broader enforceability to accepted root-level test, fixture, validator, policy, and release surfaces.

[Back to top](#top)

---

## Test authority boundary

Tests may prove that code behaves according to accepted inputs and constraints. They must not be treated as authority for those inputs or constraints.

A local KHRI test may prove:

- package import is side-effect-free;
- network and credential access are denied in the default suite;
- a parser preserves source-native identity, text, qualifiers, time, geometry, and attachment references;
- an adapter rejects an invalid descriptor;
- an unresolved narrative role is not silently mapped to a machine role;
- a candidate is held, quarantined, denied, or abstained when rights, sensitivity, cultural review, privacy, or geometry is unresolved;
- KHRI remains distinct from sibling KSHS surfaces and peer authorities;
- inventory, survey, evaluation, eligibility, recommendation, designation, ownership, condition, and current existence are not collapsed;
- no test or package write escapes a caller-owned temporary directory;
- no public artifact is emitted;
- deterministic inputs produce deterministic candidates and reason codes.

A local KHRI test cannot prove:

- current KHRI/KSHS source terms, endpoint availability, institutional authority, or legal effect;
- that a source dossier or package-local YAML is a conforming `SourceDescriptor`;
- that `connectors/khri/` or `connectors/kansas/khri/` is the final package or test home;
- that narrative `administrative` maps to a particular machine source-role value;
- that inventory inclusion equals designation, eligibility, ownership, condition, access permission, archaeological status, or current existence;
- that an exact cultural-resource or private-property location is public-safe;
- that a record is authoritative outside its declared surface, product, role, jurisdiction, and time;
- that a candidate has completed cultural, sovereignty, rights, privacy, evidence, catalog, policy, review, or release closure;
- that a workflow, commit, pull request, merge, map, export, or generated explanation is publication.

[Back to top](#top)

---

## Package under test

The bounded package snapshot established by the merged source and package documentation is:

```text
connectors/khri/
├── pyproject.toml                  # project kfm-connector-khri, version 0.0.0
├── src/
│   ├── README.md                   # v0.2 source-layout boundary
│   └── khri/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only placeholder
│       ├── admit.py                # comment-only placeholder
│       └── descriptor.yaml         # nonconforming placeholder
└── tests/
    └── README.md                   # this file
```

The first executable test increment must not pretend to test unimplemented transport, parsing, or admission behavior. It should establish the harness and prove one synthetic negative boundary at a time.

### Smallest safe first increment

1. Add one compact invented KHRI-shaped record with no real person, property, resource, coordinate, attachment, endpoint, credential, or source payload.
2. Add one explicit test configuration that blocks network and credential access.
3. Add one negative test that rejects the current placeholder descriptor or an equivalent invented invalid descriptor.
4. Assert a deterministic `HOLD`, `QUARANTINE`, `DENY`, `ABSTAIN`, or `ERROR` result using the accepted shared vocabulary.
5. Assert no lifecycle, registry, receipt, proof, catalog, release, map, API, or public-file side effect.
6. Make zero discovery and unexpected skips fail CI.

[Back to top](#top)

---

## KHRI and KSHS surface identity

Institutional relationship does not erase source-surface identity.

Tests must preserve distinctions among:

| Surface | Test expectation | Prohibited collapse |
|---|---|---|
| KHRI | Preserve KHRI surface identity, inventory/resource identifiers, survey/evaluation context, record version, source URI, and source-native fields. | Do not treat the KSHS umbrella as a substitute descriptor or collapse KHRI into all KSHS holdings. |
| Kansas Memory | Preserve distinct collection, item, presentation, rights, and media identity. | Do not treat a Kansas Memory item as a KHRI inventory or designation record. |
| KSHS State Archives proper | Preserve archival collection, series, folder, item, creator, and access context. | Do not treat archival description as KHRI survey/designation authority. |
| NRHP or other designation authority | Preserve program, jurisdiction, nomination, status, decision, effective time, and record identity. | Do not infer designation from KHRI presence or map overlap. |
| GNIS and place authorities | Preserve place-name and feature identity within source role. | Do not treat a place anchor as historic-resource status, parcel identity, or precise resource geometry. |
| Assessor, parcel, deed, or title sources | Preserve independent property and time identity. | Do not infer current ownership, title, occupancy, access permission, or parcel match from KHRI alone. |
| Archaeology and cultural-resource registries | Preserve steward, sensitivity, sovereignty, site, survey, and review authority. | Do not expose or infer archaeological status from a generic KHRI record without governed review. |
| Generated joins, maps, summaries, models, or AI text | Preserve input references, transform identity, uncertainty, policy labels, and reality boundary. | Generated carriers cannot mint source authority, designation, title truth, or public-location clearance. |

[Back to top](#top)

---

## KHRI record and claim boundaries

| Record meaning | What a test may assert | What it must reject |
|---|---|---|
| Inventory presence | A source record exists in KHRI for a stated resource and version. | Inventory presence equals current existence, legal designation, eligibility, ownership, condition, or public access. |
| Survey or evaluation | A survey/evaluation occurred under a stated method, scope, author, and date. | Survey opinion equals final agency decision or current condition. |
| Eligibility or recommendation | A source records a bounded recommendation or evaluation at a specific time. | Recommendation equals listing, designation, protection, permit approval, or perpetual status. |
| Designation or legal status | A named authority issued a decision within stated jurisdiction and effective time. | KHRI text alone creates legal status without decision evidence. |
| Address or place description | A source supplied a historical or descriptive location. | Address equals current parcel, residence, exact resource geometry, access route, or permission. |
| Geometry | A source supplied observed, digitized, inferred, generalized, buffered, withheld, or null geometry with method and uncertainty. | Geometry is exact, current, complete, public-safe, or parcel-aligned unless proved and reviewed. |
| Owner or occupant | A source records a historical association at a stated time and evidence basis. | Historical association equals current owner, resident, titleholder, contact, or living-person identity. |
| Condition or use | A source records condition/use as observed or reported at a stated time. | Historical condition/use equals current condition, safety, vacancy, demolition, or occupancy. |
| Attachment, photograph, form, or report | A source references or provides a specific media/document object with rights and sensitivity metadata. | Attachment is safe to commit, redistribute, OCR, quote, embed, or publish by default. |
| Correction or supersession | A later record amends, corrects, withdraws, or supersedes an earlier record. | Latest retrieval silently overwrites historical meaning or deletes prior provenance. |

[Back to top](#top)

---

## Fixture safety

### Allowed fixture classes

| Fixture class | Use | Required controls |
|---|---|---|
| Fully synthetic shape fixture | Parser, schema, identity, failure, and boundary tests. | Invented names/IDs; impossible or clearly fictional geometry; no live endpoint or copied payload. |
| Minimal public and rights-reviewed sample | Compatibility test requiring source-native syntax. | Source-steward, rights, privacy, and cultural-sensitivity review; minimized fields; provenance and permitted-use record. |
| Redacted or generalized sample | Sensitive-field and public-transform tests. | Transform documented; original not committed; precision and withheld fields proven absent. |
| Invalid fixture | Fail-closed tests. | Clearly marked invalid; no real sensitive material; deterministic reason code expected. |
| Golden normalized candidate | Determinism and regression tests. | Derived only from an approved fixture; stable serialization; no claim or release authority. |

### Forbidden fixture content

Do not commit:

- exact or realistically precise archaeological, sacred, burial-associated, human-remains, restricted cultural, or collection-security locations;
- private-land, owner, occupant, contact, residence, access-route, submitter, reviewer, or living-person identifiers;
- current private-property geometry or attributes that allow straightforward re-identification;
- credentials, tokens, cookies, session state, API keys, signed URLs, or private endpoints;
- bulk source exports, production snapshots, unpublished survey forms, internal review notes, nominations, attachments, photographs, or GIS packages;
- unclear-rights text, images, scans, plans, reports, or copied upstream payloads;
- real records altered only superficially while retaining recognizable identity or geometry;
- logs or snapshots containing request headers, secrets, exact coordinates, restricted text, or unredacted source responses.

### Join-induced sensitivity

Tests must evaluate the output of joins, not just the sensitivity of each input. A public place, district, parcel, owner history, address, road, building footprint, aerial image, archaeological indicator, review result, or institutional record may create a more revealing product when combined. The joined candidate inherits the most restrictive applicable posture until policy and review say otherwise.

[Back to top](#top)

---

## Required test families

All families below remain `PROPOSED` until executable files, collection output, logs, and CI evidence exist.

| Test family | Minimum proof | Required negative case |
|---|---|---|
| Import and smoke | Package imports without network, credentials, file writes, environment mutation, logging secrets, or registration side effects. | Import fails if it contacts a source, reads a credential, writes outside a temp directory, or changes global state. |
| Package metadata | Distribution/import assumptions are explicit and consistent with accepted packaging configuration. | Missing build/discovery configuration cannot be presented as installable maturity. |
| Descriptor shape | Accepted descriptor fixture validates against accepted schema and registry posture. | Current placeholder, missing fields, wrong role, unknown rights, permissive sensitivity, or unknown activation fails closed. |
| Activation gate | Explicit reviewed activation is required before an opt-in source client can run. | Missing, draft, denied, quarantined, retired, fixture-only, or unreviewed activation cannot contact a source. |
| Surface dispatch | Each record is routed to an explicit KHRI/KSHS surface and product family. | Unknown or mixed surface is held; no institutional umbrella fallback silently assigns meaning. |
| Source-role separation | Role is explicit and compatible with claim/candidate type. | Narrative `administrative` is not mapped by convenience; carrier/context cannot become original authority. |
| Record-meaning separation | Inventory, survey, evaluation, recommendation, designation, ownership, condition, and current existence remain distinct. | Any meaning upgrade without source and decision evidence fails. |
| Identity preservation | Stable upstream IDs, surface/product ID, version, source URI, and amendment/supersession references are preserved. | Missing or colliding identity is held; later retrieval does not overwrite history silently. |
| Temporal preservation | Historical, survey, decision, effective, retrieval, review, release, correction, and supersession times stay distinct. | Retrieval time substituted for survey/decision/effective time fails. |
| Crosswalk behavior | Source-native resource, type, status, program, person, and place values survive unresolved mappings. | Unknown crosswalk does not disappear or become a guessed canonical value. |
| Geometry and uncertainty | Native geometry, CRS/datum, method, precision, derivation, uncertainty, withholding, and transform state are preserved. | False precision, unsafe exact location, coordinate swap, undocumented centroid, or reconstructable geometry fails. |
| Rights and terms | Rights, attribution, redistribution, retention, media, disclaimer, and permitted use are explicit. | Unknown, noassertion, denied, expired, or contradictory rights block activation and public output. |
| Cultural sensitivity and sovereignty | Cultural/steward review, sovereignty context, exact-location policy, and withheld fields are enforced. | Missing review, sacred/burial/human-remains context, or unsafe location denies public output. |
| Privacy and private property | Historical/living-person status and private-property fields are distinguished and minimized. | Historical owner/occupant cannot become current contact, residence, title, or access truth. |
| Attachment and media | Attachments are referenced safely with rights/sensitivity metadata and no implicit download/publish. | Restricted image, form, plan, scan, or report cannot enter fixture/log/artifact output. |
| Parsing and normalization | Source-native values and qualifiers are retained; normalized candidate is deterministic. | Unknown fields or values do not disappear silently or become guessed meanings. |
| Failure outcomes | Unsafe or incomplete input returns a finite result and stable reason codes. | No implicit success, empty-success object, warning-only promotion, or permissive fallback. |
| Handoff boundary | Candidate remains caller-owned and routes only through accepted orchestration. | Package/test code cannot write directly to RAW, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, proof, receipt, or release roots. |
| No-publication | No map, tile, API response, catalog record, evidence claim, release manifest, report, citation, or public export is created. | Any publication-like side effect fails. |
| Migration and compatibility | Accepted winning-path behavior and aliases are explicit and time-bounded. | Current or proposed path cannot declare canonicality or create a second evolving implementation. |
| Determinism | Same fixture, descriptor, config, clock, and policy inputs yield identical candidate and reasons. | Hidden current time, random IDs, network state, machine paths, or unordered serialization causes failure. |

[Back to top](#top)

---

## No-network and side-effect contract

Default local and CI tests must run with network unavailable or actively denied.

### Required assertions

- Importing the package performs no HTTP, DNS, socket, subprocess, browser, credential, registry, or cloud-client action.
- Tests do not read the user's home directory, keychain, browser profile, shell history, cloud configuration, or secret manager.
- Tests use caller-provided temporary directories and do not write to repository lifecycle or authority roots.
- Environment variables are explicit test inputs; no production credential variable is required.
- Time, UUID generation, randomness, locale, timezone, and filesystem paths are controlled where they affect output.
- Logs, traces, snapshots, exception messages, and CI artifacts are safe to preserve.
- Any future live-source probe is opt-in, separately reviewed, rate-limited, terms-aware, credential-safe, culturally reviewed, auditable, and excluded from required default CI.

### Network-denial test

At least one test must fail deliberately when code attempts a network operation. A suite that simply does not happen to use the network is weaker than a suite that proves network access is blocked.

[Back to top](#top)

---

## Descriptor, role, and activation tests

The connector-local `descriptor.yaml` is a migration placeholder, not a valid activation basis.

Future tests must prove that:

1. the accepted descriptor resolves from the accepted registry/control-plane path;
2. `object_type`, schema version, stable source ID, descriptor version, product/surface scope, source type, source role, authority, publisher/steward, rights, sensitivity, cadence, access, citation, source head, admissibility limits, review, activation, lifecycle, and public-release posture satisfy the accepted schema and policy;
3. legacy aliases are rejected or migrated intentionally rather than treated as canonical new fields;
4. one institutional umbrella descriptor cannot silently authorize every KSHS surface or KHRI product;
5. narrative `administrative` language cannot be mapped to a current machine role without an accepted crosswalk;
6. unknown rights, unresolved cultural sensitivity, missing source role, missing product scope, missing review, or missing activation fails closed;
7. fixture-only descriptors can never authorize real source access or public claims;
8. connector code cannot upgrade authority, role, rights, sensitivity, review, activation, evidence, or release state.

### Required placeholder rejection

A negative fixture equivalent to this local placeholder must fail:

```yaml
name: khri
role: TBD
rights: TBD
sensitivity_floor: public
```

The failure should identify unresolved stable source identity, surface/product scope, source type/role, authority, rights, sensitivity/cultural review, cadence, access, citation, source head, admissibility, activation, lifecycle, and schema conformance without logging restricted values.

[Back to top](#top)

---

## Rights, cultural sensitivity, privacy, and geometry tests

### Rights

Tests must distinguish at least:

- verified open use within stated limits;
- verified restricted use;
- permission required;
- unknown or no assertion;
- denied or expired use.

Unknown or denied rights must force public release false and prevent live activation unless a separately governed restricted workflow explicitly permits access.

Tests must cover rights for:

- metadata text;
- photographs and scans;
- survey forms and reports;
- nomination or evaluation documents;
- plans, maps, GIS packages, and attachments;
- cached responses and downloaded files;
- fixture reuse, redistribution, quotations, and screenshots.

### Cultural sensitivity and sovereignty

Tests must cover:

- public-safe administrative metadata with no sensitive payload;
- restricted or steward-controlled records;
- archaeological, sacred, burial-associated, human-remains, traditional-cultural, or collection-security contexts;
- records requiring tribal, cultural, SHPO, property-owner, or other steward review;
- withheld, null, generalized, or transformed geometry;
- a public derivative whose transform and redaction receipt are absent.

The last case must fail. A candidate is not public-safe merely because sensitive fields were omitted informally.

### Privacy and private property

Tests must distinguish:

- historical person association from living-person data;
- historical owner/occupant from current owner, contact, resident, or titleholder;
- historic address from current residence, parcel identity, or access route;
- public record availability from permission to aggregate or republish;
- property geometry from cultural-resource geometry;
- source reference from disclosure of private or restricted content.

### Geometry

Tests must preserve and validate:

- native geometry type;
- source CRS and datum;
- coordinate method or derivation;
- observed, digitized, inferred, generalized, centroided, buffered, withheld, or null state;
- precision and uncertainty;
- geometry vintage and source feature identity;
- transform/generalization identity and reviewer state;
- public versus steward-only geometry separation.

Tests must reject false precision, undocumented centroiding, coordinate swaps, invalid ranges, missing datum where material, unsafe parcel alignment, and joins that reconstruct withheld locations.

[Back to top](#top)

---

## Identity, time, correction, and crosswalk tests

### Identity

Tests must preserve:

- KHRI/KSHS surface identity;
- source/product identifiers;
- inventory/resource identifiers;
- survey, evaluation, nomination, decision, attachment, and media identifiers;
- source URI and retrieval identity;
- version, revision, amendment, correction, withdrawal, and supersession relationships;
- cross-source join keys with per-attribute provenance.

### Time

Tests must keep distinct:

- resource construction or historical period;
- survey/fieldwork time;
- evaluation/recommendation time;
- nomination/decision time;
- effective/expiration time;
- source publication/update time;
- retrieval time;
- review time;
- release time;
- correction, withdrawal, and supersession time.

A missing time-kind may require hold or abstention. Retrieval time must never silently replace the time of the underlying historical, survey, legal, or administrative event.

### Crosswalks

Tests must preserve source-native values and version the crosswalk used for:

- resource type and subtype;
- survey/evaluation status;
- eligibility, recommendation, designation, and program status;
- place, district, parcel, person, organization, and authority identifiers;
- KHRI ↔ NRHP and other program relationships;
- KHRI/KSHS ↔ external place, archival, property, or knowledge-graph anchors.

An unresolved crosswalk must preserve the source value and yield hold/abstain rather than a guessed canonical identity.

[Back to top](#top)

---

## Lifecycle and output boundary tests

The package may eventually return caller-owned candidates. It must not own lifecycle persistence or promotion.

| Attempted behavior | Required result |
|---|---|
| Return validated in-memory bytes/record/candidate with explicit reasons | Allowed after implementation and accepted contracts exist. |
| Write directly to `data/raw/` | Fail unless an accepted external orchestrator owns the write and the package only returns the candidate. |
| Write directly to `data/quarantine/` | Same boundary: orchestration owns persistence; package returns disposition and reasons. |
| Write to `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/`, proofs, receipts, registry, rollback, or `release/` | Fail. |
| Create a public map, tile, API payload, report, summary, citation, alert, export, or AI answer | Fail. |
| Treat a commit, PR, merge, green workflow, copied file, or path move as promotion | Fail. |
| Continue after missing descriptor, rights, sensitivity, cultural review, role, identity, geometry, or review state | Hold, quarantine, deny, abstain, or error with deterministic reasons. |

Temporary files used within a test must stay under the test-owned temporary directory and be removed or retained only as explicit safe CI artifacts.

[Back to top](#top)

---

## Migration and routing tests

The repository contains a top-level KHRI package scaffold, while source documentation names a Kansas-family KHRI location that was not established at current named probes. Final package placement, compatibility class, fixture home, and test routing remain unresolved.

Future migration tests should prove:

- one accepted implementation home and one documented compatibility policy;
- an explicit class for the losing path: legacy, mirror, deprecated, external-export, transitional, redirect-only, retained, or removed;
- no duplicate live client, descriptor, credential, activation, fixture corpus, test suite, source-head state, receipt lineage, or correction history across paths;
- import aliases are explicit, deprecation-warned, versioned, and removed through a documented schedule;
- source IDs, product IDs, and public references do not change silently with a path move;
- registry, policy, test, fixture, workflow, documentation, and consumer references migrate together;
- rollback restores a coherent prior state without force-pushing or rewriting shared history.

Directory presence, dossier wording, or the word “canonical” in an older README is not sufficient migration evidence.

[Back to top](#top)

---

## Failure contract

Unsafe or incomplete input must produce one finite, inspectable outcome.

| Outcome | Test meaning |
|---|---|
| `HOLD` | Candidate is structurally parseable but lacks required governance, mapping, or review state. |
| `QUARANTINE` | Candidate may be useful but cannot safely advance; reasons are recorded. |
| `DENY` | Requested access, transform, exposure, or use is prohibited. |
| `ABSTAIN` | Evidence, identity, mapping, temporal/spatial support, or authority is insufficient for the requested interpretation. |
| `ERROR` | Deterministic contract, transport, parse, or operational failure; no permissive fallback. |

The exact enum and envelope contract remain `NEEDS VERIFICATION`. Tests must use the accepted shared contract rather than inventing incompatible local vocabulary.

Every failure result should carry:

- stable reason code;
- safe human-readable explanation;
- affected field or gate without leaking restricted content;
- source/product/descriptor reference when safe;
- retryability or remediation class;
- no partial public output;
- no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation matrix

| Condition | Required result |
|---|---|
| Zero executable tests discovered after the suite is implemented | Fail CI. |
| Required negative test skipped or xfailed without accepted issue/expiry | Fail or require an explicit governed waiver. |
| Package import attempts network, credentials, subprocess, browser, or write | Fail. |
| Local placeholder descriptor used as activation basis | Fail. |
| SourceDescriptor missing or unresolved | Hold/quarantine/deny; no source access. |
| Activation missing, draft, denied, retired, quarantined, fixture-only, or unreviewed | No source access. |
| Unknown or denied rights | No persistence/public output; fail closed. |
| Unknown cultural sensitivity, sovereignty, privacy, or reviewer state | No public output; hold or deny. |
| Missing surface/product family or source role | Hold/quarantine; no institutional umbrella fallback. |
| Narrative `administrative` mapped by convenience | Fail pending accepted crosswalk. |
| KHRI record collapsed into Kansas Memory or State Archives | Fail. |
| Inventory presence treated as legal designation | Fail. |
| Eligibility/recommendation treated as listed/designated status | Fail. |
| Historical owner/occupant treated as current person/title truth | Fail. |
| Address treated as parcel, residence, exact resource geometry, or access permission | Fail. |
| Historical condition/use treated as current condition | Fail or abstain. |
| Unresolved resource/status/person/place crosswalk | Preserve source value and hold/abstain. |
| Retrieval time substituted for survey/decision/effective time | Fail. |
| Invalid, false-precision, or reconstructable sensitive geometry | Fail or quarantine. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Fixture, attachment, log, snapshot, or artifact leaks restricted material | Fail. |
| Output writes to repository lifecycle/authority roots | Fail. |
| Test or package creates map, API, evidence, catalog, release, or public artifact | Fail. |
| Current or proposed path declares canonicality without accepted migration | Fail migration test. |
| Same controlled inputs produce non-deterministic candidate/reasons | Fail. |
| Workflow only echoes TODO and no substantive test command runs | Do not count as implementation proof; fail readiness review. |

[Back to top](#top)

---

## CI and observability

### Current limitation

The inspected `connector-gate` and `source-descriptor-validate` workflows contain TODO echo steps. Their successful execution cannot prove:

- package installation or import;
- test collection or discovered count;
- parser, normalizer, or admission behavior;
- descriptor conformance or role crosswalks;
- network denial;
- rights, cultural-sensitivity, sovereignty, privacy, or geometry enforcement;
- attachment and log safety;
- lifecycle side-effect prevention;
- package migration safety;
- source activation or release readiness.

### Future minimum CI evidence

A substantive test job should report:

- exact environment and dependency-lock identity;
- exact test command;
- collected, passed, failed, skipped, and xfailed counts;
- proof that zero discovery fails;
- proof that required negative cases ran;
- network-denial configuration;
- safe fixture inventory, provenance, review state, and hashes;
- coverage only after meaningful code exists;
- deterministic failure reason codes;
- no secret, private, cultural, or sensitive-location leakage in logs and artifacts;
- commit and package/config identity.

Coverage percentage alone is not readiness. A small negative-first suite with strong boundary assertions is more valuable than broad shallow execution over placeholder code.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior `connectors/khri/tests/README.md` blob | **CONFIRMED** | Existing v0.1 test documentation and exact rollback target. | Executable tests or passing coverage. |
| Current named test/fixture probes | **CONFIRMED NOT FOUND AT NAMED PATHS** | `conftest.py`, `test_fetch.py`, `test_admit.py`, `test_descriptor.py`, and `tests/fixtures/README.md` are not established at those paths. | Absence of differently named/generated files. |
| `connectors/khri/pyproject.toml` | **CONFIRMED** | Project name and `0.0.0` version. | Build system, installability, dependencies, entry points, or runtime. |
| Package files | **CONFIRMED** | Empty initializer, comment-only fetch/admit modules, and placeholder descriptor. | Supported connector behavior. |
| Merged source/package v0.2 READMEs | **CONFIRMED DOCUMENTATION** | Current package tree, absent helper probes, path conflict, record meanings, fail-closed boundaries, and proposed validation. | Executable implementation, coverage, activation, or release. |
| Parent connector README | **CONFIRMED v0.1 DOCUMENTATION** | Existing parent compatibility intent. | Current canonicality, completed migration, or package behavior. |
| KHRI source dossier | **CONFIRMED DRAFT DOCUMENTATION** | KSHS-operated per-surface framing, Kansas-first authority posture, product context, and placement intent. | Machine descriptor, current endpoint/terms, package migration, activation, or release. |
| KSHS umbrella dossier | **CONFIRMED DOCUMENTATION** | Institutional anti-collapse and need for surface-specific descriptors. | KHRI-specific runtime or test behavior. |
| Archaeology source-registry guide | **CONFIRMED DRAFT DOCTRINE/DOC PATH** | Deny-by-default exact cultural locations, role separation, cultural/steward review, and source-admission posture. | Implemented KHRI policy or machine registry records. |
| SourceDescriptor contract/schema | **CONFIRMED REPOSITORY SURFACES; STATUS PROPOSED** | Required field surface, deprecated aliases, machine role vocabulary, rights/sensitivity gates, and activation states. | A conforming KHRI descriptor or one accepted canonical schema path. |
| Source-authority register | **CONFIRMED EMPTY IN REVIEWED EVIDENCE** | No established machine authority entry at the inspected register. | That no authority evidence exists elsewhere. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY** | Workflow scaffolding. | Package import, test collection, descriptor conformance, rights review, cultural enforcement, or substantive CI. |
| Directory Rules | **CONFIRMED PLACEMENT DOCTRINE** | Responsibility roots, lifecycle invariant, compatibility discipline, fixtures/tests separation, migration, and no-parallel-authority rules. | Resolution of current package, test, role, and fixture conflicts. |

No live KHRI endpoint, source payload, current terms page, credential, runtime log, deployed service, EvidenceBundle, release manifest, or public client was inspected for this documentation update.

[Back to top](#top)

---

## Review burden

Before executable tests or fixtures are accepted, review should include:

| Reviewer role | Required review focus |
|---|---|
| Connector/package maintainer | Package API, import behavior, side effects, determinism, dependency posture, and migration compatibility. |
| Test/validation steward | Collection, zero-discovery failure, negative cases, reason codes, no-side-effect assertions, safe fixtures, and substantive CI. |
| Kansas/KHRI source steward | Surface/product inventory, source identity, current access method, cadence, corrections, and source-native fields. |
| KSHS/SHPO liaison | Institutional boundaries, inventory/survey/evaluation/designation semantics, stewardship, and official-source context. |
| Archaeology/cultural-review steward | Exact locations, sacred/burial/human-remains contexts, sovereignty, consultation, collection security, and redaction. |
| Settlements/historic-resources steward | Resource types, districts, built-environment semantics, place/time interpretation, and current-condition limits. |
| People/privacy reviewer | Historical versus living-person fields, residences, private contacts, ownership/occupancy ambiguity, and joins. |
| Rights reviewer | Terms, attribution, redistribution, retention, media, attachments, fixtures, quotations, and public derivatives. |
| Sensitivity reviewer | Public geometry, private property, cultural places, sensitive facilities, joins, logs, snapshots, and fixture safety. |
| Security reviewer | Network/credential posture, retries, request logging, parsers, archives/media, dependencies, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor, candidate, receipt, failure, and role-crosswalk shapes. |
| Migration/architecture reviewer | Winning path, imports, source IDs, test/fixture routing, deprecation, history, backlinks, and rollback. |

Exact individual owners or GitHub teams remain `UNKNOWN`; do not invent assignments.

[Back to top](#top)

---

## Definition of done

### Documentation revision

- [x] Current README-only test-lane maturity is explicit.
- [x] Current named test/fixture absence is bounded rather than overgeneralized.
- [x] Adjacent `0.0.0` package scaffold and invalid descriptor are recorded.
- [x] Merged v0.2 package/source boundaries are incorporated.
- [x] Stale parent canonicality wording is not ratified.
- [x] Directory Rules responsibility boundaries are preserved.
- [x] KHRI/KSHS surface and record-meaning anti-collapse rules are explicit.
- [x] Rights, cultural sensitivity, sovereignty, privacy, geometry, time, attachment, fixture, join, lifecycle, and migration controls fail closed.
- [x] CI limitations and TODO-only workflow posture are explicit.
- [x] Rollback uses an exact prior blob and transparent history.

### Executable test readiness remains open

- [ ] Accepted package path, test path, fixture home, compatibility class, product topology, source IDs, and migration plan.
- [ ] Accepted SourceDescriptor contract/schema/validator authority, role crosswalk, and conforming KHRI product descriptors.
- [ ] Current source access, terms, attribution, redistribution, retention, cadence, rate/size limits, correction, and source-head behavior.
- [ ] Safe reviewed fixtures with provenance, rights, privacy, cultural-sensitivity, and geometry controls.
- [ ] Import/network/descriptor/role/surface/meaning/identity/time/crosswalk/geometry/rights/cultural/privacy/attachment/lifecycle/migration negative tests.
- [ ] Exact test command, non-zero collected count, logs, substantive CI, owners, and review records.
- [ ] Demonstrated failure when a required boundary is removed or made permissive.

Documentation readiness does not imply executable coverage, connector readiness, source admission, activation, rights clearance, cultural/sensitivity clearance, evidence closure, release approval, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim executable coverage, package readiness, source authority, live access, activation, rights or cultural-sensitivity clearance, safe exact-location exposure, canonical-path resolution, lifecycle authority, evidence closure, or release readiness.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
2e8225eac2d244ac073bee3c2655f84de6f688cc
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, sensitivity, test-discovery, and rollback checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive inventory of `connectors/khri/tests/` | **UNKNOWN** | Mounted checkout or non-truncated tree receipt at reviewed commit. |
| Differently named or generated test-file presence | **UNKNOWN** | Direct reads and test collection output. |
| Final package and test home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import/source-ID plan, deprecation, and rollback. |
| Compatibility class of `connectors/khri/` | **CONFLICTED / NEEDS VERIFICATION** | Accepted legacy/mirror/redirect/transitional/retained decision. |
| Existence and role of `connectors/kansas/khri/` | **NOT ESTABLISHED AT NAMED PROBES** | Current tree evidence and accepted placement/migration record. |
| Root `tests/` versus connector-local test routing | **CONFLICTED / NEEDS VERIFICATION** | Directory Rules application, repository convention, and accepted test architecture. |
| Fixture home and fixture receipt model | **CONFLICTED / NEEDS VERIFICATION** | Accepted fixture registry, rights/privacy/cultural review, and test configuration. |
| KHRI product/surface topology | **NEEDS VERIFICATION** | Accepted inventory of portal/search, survey, evaluation, designation, attachment, geometry, and restricted products. |
| SourceDescriptor schema and validator authority | **CONFLICTED / PROPOSED** | One accepted contract/schema, migration, fixtures, validator, and CI command. |
| `administrative` narrative-to-machine role mapping | **CONFLICTED** | Accepted role vocabulary/crosswalk and negative tests. |
| Product descriptors and source-authority entries | **NOT ESTABLISHED** | Conforming records and reviewed registry/control-plane entries. |
| Activation decisions and source-head evidence | **NOT ESTABLISHED** | Reviewed activation records and approved source-head observations. |
| Current access surfaces, endpoints, product schemas, and cadence | **NEEDS VERIFICATION** | Current authoritative KSHS/KHRI documentation and source-steward review. |
| Current rights, attribution, redistribution, media, retention, and disclaimers | **NEEDS VERIFICATION** | Current terms and signed rights review. |
| Cultural sensitivity, sovereignty, privacy, public geometry, redaction, and joins | **NEEDS VERIFICATION** | Policy, transform profiles, fixtures, receipts, tests, and reviewer decisions. |
| Resource, survey, eligibility, designation, ownership, condition, and crosswalk semantics | **NEEDS VERIFICATION** | Product contracts, source examples, mappings, and source/domain review. |
| Executable package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Code, packaging, imports, tests, and logs. |
| Test collection and coverage | **NOT ESTABLISHED** | Test runner, exact command, collection output, logs, and negative cases. |
| Substantive connector CI | **NOT ESTABLISHED** | Real workflow commands, logs, and demonstrated negative failure. |
| Owners and review routing | **UNKNOWN** | Accepted CODEOWNERS or ownership register. |
| Repository-wide promotion prerequisites | **NEEDS VERIFICATION** | Trusted workflow results and required doctrine/release artifacts. |

[Back to top](#top)

---

## Maintainer note

Keep this lane negative-first, culturally safe, deterministic, and evidence-bounded.

The safest progression is:

1. settle package path, test path, fixture home, compatibility class, product/source IDs, descriptor authority, role vocabulary, and migration routing;
2. add one invented invalid descriptor fixture with no real person, property, resource, coordinate, attachment, endpoint, credential, or source payload;
3. prove import and network denial;
4. prove one deterministic fail-closed disposition with no side effects;
5. add surface/meaning, rights, cultural-sensitivity, privacy, identity, time, geometry, attachment, join, and migration negatives;
6. make zero discovery and unexpected skips fail substantive CI;
7. only then consider a reviewed, opt-in source probe.

A larger suite is not better if it masks zero discovery, uses unsafe fixtures, accepts permissive placeholders, or tests generated output as though it were source truth.

[Back to top](#top)
