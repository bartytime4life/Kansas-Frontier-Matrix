<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Soil Moisture Validator
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-15
policy_label: public-safe
related: [
  ../README.md,
  ../promotion_gate/README.md,
  ../../../pipelines/soil-moisture-watch/README.md,
  ../../../pipelines/usgs-mesonet-watch/README.md,
  ../../../contracts/soil_moisture/reading.schema.json,
  ../../../data/receipts/README.md,
  ../../../data/proofs/README.md,
  ../../../policy/README.md,
  ../../../schemas/README.md,
  ../../../tests/README.md
]
tags: [kfm, validators, soil-moisture, mesonet, fail-closed, receipts, spec_hash]
notes: [
  Target path was provided directly by the user.
  This revision preserves the stronger existing lane contract around station health, anomaly artifacts, evidence_refs, and receipt-bearing handoff while aligning terminology to the current Mesonet-first soil-moisture watcher and downstream promotion gate surfaces.
  Exact mounted directory inventory, executable entrypoints, schema filenames, and CI wiring for this lane remain NEEDS VERIFICATION in the current session.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Moisture Validator

Fail-closed validation helpers for Kansas soil-moisture candidate batches, anomaly artifacts, and promotion-ready review signals.

> [!NOTE]
> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `tools/validators/soil_moisture/README.md`  
> ![Status: Experimental](https://img.shields.io/badge/status-experimental-orange) ![Lane: tools/validators](https://img.shields.io/badge/lane-tools%2Fvalidators-1f6feb) ![Focus: Soil Moisture](https://img.shields.io/badge/focus-soil--moisture-8250df) ![Posture: Fail Closed](https://img.shields.io/badge/posture-fail--closed-b60205) ![Trust: Receipt≠Proof](https://img.shields.io/badge/trust-receipt%E2%89%A0proof-6f42c1) ![Implementation: Needs Verification](https://img.shields.io/badge/implementation-NEEDS%20VERIFICATION-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Validation surface](#validation-surface) · [Output posture](#output-posture) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This README defines the **lane contract** for a soil-moisture validator and a conservative **implementation-facing directory surface** for that lane. It does **not** prove that mounted code, schemas, workflows, or merge-blocking integrations already exist at this path. Exact runtime wiring remains **NEEDS VERIFICATION**.

> [!WARNING]
> **Kansas Mesonet is a viable public connector, not a free-for-all ingestion surface.** Any automation against Mesonet should remain policy-bearing, rate-aware, and explicitly aligned to the service’s usage posture.

> [!TIP]
> Keep this lane narrow: **validate here**, **promote later**, **publish elsewhere**. The validator should help downstream review, receipts, and promotion gates stay deterministic and inspectable rather than silently turning a watch surface into a sovereign publish path.

---

## Scope

`tools/validators/soil_moisture/` exists to check whether a soil-moisture candidate batch is fit to move into downstream review or promotion-bearing handoff.

For the current thin slice, this means Mesonet-first soil-moisture candidates that have already been:

- observed upstream
- normalized into canonical long-form rows
- bound to a deterministic `spec_hash`
- associated with explicit source identity and policy context

In KFM terms, this lane should validate:

- candidate-batch shape and required fields
- deterministic identity surfaces such as `spec_hash` and `schema_ver`
- cadence and station-health signals
- anomaly artifacts and threshold logic
- evidence references and receipt-bearing handoff discipline
- explicit failure semantics that remain review-visible

This lane should **not** become a hidden ingestion orchestrator, an all-purpose source harvester, or a direct publication shortcut.

### Operating posture

| Posture | Meaning here |
| --- | --- |
| **CONFIRMED** | KFM expects fail-closed, evidence-first, machine-checkable validation surfaces and treats soils / agriculture as strong watcher territory. |
| **INFERRED** | A dedicated `soil_moisture` validator lane fits naturally under `tools/validators/` because adjacent KFM docs already separate watchers, validators, policy, receipts, proofs, and publication. |
| **PROPOSED** | Exact helper filenames, CLI shape, schema names, and fixture layout below. |
| **UNKNOWN / NEEDS VERIFICATION** | Mounted file inventory, executable wiring, CI integration, and any checked-in implementation not directly surfaced in this session. |

### What this validator is for

A good first-wave validator here would answer questions like:

- Is the incoming soil-moisture candidate batch structurally valid?
- Is the canonical row shape stable enough for replay and downstream `promotion_gate/` review?
- Are station freshness and roster-health still within declared tolerances?
- Are anomalies explicit, bounded, and preserved as artifacts instead of being silently flattened away?
- Does the batch carry the evidence needed for downstream trust objects such as a `run_receipt`?
- Should downstream consumers **pass forward**, **quarantine**, or **deny** the candidate based on deterministic checks?

[Back to top](#top)

---

## Repo fit

This path sits at the handoff point between **watcher-style soil-moisture intake**, **validator logic**, and **downstream review / promotion surfaces**.

| Direction | Surface | Relationship |
| --- | --- | --- |
| Upstream | [`../README.md`](../README.md) | Parent validators lane; this README should inherit its fail-closed, deterministic posture. |
| Upstream | [`../../../pipelines/soil-moisture-watch/README.md`](../../../pipelines/soil-moisture-watch/README.md) | Current Mesonet-first soil-moisture watcher contract and canonical candidate boundary. |
| Upstream | [`../../../pipelines/usgs-mesonet-watch/README.md`](../../../pipelines/usgs-mesonet-watch/README.md) | Closest adjacent watcher-pattern surface visible in current-session evidence. |
| Upstream | [`../../../contracts/soil_moisture/reading.schema.json`](../../../contracts/soil_moisture/reading.schema.json) | Canonical first-wave row contract for soil-moisture candidates. |
| Upstream | [`../../../schemas/README.md`](../../../schemas/README.md) | Canonical schema home once this lane publishes concrete object shapes. |
| Upstream | [`../../../policy/README.md`](../../../policy/README.md) | Deny-by-default decision logic belongs there, not in this README alone. |
| Downstream | [`../promotion_gate/README.md`](../promotion_gate/README.md) | Downstream release-facing gate should consume validator results rather than repair malformed candidates. |
| Downstream | [`../../../data/receipts/README.md`](../../../data/receipts/README.md) | Compact run/process-memory outputs belong there. |
| Downstream | [`../../../data/proofs/README.md`](../../../data/proofs/README.md) | Release-grade proof objects belong there, not here. |
| Downstream | [`../../../tests/README.md`](../../../tests/README.md) | Fixture and replay coverage for positive / negative validator behavior. |

### Role in the wider system

This validator lane should sit:

1. **after** candidate-batch observation and normalization,
2. **before** review-facing promotion or publication logic,
3. **beside** policy and schema surfaces rather than replacing them,
4. **below** the trust membrane rather than bypassing it.

> [!NOTE]
> The current session did **not** surface a mounted repo tree for this exact path. The table above is therefore **repo-fit guidance**, not a claim that every linked neighbor was freshly enumerated from checkout.

[Back to top](#top)

---

## Accepted inputs

The attached corpus supports the following inputs for a first-wave soil-moisture validator.

| Input surface | Why it belongs here | Status |
| --- | --- | --- |
| Kansas Mesonet station roster snapshot | Stable list of station identifiers / names for roster-health comparison | CONFIRMED |
| Kansas Mesonet recent-activity snapshot | Supports freshness and degraded-station logic | CONFIRMED |
| Kansas Mesonet latest-observation snapshot | Supports last-seen checks and drift review | CONFIRMED |
| Kansas Mesonet interval or historical soil-moisture batch | Primary candidate batch for soil-moisture validation | CONFIRMED |
| Canonicalized candidate rows | Stable long-form subject matter for deterministic validation | CONFIRMED |
| Declared expected cadence / station thresholds | Required to interpret freshness rather than guessing | INFERRED |
| Canonicalized batch manifest + `spec_hash` | Keeps diffs and downstream receipts deterministic | CONFIRMED doctrine / PROPOSED local object |
| `schema_ver` | Binds candidate meaning to an explicit contract version | INFERRED / strongly implied |
| `evidence_refs` and receipt reference | Required trust objects for downstream reviewable handoff | CONFIRMED doctrine |
| Optional SCAN / SMAP / SSURGO context | Useful as context or corroboration, but should not silently replace Mesonet meaning | INFERRED |

### What belongs here

- candidate batches that can be normalized deterministically
- canonical rows ready for machine validation
- station-health metadata derived from explicit thresholds
- anomaly artifacts that explain why a candidate is risky
- validator-local summaries that a reviewer or downstream gate can read quickly
- explicit handoff objects that point toward receipts and later trust objects

### Good first-wave subject matter

This lane is strongest when it stays close to:

- **Kansas Mesonet soil moisture**
- **canonical candidate rows**
- **station freshness / health**
- **candidate-batch anomalies**
- **receipt-bearing handoff discipline**

It is weaker when it tries to solve, all at once:

- statewide land-cover packaging
- full agricultural interpretation
- broad hydrology publication
- cross-domain policy ownership

[Back to top](#top)

---

## Exclusions

This lane does **not**:

- poll sources by itself as the system’s sovereign watch surface
- replace source descriptors
- replace schema authority
- replace promotion-gate logic
- publish STAC / DCAT / PROV artifacts on its own
- sign artifacts on its own merely because signing exists elsewhere in the corpus
- collapse **candidate**, **receipt**, **proof**, and **catalog** objects into one file
- silently reinterpret Mesonet data-use constraints as blanket permission
- imply real scheduler, workflow, or CI wiring unless directly verified
- silently “fix” malformed candidates that should have failed before promotion review

### Out-of-lane examples

| Concern | Belongs here? | Why |
| --- | --- | --- |
| Candidate-batch schema and threshold checks | Yes | Core validator responsibility |
| Canonical row-field validation | Yes | Core deterministic subject validation |
| Station-health degradation summary | Yes | Directly supports reviewability |
| Multi-sigma anomaly artifact validation | Yes | Strong fit for deterministic checks |
| Source polling cadence orchestration | No | Better placed with watcher / pipeline surfaces |
| Cryptographic publication proof issuance | No | Belongs to attest / proofs / promotion surfaces |
| Final release decision for broader bundles | No | Promotion-gate or policy lane concern |
| Schema authorship | No | Canonical schema meaning should remain upstream |
| Generic agronomy interpretation | No | Too broad; keep the first slice close to authoritative baselines |

[Back to top](#top)

---

## Directory tree

### Current documented slice

Exact mounted contents under `tools/validators/soil_moisture/` were **not** surfaced in the current session. The only safe current tree claim is the target document itself.

```text
tools/validators/soil_moisture/
└── README.md  # target validator README (mounted inventory NEEDS VERIFICATION)
```

### Possible stable growth shape — PROPOSED

<details>
<summary><strong>Illustrative future directory shape</strong> (not asserted as mounted)</summary>

```text
tools/validators/soil_moisture/
├── README.md
├── schema_validate.py              # candidate-batch shape check
├── validate_station_health.py      # cadence / degraded-station logic
├── validate_anomalies.py           # outlier / jump checks
├── validate_identity.py            # spec_hash / schema_ver / source checks
├── evaluate.py                     # optional orchestrator wrapper
├── lib/                            # shared JSON / subprocess helpers
├── fixtures/
│   ├── pass/
│   ├── quarantine/
│   ├── deny/
│   └── error/
└── reports/
    └── README.md
```

Use this only as a design aid until a mounted repo inventory confirms what actually exists.
</details>

[Back to top](#top)

---

## Quickstart

Use this sequence when turning the lane from a draft contract into a real thin slice.

1. Define a source descriptor for **Kansas Mesonet** that names cadence, usage posture, and expected fields.
2. Normalize one candidate batch from Mesonet into a stable canonical shape.
3. Compute `spec_hash` from canonicalized content and declared source validators where available.
4. Compare roster / activity / latest-observation surfaces to derive **station health**.
5. Evaluate anomaly rules on soil-moisture variables.
6. Emit a machine-readable validation report plus any anomaly artifact.
7. Require `evidence_refs` and a `run_receipt` reference before downstream handoff.
8. Quarantine or deny candidates whose failures matter materially downstream.

Illustrative sequence only:

```text
observe
  -> normalize
  -> canonicalize
  -> spec_hash
  -> identity checks
  -> station-health checks
  -> anomaly checks
  -> evidence / receipt gate
  -> handoff or quarantine
```

### First thin-slice rule of thumb

Start with one narrow, high-signal objective:

- **Can we validate one Kansas Mesonet soil-moisture batch reproducibly and explain why it passed or failed?**

That is a better first proof than trying to complete all soil, crop, moisture, and policy logic at once.

[Back to top](#top)

---

## Usage

### Illustrative invocation — PROPOSED

The exact entrypoint for this lane was **not** surfaced. A plausible local invocation shape would look like this:

```bash
# Illustrative only — entrypoint and flags need direct repo verification.
python -m tools.validators.soil_moisture \
  --candidate data/work/mesonet/soil_moisture/candidate.json \
  --station-roster data/work/mesonet/stationnames.csv \
  --station-active data/work/mesonet/stationactive.csv \
  --most-recent data/work/mesonet/mostrecent.csv \
  --schema contracts/soil_moisture/reading.schema.json \
  --out data/work/mesonet/soil_moisture/report.json
```

### Illustrative outputs — PROPOSED

A first-wave run should stay small and reviewable.

```text
canonical candidate batch
  -> validation report
  -> anomaly artifact (only when needed)
  -> station-health metadata
  -> run_receipt handoff reference
```

### Example report shape — illustrative

```json
{
  "validator": "soil_moisture",
  "result": "quarantine",
  "spec_hash": "sha256:REPLACE_ME",
  "schema_ver": 1,
  "station_health": {
    "coverage_ratio": 0.87,
    "degraded_station_count": 12,
    "thresholds": {
      "stale_after_multiple": 3,
      "coverage_min_for_model_consumers": 0.90
    }
  },
  "anomalies": {
    "zscore_gt_4": ["station:XYZ depth:10cm"],
    "relative_jump_ge_50pct": ["station:ABC depth:5cm"]
  },
  "evidence_refs": [
    "mesonet:stationnames",
    "mesonet:stationactive",
    "mesonet:mostrecent",
    "mesonet:stationdata"
  ],
  "run_receipt_ref": "kfm://receipt/NEEDS-VERIFICATION"
}
```

> [!NOTE]
> The field names above are **illustrative examples**, not confirmed checked-in contract names.

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
  A[/rest/stationnames] --> E[Normalize candidate batch]
  B[/rest/stationactive] --> E
  C[/rest/mostrecent] --> E
  D[/rest/stationdata] --> E

  E --> F[Canonical rows]
  F --> G[spec_hash]

  G --> H[Identity checks]
  G --> I[Station-health checks]
  G --> J[Anomaly checks]

  H --> K[Validator report]
  I --> K
  J --> K

  K --> L{Evidence refs + receipt present?}
  L -->|yes| M[Handoff to review / promotion lane]
  L -->|no| N[Quarantine candidate]

  I -->|blocking freshness / coverage failure| N
  J -->|untriaged anomaly| N
  H -->|missing spec_hash / source / schema_ver| N
```

This diagram reflects the **narrow lane boundary** on purpose: Mesonet surfaces feed validation, but proof issuance and publication live downstream.

[Back to top](#top)

---

## Validation surface

### Rule matrix

| Rule surface | Minimum check | Why it matters | Outcome on failure | Status |
| --- | --- | --- | --- | --- |
| Candidate schema | Required top-level fields exist and types are stable | Prevents silent shape drift | deny or error | INFERRED validator need |
| Canonical row shape | Required row fields exist and names are stable | Keeps downstream replay and promotion deterministic | deny or error | CONFIRMED / strongly implied |
| `spec_hash` presence | Candidate manifest is canonicalized and hashed deterministically | Keeps diffs and receipts explainable | deny | CONFIRMED doctrine |
| `schema_ver` presence | Candidate meaning is bound to an explicit contract | Prevents silent contract ambiguity | deny | INFERRED / strongly implied |
| Source identity | Candidate is not anonymous | Prevents weak handoff posture | deny | CONFIRMED doctrine |
| Station freshness | Use activity / latest-observation timestamps against expected cadence | Prevents stale stations from looking healthy | quarantine or deny | CONFIRMED concept |
| Roster-loss alert | Raise alert when degraded stations exceed a declared fraction | Makes station-network quality visible | quarantine | PROPOSED local thresholding |
| Multi-sigma anomaly | Flag values with z-score `> 4` on a rolling 14-day baseline | Captures obvious outliers | quarantine | CONFIRMED packet idea |
| Relative-jump anomaly | Flag jumps `>= 50%` versus 7-day median | Captures abrupt step changes | quarantine | CONFIRMED packet idea |
| Value-domain check | `0.0 ≤ value ≤ 0.6 m3/m3` | Keeps first-wave soil-moisture semantics explicit | deny or anomaly path | CONFIRMED first-wave constraint |
| Coverage gate | Block model-consuming handoff when coverage `< 90%` | Avoids downstream overtrust | deny for those consumers | CONFIRMED packet idea |
| Evidence gate | Require `evidence_refs` for automatic downstream emit | Keeps trust objects inspectable | deny | CONFIRMED packet idea |
| Receipt gate | Require `run_receipt` handoff for promotion-bearing use | Preserves auditability | deny | CONFIRMED doctrine / packet idea |
| Usage-policy posture | Do not treat Mesonet as unrestricted scraping surface | Keeps connector design honest | deny or manual review | CONFIRMED doctrine |

### Source-role table

| Source / surface | Role in this lane | What it should not silently become |
| --- | --- | --- |
| Kansas Mesonet `/rest/stationnames` | roster reference | sovereign publication record |
| Kansas Mesonet `/rest/stationactive` | freshness / health reference | replacement for anomaly logic |
| Kansas Mesonet `/rest/mostrecent` | last-seen station health context | substitute for interval history |
| Kansas Mesonet `/rest/stationdata` | candidate soil-moisture observations | unconstrained bulk-harvest surface |
| SCAN / SMAP / SSURGO context | corroboration or enrichment context | silent override of Mesonet meaning |

### Outcome posture

This README deliberately keeps the validator-local outcome grammar narrower than the downstream promotion decision grammar.

| Validator-local outcome | Meaning |
| --- | --- |
| `pass` | candidate satisfied required checks strongly enough to move forward |
| `quarantine` | candidate is materially suspect and should be held for review |
| `deny` | candidate failed required checks |
| `error` | the validator could not safely complete evaluation |

> [!CAUTION]
> This lane should not silently map itself to downstream release decisions such as `ALLOW` or `ABSTAIN`. That mapping belongs later, with `promotion_gate/` and policy surfaces.

[Back to top](#top)

---

## Output posture

### Output and handoff objects

| Object | Role | Expected posture |
| --- | --- | --- |
| Validation report | Primary machine-readable result of the lane | deterministic, reviewer-readable |
| Anomalies artifact | Preserves flagged conditions instead of flattening them away | explicit, optional, reviewable |
| `kfm:station_health` metadata | Carries degraded / stale / coverage signals forward | structured, bounded |
| `run_receipt` reference | Links the validator result to a trust-bearing process-memory object | required downstream for promotion-bearing uses |
| Promotion-manifest handoff | Out-of-lane output consumed later | only after validator pass posture |

### Trust split reminder

| Surface | What it is | What it is not |
| --- | --- | --- |
| Validation report | subject-level deterministic check result | not a proof bundle |
| `run_receipt` | process memory for what ran | not the promotion decision |
| proof object | release-significant trust object | not the same as the validator result |
| catalog object | outward discoverability / lineage surface | not the same as validation |

### Why this split matters

The validator should make downstream review easier without pretending to own publication authority. KFM’s trust posture depends on keeping validation, receipts, proofs, and catalog closure separately identifiable.

[Back to top](#top)

---

## Task list

### Definition of done for a real first-wave implementation

- [ ] Source descriptor for Kansas Mesonet is published and reviewable.
- [ ] Candidate-batch schema is published under the repo’s canonical schema surface.
- [ ] `spec_hash` computation is deterministic and documented.
- [ ] `schema_ver` is explicit and reviewable.
- [ ] Station-health checks are explicit about cadence assumptions.
- [ ] Anomaly thresholds are declared, not hidden in code.
- [ ] Validator emits a machine-readable report on both success and failure paths.
- [ ] `evidence_refs` and `run_receipt` handoff are required for downstream promotion-bearing use.
- [ ] At least one positive fixture and one negative fixture exist.
- [ ] CI exits non-zero on blocking failures.
- [ ] Mesonet usage-policy posture is visible in both docs and implementation.
- [ ] Mounted file inventory for this path has been directly verified.

### Review checks

Before treating this lane as real beyond documentation:

- [ ] confirm the actual directory exists in the mounted repo
- [ ] confirm the actual entrypoint name
- [ ] confirm any neighboring schema / policy / test paths
- [ ] confirm whether outputs are local reports, receipts, or direct handoff objects
- [ ] confirm whether coverage thresholds are lane-owned or policy-owned
- [ ] confirm exact interaction with downstream `promotion_gate/`

[Back to top](#top)

---

## FAQ

### Does this validator publish soil-moisture data?

No. This lane validates candidate batches and emits reviewable outputs. Publication, proof attachment, and promotion-bearing decisions belong downstream.

### Is Kansas Mesonet the same as authoritative statewide soil truth?

No. In the attached corpus, Mesonet is a valuable high-frequency connector, especially for soil moisture, but it sits beside other authoritative and corroborative soil sources such as SSURGO, gSSURGO, gNATSGO, SCAN, and SMAP. It should not silently replace them.

### Why insist on `run_receipt` and `evidence_refs`?

Because KFM’s value comes from inspectable claims, not just plausible outputs. If a validator cannot say what it checked and what evidence it relied on, it becomes hard to trust downstream.

### Why keep this lane narrow?

Because the strongest current soil / agriculture direction is watcher-style, spec-hashed, receipt-bearing ingestion close to authoritative baselines. A narrow validator is easier to prove than a broad “soil intelligence” layer.

### Are the commands in this README real?

They are illustrative unless direct mounted implementation confirms them. This draft is strongest on lane role, validator posture, and review boundary.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Appendix A — Practical first checks worth implementing</strong></summary>

### Candidate-level checks

- required station identifier
- timestamp parseability
- declared depth field
- soil-moisture value present
- units explicit or normalized
- batch-level `spec_hash`
- explicit `schema_ver`
- source identity present

### Station-health checks

- station appears in roster
- station was recently active
- station has a recent latest-observation timestamp
- station gap does not exceed declared threshold

### Anomaly checks

- rolling z-score threshold
- relative jump threshold
- optional depth-specific sanity bands

### Downstream trust checks

- `evidence_refs` present
- `run_receipt` handoff present
- validator report written on deny / quarantine as well as pass
</details>

<details>
<summary><strong>Appendix B — Possible neighboring docs to add later</strong></summary>

These are sensible next documentation additions, but they are **not** asserted as mounted:

- `tools/validators/soil_moisture/fixtures/README.md`
- `schemas/soil_moisture/README.md`
- `contracts/source/kansas_mesonet_source_descriptor.md`
- `tests/e2e/runtime_proof/soil_moisture/README.md`
- `docs/patterns/soil_moisture_validation.md`
</details>

<details>
<summary><strong>Appendix C — One-line architecture summary</strong></summary>

Use this lane to turn Kansas Mesonet soil-moisture candidate batches into **deterministic, fail-closed, receipt-aware validation results** before any downstream review or promotion logic touches them.
</details>

[Back to top](#top)
