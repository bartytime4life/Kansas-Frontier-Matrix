<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fauna-readme
title: connectors/fauna/ — Fauna Connector Group
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Fauna steward · Sensitivity reviewer · Data steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine
proposed_path: connectors/fauna/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-group contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - inaturalist/README.md
  - ../ebird/README.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../docs/sources/catalog/inaturalist/README.md
  - ../../docs/sources/catalog/ebird/README.md
  - ../../data/registry/sources/fauna/
  - ../../data/raw/fauna/
  - ../../data/quarantine/fauna/
  - ../../data/receipts/fauna/
  - ../../data/proofs/fauna/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, fauna, biodiversity, occurrence-evidence, source-admission, geoprivacy, sensitive-location, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-group contract for fauna-related connector lanes."
  - "Fauna canonical-path docs state that connectors/ is organized by SOURCE, not by domain, and flag a connectors/<domain> question. Treat connectors/fauna/ as NEEDS VERIFICATION until resolved by repo tree review or ADR."
  - "Fauna connector output may enter RAW or QUARANTINE only; downstream validation, sensitivity review, EvidenceBundle closure, release, and rollback remain outside this folder."
  - "Specific child connectors, source descriptors, tests, fixtures, CI wiring, source terms, and activation state remain NEEDS VERIFICATION unless cited from current repo evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Connector Group

> Connector-group landing page for fauna-related source-admission lanes under `connectors/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Canonicality: needs verification" src="https://img.shields.io/badge/canonicality-needs__verification-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fauna/`

## Quick jumps

