<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kcc-oil-gas-reg-readme
title: connectors/kcc_oil_gas_reg/ — KCC Oil and Gas Regulatory Connector Compatibility Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas source steward · Geology steward · Environment steward · Infrastructure steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Contract/schema reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; compatibility-path; readme-only; noncanonical-path; path-conflict; source-role-conflict; regulatory-records; source-admission; no-network; fail-closed; no-activation; no-publication
current_path: connectors/kcc_oil_gas_reg/README.md
truth_posture: CONFIRMED README-only at indexed and named conventional probes, absent proposed Kansas child, absent named KCC descriptor/test/fixture paths, empty source-authority register, placeholder KCC terms policy, and TODO-only connector workflows / CONFLICTED final connector path, source ID, role vocabulary, SourceDescriptor schema and registry topology, fixture home, and test routing / PROPOSED fail-closed compatibility boundary and future candidate contract / UNKNOWN differently named files, package runtime, live source access, current terms, activation, deployment, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 40deb4a3cab0972f0c7d38930e30c3b497408b0a
  prior_blob: b54ea424e69a76b42e607ac395b831bf3c22e4ab
  readme_introduction_commit: 0e27beb861bacaf5965b974b001046040c689ff2
related:
  - ../README.md
  - ../geology/README.md
  - ../kansas/README.md
  - ../kgs_oil_gas_wells/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/sources/source-roles.md
  - ../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../data/registry/sources/source_type_registry.v1.yaml
  - ../../data/registry/sources/geology/README.md
  - ../../data/registry/geology/sources/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/domains/geology/rights/kcc_terms.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../release/README.md
tags: [kfm, connectors, kcc, oil-gas, regulatory-records, kansas, geology, environment, infrastructure, compatibility, path-conflict, source-role, rights, sensitivity, plss, wells, permits, uic, enforcement, no-network, raw, quarantine, governance]
notes:
  - "The current top-level lane is README-only at the indexed and named conventional paths inspected for this revision; no package metadata, source tree, importable module, connector-local test README, named root test, or fixture README was found."
  - "The source-catalog page proposes connectors/kansas/kcc-oil-gas-reg/, but the exact target README is absent at the pinned base; the Kansas parent and Geology connector index therefore treat final KCC placement as unresolved rather than confirmed."
  - "Geology source doctrine uses the role label regulatory, while the current SourceDescriptor contract, populated schema, source-type registry, and general source-role guide use regulatory_context. This README records the conflict and does not select or translate an enum by convenience."
  - "No KCC SourceDescriptor instance was found at the named subtype-first or domain-first registry candidate paths. The machine source-authority register has entries: [], and the KCC terms file is a PROPOSED placeholder."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; a green run proves workflow execution only, not package imports, test discovery, descriptor conformance, rights review, activation, or connector behavior."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry record, contract, schema, policy, fixture, test, workflow, source payload, credential, activation decision, lifecycle object, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KCC Oil and Gas Regulatory Connector Compatibility Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current maturity:** `CONFIRMED` README-only compatibility lane at the inspected paths; executable connector behavior not established  
> **Placement posture:** final KCC connector path, slug, source ID, registry home, role vocabulary, fixture home, and test routing are `CONFLICTED / NEEDS VERIFICATION`  
> **Authority:** documentation for a source-admission compatibility boundary only; no source, schema, policy, lifecycle, evidence, release, regulatory-decision, or publication authority.

