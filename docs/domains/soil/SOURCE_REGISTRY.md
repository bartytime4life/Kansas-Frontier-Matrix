<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/source-registry
title: Soil Source Registry Guide
type: domain-source-registry-guide
version: v1.0.0
status: draft; repository-grounded; implementation-partial
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Rights and sensitivity steward
  - OWNER_TBD - Documentation steward
created: 2026-08-24
updated: 2026-08-24
policy_label: public
owning_root: docs/
responsibility: Human-readable routing and current-state guidance for Soil source admission records
truth_posture: CONFIRMED repository paths and inspected bytes; PROPOSED planning lineage; NEEDS VERIFICATION registry topology, source rights, admission, activation, and publication state
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/SOURCES.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - data/registry/sources/soil/README.md
  - data/registry/soil/sources/README.md
  - schemas/contracts/v1/source/README.md
  - policy/domains/soil/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, soil, source-registry, source-role, rights, sensitivity, admission, fail-closed]
notes:
  - "Repository evidence snapshot: main@362d6590b9516596ad1c34a64781c13bf85d52c8."
  - "Planning lineage: KFM Soil Architecture Extended Pro PDF-Only Planning Report, sections 13 and Appendix C, printed/PDF pages 15 and 24, SHA-256 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea."
  - "The planning report explicitly had no mounted repository; its source list and paths remain proposal evidence, not repository authority or activation proof."
  - "This guide records, but does not resolve, the two existing Soil source-registry lane shapes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil source registry guide

Human-readable routing and current-state guidance for Soil source admission
records. This document does not admit a source, select a canonical registry
topology, confer authority, approve rights, or create a public data path.

> [!IMPORTANT]
> **Current determination at
> `main@362d6590b9516596ad1c34a64781c13bf85d52c8`:** the repository contains two
> Soil source-registry lane shapes. Both describe themselves as draft and both
> say the final topology needs verification. The subtype-first lane contains
> nine small `PROPOSED` placeholder records; the domain-first lane contains four
> richer greenfield templates with unresolved fields. No inspected record proves
> admission, activation, rights clearance, operational retrieval, release, or
> publication.

| Field | Current repository result |
|---|---|
| Human guide | This file under the `docs/` responsibility root |
| Registry instances | Two existing `data/` lane shapes; topology unresolved |
| Source authority | Not established by a filename, descriptor, watcher, or planning report |
| Activation posture | Fail closed; no inspected Soil record establishes an active source |
| Public posture | No registry record is a public interface or published Soil artifact |
| Sensitive-data posture | Rights and sensitivity review precede admission; exact or restricted material remains denied or quarantined |
| Lifecycle | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` |

## 1. Authority and evidence basis

Repository authority is applied in this order for this guide:

1. [accepted ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
   and the adopted [Directory Rules](../../doctrine/directory-rules.md);
2. current registry records, schemas, policies, validators, tests, and executable
   behavior at the pinned repository snapshot;
3. current authoritative repository documentation; and
4. external planning material only as proposal lineage.

The relevant planning source is **KFM Soil Architecture Extended Pro PDF-Only
Planning Report**, sections 13 and Appendix C, printed/PDF pages 15 and 24,
created 2026-04-21, SHA-256
`7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea`.
It proposes recording source role, support type, rights, attribution, access,
freshness, format, and limitations for several Soil source families. The report
also states that it was prepared without a mounted repository and that endpoints
and terms need verification. Its list therefore helps locate questions; it does
not establish current implementation, adoption, rights, or permission to use a
source.

## 2. Responsibility-root placement

This file stays at an existing path under `docs/`, whose accepted responsibility
is human-readable explanation and routing. Machine-readable registry instances
remain under `data/`; source schemas remain under `schemas/`; semantic contracts
remain under `contracts/`; policies remain under `policy/`; and validators remain
under `tools/validators/`.

No file is moved or renamed, no parallel authority home is created, and no
registry, index, or manifest update is required for this same-path documentation
repair. The document-registry delta emitted by the metadata validator remains a
review aid rather than authority.

## 3. Current registry inventory

### 3.1 Subtype-first lane

[`data/registry/sources/soil/`](../../../data/registry/sources/soil/) contains a
substantive README plus these nine records:

- `isric-soilgrids.yaml`
- `ks-mesonet.yaml`
- `nasa-smap.yaml`
- `noaa-uscrn.yaml`
- `nrcs-gnatsgo.yaml`
- `nrcs-gssurgo.yaml`
- `nrcs-scan.yaml`
- `nrcs-sda.yaml`
- `nrcs-ssurgo.yaml`

Each inspected record is a small `PROPOSED` placeholder tied to the current
documentation inventory. The lane README says the repository also contains the
domain-first path and that final topology needs an ADR, migration note, Directory
Rules update, or registry-inventory decision. It also denies activation and
publication authority.

### 3.2 Domain-first lane

[`data/registry/soil/sources/`](../../../data/registry/soil/sources/) contains a
substantive README plus four greenfield templates:

- `ksu_soil_moisture.yaml`
- `nrcs_ssurgo.yaml`
- `nrcs_statsgo2.yaml`
- `smap_soil_moisture.yaml`

These records carry more descriptive fields than the subtype-first placeholders,
but unresolved values and a richer shape do not make them canonical or active.
The lane README likewise records the subtype-first pattern and labels the exact
topology as needing verification.

### 3.3 Reconciled result

| Question | Result |
|---|---|
| Does a Soil registry path exist? | `CONFIRMED` - two path shapes exist. |
| Is one lane accepted as canonical? | `NEEDS VERIFICATION` - both lane READMEs explicitly defer the topology decision. |
| May the two descriptor sets diverge? | No - both lane READMEs warn against divergent authority records. |
| Are the records complete SourceDescriptors? | `NEEDS VERIFICATION` - the subtype-first records are placeholders and the domain-first records retain unresolved values. |
| Is any source active? | `NEEDS VERIFICATION`, with fail-closed effect - no inspected record proves activation. |
| Is any source public-ready? | No inspected registry evidence establishes rights, sensitivity, evidence, review, release, and public read-back closure. |

The duplicate lane shapes are governance and implementation drift to be resolved
by an accepted topology decision and migration plan. This guide does not silently
select the more detailed lane, merge descriptors, add redirects, or delete either
set.

## 4. Source-family orientation

The planning report and current placeholder filenames overlap on several source
families, including NRCS survey products and services, Kansas station material,
federal station networks, satellite soil-moisture products, and modeled global
soil surfaces. That overlap supports traceability only.

Before any family is treated as usable, repository evidence must establish at
least:

- the exact source identity, version or head, authority scope, and source role;
- supported Soil object and claim families without collapsing map-unit,
  component, horizon, station/depth observation, remote-sensing, or model-derived
  semantics;
- rights, license, attribution, redistribution, access, and terms currentness;
- spatial and temporal resolution, scale, cadence, limitations, and correction
  behavior;
- sensitivity handling for private-land joins, parcel-adjacent detail, precise
  locations, infrastructure, living-person data, and culturally controlled or
  otherwise restricted material;
- the selected schema and policy bindings, accountable stewards, review evidence,
  and a reversible activation decision; and
- quarantine, validation, evidence, catalog, release, publication, correction,
  revocation, and rollback requirements.

A generic source family name or government provenance is not enough to satisfy
those gates.

## 5. Admission and publication boundary

The source registry sits before lifecycle admission. A descriptor may constrain
whether and how material is admitted, but it is not the material, an
`EvidenceBundle`, a catalog entry, a release decision, or a published artifact.

```text
source proposal
  -> rights + sensitivity + source-role review
  -> governed admission decision
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> governed release and publication controls
  -> PUBLISHED
