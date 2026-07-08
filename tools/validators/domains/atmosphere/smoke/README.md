<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-atmosphere-smoke-readme
title: tools/validators/domains/atmosphere/smoke README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-smoke-steward-plus-hazards-liaison-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; atmosphere-smoke-validator; cross-lane; smoke-context; AOD; source-role-aware; alert-authority-deny; release-gated
owning_root: tools/
responsibility: proposed Atmosphere smoke validator lane for SmokeContext, AODRaster, smoke/remote-sensing masks, modeled smoke fields, source-role anti-collapse, freshness/expiry, Hazards seam boundaries, sensitive-join denial, evidence closure, policy/release/correction support, and public-surface denial checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../../README.md
  - ../../../_common/README.md
  - ../README.md
  - ../../README.md
  - ../../../air-hazards/README.md
  - ../../../atmosphere_hazards/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../../../docs/domains/atmosphere/README.md
  - ../../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../../docs/domains/atmosphere/SOURCES.md
  - ../../../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../../policy/domains/atmosphere/
  - ../../../../../policy/release/hazards/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README documents a proposed Atmosphere smoke validator lane. It does not confirm executable files."
  - "Smoke crosses Atmosphere/Air and Hazards. Atmosphere owns atmospheric smoke context, air-quality observations, remote-sensing masks, and model fields; Hazards owns hazard/event and emergency-warning context."
  - "KFM is never an alert authority. Smoke validators must deny life-safety guidance, alert issuance, stale-current claims, model-as-observation collapse, AOD-as-PM2.5 collapse, and unsupported health/exposure/impact claims."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Atmosphere meaning, Hazards meaning, EvidenceBundle content, policy rules, release decisions, or public products."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/atmosphere/smoke

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-atmosphere--smoke-informational)
![alert](https://img.shields.io/badge/alert--authority-never-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/atmosphere/smoke/` is the proposed validator lane for Atmosphere smoke checks: `SmokeContext`, `AODRaster`, smoke/remote-sensing masks, modeled smoke fields, source-role preservation, freshness/expiry, Hazards seam boundaries, sensitive-join denial, evidence closure, release readiness, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/atmosphere/smoke/` exists for validator logic that checks Atmosphere smoke candidates without collapsing smoke context into PM2.5 measurements, AQI reports, ground observations, hazard events, advisory issuance, or life-safety guidance.

The durable KFM question for this lane is:

> Does an Atmosphere smoke candidate preserve source role, product type, time/freshness, uncertainty, rights, sensitivity, Hazards seam boundaries, evidence support, policy posture, release readiness, correction paths, and rollback support before it reaches any governed surface?

The answer should be a deterministic validation result. It should not create Atmosphere truth, Hazards truth, fire-event truth, exposure truth, health guidance, PM2.5 measurements, EvidenceBundles, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/atmosphere/smoke/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Parent `tools/validators/domains/atmosphere/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: atmosphere`; this README is self-bounded. |
| Smoke seam architecture | **CONFIRMED in repo evidence / draft** | `docs/architecture/smoke-atmosphere-hazards.md` defines smoke as an Atmosphere ↔ Hazards seam and states KFM is never an emergency-alert authority. |
| `SmokeContext` contract | **CONFIRMED in repo evidence / draft** | Contract defines source-dependent smoke context and denies PM2.5 measurement, hazard/event truth, life-safety guidance, proof closure, and release approval. |
| `AODRaster` contract | **CONFIRMED in repo evidence / draft** | Contract defines AOD as a remote-sensing mask/proxy and denies PM2.5, AQI, ground-observation, health/safety, public tile, and release claims by default. |
| Paired schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | Exact schema maturity, fixtures, executable names, source registry behavior, policy bundles, report destinations, receipts, and CI integration must be verified before implementation claims. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Atmosphere smoke validator entrypoints | `tools/validators/domains/atmosphere/smoke/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Hazards smoke seam doctrine | `docs/architecture/smoke-atmosphere-hazards.md` |
| Atmosphere domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Hazards event, advisory, and alert-authority posture | `docs/domains/hazards/`, `policy/release/hazards/`, accepted Hazards lanes |
| Smoke/AOD contracts | `contracts/domains/atmosphere/SmokeContext.md`, `AODRaster.md` |
| PM2.5, air observation, forecast, wind, advisory contracts | accepted Atmosphere contract lanes |
| Schemas | `schemas/contracts/v1/domains/atmosphere/` or ADR-selected homes |
| Policy rules | `policy/domains/atmosphere/`, `policy/release/hazards/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/atmosphere/`, `data/registry/sources/hazards/`, or accepted source registry homes |
| EvidenceBundles and proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/atmosphere/smoke/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared smoke/AOD/source-role/freshness/Hazards-seam invariants and delegates meaning to owning domains.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source descriptors, fixtures, policy bundles, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as an Atmosphere contract home, Hazards contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, public runtime surface, alert surface, health/safety surface, or domain-meaning authority.

[Back to top](#top)

---

## Smoke validation invariants

| Invariant | Validator expectation | Fail condition |
|---|---|---|
| Source role preserved | Remote-sensing detection, modeled field, observed sensor, advisory context, AQI report, and regulatory archive roles remain distinct. | HRRR-Smoke or another model field is described as observation; AOD/plume mask is treated as PM2.5. |
| `SmokeContext` boundary preserved | Smoke context remains source-dependent atmospheric context. | Smoke context is presented as PM2.5 measurement, AQI, hazard event, impact claim, exposure claim, or life-safety instruction. |
| `AODRaster` boundary preserved | AOD remains a remote-sensing mask/proxy. | AOD is converted to concentration, AQI, smoke exposure, or public tile without governed method/evidence/release support. |
| Hazards seam preserved | Atmosphere smoke context may cite or be cited by Hazards without becoming event or alert truth. | KFM presents smoke context as emergency alert, evacuation instruction, or issuing authority. |
| Freshness/expiry preserved | Source time, analysis time, model run time, retrieval time, valid time, expiry, and release time remain inspectable. | Expired plume, model run, advisory, or AQI report is displayed as current. |
| Sensitive joins fail closed | Smoke/fire/AOD joins near sensitive habitat, infrastructure, archaeology, people/land, or precise assets require policy/review/release support. | Sensitive join is surfaced publicly without redaction/generalization/review support. |
| Evidence and release support | Public-bound smoke outputs carry required EvidenceBundle, policy, review, release, correction, and rollback references. | Smoke map/export/API/AI answer is surfaced without required trust artifacts. |

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/atmosphere/smoke/` include checks that:

- validate `SmokeContext` candidates against the declared semantic contract;
- validate `AODRaster` candidates against AOD-as-remote-sensing-mask boundaries;
- detect model-as-observation collapse for HRRR-Smoke, BlueSky, CAMS, or other smoke model products;
- detect AOD-as-PM2.5, AOD-as-AQI, and smoke-mask-as-ground-observation collapse;
- check source time, analysis time, model-run time, retrieval time, valid time, expiry, release time, and correction time posture;
- require source-role labels, uncertainty labels, model-run receipts, and product lineage where configured;
- require policy/review/release support for public-bound smoke maps, tiles, summaries, exports, and AI answers;
- deny life-safety guidance, alert issuance, emergency action advice, unsupported health claims, exposure claims, or impact claims;
- route Hazards-seam claims to Hazards-owned event/advisory authority where required;
- require correction, supersession, and rollback support for public-bound smoke products.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/atmosphere/smoke/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere contracts | `contracts/domains/atmosphere/` |
| Hazards contracts or event truth | accepted Hazards contract/domain lanes |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, or receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Public API, UI, map, export, tile, alert, or AI runtime code | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Smoke validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks source role or product lineage;
- collapses model output, remote-sensing mask, advisory context, or observation into another role;
- displays stale plume/model/advisory/AQI context as current;
- claims KFM issues, confirms, or replaces an emergency alert;
- offers life-safety, health, exposure, impact, evacuation, or emergency-action guidance;
- joins smoke/fire/AOD context to sensitive places, assets, people/land, habitat, or infrastructure without policy/review/release support;
- maps, exports, tiles, summarizes, or answers with smoke context without EvidenceBundle, policy, review, release, correction, and rollback support;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `ATMO_SMOKE_VALIDATION_PASS` | Configured Atmosphere smoke checks passed. |
| `ATMO_SMOKE_VALIDATION_FAIL` | Configured checks failed. |
| `SOURCE_ROLE_MISSING` | Required source-role or knowledge-character label is absent. |
| `MODEL_AS_OBSERVATION_DENIED` | Modeled smoke field is presented as observed fact. |
| `AOD_AS_PM25_DENIED` | AOD, mask, or plume proxy is treated as PM2.5 concentration. |
| `SMOKE_CONTEXT_BOUNDARY_COLLAPSE` | `SmokeContext` is treated as PM2.5, AQI, hazard event, advisory, exposure, or impact truth. |
| `ALERT_AUTHORITY_DENIED` | Candidate presents KFM as an emergency-alert or life-safety authority. |
| `FRESHNESS_WINDOW_EXPIRED` | Smoke source, plume, model run, advisory, or report is stale for the claimed use. |
| `SENSITIVE_JOIN_DENIED` | Sensitive smoke/fire/AOD join is unsafe without review/release controls. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, rollback target, or correction path is absent. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/atmosphere/smoke/
├── README.md
├── test_atmosphere_smoke_validators.py
└── fixtures/
    ├── valid_smoke_context_remote_sensing_mask/
    ├── valid_smoke_context_model_field/
    ├── aod_as_pm25_denied/
    ├── model_as_observation_denied/
    ├── expired_hms_plume_denied/
    ├── stale_advisory_context_denied/
    ├── alert_authority_denied/
    ├── sensitive_join_denied/
    ├── evidence_ref_missing/
    └── missing_release_reference/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/atmosphere/smoke
```

```bash
python tools/validators/domains/atmosphere/smoke/validate_smoke_context.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_smoke_context.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Atmosphere/Hazards contracts rather than defining meaning locally.
- [ ] Validator reads declared schemas and policy rather than defining shape or policy locally.
- [ ] `SmokeContext`, `AODRaster`, PM2.5, AQI, forecast/model, advisory, and Hazards event meanings remain distinct.
- [ ] Source role, product lineage, uncertainty, and freshness windows are visible.
- [ ] KFM is never presented as alert authority or life-safety source.
- [ ] Sensitive smoke/fire/AOD joins fail closed without accepted policy/review/release support.
- [ ] EvidenceBundle, policy, review, release, rollback, and correction support are checked where required.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual smoke validator scripts, schema paths, Atmosphere/Hazards source descriptors, policy bundles, fixtures, receipts, report destinations, freshness thresholds, sensitive-join behavior, and CI wiring before promoting this lane beyond draft. |
