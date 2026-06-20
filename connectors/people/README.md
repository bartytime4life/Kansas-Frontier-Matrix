<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-people-readme
title: connectors/people/ — People Connector Alias Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · People-DNA-Land steward · Rights steward · Consent steward · Sensitivity reviewer · Release steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: restricted; alias-lane; highest-sensitivity; deny-by-default; consent-required; source-admission-only
related:
  - ../README.md
  - ../people-dna-land/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../docs/domains/people-dna-land/API_CONTRACTS.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../policy/consent/
  - ../../release/
tags: [kfm, connectors, people, people-dna-land, alias-lane, genealogy, dna, land, consent, rights, sensitivity, restricted, deny-by-default, raw, quarantine, source-admission, governance]
notes:
  - "Draft short-name People connector lane."
  - "This lane does not supersede connectors/people-dna-land/; the fuller restricted connector boundary currently lives there."
  - "Placement is draft / ADR-class: the People lane slug and connector placement are unsettled; neither people/ nor people-dna-land/ should become canonical without an ADR, migration note, or updated Directory Rules."
  - "This is a highest-sensitivity lane. Consent, rights, sensitivity, provenance, and release gates must fail closed."
  - "Connector output may enter quarantine by default and raw only when descriptor, consent, rights, sensitivity, and provenance gates are satisfied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People Connector Alias Lane

> Draft short-name connector lane for People / DNA / Land source material. The fuller restricted connector boundary is `connectors/people-dna-land/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: alias lane" src="https://img.shields.io/badge/scope-alias__lane-blue">
  <img alt="Sensitivity: highest" src="https://img.shields.io/badge/sensitivity-highest-red">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-red">
  <img alt="Lifecycle: quarantine first" src="https://img.shields.io/badge/lifecycle-quarantine__first-orange">
</p>

`connectors/people/`

## Scope

`connectors/people/` is a draft short-name lane for People / DNA / Land connector material.

This README exists to prevent ambiguity between `people` and `people-dna-land` naming. Unless and until an ADR or migration note chooses `connectors/people/` as the canonical connector location, implementation work should prefer the fuller lane documented at `connectors/people-dna-land/`.

This folder must not become a parallel connector implementation, source-family doctrine, person truth, relationship truth, title truth, consent authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/people/`  
> **Truth posture:** the path exists in the repository as this README; whether it should remain an alias, redirect, tombstone, or canonical connector lane remains `NEEDS VERIFICATION` / ADR-class.

---

## Repo fit

```text
connectors/
├── people-dna-land/
│   └── README.md
└── people/
    └── README.md
```

Related responsibility roots:

```text
connectors/people-dna-land/               # fuller restricted connector boundary
connectors/people/                        # this short-name alias/sibling lane
docs/domains/people-dna-land/             # domain doctrine and human-facing control surfaces
data/registry/sources/                    # source descriptors and activation state
data/raw/                                 # raw staged source outputs only after gates clear
data/quarantine/                          # default holding area for unresolved/restricted material
data/receipts/                            # source, consent, rights, review, and transform receipts
data/proofs/                              # EvidenceBundles and proof packs
policy/rights/                            # rights and source-use review
policy/sensitivity/                       # sensitivity review and release constraints
policy/consent/                           # consent constraints and render gates
release/                                  # release decisions, manifests, rollback, correction state
```

---

## Relationship to `connectors/people-dna-land/`

| Path | Status | Use |
|---|---|---|
| `connectors/people-dna-land/README.md` | Existing fuller connector README | Main draft restricted People / DNA / Land connector boundary. |
| `connectors/people/README.md` | This README | Short-name alias/sibling boundary; not canonical until ratified. |

No move, delete, rename, redirect, or deprecation is implied by this README.

---

## Alias-lane contract

`connectors/people/` should remain one of these states until governance resolves it:

1. **Alias lane** — documents that `people` points to the People / DNA / Land connector boundary.
2. **Redirect lane** — keeps a README-only pointer after a migration chooses another canonical location.
3. **Canonical lane** — only if an ADR or Directory Rules update chooses `connectors/people/` and migrates files safely.
4. **Tombstone lane** — only if a migration removes the alias and records rollback guidance.

Do not place active implementation files here while the canonical home is unresolved.

---

## Source admission posture

If this lane is ever activated, it must inherit the People / DNA / Land connector rules:

- preserve source family, source descriptor reference, consent reference when required, rights posture, sensitivity posture, source role, role basis, source date, import date, citation fields, digest, review state, quarantine reason, and release-blocking flags;
- keep outputs quarantine-first and raw only after descriptor, consent, rights, sensitivity, and provenance gates clear;
- require SourceDescriptor activation before live access;
- require consent, rights, sensitivity, source-role, provenance, and release gates to fail closed;
- never treat connector admission as identity truth, relationship truth, title truth, legal determination, consent grant, or publication approval.

---

## Validation

Before relying on this lane, verify:

- an ADR, migration note, or updated Directory Rules decides `people` versus `people-dna-land` naming;
- duplicate connector implementation does not exist in both lanes;
- SourceDescriptors use stable source IDs and do not split identity across aliases;
- tests and fixtures point to the accepted connector home;
- rights, consent, sensitivity, and release documentation use the accepted name consistently;
- rollback steps are documented if files are moved or tombstoned.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] The alias/sibling/canonical/tombstone status is resolved in an ADR, migration note, or Directory Rules update.
- [ ] The accepted connector home is recorded and linked from both naming surfaces if both remain.
- [ ] No duplicate implementation, duplicate fixtures, duplicate SourceDescriptors, duplicate tests, or split release paths exist across `people` and `people-dna-land`.
- [ ] Consent, rights, source-role, provenance, sensitivity, and release gates are inherited from the accepted People / DNA / Land connector boundary.
- [ ] Outputs, if any, are verified to enter quarantine by default and raw only after gates clear.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/people/` is a draft short-name People / DNA / Land alias/sibling lane. It is not the canonical connector home unless ratified. It is not source-family doctrine, person truth, relationship truth, title truth, consent authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
