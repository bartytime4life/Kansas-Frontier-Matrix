<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-nfhl-readme
title: connectors/fema-nfhl/ — FEMA NFHL Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Hydrology steward · Hazards steward · Data steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-only; not-for-life-safety
proposed_path: connectors/fema-nfhl/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/sources/catalog/fema/README.md
  - ../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../docs/sources/catalog/fema/map-service-center.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../data/registry/sources/
  - ../../data/raw/hydrology/
  - ../../data/quarantine/hydrology/
  - ../../data/raw/hazards/
  - ../../data/quarantine/hazards/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, fema, nfhl, floodplain, flood-hazard, hydrology, hazards, regulatory-context, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-lane contract for FEMA NFHL source admission."
  - "Visible FEMA source-catalog docs reference connectors/fema/ as the family connector location; connectors/fema-nfhl/ canonicality is NEEDS VERIFICATION until resolved by repo tree review or ADR."
  - "NFHL is regulatory flood hazard context, not observed inundation, forecast, warning, or life-safety guidance."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, policy, review, release, and rollback remain outside this folder."
  - "Specific endpoints, bulk-download behavior, service surfaces, descriptors, tests, fixtures, CI wiring, terms, and activation state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA NFHL Connector

> Source-specific intake and admission lane for FEMA National Flood Hazard Layer material used by KFM Hydrology, Hazards, and exposure-context workflows.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Life safety: not guidance" src="https://img.shields.io/badge/life__safety-not__guidance-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fema-nfhl/`

## Quick jumps

