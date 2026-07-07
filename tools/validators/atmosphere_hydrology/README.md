<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-atmosphere-hydrology-readme
title: tools/validators/atmosphere_hydrology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-hydrology-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; atmosphere-hydrology; precipitation-forcing-aware
owning_root: tools/
responsibility: proposed cross-domain validator lane for Atmosphere/Air evidence cited by Hydrology claims, including precipitation, drought, flood-weather forcing, source-role, evidence, freshness, correction, lifecycle, regulatory-context, and release-boundary checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/atmosphere/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/CROSSWALK_RULES.md
  - ../../../contracts/domains/atmosphere/
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../policy/domains/atmosphere/
  - ../../../policy/domains/hydrology/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed cross-domain validator lane. It does not confirm executable files."
  - "Atmosphere/Air owns atmospheric context. Hydrology owns water-system identity, observations, regulatory flood context, and hydrologic interpretation. Validators must not collapse those responsibilities."
  - "Validators enforce declared contracts, schemas, and policy. They do not create EvidenceBundles, define source roles, approve release, publish public outputs, or provide emergency/life-safety warnings."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/atmosphere_hydrology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-atmosphere--hydrology--validators-informational)
![edge](https://img.shields.io/badge/edge-precipitation--forcing-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/atmosphere_hydrology/` is the proposed cross-domain validator lane for Hydrology products that cite Atmosphere/Air evidence: precipitation, drought, flood-weather forcing, weather observations, model fields, freshness, correction propagation, regulatory-vs-observed separation, source-role discipline, and public-release boundaries.

---

## Purpose

`tools/validators/atmosphere_hydrology/` exists for validator logic that is genuinely cross-domain between Atmosphere/Air and Hydrology.

The durable KFM question for this lane is:

> Does a Hydrology candidate cite Atmosphere/Air evidence without re-owning atmospheric truth, collapsing modeled/observed/regulatory roles, treating regulatory context as observed condition, or skipping evidence, lifecycle, correction, policy, and release gates?

The answer should be a deterministic validation result. It should not create atmospheric observations, hydrologic observations, NFHL claims, hydrograph truth, EvidenceBundles, policy decisions, release decisions, emergency messages, or map/API products.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/atmosphere_hydrology/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Atmosphere/Hydrology edge | **CONFIRMED in repo evidence / draft** | Atmosphere cross-lane docs list Hydrology as a consumer of precipitation, drought, and flood-weather forcing while preserving ownership, source role, sensitivity, and EvidenceBundle support. |
| Hydrology boundary | **CONFIRMED in repo evidence / draft** | Hydrology owns gauges, time series, watersheds, reaches, NFHL regulatory context, and hydrographic interpretation; it is not an emergency warning system. |
| Source-role anti-collapse posture | **CONFIRMED in repo evidence / draft** | Atmosphere and Hydrology docs deny AQI/AOD/model/observation collapse and NFHL/observed/model/warning collapse. |
| Contract/schema paths | **PROPOSED / NEEDS VERIFICATION** | Domain-specific schema and contract homes require path verification before implementation claims. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove policy bundles, source descriptors, release gates, or CI are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Cross-domain Atmosphere/Hydrology validator entrypoints | `tools/validators/atmosphere_hydrology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Atmosphere/Air schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy rules | `policy/domains/atmosphere/`, `policy/domains/hydrology/`, or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/atmosphere_hydrology/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it validates a cross-lane invariant and reads declared contracts, schemas, policy, and source descriptors.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, public runtime surface, or emergency-warning surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/atmosphere_hydrology/` include checks that:

- preserve Atmosphere/Air ownership of precipitation, temperature, wind, weather observation, weather station, forecast/model, climate normal, climate anomaly, and advisory context evidence;
- preserve Hydrology ownership of watersheds, HUC units, reaches, gauges, flow observations, water-level observations, water-quality observations, NFHL regulatory context, hydrographs, and upstream traces;
- prevent modeled precipitation, forecast fields, radar estimates, or climate context from being presented as observed hydrologic measurements;
- prevent hydrologic model output from being relabeled as gauge observation;
- prevent NFHL or other regulatory context from being treated as observed inundation or forecast flooding;
- require SourceDescriptor role, authority, rights, sensitivity, cadence, and freshness posture for cited Atmosphere/Air evidence;
- require EvidenceRef or EvidenceBundle support for public-bound hydrology claims;
- require correction propagation when cited Atmosphere/Air evidence is revised, superseded, stale, or version-changed;
- enforce `ABSTAIN`, `DENY`, `NARROWED`, or `BOUNDED` behavior for governed-AI surfaces when evidence or policy is insufficient.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/atmosphere_hydrology/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air contracts | `contracts/domains/atmosphere/` |
| Hydrology contracts | `contracts/domains/hydrology/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/` lifecycle roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Connectors or pipelines | `connectors/`, `pipelines/` |
| Emergency, warning, or life-safety products | official authorities outside KFM; KFM only carries governed context |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Cross-domain validation posture

This validator lane is for ownership, source-role, evidence, freshness, regulatory-context, and release-boundary anti-collapse checks.

It should fail closed, narrow, or route to review when a candidate collapses:

- modeled atmospheric output into observed hydrologic measurement;
- aggregate climate baseline into per-gauge or per-reach truth;
- radar/model precipitation into observed gauge rainfall without proper role marking;
- NFHL regulatory context into observed flood extent;
- modeled hydrograph into observed flow or water level;
- expired or stale advisory context into current state;
- Atmosphere-owned observations into Hydrology-owned data;
- Hydrology-owned interpretation into Atmosphere-owned measurement.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `ATM_HYD_VALIDATION_PASS` | Configured Atmosphere/Hydrology cross-domain checks passed. |
| `ATM_HYD_VALIDATION_FAIL` | Configured checks failed. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses modeled, observed, aggregate, regulatory, candidate, or synthetic roles. |
| `ATMOSPHERE_OWNERSHIP_CONFLICT` | Hydrology candidate appears to redefine or re-own Atmosphere/Air evidence. |
| `HYDROLOGY_OWNERSHIP_CONFLICT` | Atmospheric context is being used to claim unsupported Hydrology truth. |
| `REGULATORY_OBSERVED_COLLAPSE` | Regulatory flood context is treated as observed inundation or forecast truth. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `FRESHNESS_OR_CORRECTION_REQUIRED` | Stale, superseded, corrected, or unversioned evidence requires action. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `EMERGENCY_BOUNDARY_DENIED` | Candidate attempts to turn KFM context into warning or life-safety instruction. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/atmosphere_hydrology/
├── README.md
├── test_atmosphere_hydrology_validators.py
└── fixtures/
    ├── valid_precipitation_forcing_context/
    ├── modeled_precip_as_gauge_obs_denied/
    ├── nfhl_as_observed_flood_denied/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── stale_atmosphere_source_abstain/
    ├── model_hydrograph_as_observation_denied/
    └── emergency_boundary_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/atmosphere_hydrology
```

```bash
python tools/validators/atmosphere_hydrology/validate_atmosphere_hydrology_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_atmosphere_hydrology_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Atmosphere/Air and Hydrology ownership boundaries are preserved.
- [ ] Source-role and knowledge-character fields are explicit.
- [ ] Modeled, observed, aggregate, regulatory, candidate, and synthetic records remain distinct.
- [ ] NFHL and regulatory contexts are not treated as observed inundation or forecast truth.
- [ ] Public-bound hydrology products require EvidenceRef or EvidenceBundle support.
- [ ] Corrections and stale-state signals propagate to dependent hydrology products.
- [ ] KFM is not used as an emergency or life-safety system.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify contracts, schemas, policy bundles, source descriptors, fixtures, validator entrypoints, and CI wiring before promoting this lane beyond draft. |
