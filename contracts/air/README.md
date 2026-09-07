<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-air-readme
title: contracts/air/ — Air / Atmosphere Contract Compatibility Index
type: readme
version: v0.2
status: draft; compatibility-index; repository-grounded; non-canonical
owners: OWNER_TBD — Atmosphere steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; air; atmosphere; compatibility-path; semantic-contracts; no-parallel-authority
related:
  - ../README.md
  - ../domains/atmosphere/README.md
  - ../../docs/domains/atmosphere/README.md
  - ../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../docs/domains/atmosphere/API_CONTRACTS.md
  - ../../docs/domains/atmosphere/MAP_UI_CONTRACTS.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/domains/atmosphere/
  - ../../schemas/contracts/v1/air/
  - ../../policy/domains/atmosphere/
  - ../../tests/domains/atmosphere/
  - ../../fixtures/domains/atmosphere/
tags: [kfm, contracts, air, atmosphere, compatibility, semantic-contracts, object-families, weather, air-quality, smoke-context, aod, climate, source-role, evidence, governance]
notes:
  - "This folder currently contains only this README and functions as an air-slug compatibility/index lane."
  - "The repository's current semantic contract home is contracts/domains/atmosphere/. Do not add new canonical contracts under contracts/air/."
  - "The current schema target is schemas/contracts/v1/domains/atmosphere/; schemas/contracts/v1/air/ is a placement placeholder with legacy residue, not a second authority."
  - "Presence of contracts, schemas, policies, fixtures, or tests does not establish source admission, scientific validity, runtime behavior, review, release, deployment, promotion, or publication."
  - "Atmosphere/Air contracts are not emergency advisories, life-safety direction, model truth, or public release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Air / Atmosphere Contract Compatibility Index

> Compatibility and navigation README for the historical contracts/air slug. Current Atmosphere semantic contracts belong under contracts/domains/atmosphere/; this path must not become a parallel authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility index" src="https://img.shields.io/badge/path-compatibility%20index-orange">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-green">
  <img alt="Authority: non-canonical" src="https://img.shields.io/badge/authority-non--canonical-lightgrey">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blue">
</p>

contracts/air/

## Quick jumps