[Scope](#scope) · [Canonicality warning](#canonicality-warning) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Admission posture](#admission-posture) · [Regulatory and life-safety boundary](#regulatory-and-life-safety-boundary) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fema-nfhl/` is the connector lane for FEMA NFHL source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, and tests for NFHL source material.

It must not become flood truth, observed inundation truth, emergency-alert authority, regulatory interpretation authority, insurance determination authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/fema-nfhl/`  
> **Truth posture:** README path is CONFIRMED. Connector implementation, canonical path, source activation, endpoint coverage, bulk strategy, tests, fixtures, policy enforcement, and CI wiring remain `NEEDS VERIFICATION`.

---

## Canonicality warning

Visible FEMA source-catalog docs point to `connectors/fema/` as the FEMA family connector location. This README lives at `connectors/fema-nfhl/`.

Treat this path as **NEEDS VERIFICATION** until one of these is confirmed:

1. `connectors/fema-nfhl/` is the accepted source-specific NFHL connector home;
2. `connectors/fema/` is the canonical FEMA family connector home and this folder is a compatibility path;
3. the repo needs a migration note or ADR to resolve the split;
4. this folder should be folded into a different source-family structure.

Do not create additional FEMA connector paths without checking Directory Rules, existing source catalog references, source descriptors, and any ADR or migration note.

---

## Repo fit

```text
connectors/
└── fema-nfhl/
    └── README.md
```

Known related paths:

```text
docs/sources/catalog/fema/README.md              # FEMA source-family catalog entry
docs/sources/catalog/fema/nfhl-flood-hazard.md   # NFHL product page
docs/sources/catalog/fema/map-service-center.md  # FEMA Map Service Center companion profile
connectors/fema/                                 # referenced by visible FEMA source-catalog metadata; NEEDS VERIFICATION
connectors/fema-nfhl/                            # this connector lane
```

Related responsibility roots:

```text
connectors/                                      # source-specific fetch and admission code
docs/domains/hydrology/                          # hydrology domain doctrine
docs/domains/hazards/                            # hazards domain doctrine
data/registry/sources/                           # source descriptors and activation state
data/raw/hydrology/                              # raw staged hydrology source outputs, if admitted
data/quarantine/hydrology/                       # held hydrology material requiring review
data/raw/hazards/                                # raw staged hazards source outputs, if admitted
data/quarantine/hazards/                         # held hazards material requiring review
data/receipts/                                   # process and validation receipts
data/proofs/                                     # EvidenceBundles and proof packs
policy/sensitivity/                              # sensitivity and release rules
release/                                         # release decisions and rollback/correction state
```

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/hydrology/ or data/raw/hazards/
  data/quarantine/hydrology/ or data/quarantine/hazards/

NOT HERE:
  observed flood extent
  flood forecast or warning
  insurance determination
  legal/regulatory interpretation
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, or stage NFHL source material. It does not decide whether a location is safe, insured, compliant, eligible, or currently flooded.

---

## Inputs

Potential input classes include:

- source descriptor references;
- steward-approved NFHL access surface identifiers;
- bulk package metadata or service-layer metadata;
- feature classes and regulatory attributes preserved from source material;
- jurisdiction, county, panel, study, version, or effective-date filters where allowed;
- datum, units, coordinate reference system, and elevation metadata;
- test fixtures that preserve source shape without becoming legal or life-safety guidance.

All live access and bulk-download behavior is **NEEDS VERIFICATION** until source terms, access method, freshness cadence, record identity, and validation expectations are reviewed.

---

## Exclusions

Do not place these in `connectors/fema-nfhl/`:

| Excluded material | Correct handling |
|---|---|
| SourceDescriptor authority records | `data/registry/sources/` or accepted source registry home. |
| Machine-checkable schemas | `schemas/contracts/v1/...` under accepted schema-home convention. |
| Policy decisions or release rules | `policy/` and release review surfaces. |
| Processed hydrology or hazard records | Downstream lifecycle roots only. |
| Published maps, tiles, catalogs, or public claims | Release and publication roots only. |
| Insurance, legal, or life-safety determination text | Out of scope; redirect to official channels and reviewed public guidance. |
| Large source payloads or bulk extracts | Store only through approved RAW/QUARANTINE lifecycle paths with receipts. |
| Generated summaries used as evidence | Not allowed; EvidenceBundle-backed claims only. |

---

## Admission posture

NFHL connector output must be conservative.

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved features;
- no conversion of NFHL regulatory context into observed inundation;
- no forecast, warning, life-safety, insurance, or legal determination language;
- no dropping of source regulatory attributes that downstream validation requires;
- no assumption that datum, elevation units, version, or effective date are valid without checks;
- unclear freshness, version, attribute, datum, rights, or source-shape questions route to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Bulk package incomplete | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Feature schema drift detected | `NEEDS_VERIFICATION`; drift note candidate. |
| Datum or unit metadata unclear | Quarantine or review-required result. |
| Effective date or version missing | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |
| Source terms unclear | `NEEDS_VERIFICATION`; no live activation. |

---

## Regulatory and life-safety boundary

NFHL is treated as regulatory flood hazard context in KFM. It is not observed inundation, not a real-time event feed, not a forecast, and not a public safety instruction.

Connector code and docs should preserve these defaults:

1. Preserve source regulatory attributes verbatim where possible.
2. Preserve version, effective-date, panel, study, jurisdiction, datum, units, and source lineage metadata where available.
3. Keep visualization surfaces separate from analytic vector source material when source docs require that separation.
4. Prevent export language that looks like an insurance, legal, emergency, or site-specific determination.
5. Public surfaces must redirect emergency or life-safety decisions to official channels.
6. Derived maps, tiles, summaries, vector indexes, and AI-generated text are not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- feature class, regulatory zone, version, effective date, datum, units, and source lineage fields are preserved where available;
- visualization-only material is not treated as analytic source data;
- malformed or incomplete responses fail closed;
- NFHL records remain regulatory-context candidates until downstream validation;
- no test or connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and proposed source ID are verified.
- [ ] The canonical relationship between `connectors/fema/` and `connectors/fema-nfhl/` is resolved.
- [ ] Live access is disabled by default.
- [ ] Bulk/source access method is documented before activation.
- [ ] Source regulatory attributes are preserved in parser output.
- [ ] Datum, units, effective date, version, and lineage metadata are preserved where available.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims, warnings, legal determinations, or insurance determinations are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, stale/version-missing, datum/units-unclear, schema-drift, and visualization-vs-analytic cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm whether canonical connector home is `connectors/fema-nfhl/` or `connectors/fema/`. | **NEEDS VERIFICATION** | Directory Rules, repo tree, source-catalog metadata, and ADR/migration note. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub listing. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm NFHL access method, preferred bulk strategy, and service surfaces. | **NEEDS VERIFICATION** | Source steward review and source catalog updates. |
| Confirm source terms and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm datum, units, version, effective-date, and regulatory-attribute handling. | **NEEDS VERIFICATION** | Fixture review and downstream schema/contract checks. |
| Confirm fixture strategy for NFHL feature material. | **NEEDS VERIFICATION** | Test fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector as regulatory-context intake, not flood-event truth. It can make NFHL material easier to inspect, stage, validate, and cite, but it must not make regulatory layers look like observed flooding, forecasts, warnings, legal advice, insurance determinations, or public-safety guidance.
