<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/source-registry
title: Soil Source Registry Guide
type: domain-source-registry-guide
version: v1.2.0
prior_version: v1.1.0
status: draft; repository-grounded; implementation-partial
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Rights and sensitivity steward
  - OWNER_TBD - Documentation steward
created: 2026-08-24
updated: 2026-10-11
policy_label: public
owning_root: docs/
responsibility: Human-readable routing and current-state guidance for Soil source admission records
truth_posture: CONFIRMED accepted subtype-first registry placement, inspected Soil lane bytes, and the admitted noaa-uscrn.yaml descriptor; PROPOSED planning lineage; NEEDS VERIFICATION descriptor migration, schema binding, rights and admission of the eight placeholder families, release activation, and publication state
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
  - docs/adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md
  - data/registry/sources/soil/noaa-uscrn.yaml
tags: [kfm, soil, source-registry, source-role, rights, sensitivity, admission, fail-closed]
notes:
  - "Repository evidence snapshot: main@366cfa9185b0d10ca27f128a8a041ca8c5312896."
  - "Planning lineage: KFM Soil Architecture Extended Pro PDF-Only Planning Report, sections 13 and Appendix C, printed/PDF pages 15 and 24, SHA-256 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea."
  - "The planning report explicitly had no mounted repository; its source list and paths remain proposal evidence, not repository authority or activation proof."
  - "Accepted ADR-0029 and Directory Rules DIR-SOURCE-001 through DIR-SOURCE-004 make data/registry/sources/ the canonical writer and limit data/registry/<domain>/sources/ to a generated or compatibility view."
  - "This guide reconciles routing posture only; it does not migrate the four domain-first templates or select a SourceDescriptor schema."
  - "Repository evidence snapshot (v1.2.0): main@b2f62f6ffe9cf439716f387f8893e600905b9947 (short b2f62f6f). The earlier main@366cfa91 snapshot above is kept as lineage."
  - "2026-10-11 (v1.2.0): current determination, inventory, and reconciled-result table updated for the admitted NOAA USCRN descriptor (data/registry/sources/soil/noaa-uscrn.yaml; ADR-0046); the other eight subtype-first records remain PROPOSED placeholders; admission is not release activation or publication; documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil source registry guide

Human-readable routing and current-state guidance for Soil source admission
records. This document does not admit or migrate a source, select a descriptor
schema, confer authority, approve rights, or create a public data path.

> [!IMPORTANT]
> **Current determination at
> `main@b2f62f6ffe9cf439716f387f8893e600905b9947`:** accepted ADR-0029 adopts
> Directory Rules `DIR-SOURCE-001` through `DIR-SOURCE-004`. Those rules make
> `data/registry/sources/` the canonical machine source-identity and descriptor
> writer and permit `data/registry/<domain>/sources/` only as a generated view,
> not an independent writer. The canonical Soil lane holds nine records. One,
> [`noaa-uscrn.yaml`](../../../data/registry/sources/soil/noaa-uscrn.yaml), is
> an admitted `SourceDescriptor` (`review_state: approved`,
> `lifecycle.registry_state: active`, `rights.rights_status: verified_open`,
> `release_state: candidate`), admitted by the repository owner on 2026-10-11
> alongside accepted
> [ADR-0046](../../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md).
> The other eight remain small `PROPOSED` placeholders. The domain-first
> compatibility lane retains four richer greenfield templates with unresolved
> fields pending a reviewed migration. Admission is not publication: the USCRN
> descriptor's `release_state` is `candidate`, its `public_release` block sets
> `requires_review: true` and requires a passing `kfm.soil-release-decision/v1`
> record for each package, and `tools/release/soil_release.py` states "Nothing
> here fetches source data, stages, activates or serves." No inspected record
> proves release activation, serving, or publication.
>
> *Superseded determination at `main@366cfa9185b0d10ca27f128a8a041ca8c5312896`
> (kept as lineage):* the canonical Soil lane contained nine small `PROPOSED`
> placeholders, and no inspected record proved admission, activation, rights
> clearance, operational retrieval, release, or publication.

| Field | Current repository result |
|---|---|
| Human guide | This file under the `docs/` responsibility root |
| Registry instances | Canonical subtype-first writer plus an unmigrated domain-first compatibility lane |
| Source authority | Not established by a filename, descriptor, watcher, or planning report |
| Activation posture | Fail closed. Only `noaa-uscrn.yaml` carries `lifecycle.registry_state: active` (registry admission); no other inspected Soil record establishes an active source, and no record establishes release activation or serving |
| Public posture | No registry record is a public interface or published Soil artifact; the USCRN descriptor is `release_state: candidate` and no USCRN release manifest or published artifact was found under `release/` or `data/published/` |
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

Directory Rules `DIR-SOURCE-001` through `DIR-SOURCE-003` establish source-first
capture identity, one registration for each canonical `source_id`, and
`data/registry/sources/` as the machine descriptor home. `DIR-SOURCE-004`
allows `data/registry/<domain>/sources/` only as a generated view and prohibits
it from becoming an independent writer. That accepted placement decision
outranks the older unresolved-topology text still present in the Soil lane.

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