[Status](#status) · [Scope](#scope) · [Placement posture](#placement-posture) · [Repo fit](#repo-fit) · [Current implementation snapshot](#current-implementation-snapshot) · [Accepted content](#accepted-content) · [Exclusions](#exclusions) · [Contract boundaries](#contract-boundaries) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done) · [Last reviewed](#last-reviewed)

---

## Status

> [!IMPORTANT]
> Status: draft / compatibility index
> 
> Owner: OWNER_TBD
> 
> Path: contracts/air/
> 
> Path posture: CONFIRMED as a present compatibility/index lane; contracts/domains/atmosphere/ is the current semantic-contract home.
> 
> Truth posture: The target file, canonical Atmosphere contract lane, schema lanes, policy lane, fixture lane, test lane, root contract guidance, and accepted directory-governance decision were checked against main@81b1cf3a93ea52d18cdf03cfacfd3ee606b8b098. This README records placement and boundaries; it does not promote any implementation or scientific claim.

---

## Scope

contracts/air/ is retained for compatibility with the historical air slug and for a small, explicit pointer to the current Atmosphere contract lane.

The canonical semantic meaning layer currently lives at ../domains/atmosphere/. That lane contains expanded object-family contracts for air observations, PM2.5, ozone, stations, weather, wind, precipitation, temperature, smoke, AOD, climate, forecasts, advisory context, and a finite Atmosphere/Air decision envelope, plus supporting assessment and identity contracts.

This README does not move or delete the compatibility folder. It prevents the folder from being mistaken for a second writable contract root. Any migration, alias retirement, or authority change requires an accepted ADR or a governed migration note.

---

## Placement posture

### Current responsibility split

| Responsibility | Current home | Posture |
|---|---|---|
| Human-readable semantic meaning | contracts/domains/atmosphere/ | CONFIRMED current repository lane; maturity remains mixed. |
| Historical air contract slug | contracts/air/ | CONFIRMED compatibility/index only; no new canonical files. |
| Machine-checkable Atmosphere shapes | schemas/contracts/v1/domains/atmosphere/ | CONFIRMED current domain schema lane; many files remain PROPOSED scaffolds or compatibility mirrors. |
| Historical air schema slug | schemas/contracts/v1/air/ | CONFIRMED placement placeholder with AirStation.schema.json residue; not a parallel authority. |
| Atmosphere policy source | policy/domains/atmosphere/ | CONFIRMED direct rule files; policy README records proposed/default-only, evaluator-unbound posture. |
| Synthetic examples | fixtures/domains/atmosphere/ | CONFIRMED fixture lane with bounded executable profiles and broader inventory gaps. |
| Behavioral proof | tests/domains/atmosphere/ | CONFIRMED test lane with bounded executable profiles and broader semantics still needing verification. |

The accepted Directory Rules decision (ADR-0029) makes placement a responsibility question, not a topic-name preference. A historical alias does not acquire authority merely because it exists or has a familiar slug.

### Compatibility rule

Do not create a new file under contracts/air/ to avoid the canonical Atmosphere lane. If a verified consumer requires an air path, record it as a one-way compatibility/index surface with a canonical target, owner, migration/exit criteria, and rollback plan. Otherwise return HOLD rather than creating parallel authority.

---

## Repo fit

    contracts/
    ├── README.md
    ├── air/
    │   └── README.md                         # this compatibility index
    └── domains/
        └── atmosphere/
            ├── README.md                     # semantic-contract lane
            ├── AirStation.md
            ├── AirObservation.md
            ├── PM25Observation.md
            ├── OzoneObservation.md
            ├── SmokeContext.md
            ├── AODRaster.md
            ├── WeatherStation.md
            ├── WeatherObservation.md
            ├── WindField.md
            ├── PrecipitationObservation.md
            ├── TemperatureObservation.md
            ├── ClimateNormal.md
            ├── ClimateAnomaly.md
            ├── ForecastContext.md
            ├── AdvisoryContext.md
            └── AtmosphereAirDecisionEnvelope.md

| Responsibility root | Role relative to this compatibility index |
|---|---|
| ../README.md | Contracts root: semantic meaning, field intent, invariants, exclusions, and compatibility semantics. |
| ../domains/atmosphere/ | Current Atmosphere/Air semantic-contract authority and object-family index. |
| ../../docs/domains/atmosphere/ | Domain scope, source roles, object families, public boundary, and verification backlog. |
| ../../schemas/contracts/v1/domains/atmosphere/ | Current domain schema lane; machine shape is separate from contract prose. |
| ../../schemas/contracts/v1/air/ | Historical schema placement placeholder; do not add canonical definitions without a governed decision. |
| ../../policy/domains/atmosphere/ | Atmosphere-specific admissibility, anti-collapse, freshness, caveat, and publication policy source. |
| ../../fixtures/domains/atmosphere/ | Deterministic synthetic examples, including valid, invalid, source, and bounded profile lanes. |
| ../../tests/domains/atmosphere/ | No-network and policy/schema/semantic boundary tests. |
| ../../data/registry/sources/ | SourceDescriptor and source-admission responsibility. |
| ../../data/proofs/ | EvidenceBundle and proof objects; contract prose is not proof closure. |
| ../../release/ | Release, correction, rollback, and publication decisions. |

---

## Current implementation snapshot

The current tree contains more than the old compatibility README recorded, but maturity is mixed and must remain bounded:

| Surface | Current evidence at main@81b1cf3a93ea52d18cdf03cfacfd3ee606b8b098 | Limit |
|---|---|---|
| contracts/air/ | Only this README is present. | No object contract is canonical here. |
| contracts/domains/atmosphere/ | 44 direct Markdown files: the parent README, 15 primary object-family contracts, the AtmosphereAirDecisionEnvelope support contract, lowercase compatibility/legacy forms, and supporting identity, validation, reconciliation, sensor, burn, and layer records. | File presence does not establish complete pairing, stewardship, review, scientific validity, or runtime use. |
| schemas/contracts/v1/air/ | README plus AirStation.schema.json. | The README identifies this as a compatibility placeholder; no new canonical schema should be added here. |
| schemas/contracts/v1/domains/atmosphere/ | 72 files plus receipts/ and registry/ directories, including primary shapes, lower/upper-case mirrors, decision/evidence/release/receipt schemas, and source/validation support schemas. | The lane README calls many shapes PROPOSED scaffolds; duplicate naming and strictness require continued verification. |
| policy/domains/atmosphere/ | README plus 13 Rego files. | Policy README records default-only/proposed rules, no accepted bundle, and no evaluator binding. |
| fixtures/domains/atmosphere/ | README plus 11 child lanes. | Bounded profiles are executable; broad payload inventory remains partial. |
| tests/domains/atmosphere/ | README, 16 Python test modules, and six child lanes. | Four standard-library profiles are bounded; passing tests do not establish release or publication. |

---

## Accepted content

Only compatibility/index material belongs in this folder:

- a pointer to ../domains/atmosphere/ as the semantic-contract home;
- migration, alias, drift, or exit notes with an explicit canonical target;
- links to paired Atmosphere schemas, policy, fixtures, tests, source descriptors, proofs, and release records;
- a bounded explanation of why an existing consumer still requires the air slug;
- rollback information for this compatibility pointer.

Any content copied here must be one-way and non-authoritative. Contract meaning, field intent, object invariants, and object-family definitions belong in the canonical Atmosphere lane.

---

## Exclusions

| Does not belong here | Correct home |
|---|---|
| New semantic object contracts | ../domains/atmosphere/ after path/owner verification. |
| JSON Schema or machine shape | ../../schemas/contracts/v1/domains/atmosphere/ after schema pairing and validation review. |
| Historical alias schema definitions | ../../schemas/contracts/v1/air/ only if an accepted migration/compatibility decision explicitly requires them. |
| Rego or executable policy | ../../policy/domains/atmosphere/. |
| Fixture payloads or expected errors | ../../fixtures/domains/atmosphere/. |
| Test code or validator implementations | ../../tests/domains/atmosphere/ and ../../tools/validators/. |
| Source records or live retrieval | ../../data/registry/sources/ and lifecycle-specific data roots. |
| EvidenceBundle, proof, receipt, catalog, or triplet instances | ../../data/ responsibility roots. |
| Release, correction, rollback, or publication authority | ../../release/ and accepted release controls. |
| Emergency warnings, exposure determinations, health guidance, or life-safety direction | Official issuing authorities and the governed Hazards lane; Atmosphere advisory context is referral-only. |
| Public API DTOs, map behavior, or UI rendering | Governed API and application roots after verification. |

---

## Contract boundaries

The canonical Atmosphere contract lane preserves these distinctions. This compatibility README points to them; it does not redefine them:

- AQI is not pollutant concentration.
- AOD is not surface PM2.5.
- Forecast, model, reanalysis, and fusion output is not an observation.
- A low-cost sensor is not automatically equivalent to a regulatory monitor.
- AirNow preliminary/operational context is not an AQS certified archive.
- Smoke, plume, hotspot, or prescribed-burn context is not exposure, health effect, impact proof, or evacuation guidance.
- Climate normal/anomaly context is not a current weather observation.
- Advisory context is not a KFM-issued alert or life-safety instruction.
- A derived raster, tile, graph, dashboard, receipt, or AI answer is not sovereign evidence.
- Receipt, proof, review, promotion, release, deployment, and publication remain separate states.
- Freshness, correction, withdrawal, rights, sensitivity, and source-role state must remain visible.

---

## Lifecycle

The compatibility pointer participates only in navigation; the authority flow remains:

    contracts/air compatibility index
      -> contracts/domains/atmosphere semantic contracts
      -> schemas/contracts/v1/domains/atmosphere
      -> policy/domains/atmosphere
      -> fixtures/domains/atmosphere
      -> tests/domains/atmosphere
      -> data/proofs and validation evidence
      -> release / correction / rollback

This path does not move data, validate an instance, admit a source, make a policy decision, issue an advisory, close evidence, release a layer, or publish a public claim.

---

## Validation

Before adding or retaining anything under contracts/air/, verify:

- a consumer actually requires the historical air path;
- the canonical target remains contracts/domains/atmosphere/;
- the change is a one-way compatibility/index update, not a second semantic contract;
- paired schema, policy, fixture, test, source, proof, release, and rollback links are current;
- any schema reference targets schemas/contracts/v1/domains/atmosphere/ unless an accepted decision says otherwise;
- source roles and knowledge characters remain explicit;
- AQI/concentration, AOD/PM2.5, model/observation, sensor/regulatory, advisory/emergency, and climate/current-time boundaries remain tested or clearly marked as gaps;
- no claim of scientific validity, source admission, public safety, API/UI readiness, release, deployment, promotion, or publication is inferred from file presence or passing tests;
- any alias retirement has an owner, migration evidence, exit criteria, and rollback plan.

Current bounded evidence includes Atmosphere tests for advisory/life-safety separation, AQI/concentration denial, AOD/PM2.5 denial, model/observation separation, no-live-fetch behavior, finite decision outcomes, temporal/unit distinctions, low-cost sensor caveats, prescribed-burn quality flags, and observed/modeled profiles. These are useful proof slices, not complete domain closure.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| contracts/air/README.md before this edit, blob 47c6425000418602a3a351e116a4507a51de67e7 | CONFIRMED | Existing compatibility README and its original boundary intent. | It was not blank; its conflicted/unknown inventory and rollback claims were stale. |
| contracts/domains/atmosphere/README.md, blob 2626d011b5d80e6d58870be3eff817d95116ffc7 | CONFIRMED | Current semantic-contract home, primary object roster, anti-collapse rules, and non-runtime posture. | Mixed contract maturity and schema pairing remain open. |
| schemas/contracts/v1/domains/atmosphere/README.md, blob cad321bf62d7da2a723388d5978e04fbfc694b5b | CONFIRMED | Current Atmosphere schema lane and its proposed/scaffold posture. | Presence and index claims do not prove every schema is strict, accepted, or consumed. |
| schemas/contracts/v1/air/README.md, blob 6f2504a9054769f343cc33424171ebdb80157576 | CONFIRMED | Historical air schema path is a compatibility placeholder; do not add canonical definitions there without a decision. | The legacy AirStation.schema.json residue still needs migration/retirement handling. |
| policy/domains/atmosphere/README.md, blob a300dfd5abda1b58a07fd978935dd40ef232ec71 | CONFIRMED | Direct policy inventory and default-only/evaluator-unbound limits. | Rule presence is not policy activation, bundle acceptance, or runtime enforcement. |
| fixtures/domains/atmosphere/README.md, blob 121ec0e4547384cb14f1a46ca6e93cbdbcc9c4b1 | CONFIRMED | Fixture lanes and bounded executable profiles. | Broader payload inventory and scientific validity remain partial. |
| tests/domains/atmosphere/README.md, blob 29204b56a1e35ff74ba8a2e33bd8a424175e9dab | CONFIRMED | Test-lane responsibility, no-network posture, and bounded profile coverage. | Passing tests do not authorize sources, release, deployment, or publication. |
| docs/domains/atmosphere/README.md, blob 7e7a96a3f22547fd12afcce5dc7ccd82ddd226af | CONFIRMED | Domain scope, Atmosphere/Air/Climate boundary, and non-emergency posture. | Domain documentation is explanatory and subordinate to schemas, policy, evidence, and release authority. |
| contracts/README.md, blob e0b7c126e00a8ac6e8890774ed26cf21aef534ba | CONFIRMED | contracts/ owns semantic meaning and must not become schema, policy, evidence, lifecycle, release, or runtime authority. | Root guidance does not itself migrate aliases. |
| docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md, blob a4de0d7a96b78da59cfc499d1025e1508afd8dd9 | ACCEPTED | Directory Rules v2 placement authority and no-parallel-authority discipline. | Post-adoption migration and independent review remain separate evidence. |
| Drive Atmosphere/Air architecture report and Notion Atmosphere builder page | LINEAGE / read-only | Historical design rationale, source-role distinctions, and coordination posture. | The Drive report explicitly lacked a mounted repository; neither source overrides current GitHub state. |

---

## Rollback

Rollback is required if this README is used to justify creating canonical contracts under contracts/air/, duplicate schema authority under schemas/contracts/v1/air/, unreviewed path migration, source activation, emergency guidance, public release, or runtime behavior.

Rollback target: prior README blob 47c6425000418602a3a351e116a4507a51de67e7.

---

## Definition of done

- [x] The air path is identified as a compatibility/index lane rather than a second contract authority.
- [x] The current semantic contract home and current schema target are linked.
- [x] Current policy, fixture, and test lanes are recorded with bounded maturity limits.
- [x] The old blank-file, unknown-inventory, and obsolete rollback claims are corrected.
- [ ] A verified consumer, owner, canonical target, migration/exit criteria, and rollback plan are recorded for any future alias use.
- [ ] Remaining legacy schema residue under schemas/contracts/v1/air/ is migrated, retired, or explicitly retained by an accepted decision.
- [ ] Contract-to-schema-to-policy-to-fixture-to-test coverage is inventoried without promoting scaffolds to accepted authority.
- [ ] Independent stewardship, review, scientific validity, source admission, release, deployment, promotion, and publication evidence are closed where applicable.

---

## Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-09-07 |
| Repository | bartytime4life/Kansas-Frontier-Matrix |
| Base ref | main@81b1cf3a93ea52d18cdf03cfacfd3ee606b8b098 |
| Prior target blob | 47c6425000418602a3a351e116a4507a51de67e7 |
| Canonical contract README blob | 2626d011b5d80e6d58870be3eff817d95116ffc7 |
| Canonical schema README blob | cad321bf62d7da2a723388d5978e04fbfc694b5b |
| Change posture | Documentation-only compatibility-index refresh; draft PR recommended; no migration, merge, release, deployment, promotion, or publication claimed. |

Re-check the exact current tree before merging if the base branch moves or if a contract/schema migration lands.

---

## Status summary

contracts/air/ is a repository-grounded compatibility/index lane for the historical Air slug. The current semantic contract authority is contracts/domains/atmosphere/, the current schema target is schemas/contracts/v1/domains/atmosphere/, and Atmosphere policy, fixture, and test lanes contain bounded work with mixed maturity. This README is not a contract, schema, policy, source registry, proof, release, emergency-alert, API, UI, runtime, or publication authority.

<p align="right"><a href="#top">Back to top</a></p>

