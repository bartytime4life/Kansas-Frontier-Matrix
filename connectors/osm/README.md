<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-osm-readme
title: connectors/osm/ — OSM Connector Alias Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · OpenStreetMap steward · Roads-Rail-Trade steward · Settlements-Infrastructure steward · Spatial Foundation steward · Rights steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; alias-lane; volunteered-geographic-information; attribution-required; source-admission-only
related:
  - ../README.md
  - ../openstreetmap/README.md
  - ../openstreetmap/src/README.md
  - ../openstreetmap/src/openstreetmap/README.md
  - ../openstreetmap/tests/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../docs/sources/catalog/README.md
  - ../../docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, osm, openstreetmap, alias-lane, volunteered-geographic-information, attribution, odbl, raw, quarantine, source-admission, governance]
notes:
  - "Draft short-name OSM connector lane."
  - "This lane does not supersede connectors/openstreetmap/; the fuller OpenStreetMap connector boundary currently lives there."
  - "Placement is draft / ADR-class: neither osm/ nor openstreetmap/ is listed in Directory Rules §7.3 canonical connector roots unless later ratified."
  - "No dedicated docs/sources/catalog/openstreetmap product page was found during parent connector documentation; source-family and product doctrine remain NEEDS VERIFICATION."
  - "Connector output may enter raw or quarantine admission lanes only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# OSM Connector Alias Lane

> Draft short-name connector lane for OpenStreetMap source material. The fuller connector boundary is `connectors/openstreetmap/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: alias lane" src="https://img.shields.io/badge/scope-alias__lane-blue">
  <img alt="Placement: needs ADR" src="https://img.shields.io/badge/placement-NEEDS__ADR-orange">
  <img alt="Rights: attribution required" src="https://img.shields.io/badge/rights-attribution__required-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/osm/`

## Scope

`connectors/osm/` is a draft short-name lane for OpenStreetMap connector material.

This README exists to prevent ambiguity between `osm` and `openstreetmap` naming. Unless and until an ADR or migration note chooses `connectors/osm/` as the canonical location, implementation work should prefer the fuller lane documented at `connectors/openstreetmap/`.

This folder must not become a parallel connector implementation, source-family doctrine, domain truth, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/osm/`  
> **Truth posture:** the path exists in the repository as this README; whether it should remain an alias, redirect, tombstone, or canonical connector lane remains `NEEDS VERIFICATION` / ADR-class.

---

## Repo fit

```text
connectors/
├── openstreetmap/
│   ├── README.md
│   ├── src/
│   │   ├── README.md
│   │   └── openstreetmap/
│   │       └── README.md
│   └── tests/
│       └── README.md
└── osm/
    └── README.md
```

Related responsibility roots:

```text
connectors/openstreetmap/                 # fuller draft OpenStreetMap connector lane
connectors/osm/                           # this short-name alias/sibling lane
docs/domains/roads-rail-trade/            # roads / trails / routing-context adjacency
docs/domains/settlements-infrastructure/  # places and infrastructure context
docs/sources/catalog/                     # source-family/product doctrine; OSM page currently NEEDS VERIFICATION
data/registry/sources/                    # source descriptors and activation state
data/raw/                                 # raw staged source outputs by owning domain
data/quarantine/                          # held material requiring source/role/rights/sensitivity review
data/receipts/                            # ingest, checksum, query, transform, and review receipts
data/proofs/                              # EvidenceBundles and proof packs
policy/rights/                            # attribution, license, share-alike, and source-use review
policy/sensitivity/                       # location and release rules
release/                                  # release decisions, manifests, rollback, correction state
```

---

## Relationship to `connectors/openstreetmap/`

| Path | Status | Use |
|---|---|---|
| `connectors/openstreetmap/README.md` | Existing fuller connector README | Main draft OpenStreetMap connector boundary. |
| `connectors/openstreetmap/src/README.md` | Existing source-root README | Source-code root boundary. |
| `connectors/openstreetmap/src/openstreetmap/README.md` | Existing package README | Importable package boundary. |
| `connectors/openstreetmap/tests/README.md` | Existing tests README | No-network test boundary. |
| `connectors/osm/README.md` | This README | Short-name alias/sibling boundary; not canonical until ratified. |

No move, delete, rename, redirect, or deprecation is implied by this README.

---

## Alias-lane contract

`connectors/osm/` should remain one of these states until governance resolves it:

1. **Alias lane** — documents that `osm` means OpenStreetMap and points to `connectors/openstreetmap/`.
2. **Redirect lane** — keeps a README-only pointer after a migration chooses `connectors/openstreetmap/`.
3. **Canonical lane** — only if an ADR or Directory Rules update chooses `connectors/osm/` and migrates files safely.
4. **Tombstone lane** — only if a migration removes the alias and records rollback guidance.

Do not place active implementation files here while the canonical home is unresolved.

---

## Source admission posture

If this lane is ever activated, it must inherit the OpenStreetMap connector rules:

- preserve provider/extract source, query or manifest, source date, retrieval time, file identity, digest, OSM element type/id/version, timestamp, tags, geometry, relation context, source URL, attribution posture, license-review posture, source-role posture, completeness caveat, sensitivity posture, conflict status, and quarantine reason when review is required;
- keep all outputs limited to raw or quarantine admission envelopes;
- require SourceDescriptor activation before live access;
- require rights, attribution, provider terms, source-role, freshness, completeness, and sensitivity gates to fail closed.

---

## Validation

Before relying on this lane, verify:

- an ADR, migration note, or updated Directory Rules decides `osm` versus `openstreetmap` naming;
- duplicate connector implementation does not exist in both lanes;
- SourceDescriptors use stable source IDs and do not split identity across aliases;
- tests and fixtures point to the accepted connector home;
- rights, attribution, and release documentation use the accepted name consistently;
- rollback steps are documented if files are moved or tombstoned.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] The alias/sibling/canonical/tombstone status is resolved in an ADR, migration note, or Directory Rules update.
- [ ] The accepted connector home is recorded and linked from both naming surfaces if both remain.
- [ ] No duplicate implementation, duplicate fixtures, duplicate SourceDescriptors, duplicate tests, or split release paths exist across `osm` and `openstreetmap`.
- [ ] Rights, attribution, source-role, freshness, completeness, and sensitivity gates are inherited from the accepted OpenStreetMap connector boundary.
- [ ] Outputs, if any, are verified to enter only raw or quarantine admission lanes.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/osm/` is a draft short-name OpenStreetMap alias/sibling lane. It is not the canonical connector home unless ratified. It is not source-family doctrine, domain truth, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public map authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