Eight of these records (`isric-soilgrids.yaml`, `ks-mesonet.yaml`,
`nasa-smap.yaml`, `nrcs-gnatsgo.yaml`, `nrcs-gssurgo.yaml`, `nrcs-scan.yaml`,
`nrcs-sda.yaml`, `nrcs-ssurgo.yaml`) are small `PROPOSED` placeholders tied to
the documentation inventory: each holds only `status: PROPOSED`, `path`,
`source_docs`, and a placeholder note.

`noaa-uscrn.yaml` is the one admitted record. It is a full `SourceDescriptor`
(`schema_version: v1`, `source_id: kfm://source/noaa-uscrn`,
`descriptor_version: 1.0.0`, `source_role: observation`) stored as JSON, which
is valid YAML. Its admitted scope is daily volumetric soil moisture and soil
temperature at 5, 10, 20, 50 and 100 cm for the two Kansas USCRN stations
(WBAN 53974 Manhattan 6 SSW, WBAN 03067 Oakley 19 SSW). It records
`review_state: approved`, `lifecycle.registry_state: active`,
`rights.rights_status: verified_open` (verified by `@bartytime4life` on
2026-10-11), `sensitivity_default: public`, and `release_state: candidate`.
Its `public_release` block allows release only with review, a passing
`kfm.soil-release-decision/v1` record for each package, and owner self-release
under [ADR-0046](../../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md).

Accepted Directory Rules make this subtype-first lane the canonical writer.
Canonical placement does not make the eight placeholders complete, admitted,
active, rights-cleared, or public, and admission of USCRN does not release or
publish it. The lane README also denies activation and publication authority.

### 3.2 Domain-first lane

[`data/registry/soil/sources/`](../../../data/registry/soil/sources/) contains a
substantive README plus four greenfield templates:

- `ksu_soil_moisture.yaml`
- `nrcs_ssurgo.yaml`
- `nrcs_statsgo2.yaml`
- `smap_soil_moisture.yaml`

These records carry more descriptive fields than the subtype-first placeholders,
but unresolved values and a richer shape do not make them canonical or active.
They are retained as unmigrated compatibility material. Independent writes are
denied; a future generated view or retirement requires reviewed source mapping,
consumer and link closure, retained lineage, and a mechanical rollback target.

### 3.3 Reconciled result

| Question | Result |
|---|---|
| Does a Soil registry path exist? | `CONFIRMED` - two path shapes exist. |
| Is one lane accepted as canonical? | `CONFIRMED` - ADR-0029 adopts Directory Rules that make `data/registry/sources/` the canonical writer. |
| May the two descriptor sets diverge? | No - `DIR-SOURCE-004` prohibits the domain-first view from becoming an independent writer. |
| Are the records complete SourceDescriptors? | Partly - `noaa-uscrn.yaml` is a full admitted `SourceDescriptor`; the other eight subtype-first records are placeholders and the domain-first records retain unresolved values (`NEEDS VERIFICATION`). |
| Is compatibility migration complete? | No - the four domain-first templates remain and no reviewed mapping, generator, redirect, or retirement record was found. |
| Is any source active? | Registry admission only for USCRN - `noaa-uscrn.yaml` records `review_state: approved` and `lifecycle.registry_state: active`. No other inspected record proves activation, and no record proves release activation or serving (fail-closed). |
| Is any source public-ready? | No - USCRN rights are `verified_open` and its sensitivity default is `public`, but its `release_state` is `candidate` and release needs review plus a passing `kfm.soil-release-decision/v1` record; no inspected evidence establishes release and public read-back closure for any Soil source. |

The accepted topology is clear, while physical compatibility migration remains
implementation drift. This guide does not merge descriptors, create a generator,
add redirects, or delete either set. It prevents additional drift by routing new
canonical work to the subtype-first lane and denying independent writes in the
domain-first lane.

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

## 6. Required reconciliation before descriptor or migration work

Canonical placement is resolved by ADR-0029 and Directory Rules
`DIR-SOURCE-001` through `DIR-SOURCE-004`. Do not add or enrich competing Soil
source records until all remaining conditions are resolved in repository
authority:

1. define migration and compatibility behavior for the non-canonical lane,
   including redirects or tombstones if adopted;
2. identify the authoritative SourceDescriptor schema and registry binding rather
   than choosing among similarly named schema files by filename;
3. reconcile source-role and support-type vocabularies with current policies,
   schemas, validators, and tests;
4. identify accountable source, rights, sensitivity, policy, evidence, release,
   correction, and rollback stewards; and
5. prove fail-closed outcomes with licensed or synthetic fixtures before any live
   retrieval or source activation is considered.

Until those conditions close, the safe outcomes are `DEFER`, `QUARANTINE`, or
`DENY`; lack of evidence is not approval.

## 7. Explicit non-effects

This guide does not:

- contact, scrape, download, ingest, mirror, or activate a source;
- verify endpoint availability, credentials, current terms, or redistribution
  rights;
- move, rename, rewrite, generate, redirect, or retire either descriptor set;
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
- [ADR-0046](../../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md) - owner self-release for admitted public soil data
- [Admitted USCRN descriptor](../../../data/registry/sources/soil/noaa-uscrn.yaml)

## 9. Maintenance rule

Update this guide only from cited repository evidence. If a future accepted
decision binds the SourceDescriptor schema, completes compatibility migration,
or changes an operational source state, pin the exact decision, affected schema
and policy bindings, migration behavior, tested SHA, and rollback boundary. Do
not infer currentness from modification date, record detail, or
planning-language confidence.
