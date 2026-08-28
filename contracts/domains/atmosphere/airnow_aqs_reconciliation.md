# Synthetic AirNow-to-AQS Reconciliation Contract

**Status:** PROPOSED fixture-only implementation contract  
**Owning domain:** Atmosphere / Air  
**Artifact family:** `AirnowAqsReconciliationReport`  
**Source basis:** *New Ideas 4-2-26.pdf* — provisional AirNow context, authoritative AQS replacement, canonical monitor identity, and fail-closed regulatory-use gates  
**Directory Rules basis:** Atmosphere meaning belongs under `contracts/domains/atmosphere/`; the bounded evaluator belongs under the existing Atmosphere validator lane.

## Purpose

Define how one synthetic AirNow record may be related to one synthetic EPA AQS record without collapsing their source roles. AirNow remains a preliminary public-report or NowCast source. AQS remains the regulatory archive. A matching, validated, certified AQS concentration may be proposed as the authoritative successor to a provisional AirNow concentration, but this fixture profile never performs source replacement or release.

## Canonical monitor identity

The profile computes the monitor key:

```text
state_code-county_code-site_number-parameter_code-poc
```

The state, county, site, parameter, and parameter-occurrence-code fields must match before any supersession is proposed. A location, name, or timestamp similarity is not a substitute for canonical identity.

## Source-role rules

- AirNow must use `provisional_public_report`.
- AQS must use `regulatory_archive`.
- AirNow NowCast is a derived AQI product and must never be relabeled as a concentration.
- AQS replacement requires a concentration record with `qa_state=validated` and `certification_state=certified`.
- An absent AQS record cannot satisfy a regulatory request.
- A pending or unvalidated AQS record produces abstention, not an allow.
- The AirNow record remains preserved in lineage even when a successor is proposed.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PROPOSED_WORK_RECORD` | Matching validated and certified AQS concentration is available for steward-reviewed supersession. |
| `ABSTAIN` | AirNow is context-only, AQS validation/certification is pending, or the AirNow object is a NowCast rather than a replaceable concentration. |
| `DENY` | Regulatory use was requested but no authoritative AQS record exists. |
| `ERROR` | Shape, source role, canonical identity, time, quantity, or governance state is inconsistent. |

## Output minimization

The report contains canonical identity, hashes, source states, lineage intent, and a finite decision. It does not echo measurement values. It is not an air-quality determination, certification report, EvidenceBundle, PolicyDecision, ReleaseManifest, health recommendation, alert, or publication decision.

## Trust boundary

- No live AirNow, AQS, KDHE, AirNowTech, or EPA endpoint access.
- No credentials, source activation, raw capture, regulatory certification, lifecycle write, alert, promotion, release, or publication.
- Passing validation proves only fixture consistency.

## Rollback

Remove the contract, schemas, evaluator, fixtures, tests, workflow, and generated authoring receipt. No live source, observation, API, map, alert, release, or published object requires cleanup.
