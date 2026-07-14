<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-agriculture-readme
title: configs/domains/agriculture/ — Agriculture Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Agriculture steward · Privacy steward · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; agriculture; privacy-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/agriculture/README.md
truth_posture: CONFIRMED canonical agriculture slug, repository-present parent config contract, repository-present Agriculture doctrine, and documentation-only lane / PROPOSED future consumer-bound templates / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, rights review, aggregation thresholds, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, or publish an Agriculture configuration payload."
  - "v0.2 expands the Agriculture-specific scope, source-role, privacy, aggregation, validation, correction, and rollback contract without creating a new policy, schema, registry, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Domain Configuration

`configs/domains/agriculture/`

> Safe-to-commit, Agriculture-specific configuration documentation and future consumer-bound templates. This lane does not own agricultural truth, source admission, policy, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Privacy](#privacy-aggregation-and-sensitive-data) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Agriculture payload, loader, consumer binding, or activation is established by this README

> [!CAUTION]
> Directory presence, a future configuration file, or a parsed value must never trigger source activation, field-level exposure, operator identification, lifecycle promotion, release, or publication. Missing or ambiguous privacy, rights, policy, or evidence support must fail closed.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Agriculture lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide what agricultural claims are true, which sources are admissible, whether sensitive detail may be exposed, or whether an artifact may be released.

This README is intended for:

- Agriculture domain stewards;
- configuration and developer-experience maintainers;
- privacy, rights, sensitivity, policy, and release reviewers;
- package, pipeline, app, runtime, test, and tooling owners that may consume Agriculture configuration;
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Agriculture domain meaning | **None.** Domain doctrine remains in [`docs/domains/agriculture/`](../../../docs/domains/agriculture/README.md). |
| Source identity, role, rights, and activation | **None.** These require the applicable source registry, connector, policy, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Policy or sensitivity decision | **None.** A value may select an already-governed profile; it cannot create or weaken policy. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or convert an estimate into an observation. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority by repetition, proximity, or successful parsing.

[Back to top](#top)

---

## Status

### Confirmed

- `agriculture` is a canonical KFM domain slug.
- The repository contains a parent domain-configuration contract at [`configs/domains/README.md`](../README.md).
- The repository contains Agriculture doctrine at [`docs/domains/agriculture/README.md`](../../../docs/domains/agriculture/README.md).
- This lane currently contains a documentation boundary only.
- The parent contract treats domain configuration as non-secret, non-authoritative, and inactive unless a consumer and validation path are verified.

### Proposed

- Future templates or examples for explicitly named Agriculture consumers.
- Conservative defaults for review routing, aggregation, hold, abstention, generalization, or display behavior when those values select already-governed profiles.
- Migration notes for a real Agriculture configuration key or path change.

### Unknown

- Current Agriculture configuration consumers.
- File discovery, loader behavior, merge order, precedence, override rules, and unknown-key handling.
- Executable schema binding, validators, fixtures, tests, CI enforcement, deployment integration, and runtime use.
- Accepted owners and CODEOWNERS enforcement for this lane.

### Needs verification before the first payload

- the exact consumer and owning package, app, pipeline, service, or tool;
- the accepted file format and version;
- the canonical schema or contract reference;
- privacy, aggregation, geoprivacy, rights, policy, and release review requirements;
- deterministic validation and no-network tests;
- rollback, deactivation, migration, and correction behavior;
- the precedence rule relative to default, environment, local, test, deployment, and runtime settings.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, bounded, non-secret Agriculture configuration support for a named consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define the configuration boundary. | Preserve non-authority, privacy, rights, evidence, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Synthetic values only; clearly non-operational; no automatic discovery. |
| Conservative review defaults | Select an existing hold, abstain, generalize, redact, or review profile. | Cannot reduce policy or release burden. |
| Public-safe display hints | Select a verified generalized display profile. | Must not contain exact protected geometry or grant exposure. |
| Migration notes | Document a real key or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |

Examples must remain synthetic and must not resemble a real operator, parcel, field, facility, or protected location closely enough to enable reconstruction.

### What does not belong here

- private producer, operator, tenant, employee, or living-person data;
- person-parcel, operator-field, ownership, title, or identity joins;
- exact field boundaries, facility coordinates, well locations, storage locations, or other reconstructable sensitive detail;
- real crop, livestock, yield, irrigation, conservation, survey, market, assessor, or source payloads;
- credentials, tokens, connection strings, private endpoints, workstation paths, or deployment secrets;
- source admission, activation, cadence, authority-role, rights, or license decisions;
- schemas, contracts, policy, registries, receipts, proofs, manifests, release records, or publication decisions;
- settings that present modeled, inferred, estimated, or classified outputs as direct observations;
- settings that treat assessor records as title truth or agricultural estimates as operator-confirmed facts;
- hidden bypasses for aggregation, redaction, review, deny, abstain, quarantine, or release gates;
- auto-discovery behavior based only on directory or filename presence.

[Back to top](#top)

---

## Repository fit

This directory is a child of the canonical domain-configuration boundary:

```text
configs/
└── domains/
    ├── README.md
    └── agriculture/
        └── README.md
```

The responsibility split is:

- [`configs/`](../../README.md): repository-wide safe configuration boundary;
- [`configs/domains/`](../README.md): common rules for domain-scoped defaults and templates;
- `configs/domains/agriculture/`: Agriculture-specific configuration support;
- [`docs/domains/agriculture/`](../../../docs/domains/agriculture/README.md): Agriculture doctrine, ubiquitous language, objects, source families, sensitivity, and lifecycle expectations;
- source registries, connectors, contracts, schemas, policy, tests, receipts, proofs, catalogs, and release surfaces: their own canonical responsibility roots.

This README must not duplicate those authorities. It should link to them once verified.

[Back to top](#top)

---

## Inputs

A future Agriculture configuration payload requires all of the following:

1. **Named consumer** — exact package, app, pipeline, service, runtime, test harness, or tool.
2. **Declared format** — file type, format version, and canonical parser.
3. **Authority references** — verified contract, schema, policy, source registry, and domain documentation as applicable.
4. **Safe values** — synthetic placeholders or non-sensitive defaults only.
5. **Source-role separation** — aggregate, field-candidate, survey, modeled, inferred, assessor, and private roles remain distinguishable.
6. **Privacy and rights review** — aggregation, geoprivacy, living-person, operator, parcel, field, facility, and redistribution risks are reviewed.
7. **Validation path** — deterministic parsing, schema checks, semantic checks, no-network fixtures, and expected finite outcomes.
8. **Precedence rule** — explicit relation to defaults, environment, local, test, deployment, command-line, and runtime overlays.
9. **Failure posture** — deny, abstain, hold, quarantine, or error behavior is explicit and fail-safe.
10. **Rollback path** — prior known-good configuration, deactivation behavior, and correction lineage are identified.

A payload that lacks any required item remains **PROPOSED** and must not be treated as active.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated configuration file may support a named consumer by selecting safe, already-governed behavior. It may not:

- admit or activate a source;
- identify a producer or operator;
- expose a field or facility;
- waive aggregation, redaction, rights, policy, review, or release requirements;
- create evidence or establish claim truth;
- promote an object through the trust membrane;
- create a receipt, proof, catalog entry, release record, or publication state.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should document, in the file or an adjacent verified specification:

| Field | Required meaning |
|---|---|
| Consumer | Exact component that reads the file. |
| Purpose | One bounded behavior supported by the file. |
| Format and version | Parser-visible type and compatibility version. |
| Canonical authority references | Schema, contract, policy, registry, and domain links without duplicated normative text. |
| Defaults | Safe, non-secret, fail-closed values. |
| Allowed overrides | Explicitly bounded override sources and keys. |
| Precedence | Deterministic merge or replacement order. |
| Unknown-key behavior | Reject, warn, or ignore; never left implicit. |
| Sensitivity posture | Applicable tiers, aggregation, generalization, and restricted fields. |
| Source-role behavior | How aggregate, modeled, inferred, survey, field-candidate, and private roles remain separate. |
| Finite outcomes | Expected `ANSWER`, `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` behavior where applicable. |
| Validation | Parser, schema, semantic, privacy, rights, and no-network checks. |
| Observability | Safe diagnostics without secrets or sensitive values. |
| Correction and rollback | Prior version, migration, deactivation, and revert path. |

No value may grant authority that the referenced canonical surface does not already provide.

[Back to top](#top)

---

## Privacy, aggregation, and sensitive data

Agriculture configuration must preserve the doctrine that field-level and operator-level detail is denied by default on public surfaces.

### Required safeguards

- Public-safe behavior must prefer county, HUC, grid, or another verified aggregation profile.
- A configuration file may select a governed aggregation or generalization profile; it must not define an unreviewed privacy threshold as policy.
- Exact field, facility, well, storage, and operator-linked detail must remain restricted unless rights, sensitivity, policy, evidence, and release review explicitly allow it.
- Person-parcel and operator-field joins must remain outside ordinary public configuration and public display paths.
- Small-cell, sparse-category, temporal differencing, and cross-layer reconstruction risks must be considered before a public-safe profile is selected.
- Missing rights, redistribution, or attribution support must produce a hold, denial, abstention, quarantine, or other fail-closed outcome.

### Source-role safeguards

Configuration must not collapse:

- direct observation into model output;
- field candidate into confirmed field boundary;
- survey estimate into operator-confirmed fact;
- assessor or parcel data into title truth;
- contextual source into primary evidence;
- derived indicator into canonical source truth.

[Back to top](#top)

---

## Validation

### Current document checks

- One H1 and logical heading hierarchy.
- Repository-relative links target known responsibility roots.
- No credential, private endpoint, personal path, operator identity, parcel join, exact sensitive geometry, or real source payload is present.
- Aggregate, field-candidate, survey, modeled, inferred, assessor, and private roles remain distinct.
- The README does not create a schema, contract, policy, registry, receipt, proof, release, or publication authority.
- Executable configuration validation is **NOT APPLICABLE** while no payload and consumer are established.

### Required checks for a future payload

| Check | Expected result |
|---|---|
| Parse and format validation | File is deterministic and accepted by the named parser. |
| Schema or contract validation | File conforms to the canonical referenced authority. |
| Unknown-key test | Behavior is explicit and tested. |
| Precedence test | Merge or replacement order is deterministic. |
| No-network fixture test | Validation does not require live external services. |
| Secret and private-data scan | No credentials, private endpoints, paths, or protected records. |
| Sensitivity and reconstruction review | No unsafe field, operator, parcel, facility, or small-cell exposure. |
| Source-role test | Modeled, inferred, survey, aggregate, candidate, and private roles remain distinguishable. |
| Fail-closed test | Missing rights, policy, evidence, or review produces a safe finite outcome. |
| Rollback test | Prior known-good behavior can be restored without history rewrite. |

A successful parse does not prove that the values are authorized, safe, active, or publication-ready.

[Back to top](#top)

---

## Failure behavior

A future consumer must treat malformed, unknown, stale, unauthorized, rights-uncertain, or sensitivity-unsafe Agriculture configuration conservatively.

Expected behavior should be chosen from the consumer's verified finite outcomes, such as:

- `ABSTAIN` when evidence or meaning is insufficient;
- `DENY` when policy or sensitivity prohibits the requested behavior;
- `HOLD` when review, rights, aggregation, or release state is incomplete;
- `ERROR` when the file cannot be parsed or validated safely.

The consumer must not silently substitute permissive defaults, expose exact detail, activate a source, or continue publication behavior after a validation failure.

[Back to top](#top)

---

## Review burden

README-only changes require configuration/documentation review and Agriculture domain review.

A future payload also requires, as applicable:

- consumer-owner review;
- schema or contract review;
- privacy, aggregation, sensitivity, and geoprivacy review;
- source-rights and attribution review;
- policy and release review;
- validation and test review;
- security review for secret, endpoint, path, and diagnostic handling.

No single reviewer or config owner may convert configuration into source, evidence, policy, release, or publication authority.

[Back to top](#top)

---

## Maintenance

Before adding or changing a non-README file:

- [ ] Confirm the exact consumer and owner.
- [ ] Confirm the file format, version, parser, and canonical schema or contract.
- [ ] Confirm the change does not create a parallel authority.
- [ ] Confirm values are synthetic, non-secret, and safe for a public repository.
- [ ] Confirm source roles remain distinct.
- [ ] Confirm aggregation, privacy, rights, and sensitivity behavior fails closed.
- [ ] Confirm precedence and unknown-key behavior.
- [ ] Add deterministic no-network fixtures and tests.
- [ ] Record migration, deactivation, correction, and rollback behavior.
- [ ] Verify directory placement, ADR implications, drift-register impact, links, and navigation.
- [ ] Confirm directory or filename presence does not trigger automatic activation.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/agriculture/README.md`](../../../docs/domains/agriculture/README.md) — Agriculture doctrine and domain boundary.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — known placement and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — repository placement law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

A separate ADR or other accepted governance decision is required before this lane is used to:

- redefine the canonical Agriculture domain boundary;
- establish a new schema, contract, policy, source-registry, receipt, proof, release, or publication authority;
- create universal domain-config discovery or precedence behavior;
- alter public aggregation, privacy, sensitivity, geoprivacy, rights, or release controls;
- make directory presence or filename convention an activation mechanism.

[Back to top](#top)

---

## Rollback and correction

For this documentation boundary, rollback means a transparent revert of the commit that changed this file, followed by link and Markdown validation.

For a future payload:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. restore the recorded prior known-good version;
3. re-run parse, schema, semantic, privacy, rights, fail-closed, and no-network checks;
4. preserve the correction lineage and explain the affected behavior;
5. create any required correction, withdrawal, or replacement record in its canonical authority surface.

Do not reset, force-push, rewrite shared history, or claim that deleting a file erases previously released behavior.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@a5015c9047f6211a575748485a7485cc7271a6d1`.

Review again before the first non-README payload, consumer binding, precedence rule, source-related setting, privacy threshold selection, or runtime activation.