[Scope](#scope) · [Canonicality warning](#canonicality-warning) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Child connector lanes](#child-connector-lanes) · [Admission posture](#admission-posture) · [Sensitivity posture](#sensitivity-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fauna/` is a connector-group landing page for fauna-related source-admission lanes.

It may explain how fauna-related connectors should behave when retrieving, parsing, staging, or quarantining source material such as community observations, agency records, museum records, biodiversity APIs, or other fauna source families.

It must not become fauna truth, species truth, taxonomy authority, legal-status authority, sensitive-location authority, source-family authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/fauna/`  
> **Truth posture:** README path is CONFIRMED. The canonicality of a domain-group under `connectors/` remains `NEEDS VERIFICATION` because visible fauna path guidance says `connectors/` is organized by source rather than by domain.

---

## Canonicality warning

The fauna canonical-path register states that `connectors/` is organized by **source**, not by domain, and flags `connectors/<domain>` as an open placement question. Therefore, this README should be treated as one of these until resolved:

1. a temporary compatibility landing page;
2. a fauna-scoped grouping index for source lanes;
3. a migration target that requires ADR support;
4. a folder that should eventually be replaced by source-first connector homes.

Do not add new child connector lanes under `connectors/fauna/` merely because they are fauna-related. First check Directory Rules, current repo tree, source catalog references, existing connector paths, and any ADR or migration note.

---

## Repo fit

```text
connectors/
└── fauna/
    ├── README.md
    └── inaturalist/
        └── README.md
```

Known or likely related connector/source paths:

```text
connectors/fauna/inaturalist/          # fauna-scoped iNaturalist connector lane in this subtree
connectors/ebird/                      # source-first eBird connector lane observed elsewhere in repo evidence
connectors/inaturalist/                # referenced by visible iNaturalist source-catalog metadata; NEEDS VERIFICATION
```

Related responsibility roots:

```text
connectors/                            # source-specific fetch and admission code
docs/domains/fauna/                    # fauna domain doctrine and sensitivity posture
docs/sources/catalog/                  # source-family briefings
data/registry/sources/fauna/           # source descriptors and activation state
data/raw/fauna/                        # raw staged fauna source outputs
data/quarantine/fauna/                 # held material requiring review
data/receipts/fauna/                   # process and validation receipts
data/proofs/fauna/                     # EvidenceBundles and proof packs
policy/sensitivity/                    # sensitivity and release rules
policy/rights/                         # rights and license policy, if present
release/                               # release decisions and rollback/correction state
```

---

## Authority boundary

```text
THIS GROUP MAY EXPLAIN:
  fauna-related connector admission posture
  child connector responsibilities
  source-admission limits
  geoprivacy and sensitive-location defaults
  validation and rollback expectations
  open placement questions

THIS GROUP MUST NOT CONTAIN OR DECIDE:
  species occurrence truth
  legal/listed-status truth
  taxonomy authority
  source descriptor authority
  sensitive-location release decisions
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

Fauna connectors may help retrieve or stage source material. They do not decide whether a record is true, taxonomically settled, rights-cleared, location-safe, regulatory, or publishable.

---

## Child connector lanes

Current or nearby lanes should be treated with evidence labels.

| Connector lane | Status | Notes |
|---|---:|---|
| `connectors/fauna/inaturalist/` | **CONFIRMED path / PROPOSED contract** | Fauna-scoped iNaturalist lane created as source-admission guidance. Canonicality needs reconciliation with source-first iNaturalist references. |
| `connectors/ebird/` | **CONFIRMED nearby source-first lane** | eBird uses a source-first connector home in visible repo evidence. It should not be silently moved under this folder without ADR or migration support. |
| `connectors/inaturalist/` | **NEEDS VERIFICATION** | Referenced by source-catalog metadata as an iNaturalist connector home; verify whether it exists and whether it supersedes or complements `connectors/fauna/inaturalist/`. |
| Additional fauna connectors | **PROPOSED** | Add only after source descriptor, source catalog entry, placement review, and sensitivity posture are clear. |

---

## Admission posture

Fauna connector output must be conservative.

Expected behavior across child connectors:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved records;
- no automatic conversion from observation, specimen, or report to confirmed occurrence truth;
- no assumption that taxonomic identity is settled without downstream resolution;
- no public display of precise sensitive locations without policy review;
- no loss of source geoprivacy, obscuration, rights, license, or attribution metadata;
- unclear rights, sensitivity, geoprivacy, or taxonomic certainty routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Per-record license missing or unclear | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Sensitive location marker detected | Redact, generalize, quarantine, or deny according to policy. |
| Geoprivacy or obscuration field present | Preserve and enforce; do not de-obscure. |
| Taxon uncertainty unsupported | Carry as candidate evidence only; do not promote. |
| Source response malformed | `ERROR` with safe metadata. |
| Source terms unclear | `NEEDS_VERIFICATION`; no live activation. |

---

## Sensitivity posture

Fauna source material can expose protected ecological information. The folder’s default posture is to preserve source safeguards and require review before any public release.

Minimum posture:

1. Source geoprivacy fields must be preserved.
2. Obscured coordinates must not be reverse-engineered or replaced with precise coordinates.
3. Sensitive precise locations must default to quarantine, redaction, generalization, or deny.
4. Observer, collector, and media metadata must be treated as rights- and privacy-relevant.
5. Public release requires downstream policy checks, redaction profile, EvidenceBundle support, review state, release state, and rollback path.
6. Derived maps, tiles, summaries, vector indexes, and AI-generated text are not sovereign truth.

---

## Validation

Connector-local and group-level validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- timestamps, retrieval metadata, source identifiers, taxon identifiers, and license fields are explicit where available;
- geoprivacy and obscuration fields are preserved;
- sensitive-location indicators route to deny/quarantine/generalization behavior;
- malformed or incomplete responses fail closed;
- occurrence records remain candidate evidence until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this folder.

---

## Definition of done

This connector group is ready for first review when:

- [ ] Directory Rules and ADR review determine whether `connectors/fauna/` is canonical, compatibility-only, or a migration target.
- [ ] Existing source-first fauna connector paths are inventoried before adding more children here.
- [ ] Child connector READMEs link to source catalog entries and source descriptors.
- [ ] Live access is disabled by default across child connectors.
- [ ] Credentials are excluded from source control.
- [ ] Per-record rights/license handling is documented before activation.
- [ ] Geoprivacy fields are preserved and tested.
- [ ] Sensitive precise locations route to deny/quarantine/generalization by default.
- [ ] Connector outputs are limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, empty, geoprivacy, sensitive-location, rights-unclear, and taxon-uncertain cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve whether `connectors/fauna/` is canonical or compatibility-only. | **NEEDS VERIFICATION** | Directory Rules, ADR, repo tree, and migration note. |
| Inventory existing fauna source connector homes under `connectors/`. | **NEEDS VERIFICATION** | Repo tree and search results. |
| Confirm relationship between `connectors/fauna/inaturalist/` and any `connectors/inaturalist/`. | **NEEDS VERIFICATION** | Repo tree, source-catalog metadata, and ADR/migration decision. |
| Confirm child connector test locations. | **NEEDS VERIFICATION** | Test tree and CI workflows. |
| Confirm source descriptor homes and source IDs for fauna connectors. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm per-record license and media-rights handling. | **NEEDS VERIFICATION** | Source profiles, rights policy, and fixture review. |
| Confirm geoprivacy and sensitive-location redaction behavior. | **NEEDS VERIFICATION** | Sensitivity policy, fauna steward review, and redaction profile. |
| Confirm fixture strategy for biodiversity observation/specimen material. | **NEEDS VERIFICATION** | Test fixture registry and sensitivity review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Use this folder cautiously. If `connectors/fauna/` remains in the repo, it should make fauna connector boundaries more inspectable without becoming a parallel source hierarchy. Prefer source-first connector homes unless Directory Rules, ADRs, or migration notes explicitly authorize this domain-group layer.
