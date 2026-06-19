<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-goes-abi-aod-readme
title: connectors/goes_abi_aod/ — GOES ABI Aerosol Optical Depth Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Atmosphere/Air steward · Hazards steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; modeled-product; rights-and-sensitivity-gated
proposed_path: connectors/goes_abi_aod/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/sources/catalog/noaa/goes-abi-aod.md
  - ../../docs/sources/catalog/noaa/README.md
  - ../../docs/sources/catalog/noaa/IDENTITY.md
  - ../../docs/sources/catalog/noaa/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../docs/domains/atmosphere/README.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md
  - ../../data/registry/sources/
  - ../../data/raw/atmosphere/
  - ../../data/quarantine/atmosphere/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, noaa, goes, abi, aod, aerosol-optical-depth, atmosphere, air-quality, modeled, satellite-retrieval, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank connector README for GOES ABI AOD source admission."
  - "Visible source-catalog docs treat GOES ABI AOD as a modeled satellite retrieval with mandatory receipt discipline, not as a direct surface observation."
  - "Dominant anti-collapse: AOD is not PM2.5, not smoke detection, and not an air-quality advisory."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, ModelRunReceipt closure, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Implementation files, source activation, SourceDescriptor, retrieval method, fixtures, tests, CI wiring, rights, and current access method remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GOES ABI Aerosol Optical Depth Connector

> Source-admission lane for GOES Advanced Baseline Imager Aerosol Optical Depth source material.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Source role: modeled" src="https://img.shields.io/badge/source__role-modeled-purple">
  <img alt="Anti-collapse: AOD is not PM2.5" src="https://img.shields.io/badge/anti--collapse-AOD%20%E2%89%A0%20PM2.5-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/goes_abi_aod/`

## Quick jumps

[Scope](#scope) · [Evidence basis](#evidence-basis) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Anti-collapse](#anti-collapse) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/goes_abi_aod/` is the connector lane for GOES ABI Aerosol Optical Depth source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, fixture helpers, quality-flag handling helpers, and tests for GOES ABI AOD-shaped material.

It must not become AOD truth, PM2.5 truth, smoke truth, air-quality-advisory authority, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Evidence basis

Repo evidence checked for this update:

- `connectors/goes_abi_aod/README.md` existed but was blank.
- `docs/sources/catalog/noaa/goes-abi-aod.md` describes GOES ABI AOD as a NOAA source product page.
- That source page treats GOES ABI AOD as a satellite retrieval / modeled column property.
- The same source page states the dominant anti-collapse: AOD is not PM2.5 and must not be treated as a direct observation of a surface property.

This connector README does not invent current endpoints, buckets, product IDs, cadence, file naming, API credentials, rate limits, license terms, or activation state.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/atmosphere/
  data/quarantine/atmosphere/

NOT HERE:
  PM2.5 estimates
  smoke detections
  exposure determinations
  air-quality advisories
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, stage, or inspect GOES ABI AOD source material. It does not decide whether a pixel, raster, tile, aggregate, map, or summary is validated, calibrated, sensitivity-safe, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no conversion of AOD into PM2.5 or AQI inside the connector;
- no relabeling of AOD as direct surface observation;
- no use as smoke detection or air-quality advisory;
- no loss of source product, satellite/platform, instrument, retrieval time, algorithm/version, projection, quality flags, uncertainty, retrieval metadata, role, or review metadata;
- unclear rights, source role, product scope, retrieval quality, cloud contamination, or schema drift routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Product scope unclear | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Rights or attribution unclear | `NEEDS_VERIFICATION`; no promotion. |
| Retrieval algorithm/version unclear | Quarantine or review-required result. |
| Quality/cloud flags unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Anti-collapse

The parent source page states the controlling doctrine plainly:

```text
AOD is not PM2.5.
```

Connector code must enforce the following boundaries:

1. AOD is a satellite retrieval, not a direct surface measurement.
2. AOD is not PM2.5, AQI, smoke concentration, smoke detection, visibility, or exposure.
3. AOD-to-PM2.5 workflows require downstream calibrated modeling, uncertainty accounting, receipts, and validation.
4. Cloud-affected or low-quality retrieval material must fail closed before public release.
5. Any derived raster, tile, map, summary, model field, or AI explanation is downstream carrier content, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- product, platform, instrument, retrieval time, algorithm/version, projection, quality flags, uncertainty, retrieval, source-role, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- GOES ABI AOD records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, ModelRunReceipt closure, EvidenceBundle closure, release gates, public caveats, and rollback remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Retrieval/download method is documented before activation.
- [ ] Product, platform, instrument, retrieval time, algorithm/version, projection, quality, uncertainty, and source role metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] AOD-to-PM2.5, AOD-as-smoke, and AOD-as-advisory behavior is explicitly denied in tests or validators.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, rights-unclear, product-scope-unclear, version-unclear, quality-flag-unclear, cloud-affected, and schema-drift cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm current access method and product naming. | **NEEDS VERIFICATION** | Source steward review and current NOAA source docs. |
| Confirm retrieval algorithm/version metadata handling. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm quality flag and cloud-screen handling. | **NEEDS VERIFICATION** | Parser tests, validators, and atmosphere-domain review. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector narrow. It can prepare GOES ABI AOD material for governed admission, but it must not convert AOD into PM2.5, smoke detection, exposure, advisory text, public truth, release artifacts, or published layers without downstream evidence, receipt, policy, review, release, and rollback support.
