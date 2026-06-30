<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://example/focus-flow/hydrology-huc12-question
title: Hydrology HUC12 Focus Question Example
type: example
version: v0.1.0
status: draft
owners: TODO(owner): examples steward; TODO(owner): Focus Mode steward; TODO(owner): governed API steward; TODO(owner): hydrology steward; TODO(owner): evidence steward; TODO(owner): policy steward; TODO(owner): UI steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - greenfield placeholder existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related: [README.md, ../evidence_bundles/README.md, ../../docs/architecture/governed-ai/FOCUS_FLOW.md, ../../docs/architecture/governed-api.md, ../../apps/explorer-web/src/features/focus_panel/README.md, ../../apps/governed-api/README.md, ../../docs/domains/hydrology/README.md, ../../data/proofs/evidence_bundle/README.md, ../../data/catalog/domain/hydrology/README.md, ../../data/proofs/hydrology/README.md, ../../data/published/layers/hydrology/README.md, ../../policy/focus/README.md]
tags: [kfm, examples, focus-flow, focus-mode, hydrology, huc12, watershed, governed-api, governed-ai, evidence-ref, evidence-bundle, citation-validation, finite-outcomes, abstain, deny, no-public-path, non-authoritative, cite-or-abstain]
notes: ["This file replaces a greenfield placeholder at `examples/focus_flows/hydrology_huc12_question.md`.", "This example is synthetic and non-authoritative. It does not assert real HUC12 facts, water conditions, flood status, regulatory determinations, emergency guidance, or source truth.", "The expected outcome is `ABSTAIN` because the example EvidenceRef and EvidenceBundle are illustrative and not operationally resolved in this file.", "Hydrology source roles must not collapse: HUC/WBD context, observed gauge readings, NFHL regulatory context, modeled hydrographs, and emergency warnings are different truth classes."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology HUC12 Focus Question Example

Synthetic Focus Mode walkthrough for a user asking a bounded Hydrology question about a selected HUC12 feature.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: examples" src="https://img.shields.io/badge/root-examples%2F-6f42c1">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f6feb">
  <img alt="Outcome: ABSTAIN" src="https://img.shields.io/badge/expected%20outcome-ABSTAIN-orange">
  <img alt="Authority: non authoritative" src="https://img.shields.io/badge/authority-non--authoritative-critical">
</p>

**Path:** `examples/focus_flows/hydrology_huc12_question.md`  
**Example status:** synthetic / illustrative / non-authoritative  
**Expected finite outcome:** `ABSTAIN`  
**Quick links:** [Scenario](#scenario) · [Example request](#example-request) · [Governed flow](#governed-flow) · [Expected response envelope](#expected-response-envelope) · [What an ANSWER would require](#what-an-answer-would-require) · [Hydrology guardrails](#hydrology-guardrails) · [Forbidden uses](#forbidden-uses) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> This is an **example**, not a runtime fixture or API response. It must not be copied into production as a Focus request, model prompt, route fixture, EvidenceBundle, ProofPack, CitationValidationReport, AIReceipt, policy decision, release decision, map payload, public Hydrology layer, or test oracle.

> [!CAUTION]
> This example does not provide flood warnings, emergency alerts, evacuation guidance, observed inundation claims, water-rights conclusions, regulatory determinations, engineering advice, dam-safety direction, or live water-condition status.

---

## Scenario

A public user clicks a released public-safe Hydrology layer feature that represents a generalized HUC12 watershed context and asks:

> What hydrology context can KFM safely summarize for this HUC12?

The selected feature and IDs below are synthetic. They do not identify a real HUC12 watershed.

| Field | Example value | Boundary |
|---|---|---|
| Selected feature | `kfm://example/feature/hydrology/huc12/EXAMPLE-000000000000` | Synthetic feature ref only. |
| Domain object family | `HUCUnit` | HUC/WBD context, not water condition truth. |
| User role | `public` | Public role receives only released, policy-allowed, cited context. |
| Visible layer | `kfm://example/layer/hydrology/huc12-public-safe` | Synthetic released-context sketch; not a layer manifest. |
| Requested transform | `summarize` | Candidate answer must cite evidence or abstain. |
| Expected outcome | `ABSTAIN` | Example EvidenceRefs do not resolve to operational EvidenceBundles here. |

---

## Example request

This request sketch is intentionally non-runtime. It demonstrates shape and gates only.

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/focus-flow/hydrology-huc12-question",
  "focus_mode_request": {
    "question": "What hydrology context can KFM safely summarize for this HUC12?",
    "surface": "focus_mode",
    "user_role": "public",
    "requested_transform": "summarize",
    "map_context": {
      "context_id": "kfm://example/map-context/hydrology-huc12",
      "camera_state": {
        "bbox": ["SYNTHETIC_MINX", "SYNTHETIC_MINY", "SYNTHETIC_MAXX", "SYNTHETIC_MAXY"],
        "zoom": "SYNTHETIC_ZOOM"
      },
      "time_lock": "2026-06-30T00:00:00Z",
      "visible_layers": [
        "kfm://example/layer/hydrology/huc12-public-safe"
      ],
      "selected_feature": {
        "feature_ref": "kfm://example/feature/hydrology/huc12/EXAMPLE-000000000000",
        "feature_type": "HUCUnit",
        "domain": "hydrology",
        "public_release_state": "example_released_context_not_real"
      }
    },
    "evidence_refs": [
      {
        "evidence_ref": "kfm://example/evidence-ref/hydrology/huc12-context/001",
        "expected_bundle": "kfm://example/evidence-bundle/hydrology/huc12-context/001",
        "status": "synthetic_unresolved",
        "claim_scope": "HUC12 identity and public-safe watershed context"
      }
    ],
    "forbidden_intents": [
      "current flood warning",
      "observed inundation claim",
      "emergency or life-safety guidance",
      "official regulatory determination",
      "water-rights conclusion",
      "engineering advice"
    ]
  }
}
```

---

## Governed flow

| Stage | Example result | Why |
|---|---|---|
| 1. Client scopes request | `PASS` as an illustrative request sketch | The example uses released-context language and synthetic IDs. This is not runtime schema validation. |
| 2. Governed API schema check | `NEEDS VERIFICATION` | Focus request schema and route behavior are not proven by this example. |
| 3. Policy precheck | `allow_to_resolve_evidence` as an example posture | A public-safe HUC12 context question may proceed to evidence resolution, but emergency, live-warning, restricted, or role-forbidden intents would return `DENY`. |
| 4. EvidenceRef resolution | `FAIL` | The example EvidenceRef is synthetic and does not resolve to an operational EvidenceBundle here. |
| 5. Adapter/model call | `SKIPPED` | No substantive answer should be generated when required evidence does not resolve. |
| 6. Citation validation | `SKIPPED` | There are no operational cited spans to validate. |
| 7. Policy postcheck | `SKIPPED` | No answer payload exists to postcheck. |
| 8. Runtime envelope | `ABSTAIN` | Cite-or-abstain requires a non-substantive outcome. |

```mermaid
sequenceDiagram
    autonumber
    participant U as User / Focus Panel
    participant API as Governed API
    participant POL as Policy
    participant ER as Evidence Resolver
    participant ADP as Model Adapter
    participant CIT as Citation Validator
    participant OUT as Runtime Envelope

    U->>API: Synthetic FocusModeRequest for HUC12 context
    API->>POL: Precheck request, role, release/sensitivity context
    POL-->>API: Example allow_to_resolve_evidence
    API->>ER: Resolve EvidenceRef to EvidenceBundle
    ER-->>API: Unresolved synthetic EvidenceBundle
    API--xADP: Adapter not called for substantive answer
    API--xCIT: Citation validation not run
    API->>OUT: ABSTAIN with reason code
    OUT-->>U: Non-substantive response; no hydrology claim emitted
```

---

## Expected response envelope

This is an illustrative envelope sketch, not a runtime response.

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/focus-flow/hydrology-huc12-question",
  "runtime_response_envelope": {
    "outcome": "ABSTAIN",
    "reason_code": "EVIDENCE_BUNDLE_UNRESOLVED_EXAMPLE",
    "message": "KFM cannot answer this HUC12 question from this example file because the cited EvidenceBundle and CitationValidationReport are illustrative only and do not resolve here.",
    "evidence_refs": [
      {
        "evidence_ref": "kfm://example/evidence-ref/hydrology/huc12-context/001",
        "resolution_state": "synthetic_unresolved"
      }
    ],
    "policy_decision": {
      "decision": "abstain",
      "reason_code": "missing_resolvable_evidence",
      "policy_ref": "kfm://example/policy/focus/hydrology/public-safe-context"
    },
    "citation_validation": {
      "status": "not_run",
      "reason": "no operational EvidenceBundle or cited spans were resolved"
    },
    "evidence_drawer": {
      "enabled": false,
      "reason": "example refs do not resolve to operational EvidenceBundles"
    },
    "safe_next_step": "Open a released Hydrology layer metadata panel or Evidence Drawer only after governed evidence refs resolve through the API.",
    "forbidden_claims": [
      "current flood warning",
      "observed flooding",
      "NFHL as observed inundation",
      "evacuation or life-safety guidance",
      "official regulatory determination",
      "water-rights or engineering conclusion"
    ]
  }
}
```

---

## What an ANSWER would require

A substantive `ANSWER` example should not be added until each item below is represented by synthetic but internally consistent references or by real operational fixtures in the correct root.

| Requirement | Required support | If missing |
|---|---|---|
| Released HUC12 context | ReleaseManifest and public-safe Hydrology layer artifact or governed API projection | `ABSTAIN` or `ERROR`, depending on failure class. |
| Resolved evidence | EvidenceRef resolves to EvidenceBundle or equivalent proof support | `ABSTAIN`. |
| Source-role separation | HUC/WBD unit, gauge observation, NFHL regulatory context, model output, and warning/advisory roles remain distinct | `DENY` or `ABSTAIN`. |
| Citation validation | Every cited span validates against resolved evidence | `ABSTAIN`. |
| Policy allow | Rights, sensitivity, release state, role, and public-safety boundary permit the answer | `DENY`. |
| No emergency intent | The answer cannot read as warning, evacuation, rescue, engineering, regulatory, or life-safety advice | `DENY`. |
| Evidence Drawer handoff | Drawer payload points to governed evidence projection, not this example file | `ABSTAIN` or no drawer handoff. |

---

## Hydrology guardrails

| Risk | Guardrail |
|---|---|
| HUC12 context becomes water-condition truth | A HUC12 boundary or watershed unit is context. It does not prove current flow, water level, flooding, drought, or water quality by itself. |
| NFHL becomes observed flooding | NFHL/FEMA flood-hazard material is regulatory context only and must not be presented as observed inundation, forecast flooding, hydraulic-model output, or real-time flood status. |
| Gauge reading becomes area truth | Gauge observations require site identity, units, datum, observation time, retrieval time, qualifiers, and evidence support; they do not automatically summarize an entire HUC12. |
| Modeled hydrograph becomes observation | Modeled or reconstructed hydrographs must remain model outputs with method/run support, not observed conditions. |
| Hydrology becomes emergency system | KFM Hydrology examples must not issue flood warnings, evacuation advice, rescue guidance, dam-safety instructions, or life-safety directions. |
| Cross-domain absorption | Soil, Agriculture, Geology, Infrastructure, Hazards, Habitat, Flora, Fauna, People/Land, and Spatial Foundation claims remain owned by their lanes. Hydrology may cite approved context; it does not absorb ownership. |
| Example becomes evidence | This file is not an EvidenceBundle, proof record, citation report, receipt, release manifest, or public API response. |

---

## Forbidden uses

Do not use this file as:

- a Focus API request fixture;
- a route handler example with runtime authority;
- a model prompt or model output;
- an EvidenceBundle, ProofPack, CitationValidationReport, AIReceipt, PolicyDecision, ReleaseManifest, RollbackCard, or CorrectionNotice;
- a published Hydrology layer or map payload;
- a real HUC12 fact sheet;
- flood, drought, warning, advisory, regulatory, water-rights, engineering, or life-safety guidance;
- a substitute for hydrology source registry, proof, catalog, published layer, or release records.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `examples/focus_flows/hydrology_huc12_question.md` existed as a greenfield placeholder before this update. |
| Example-lane contract | CONFIRMED README | `examples/focus_flows/README.md` defines Focus Flow examples as illustrative and non-authoritative. |
| Focus Flow doctrine | CONFIRMED architecture doc | Focus Mode uses governed API, policy gates, EvidenceBundle resolution, citation validation, and finite outcomes. |
| Governed API doctrine | CONFIRMED architecture doc | Public clients use governed API envelopes and do not read RAW/WORK/QUARANTINE/internal stores directly. |
| Hydrology domain doctrine | CONFIRMED README | Hydrology owns HUCs/watersheds and water-context object families but is not an emergency flood-warning system. |
| Hydrology catalog lane | CONFIRMED README | Hydrology catalog records require source-role separation and do not make claims true or public by placement. |
| Hydrology proof lane | CONFIRMED README | Hydrology proof support must preserve HUC12/WBD context, source roles, validation, policy, release, and rollback posture. |
| Hydrology published layer lane | CONFIRMED README | HUC unit layers are proposed public-safe layer lanes; release/proof/policy gates remain required. |
| Example EvidenceRef and EvidenceBundle | SYNTHETIC / UNRESOLVED | The IDs in this file are illustrative and not operational evidence. |
| Focus schemas, route behavior, validators, AIReceipt emission, citation validation, executable policy | NEEDS VERIFICATION | This example proves none of those. |
| Public release readiness | DENY | This example cannot publish, prove, answer, warn, or regulate. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a greenfield placeholder. | Did not define example boundaries. |
| [`README.md`](README.md) | CONFIRMED README | Focus Flow examples are illustrative, non-authoritative, finite-outcome examples with no direct lifecycle/internal-store reads. | Does not prove this child example is executable. |
| [`../../docs/architecture/governed-ai/FOCUS_FLOW.md`](../../docs/architecture/governed-ai/FOCUS_FLOW.md) | CONFIRMED architecture doc | Request → policy → evidence → adapter → citation → policy → envelope; finite outcomes; no browser-to-model shortcut. | Implementation specifics remain PROPOSED/NEEDS VERIFICATION in that doc. |
| [`../../docs/architecture/governed-api.md`](../../docs/architecture/governed-api.md) | CONFIRMED architecture doc | Governed API is the public trust membrane and returns finite `RuntimeResponseEnvelope` outcomes. | Route files, schemas, validators, and framework behavior remain PROPOSED/NEEDS VERIFICATION. |
| [`../../docs/domains/hydrology/README.md`](../../docs/domains/hydrology/README.md) | CONFIRMED doctrine / PROPOSED implementation | Hydrology scope, HUC units, watersheds, gauge observations, NFHL regulatory context, source-role boundaries, and not-emergency-warning posture. | Does not prove this example's synthetic IDs resolve to real artifacts. |
| [`../../data/proofs/evidence_bundle/README.md`](../../data/proofs/evidence_bundle/README.md) | CONFIRMED README | EvidenceBundle lane supports EvidenceRef closure, cite-or-abstain, citation validation, and governed answer support. | Concrete Hydrology EvidenceBundle inventory remains NEEDS VERIFICATION. |
| [`../../data/catalog/domain/hydrology/README.md`](../../data/catalog/domain/hydrology/README.md) | CONFIRMED README | Hydrology catalog lane preserves HUC, source-role, evidence, temporal, policy, and release references. | Catalog records do not publish or answer by themselves. |
| [`../../data/proofs/hydrology/README.md`](../../data/proofs/hydrology/README.md) | CONFIRMED README | Hydrology proof lane includes HUC12 context proof patterns and public-safety boundary posture. | Proof schemas, validators, emitted proof packs, and CI remain UNKNOWN/NEEDS VERIFICATION. |
| [`../../data/published/layers/hydrology/README.md`](../../data/published/layers/hydrology/README.md) | CONFIRMED README | Published layer lane proposes `huc_units/` and requires release/proof/policy/public-safe gates. | Does not prove released layer payloads or route behavior exist. |

[Back to top](#top)