> [!WARNING]
> A KCC filing, permit, order, index entry, directory name, catalog page, placeholder policy, empty authority register, or green TODO-only workflow is not implementation or public-release evidence. Live source access and activation remain denied until placement, descriptor, rights, sensitivity, access, fixture, test, and review gates close.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-status) · [Placement](#placement-and-naming-conflict) · [Role conflict](#source-role-and-descriptor-conflict) · [Record boundaries](#regulatory-record-boundaries) · [Identity and time](#identity-time-geometry-and-joins) · [Rights](#rights-sensitivity-and-access) · [Lifecycle](#lifecycle-and-publication-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kcc_oil_gas_reg/` is the repository-present documentation lane for an unresolved KCC oil-and-gas regulatory connector path.

Its present responsibility is to:

- record the exact compatibility surface that exists;
- prevent a README-only directory from being mistaken for a working or canonical connector;
- preserve the distinction between regulatory records and physical, geological, production, environmental, legal-title, or operational claims;
- expose path, role, descriptor, registry, policy, fixture, and test conflicts before code is added;
- define fail-closed boundaries for rights, sensitivity, geometry, time, identity, and cross-source joins;
- preserve a reversible migration target while the repository chooses one accepted KCC connector topology.

This directory does not prove that the snake_case slug is final, that the proposed Kansas child exists, that a KCC source may be contacted, that any filing family is in scope, or that any KCC-derived record is safe to publish.

Directory Rules place source-specific fetch, probe, preservation, and admission mechanics under `connectors/`. Source catalog doctrine, source authority records, contracts, schemas, policy, evidence closure, lifecycle promotion, release, public APIs, maps, and generated explanations remain in their owning responsibility roots.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, and admission mechanics. |
| Current path | **CONFIRMED** | `connectors/kcc_oil_gas_reg/README.md` exists at the pinned base. |
| Current implementation | **NOT FOUND AT INDEXED OR NAMED CONVENTIONAL PROBES / OTHERWISE UNKNOWN** | No package metadata, source layout, importable module, connector-local tests, named root test, or fixture README was found at the paths listed below. |
| Final connector path | **CONFLICTED** | The live top-level path exists; the catalog proposes `connectors/kansas/kcc-oil-gas-reg/`; that child README is absent; current parent docs treat placement as unresolved. |
| Source identity | **CONFLICTED / NEEDS VERIFICATION** | `kcc_oil_gas_reg`, `kcc-oil-gas-reg`, and a final stable KFM source ID have not been reconciled by an accepted migration or descriptor. |
| Source role vocabulary | **CONFLICTED** | Geology doctrine uses `regulatory`; the current SourceDescriptor contract/schema and source-type registry use `regulatory_context`. |
| SourceDescriptor instance | **NOT FOUND AT NAMED CANDIDATE PATHS** | No KCC descriptor record was found under the named subtype-first or domain-first geology registry candidates. |
| Machine authority | **NOT ESTABLISHED** | The source-authority register is `PROPOSED` with `entries: []`; source-registry topology itself is conflicted. |
| Rights policy | **PLACEHOLDER** | `policy/domains/geology/rights/kcc_terms.yaml` is a proposed placeholder, not a current rights decision. |
| Executable tests and fixtures | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | No KCC-specific executable test or fixture contract was found at the probed paths. |
| Connector CI | **TODO-ONLY** | Connector and descriptor workflows execute `echo TODO ...`; success is not substantive coverage. |
| Source access and activation | **DENIED / NOT VERIFIED** | No reviewed descriptor, accepted access method, source head, rights review, sensitivity review, or activation decision was verified. |
| Public output | **NONE FROM THIS LANE** | This README emits no source payload, lifecycle record, evidence object, map, API response, release, or publication artifact. |

Editing this README does not ratify the current path, proposed child, source ID, role mapping, descriptor topology, filing scope, access method, rights posture, sensitivity posture, or release class.

[Back to top](#top)

---

## Current status

### Bounded repository snapshot

The directly inspected connector surface is:

```text
connectors/kcc_oil_gas_reg/
└── README.md                           # this compatibility boundary
```

Exact probes returned `Not Found` for:

```text
connectors/kcc_oil_gas_reg/pyproject.toml
connectors/kcc_oil_gas_reg/src/README.md
connectors/kcc_oil_gas_reg/tests/README.md
connectors/kcc_oil_gas_reg/src/kcc_oil_gas_reg/__init__.py
connectors/kcc_oil_gas_reg/src/kcc_oil_gas_reg/fetch.py
connectors/kansas/kcc-oil-gas-reg/README.md

data/registry/sources/geology/kcc-oil-gas-reg.yaml
data/registry/sources/geology/kcc_oil_gas_reg.yaml
data/registry/geology/sources/kcc-oil-gas-reg.yaml
data/registry/geology/sources/kcc_oil_gas_reg.yaml

tests/connectors/kcc_oil_gas_reg/README.md
tests/connectors/kcc_oil_gas_reg/test_descriptor.py
tests/domains/geology/test_kcc_source_role.py
fixtures/domains/geology/kcc_oil_gas_reg/README.md
```

These absence statements are bounded to the pinned commit, indexed search, and exact named probes. Differently named, generated, unindexed, or newly concurrent files remain `UNKNOWN`.

### Current dependency posture

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| KCC source-catalog page | Draft human-facing product page; proposes a Kansas child and describes regulatory semantics. | Useful doctrine and migration input; not machine authority, path-presence proof, rights approval, or activation. |
| Geology source registry docs | Use a seven-role vocabulary containing `regulatory`. | Human/domain doctrine; field names are described as illustrative. |
| SourceDescriptor contract/schema | Current populated schema uses `source_type: regulatory_record` and `source_role: regulatory_context`; schema status is `PROPOSED`. | Machine-shape evidence for the current populated schema, but not an accepted resolution of the domain vocabulary conflict. |
| General source-role guide | Defines “Regulatory context” and forbids treating it as physical observation. | Supports anti-collapse semantics; not a KCC descriptor instance. |
| Source-type registry | `PROPOSED` companion registry; uses `regulatory_record` and `regulatory_context`. | Supports current controlled vocabulary, not activation. |
| Source registry | Both `data/registry/sources/geology/` and `data/registry/geology/sources/` exist as documented candidates. | Do not duplicate KCC descriptor authority across both lanes. |
| Source-authority register | `PROPOSED`; `entries: []`. | No KCC machine-authority entry is established. |
| KCC terms policy | Placeholder created from a docs inventory. | No current license, redistribution, attribution, disclaimer, access, or release decision. |
| Connector workflows | TODO echo steps. | A green run cannot establish connector behavior or descriptor validity. |

[Back to top](#top)

---

## What belongs here

### Current allowed content

Until an accepted path and migration decision exists, this directory should remain documentation-only:

- compatibility and migration notes;
- bounded repository evidence about the current path;
- links to source catalog, contracts, schemas, registry, policy, and peer-source documentation;
- explicit path, source-ID, role-vocabulary, rights, sensitivity, and test conflicts;
- deprecation, redirect, or losing-path instructions after those are accepted;
- rollback instructions that restore the previous README without rewriting history.

### Future allowed content only after a placement decision

If an accepted ADR or migration retains this path as the implementation lane, it may then host narrowly scoped source-admission mechanics such as:

- explicit opt-in transport clients with no-network import and default-test behavior;
- parsers that preserve source-native filing, docket, permit, decision, status, amendment, and upstream identifiers;
- source-head and checksum helpers;
- pure validation and candidate-envelope builders;
- deterministic finite outcomes and stable reason codes;
- package-local tests for behavior owned by the retained package;
- migration shims with ownership, warnings, sunset criteria, tests, and rollback.

A README, source-catalog proposal, or existing folder is not sufficient authority to begin that implementation.

## What does not belong here

This directory must not contain or imply authority over:

- canonical connector placement, source ID, source role, source rights, source sensitivity, or activation;
- SourceDescriptor records, machine source-authority entries, contracts, schemas, policies, or release decisions;
- bulk source downloads, filing archives, docket corpora, PDF caches, database exports, production tables, well datasets, or unreviewed upstream samples;
- credentials, cookies, authorization headers, account details, signed URLs, private endpoints, or secrets;
- regulatory decisions authored by KFM, legal advice, title truth, current operational status, emergency guidance, life-safety advice, drilling guidance, reservoir conclusions, aquifer-safety conclusions, or investment guidance;
- a claim that a permit proves drilling, completion, operation, injection, production, compliance in the field, or subsurface occurrence;
- a claim that reported production is automatically KGS observation, reserve, forecast, or per-place geological truth;
- real private-owner, royalty-owner, residence, parcel, non-public business, or harmful infrastructure joins in fixtures, logs, examples, or generated output;
- network access on import, installation, default tests, or documentation rendering;
- direct writes to RAW, QUARANTINE, WORK, PROCESSED, CATALOG, TRIPLET, proof, release, rollback, or PUBLISHED stores from package helpers;
- EvidenceBundle closure, proof generation, catalog closure, promotion, correction, withdrawal, supersession, rollback, or public release;
- generated text, maps, tiles, dashboards, indexes, or graph edges presented as KCC or KFM sovereign truth.

Public availability upstream is not equivalent to KFM rights clearance, sensitivity clearance, evidence closure, or release approval.

[Back to top](#top)

---

## Inputs and outputs

### Current

The inspected directory declares no supported function, class, command, endpoint, configuration contract, credential variable, descriptor reference, fixture shape, runner, or output envelope.

It emits no response bytes, parsed record, validation result, decision, candidate, receipt, lifecycle write, map artifact, API payload, or public claim.

### Future admissible inputs

Only after placement, descriptor, review, and activation decisions are accepted, a retained connector may consume:

- a conforming, reviewed, product- or filing-family-specific SourceDescriptor reference;
- an explicit activation decision and approved access configuration;
- caller-supplied bytes, files, metadata, or an explicitly reviewed transport result;
- source, filing-family, record, docket, permit, operator, lease, well, or other upstream identity as actually supplied by the source;
- source-head evidence, retrieval time, run identity, and destination intent;
- rights, attribution, disclaimer, redistribution, sensitivity, geometry, coordinate derivation, uncertainty, temporal, review, correction, and supersession context;
- compact synthetic or explicitly rights-cleared fixtures.

### Future allowed outputs

A retained connector may return in-memory, caller-owned parsed records, preservation findings, validation findings, and explicit outcomes such as:

```text
admit-candidate
hold/quarantine-candidate
deny
abstain
no-op
rate-limit
error
```

Caller-owned orchestration chooses whether and where to persist an accepted candidate. The connector must not select lifecycle sinks, mint authoritative receipts, close evidence, approve release, or publish.

[Back to top](#top)

---

## Placement and naming conflict

| Surface | Current evidence | Safe posture |
|---|---|---|
| `connectors/kcc_oil_gas_reg/` | Present; README-only at the inspected conventional paths. | **Compatibility evidence / final status unresolved.** Presence does not establish canonicality. |
| `connectors/kansas/` | Present Kansas source-family coordination lane. | **Family placement present / child topology provisional.** |
| `connectors/kansas/kcc-oil-gas-reg/` | Proposed by the KCC catalog; exact README probe returned `404`. | **PROPOSED / NOT PRESENT AT PINNED BASE.** |
| `connectors/geology/` | Documentation-only compatibility index; rejects domain-scoped source implementations. | **Not a KCC implementation home.** |
| `connectors/kgs_oil_gas_wells/` | Present KGS wells/production compatibility lane. | **Peer-source migration evidence, not KCC authority.** |
| `docs/sources/catalog/kansas/kcc-oil-gas-reg.md` | Draft human-facing page; records OPEN-KCC-01 path migration. | **Doctrine input / open migration item, not an accepted path decision.** |
| Registry paths | Both subtype-first and domain-first Geology source-registry lanes exist. | **CONFLICTED topology; no duplicate KCC descriptor sets.** |

A final migration decision must cover:

- `kcc_oil_gas_reg` versus `kcc-oil-gas-reg` naming;
- final parent path and losing-path disposition;
- distribution/import name if a package is introduced;
- stable source ID and filing-family identity;
- descriptor and authority-register placement;
- source-role vocabulary and compatibility mapping;
- fixture and test routing;
- credential and access configuration ownership;
- RAW/QUARANTINE candidate routing and receipt ownership;
- KCC × KGS crosswalks and per-attribute provenance;
- inbound links, history, deprecation, correction, supersession, and rollback.

Until that scope is accepted, operational implementation here remains `PROPOSED / FROZEN`.

[Back to top](#top)

---

## Source role and descriptor conflict

The repository currently carries two related but non-identical vocabularies.

| Surface | Current term | Current posture |
|---|---|---|
| KCC source-catalog page | `regulatory` | Draft domain/source prose. |
| Geology Source Registry | `regulatory` | Seven-role geology doctrine; descriptor field surface is explicitly illustrative. |
| General source-role guide | “Regulatory context” | Human-readable source-governance semantics. |
| SourceDescriptor contract | `regulatory_context` | Current contract vocabulary; schema status remains `PROPOSED`. |
| Populated SourceDescriptor schema | `regulatory_context` | Machine enum in the currently populated singular-path schema. |
| Source Type Registry v1 | `regulatory_context` | `PROPOSED` companion registry. |
| KCC SourceDescriptor instance | Not found at named candidate paths | No accepted record resolves the vocabulary for KCC. |

The semantic agreement is strong: KCC material may support regulatory or administrative context within its jurisdiction and time scope; it must not become independent physical observation or geology truth.

The machine mapping is not settled. This README therefore must not:

- write `source_role: regulatory` into a descriptor that the current schema would reject;
- silently rewrite every domain reference to `regulatory_context`;
- create a local alias or translation layer without contract/schema review;
- infer that `regulatory_context` allows legal-title, physical-operation, safety, environmental-impact, or subsurface claims;
- treat a passing empty or permissive schema as approval.

A future accepted implementation should either align the domain vocabulary with the contract enum or publish an explicit, tested compatibility mapping. That decision belongs with source, contract/schema, policy, and affected domain stewards.

[Back to top](#top)

---

## Regulatory record boundaries

The filing-family inventory itself remains `NEEDS VERIFICATION`. If the following families are admitted, their claim boundaries must remain explicit.

| Candidate record family | May support, within descriptor limits | Must not prove by itself |
|---|---|---|
| Permit, application, or authorization | That an identified application or agency decision exists, with recorded status and dates. | That drilling, completion, operation, injection, production, or compliance occurred in the field. |
| Operator, lease, or administrative filing | That a party submitted or was recorded in an administrative relationship at a stated time. | Legal title, beneficial ownership, royalty ownership, current operations, or non-public business truth. |
| Plugging or compliance filing | That a filing, order, inspection result, or agency status was recorded. | Independent field verification, permanent physical condition, or absence of environmental impact without separate evidence. |
| UIC authorization or related filing | That an authorization or regulatory condition was recorded. | Current injection activity, aquifer safety, groundwater quality, engineering fitness, or absence of risk. |
| Production report | That a reported value was filed for a stated reporting unit, period, and revision. | KGS observation, reserve, forecast, reservoir content, per-well truth, or investment-grade production truth without separate source support. |
| Enforcement action, order, or resolution | That a formal action or status was recorded within a jurisdiction and time scope. | Independent physical observation, complete incident history, current hazard status, or guilt beyond the record's legal scope. |
| Docket, index, or portal search result | Discovery and administrative routing to an upstream record. | Completeness, final decision state, full record content, or durable identity without source-native verification. |

KCC material must remain distinct from:

- KGS wells, production, maps, logs, or subsurface interpretation;
- KDHE environmental, water-quality, or disposal oversight records;
- KDA-DWR water-right or water-use records;
- land-title and ownership authority;
- operational notices and life-safety authorities;
- KFM-generated joins, summaries, maps, tiles, or model outputs.

[Back to top](#top)

---

## Identity time geometry and joins

### Identity

A future connector must preserve source-native identity rather than minting a convenient replacement. Where present, preserve:

- upstream system and record identifiers;
- docket, case, permit, filing, order, enforcement, report, revision, and amendment identifiers;
- filing type and record class;
- operator, lease, well, facility, project, or other entity identifiers as supplied;
- direct upstream record URI or retrieval reference;
- source version, source head, content digest, and retrieval event;
- supersession, amendment, withdrawal, correction, and status lineage.

No deterministic KFM identity recipe is approved by this README. Any normalized identifier must be documented, collision-tested, source-role-aware, and reversible to the upstream identity.

### Time

Do not collapse:

```text
submitted / filed
received
issued / denied
effective
expires
amended
revoked / withdrawn
enforcement opened
enforcement resolved
reported period
retrieved
released
corrected / superseded
```

A filing date is not a decision date. A decision date is not an effective period. A reported period is not retrieval time. A portal's current display is not proof that no earlier or later amendment exists.

### Geometry and uncertainty

Current KCC CRS, datum, location method, PLSS use, coordinate precision, and public-geometry posture were not verified in this revision.

A future connector must:

- preserve source-native CRS and datum where supplied;
- distinguish source-supplied coordinates from geocoded, PLSS-derived, centroid, digitized, or transformed geometry;
- retain derivation method, resolution, uncertainty, and transform lineage;
- avoid invented precision;
- hold malformed, missing, internally inconsistent, or unexplained geometry;
- avoid deciding public precision inside connector code;
- route geometry requiring redaction, generalization, aggregation, or review to policy-owned downstream processing.

Do not assume every KCC record has geometry or that every point represents an observed physical position.

### Join-induced sensitivity

The most restrictive applicable posture governs a join. Hold or deny by default when KCC material is joined with:

- private owner, royalty-owner, residence, parcel, contact, or non-public business data;
- precise drinking-water, aquifer-vulnerability, private-well, or sensitive subsurface information;
- critical or security-relevant infrastructure detail;
- KGS records where a join would erase per-attribute source role or time;
- aggregates assigned to one well, parcel, operator, place, or person without support;
- uncertainty-bearing coordinates treated as surveyed precision.

[Back to top](#top)

---

## Rights sensitivity and access

No current KCC license, terms, attribution string, redistribution permission, disclaimer text, division identity, endpoint, access method, credential posture, filing-family inventory, cadence, rate limit, or source-head contract was verified in this revision.

The repository evidence currently supports only these conclusions:

- the KCC catalog page marks rights and current terms `NEEDS VERIFICATION`;
- the KCC terms policy file is a placeholder;
- the source-authority register contains no entries;
- no KCC descriptor or activation decision was found at the named candidate paths;
- no live source was contacted;
- unknown or unasserted rights must fail closed for public release under the current SourceDescriptor schema;
- sensitive or restricted posture requires review;
- upstream public access does not establish KFM redistribution, disclaimer, derivative, or release permission.

A future connector must never:

- embed credentials or private endpoints;
- infer open rights from a browsable portal;
- drop upstream attribution or use constraints;
- convert an unknown access method into an assumed REST API;
- treat a successful fetch as activation or release approval;
- decide that exact geometry, operator data, or joined records are public-safe;
- publish a not-for-life-safety or legal disclaimer as decoration without preserving its governed meaning.

[Back to top](#top)

---

## Lifecycle and publication boundary

Current lifecycle behavior is **none**. A future connector may return caller-owned candidates only.

```text
accepted product or filing-family SourceDescriptor
  + activation decision
  + approved access and policy context
    -> explicit opt-in fetch or caller-supplied bytes
    -> preserve source-native identity, role, time, geometry, rights, and disclaimer
    -> parse / validate / finite outcome
    -> return caller-owned candidate
    -> orchestration persists RAW, QUARANTINE, or receipt state
    -> downstream pipelines own WORK and PROCESSED
    -> evidence, catalog, triplet, policy, review, proof, and release gates
    -> PUBLISHED public-safe artifact
```

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a connector return value, successful request, file copy, Git commit, merged pull request, workflow completion, map render, search result, or generated explanation.

The connector cannot close an EvidenceBundle, approve a PolicyDecision, issue a ReleaseManifest, create legal or regulatory authority, or make KFM an official KCC channel.

[Back to top](#top)

---

## Validation

No package build, install, import test, fetch test, parser test, admission test, KCC descriptor validation, fixture run, source probe, or package-specific test command was verified.

Required future coverage includes:

1. importing or collecting tests causes no network, DNS, credential, filesystem, cache, registry, lifecycle, or publication side effect;
2. the current README-only directory cannot be reported as an active connector;
3. the proposed Kansas child is not treated as present or canonical without migration evidence;
4. missing, malformed, conflicted, unreviewed, or unactivated descriptors deny or hold access;
5. the `regulatory` versus `regulatory_context` vocabulary conflict cannot be resolved implicitly;
6. record family, filing type, source identity, source URI, upstream version, and amendment/supersession lineage are preserved;
7. permits, filings, reports, orders, and indexes cannot be upgraded into physical observation, geology, production, environmental-impact, title, safety, or operational claims;
8. submitted, decision, effective, expiry, reporting, enforcement, retrieval, release, and correction times remain distinct;
9. source-native CRS, datum, geometry method, derivation, uncertainty, and transform lineage remain explicit;
10. missing or unexplained geometry holds or quarantines rather than gaining invented precision;
11. unknown rights, access, attribution, redistribution, disclaimer, or sensitivity block live activation or public use;
12. sensitive joins fail closed and preserve per-attribute source and time;
13. package helpers cannot write lifecycle, evidence, catalog, triplet, proof, release, rollback, or publication state;
14. fixtures are compact, synthetic or rights-cleared, public-safe, source-labeled, and expected-outcome-labeled;
15. secrets, private endpoints, restricted payloads, private identities, and sensitive coordinates never appear in logs, errors, snapshots, examples, or committed fixtures;
16. CI runs an accepted command, reports discovered test count, and fails on zero discovery, TODO-only execution, or missing negative coverage.

| Condition | Required outcome |
|---|---|
| Current directory treated as implemented | **FAIL** |
| Proposed child treated as present without evidence | **FAIL** |
| Role vocabulary translated silently | **FAIL / HOLD** |
| Descriptor, authority entry, review, rights, sensitivity, or activation missing | **DENY** |
| Permit treated as drilling, completion, operation, injection, or production evidence | **FAIL / DENY** |
| Production filing treated as reserve, forecast, KGS observation, or per-place geology truth | **FAIL / DENY** |
| UIC authorization treated as aquifer safety or current injection status | **FAIL / DENY** |
| Filing time, decision time, effective time, and reporting period collapsed | **FAIL / HOLD** |
| Geometry method or uncertainty missing | **HOLD / QUARANTINE** |
| Sensitive owner, parcel, residence, infrastructure, or water-resource join lacks review | **DENY / QUARANTINE** |
| Unknown rights, attribution, redistribution, disclaimer, or access | **HOLD / DENY PUBLIC USE** |
| Default import or test contacts a live source | **FAIL** |
| Package writes beyond a caller-owned candidate | **FAIL** |
| Workflow only echoes TODO or discovers zero tests | **FAIL AS COVERAGE CLAIM** |
| Connector result treated as evidence closure, official decision, or publication | **FAIL / DENY** |

[Back to top](#top)

---

## Review burden

A README-only clarification needs connector/package or docs review plus source and validation review.

Any executable KCC work additionally needs:

- Kansas source and KCC source review;
- Geology review, with Environment and Infrastructure review where record scope or joins require it;
- contract/schema review for the role-vocabulary conflict and descriptor shape;
- registry/control-plane review for source ID, authority entry, activation, and topology;
- rights review for terms, attribution, redistribution, disclaimers, and source access;
- privacy/sensitivity and security review for precise location and cross-source joins;
- fixture/test and CI review;
- independent release authority for any release-affecting behavior.

Current CODEOWNERS supplies a repository-wide fallback but no KCC-specific owner. Named stewards and approvers remain `UNKNOWN`; do not invent them.

---

## Related folders

| Surface | Current relationship |
|---|---|
| [`../README.md`](../README.md) | Connector-root authority and source-admission boundary. |
| [`../geology/README.md`](../geology/README.md) | Current Geology compatibility index; records mixed KCC/KGS source paths and rejects domain-scoped implementation. |
| [`../kansas/README.md`](../kansas/README.md) | Present Kansas family coordination lane; records the absent KCC child and unresolved migration. |
| [`../kgs_oil_gas_wells/README.md`](../kgs_oil_gas_wells/README.md) | KGS wells/production peer compatibility lane; must remain source-role-distinct from KCC. |
| [`../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md`](../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md) | Draft human-facing KCC product page and OPEN-KCC backlog; not machine authority. |
| [`../../docs/sources/catalog/kansas/ksgs.md`](../../docs/sources/catalog/kansas/ksgs.md) | KGS source-family orientation for the parallel-but-distinct geology/production source. |
| [`../../docs/sources/source-roles.md`](../../docs/sources/source-roles.md) | Human-readable source-role guide using Regulatory Context semantics. |
| [`../../docs/domains/geology/SOURCE_REGISTRY.md`](../../docs/domains/geology/SOURCE_REGISTRY.md) | Geology admission doctrine using the `regulatory` role label. |
| [`../../contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Current SourceDescriptor meaning and fail-closed invariants. |
| [`../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Populated `PROPOSED` schema using `regulatory_context`. |
| [`../../data/registry/sources/source_type_registry.v1.yaml`](../../data/registry/sources/source_type_registry.v1.yaml) | Proposed source-type and source-role companion registry. |
| [`../../data/registry/sources/geology/README.md`](../../data/registry/sources/geology/README.md) | Subtype-first source-registry candidate. |
| [`../../data/registry/geology/sources/README.md`](../../data/registry/geology/sources/README.md) | Domain-first parallel registry lane; final topology unresolved. |
| [`../../control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | Proposed machine authority register; currently empty. |
| [`../../policy/domains/geology/rights/kcc_terms.yaml`](../../policy/domains/geology/rights/kcc_terms.yaml) | Placeholder KCC terms policy; not a rights decision. |
| [`../../release/README.md`](../../release/README.md) | Release-decision authority outside this connector lane. |

---

## ADRs

Directory Rules assign source mechanics to `connectors/`, object meaning to `contracts/`, shape to `schemas/`, admissibility to `policy/`, enforceability to `tests/`, and release decisions to `release/`. Connectors do not publish or write downstream lifecycle state.

No accepted ADR or migration was verified that resolves:

- final KCC connector path or slug;
- losing-path disposition;
- package/distribution/import identity;
- stable KCC source ID;
- `regulatory` versus `regulatory_context`;
- SourceDescriptor schema and registry topology;
- filing-family decomposition;
- fixture and test homes;
- KCC × KGS joined-registry behavior.

OPEN-KCC-01 in the catalog is an open migration item, not an accepted path decision. This one-file documentation revision creates no new path, contract, policy, authority root, or lifecycle boundary and does not itself require an ADR.

---

## Last reviewed

- **Documentation review:** `2026-07-13`
- **Evidence base:** `main` at `40deb4a3cab0972f0c7d38930e30c3b497408b0a`
- **Prior README blob:** `b54ea424e69a76b42e607ac395b831bf3c22e4ab`
- **README introduction commit:** `0e27beb861bacaf5965b974b001046040c689ff2`

This is not a KCC source review, rights review, legal analysis, privacy/security approval, sensitivity approval, activation, runtime proof, release decision, or publication date.

---

## Evidence basis

| Evidence | Supports | Does not prove |
|---|---|---|
| Prior README blob and introduction commit | Exact v0.1 baseline, stale canonical certainty, remote badges, and rollback placeholder. | Runtime, canonical placement, source access, or rights. |
| Exact target and conventional path probes | Current README presence and named missing package/test/fixture/child paths. | Complete recursive absence of differently named or unindexed files. |
| Kansas and Geology connector READMEs | Current parent placement posture and source-first connector boundary. | Final accepted KCC child, implementation, or activation. |
| KCC and KGS source-catalog pages | Record-family proposals, anti-collapse semantics, path proposal, and open questions. | Machine authority, current terms, endpoint stability, source payloads, or public safety. |
| Source-role guide and Geology Source Registry | Regulatory-context semantics and domain `regulatory` vocabulary. | Accepted machine mapping or KCC descriptor instance. |
| SourceDescriptor contract, populated schema, and source-type registry | Current richer descriptor requirements and `regulatory_context` machine vocabulary. | Accepted canonical schema migration, validator wiring, or KCC activation. |
| Both geology source-registry READMEs | Registry topology conflict and no-duplicate-authority rule. | A KCC descriptor instance. |
| Authority register and KCC terms file | Empty machine register and placeholder terms posture. | Rights, sensitivity, access, or activation approval. |
| Connector workflow files | TODO-only workflow definitions. | Package behavior, tests, descriptor validity, rights review, or source activation. |
| Directory Rules and connector-root doctrine | Responsibility roots, lifecycle boundary, and reversible migration discipline. | Final KCC path, source role mapping, or runtime. |

All claims are bounded to the pinned commit, exact reads, indexed search, and named probes.

[Back to top](#top)

---

## Definition of done

### This documentation revision

- [x] Records the current base commit, prior blob, and introduction commit.
- [x] Replaces unsupported canonical-child certainty with a current conflicted placement posture.
- [x] Records the README-only inspected state and exact named probes.
- [x] Surfaces `regulatory` versus `regulatory_context` without choosing an enum by convenience.
- [x] Records source-registry topology conflict, absent named KCC descriptor paths, empty authority register, placeholder terms policy, and TODO-only workflows.
- [x] Preserves regulatory/geology/production/environment/title/operations anti-collapse boundaries.
- [x] Preserves rights, sensitivity, identity, time, geometry, join, lifecycle, evidence, release, correction, and rollback boundaries.
- [x] Changes only this Markdown file.

### Implementation readiness remains open

- [ ] Accepted connector path, slug, source ID, role mapping, descriptor schema, registry topology, fixture home, and test routing.
- [ ] Product- or filing-family descriptors, machine authority entries, reviews, source heads, and activation decisions.
- [ ] Current endpoint or portal modality, access posture, division identity, terms, attribution, redistribution, disclaimers, filing scope, cadence, rate limits, and correction behavior.
- [ ] Source-native identity, amendment/supersession model, temporal model, CRS/datum, geometry method, uncertainty, and public-precision policy.
- [ ] Compact safe fixtures, executable negative-first tests, substantive CI, owners, migration warnings, and rollback-tested implementation.

Documentation readiness does not imply connector readiness, source access, source authority, rights approval, sensitivity clearance, evidence closure, release approval, or publication.

---

## Rollback

Rollback is required if this README is used to claim canonical status, source-role resolution, implementation/test/CI behavior, source access, activation, rights/sensitivity clearance, legal or regulatory authority, public safety, downstream lifecycle authority, evidence closure, or release.

Before merge, leave the draft pull request unmerged and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
b54ea424e69a76b42e607ac395b831bf3c22e4ab
```

from base:

```text
40deb4a3cab0972f0c7d38930e30c3b497408b0a
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, source-role, and policy checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Complete recursive connector inventory | **UNKNOWN** | Non-truncated Git tree receipt or mounted checkout. |
| Final connector path, slug, package, source ID, and losing-path disposition | **CONFLICTED** | Accepted ADR/migration, consumer inventory, backlinks, tests, and rollback plan. |
| `regulatory` versus `regulatory_context` | **CONFLICTED** | Contract/schema/domain/source-steward decision plus compatibility tests. |
| SourceDescriptor schema and validator authority | **CONFLICTED / NEEDS VERIFICATION** | One accepted meaningful schema, validator, fixtures, CI command, and migration. |
| KCC descriptor registry home and record | **NOT FOUND AT NAMED PATHS** | Accepted registry topology and conforming descriptor instance. |
| Source-authority entry and activation decision | **NOT ESTABLISHED** | Reviewed control-plane/registry records and activation receipt. |
| Current KCC division identity and source surfaces | **NEEDS VERIFICATION** | Current authoritative KCC documentation and source-steward review. |
| Access modality, endpoint, credentials posture, cadence, limits, and source head | **NEEDS VERIFICATION** | Approved access contract and observed source-head evidence. |
| Filing-family scope and collection decomposition | **NEEDS VERIFICATION** | Source inventory and steward decision. |
| Stable upstream IDs, amendments, supersession, and correction behavior | **NEEDS VERIFICATION** | Current source records and identity tests. |
| Rights, attribution, redistribution, disclaimers, and reuse | **NEEDS VERIFICATION** | Current terms and rights review. |
| Sensitivity, public geometry, PLSS/coordinate derivation, CRS/datum, and uncertainty | **NEEDS VERIFICATION** | Source artifacts, policy, transforms, fixtures, tests, and review records. |
| KCC × KGS joins and per-attribute provenance | **NEEDS VERIFICATION** | Crosswalk contract, source-role tests, evidence model, and steward decision. |
| Private-owner, royalty-owner, parcel, residence, infrastructure, water-resource, and business joins | **NEEDS VERIFICATION** | Rights/privacy/security/sensitivity policy and negative fixtures. |
| Executable package, tests, fixtures, and substantive CI | **NOT IMPLEMENTED AT NAMED PROBES** | Code, safe fixtures, exact command, discovered test count, logs, and demonstrated negative failure. |
| Owners and review-routing | **UNKNOWN** | Accepted CODEOWNERS or ownership records. |
| Repository-wide promotion prerequisites | **NEEDS VERIFICATION** | Trusted workflow results and required doctrine/release artifacts. |

[Back to top](#top)

---

## Maintainer note

Keep this lane documentation-only until placement, source identity, descriptor vocabulary, registry topology, access, rights, sensitivity, and review conflicts are resolved.

The safest first executable increment is synthetic and negative-first:

1. use one compact invented regulatory-record fixture with no real person, owner, parcel, well coordinate, credential, endpoint, or KCC payload;
2. prove the accepted descriptor vocabulary and reject the wrong role token;
3. preserve filing family, upstream ID, amendment lineage, time fields, geometry method, uncertainty, rights, sensitivity, attribution, and disclaimer fields;
4. return a caller-owned hold/quarantine candidate with deterministic reasons;
5. prove no network, credential lookup, lifecycle write, evidence closure, catalog write, release, or publication side effect;
6. fail CI on zero discovery, TODO-only execution, role drift, or negative-case regression.

Only after that slice, an accepted migration, product-specific governance, and observed CI should an opt-in source-access test be considered.

[Back to top](#top)
