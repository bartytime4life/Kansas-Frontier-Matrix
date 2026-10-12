<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-fauna-readme
title: contracts/domains/fauna — Fauna Contract Lane README
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Fauna steward · Contract steward · Schema steward · Policy steward · Sensitivity reviewer · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; contracts; domains; fauna; semantic-contracts; sensitivity-aware; no-parallel-authority
tags: [kfm, contracts, fauna, biodiversity, semantic-contracts, source-role, sensitivity, geoprivacy, evidence, policy, release, governance]
related:
  - ../../README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/SOURCES.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SCHEMAS.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../tests/domains/fauna/
  - ../../../fixtures/domains/fauna/
  - ../../../data/registry/sources/fauna/
  - ../../../release/candidates/fauna/
notes:
  - "This README governs the semantic Markdown contract lane for Fauna only."
  - "Contracts define meaning; schemas define machine shape; policy decides allow/deny/restrict/abstain; tests and fixtures prove enforcement; release records publish and roll back."
  - "Sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, telemetry, steward-controlled records, and re-identifying joins require fail-closed handling unless reviewed, transformed, receipted, and released."
  - "Implementation depth varies: several related repo files are scaffold or placeholder documents. Runtime enforcement, validator completeness, and release workflow behavior remain NEEDS VERIFICATION."
  - "The user-provided Markdown Authoring Agent v2 prompt was treated as authoring guidance, not pasted into this README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/domains/fauna

> Semantic contract lane for Fauna-domain object meaning: taxonomy, conservation status, observations, ranges, monitoring, sensitive sites, geoprivacy, and release-aware biodiversity claims.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2ea44f">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Schema home: schemas/contracts/v1" src="https://img.shields.io/badge/schema__home-schemas%2Fcontracts%2Fv1-purple">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
</p>