```

Every arrow remains fail closed until its own governing requirements are
satisfied. Watchers, connectors, builders, indexers, maps, summaries, and AI
generators do not become publishers. Derived layers, tiles, indexes, embeddings,
or language are not canonical Soil truth. Evidence-dependent claims must resolve
through governed evidence references and cite or abstain.

## 6. Required reconciliation before descriptor work

Do not add or enrich competing Soil source records until all of the following are
resolved in repository authority:

1. select the canonical Soil source-registry lane and document the accepted
   Directory Rules or ADR basis;
2. define migration and compatibility behavior for the non-canonical lane,
   including redirects or tombstones if adopted;
3. identify the authoritative SourceDescriptor schema and registry binding rather
   than choosing among similarly named schema files by filename;
4. reconcile source-role and support-type vocabularies with current policies,
   schemas, validators, and tests;
5. identify accountable source, rights, sensitivity, policy, evidence, release,
   correction, and rollback stewards; and
6. prove fail-closed outcomes with licensed or synthetic fixtures before any live
   retrieval or source activation is considered.

Until those conditions close, the safe outcomes are `DEFER`, `QUARANTINE`, or
`DENY`; lack of evidence is not approval.

## 7. Explicit non-effects

This guide does not:

- contact, scrape, download, ingest, mirror, or activate a source;
- verify endpoint availability, credentials, current terms, or redistribution
  rights;
- choose a registry topology or make either descriptor set authoritative;
- promote material or emit an operational admission, promotion, release, or
  publication decision;
- publish data, layers, maps, tiles, indexes, embeddings, summaries, or generated
  text; or
- weaken a schema, validator, policy, evidence resolver, promotion control, or
  publication gate.

## 8. Related repository surfaces

- [Soil domain index](README.md)
- [Soil source orientation](SOURCES.md)
- [Canonical-path assessment](CANONICAL_PATHS.md)
- [Soil lifecycle guide](DATA_LIFECYCLE.md)
- [Subtype-first registry lane](../../../data/registry/sources/soil/README.md)
- [Domain-first registry lane](../../../data/registry/soil/sources/README.md)
- [Source schema lane](../../../schemas/contracts/v1/source/README.md)
- [Soil policy lane](../../../policy/domains/soil/README.md)
- [Adopted Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

## 9. Maintenance rule

Update this guide only from cited repository evidence. If a future accepted
decision selects a topology or an operational decision changes a source state,
pin the exact decision, affected schema and policy bindings, migration behavior,
tested SHA, and rollback boundary. Do not infer currentness from modification
date, record detail, or planning-language confidence.