`contracts/domains/fauna/README.md`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Contract lane map](#contract-lane-map) · [Fauna trust rules](#fauna-trust-rules) · [Authoring checklist](#authoring-checklist) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Scope

`contracts/domains/fauna/` is the Fauna lane inside the canonical `contracts/` responsibility root.

It owns **semantic Markdown contracts** for Fauna-domain object families: the meaning of a `Taxon`, `ConservationStatus`, `OccurrenceEvidence`, `SensitiveSite`, range, monitoring, mortality, disease, invasive-species, redaction/publication, and other Fauna objects once those contracts are authored and reviewed.

It does **not** own:

- JSON Schema shape;
- admissibility or sensitivity policy;
- source descriptors;
- raw, work, quarantine, processed, catalog, or published data;
- release manifests, promotion decisions, correction notices, or rollback cards;
- runnable validators, tests, fixtures, packages, pipelines, or UI code.

> [!IMPORTANT]
> **Contract meaning is not publication permission.** A Fauna contract can define what an object means, but public exposure still requires evidence, source role, rights, sensitivity, validation, policy, review, release state, correction path, and rollback support.

---

## Repo fit

Directory Rules place object meaning in `contracts/`, machine shape in `schemas/`, policy decisions in `policy/`, proof in `tests/`, fixtures in `fixtures/`, lifecycle data in `data/`, and release decisions in `release/`. Domain-specific files use `fauna` as a segment inside those responsibility roots.

| Responsibility | Fauna lane path | Authority in this README |
|---|---|---|
| Human domain doctrine | `../../../docs/domains/fauna/` | Linked, not owned here |
| Semantic object meaning | `./` | **Owned here** |
| Machine shape | `../../../schemas/contracts/v1/domains/fauna/` | Linked only |
| Domain policy | `../../../policy/domains/fauna/` | Linked only |
| Sensitivity policy | `../../../policy/sensitivity/fauna/` | Linked only |
| Fixtures | `../../../fixtures/domains/fauna/` | Linked only |
| Tests / validators | `../../../tests/domains/fauna/`, `../../../tools/validators/domains/fauna/` | Linked only |
| Source registry | `../../../data/registry/sources/fauna/` | Linked only |
| Lifecycle data | `../../../data/<phase>/fauna/` | Linked only |
| Release decisions | `../../../release/candidates/fauna/`, `../../../release/manifests/` | Linked only |

This split prevents a contract document from quietly becoming a schema, a policy bundle, a source registry, a release manifest, or a public truth store.

---

## What belongs here

Accepted content in `contracts/domains/fauna/`:

| Contract class | Examples | Required posture |
|---|---|---|
| Object-family meaning | `taxon.md`, `taxon_crosswalk.md`, `conservation_status.md` | Define meaning, claim support, exclusions, lifecycle, and links to schema/policy. |
| Observation and evidence meaning | `occurrence_evidence.md`, `monitoring_event.md`, `mortality_observation.md`, `disease_observation.md` | Preserve source role, evidence support, time, geometry scope, sensitivity posture, and correction path. |
| Sensitive-location meaning | `sensitive_site.md`, `occurrence_restricted.md`, `occurrence_public.md` | Fail closed; do not expose exact sensitive locations or transform parameters. |
| Range and model meaning | `range_polygon.md`, `seasonal_range.md`, `migration_route.md`, `richness_indicator.md` | Separate observed, modeled, aggregate, and synthetic roles. |
| Publication-support meaning | `redaction_receipt.md`, `release_manifest.md`, `promotion_decision.md` if domain-specific variants are retained | Do not duplicate cross-domain release/correction authority unless an ADR or root README supports it. |
| Lane-level contract guides | `README.md` | Explain contract-lane ownership, review gates, and drift prevention. |

Contract files should answer:

1. What does this Fauna object mean?
2. What claim class can it support?
3. What does it explicitly **not** assert?
4. Which schema defines its machine shape?
5. Which policy gates its admissibility and release?
6. Which evidence, receipt, review, correction, and rollback references must resolve?

---

## What does not belong here

| If the artifact is… | Put it in… | Reason |
|---|---|---|
| `.schema.json` | `../../../schemas/contracts/v1/domains/fauna/` | Schema home is separate; contracts define meaning only. |
| Policy / allow-deny logic | `../../../policy/domains/fauna/` or `../../../policy/sensitivity/fauna/` | Policy decides admissibility and release tier. |
| Valid/invalid examples | `../../../fixtures/domains/fauna/` | Fixtures prove behavior without becoming contracts. |
| Tests / runnable validators | `../../../tests/domains/fauna/`, `../../../tools/validators/domains/fauna/` | Tests and tools prove or execute checks. |
| Source descriptors | `../../../data/registry/sources/fauna/` | Source identity, rights, cadence, and role live in the registry. |
| Raw source data | `../../../data/raw/fauna/` | RAW is lifecycle data, not contract meaning. |
| Work or quarantine data | `../../../data/work/fauna/`, `../../../data/quarantine/fauna/` | Not public and not contract authority. |
| Published artifacts | `../../../data/published/`, `../../../release/` | Publication requires governed release records. |
| UI / Evidence Drawer code | `../../../apps/explorer-web/`, `../../../packages/` | UI is delivery/interpretation, not truth authority. |
| Habitat × fauna joins | lowest common responsibility root or Habitat/Fauna cross-lane docs | Cross-domain joins must not be hidden under one domain contract. |

> [!WARNING]
> A JSON Schema, policy file, release manifest, or source descriptor placed under `contracts/domains/fauna/` creates parallel authority drift. Move it to the owning responsibility root instead of preserving it here.

---

## Contract lane map

Current repo evidence shows this lane is still mixed in maturity: the lane README exists, some contract files exist as scaffolds, and related schema/policy/runtime artifacts vary from scaffold to placeholder.

```text
contracts/domains/fauna/
├── README.md                         # this lane guide
├── conservation_status.md             # scaffold observed in repo
├── domain_layer_descriptor.md         # greenfield scaffold observed in repo
└── ...                                # additional object contracts are PROPOSED / NEEDS VERIFICATION
```

Known related repo evidence from current inspection:

| Observed item | Status | Notes |
|---|---|---|
| `conservation_status.md` | `PROPOSED scaffold` | Planned contract path exists, not domain-reviewed content. |
| `domain_layer_descriptor.md` | `PROPOSED greenfield scaffold` | Names schema pairing but fields/invariants/lifecycle remain placeholders. |
| `schemas/contracts/v1/domains/fauna/*.schema.json` | `CONFIRMED search results for several files` | Presence of individual schemas varies; shape authority is outside this README. |
| `policy/domains/fauna/ebird_redistribution.md` | `PROPOSED scaffold` | Rights/policy content requires review before authority. |
| `policy/sensitivity/fauna/tier_mapping.yaml` | `PROPOSED placeholder` | Binding tier mapping still needs review. |
| `packages/domains/fauna/src/fauna/identity.py` | `greenfield placeholder` | Runtime/package behavior not proven. |
| `pipelines/domains/fauna/normalize.py` | `greenfield placeholder` | Pipeline behavior not proven. |

---

## Fauna trust rules

Fauna contracts must preserve these rules by default:

### 1. Source role is part of identity

Fauna records distinguish `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic` source roles. Promotion does not turn one role into another. A regulatory listing is not an observed sighting; a model is not an occurrence; an aggregate is not a per-place record.

### 2. Sensitive locations fail closed

Sensitive taxa, exact sensitive occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, telemetry, steward-controlled records, and re-identifying joins must not be exposed merely because a contract exists. Exact sensitive locations default to denial unless policy, review, transform, receipt, release, and rollback support permit a public-safe representation.

### 3. Aggregators do not erase origin role

GBIF, eBird, iNaturalist, iDigBio, BISON, and similar sources may be access paths or aggregators. The record still needs a governed source role, rights posture, sensitivity posture, and provenance chain.

### 4. Habitat/context joins are not fauna truth

Habitat, hydrology, soil, land-cover, ownership, or hazard context can support interpretation only through governed joins. A context layer does not become a Fauna observation by being useful to Fauna.

### 5. AI and UI are downstream carriers

Evidence Drawer views, Focus Mode summaries, generated explanations, map tiles, and dashboards may help users understand released Fauna claims. They are not evidence roots, publication authorities, or policy decisions.

---

## Authoring checklist

Before adding or revising a Fauna contract:

- [ ] Confirm the object belongs in the Fauna domain and not Habitat, Flora, Hydrology, Hazards, Archaeology, People/DNA/Land, or a cross-domain root.
- [ ] Confirm the file is semantic Markdown, not JSON Schema, policy, fixture, test, release, or data.
- [ ] Link to the paired schema in `schemas/contracts/v1/domains/fauna/` when known.
- [ ] Link to relevant policy in `policy/domains/fauna/` or `policy/sensitivity/fauna/` when known.
- [ ] State source-role boundaries and anti-collapse rules.
- [ ] State sensitivity/geoprivacy defaults and public-release blockers.
- [ ] Name EvidenceRef/EvidenceBundle, RedactionReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, CorrectionNotice, and rollback expectations where relevant.
- [ ] Mark runtime, validator, fixture, release, and UI behavior as `NEEDS VERIFICATION` unless directly proven.
- [ ] Avoid exact sensitive-location examples, transform radii, fuzzing parameters, private-land details, or other exposure aids.
- [ ] Preserve rollback target when replacing a scaffold.

---

## Validation

This README is valid when:

- it keeps `contracts/domains/fauna/` narrowed to semantic Markdown contracts;
- no `.schema.json`, policy bundle, source descriptor, data artifact, fixture, test, release manifest, or runtime code is normalized under this lane;
- contract docs cross-link to their schema, policy, evidence, review, and release dependencies without claiming those are implemented unless verified;
- sensitive Fauna surfaces remain deny-by-default until governed redaction/generalization/review/release permits exposure;
- contributors can tell where to put meaning, shape, policy, proof, data, release, and UI work.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/README.md` | `CONFIRMED repo evidence` | Root `contracts/` purpose: semantic meaning; contracts say what objects mean, schemas say what they look like. | Does not define Fauna-specific sensitivity or source-role rules. |
| Prior `contracts/domains/fauna/README.md` | `CONFIRMED repo evidence` | Target existed as a greenfield scaffold. | Its “what belongs here” was overbroad and contradicted root responsibility split. |
| `docs/domains/fauna/README.md` | `CONFIRMED repo evidence` | Human-facing Fauna lane scope, sensitivity posture, domain placement, exclusions, and trust membrane. | Explains domain doctrine; does not make contract-lane files authoritative. |
| `docs/domains/fauna/SOURCES.md` and `SOURCE_ROLES.md` | `CONFIRMED repo evidence` | Source-role discipline, canonical seven-class enum, anti-collapse mapping, aggregator trap. | SourceDescriptor records and runtime enforcement remain outside this README. |
| `docs/domains/fauna/SENSITIVITY.md` | `CONFIRMED repo evidence` | Deny-by-default, T4 defaults, geoprivacy, RedactionReceipt, ReviewRecord, PolicyDecision posture. | Binding policy still lives under policy roots. |
| `docs/domains/fauna/SCHEMAS.md` | `CONFIRMED repo evidence` | Meaning/shape/policy/proof split and schema-home rule. | Schema files remain outside contract authority. |
| `policy/domains/fauna/ebird_redistribution.md` | `CONFIRMED repo evidence` | Policy path exists but is a scaffold. | Does not prove reviewed redistribution policy. |
| `policy/sensitivity/fauna/tier_mapping.yaml` | `CONFIRMED repo evidence` | Sensitivity tier mapping placeholder exists. | Does not prove adopted tier mapping behavior. |
| `packages/domains/fauna/src/fauna/identity.py` and `pipelines/domains/fauna/normalize.py` | `CONFIRMED repo evidence` | Package/pipeline placeholders exist. | Does not prove runtime identity or normalization behavior. |

---

## Rollback

Rollback if this README is used to justify putting schemas, policy, source records, data lifecycle artifacts, fixtures, tests, release decisions, UI code, or runtime behavior under `contracts/domains/fauna/`; if it weakens sensitive-location fail-closed behavior; or if it treats scaffolded Fauna contracts as domain-reviewed authority.

Rollback target: prior scaffold blob SHA `e6d85e2862cbedf2474c422f55c298d434fa4a42`.

<p align="right"><a href="#top">Back to top</a></p>
