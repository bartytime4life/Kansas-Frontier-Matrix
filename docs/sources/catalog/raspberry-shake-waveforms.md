<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources/catalog/raspberry-shake-waveforms
title: Raspberry Shake waveform preview gate
type: source-boundary-reference
version: v1.0.0-draft
status: draft; branch-only; not-merged; not-released; not-deployed
policy_label: public
responsibility: >
  Freeze the smallest browser-local waveform preview that can be reviewed
  without activating a provider source, proxying data, or implying a release.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Raspberry Shake waveform preview gate

> Status: branch-only draft. This document and the preview code do not activate a Raspberry Shake source, create a KFM connector, expose a public endpoint, deploy the Site, or release an observation.

## Decision

The current provider and KFM boundaries support one narrow slice:

- A user may select one local MiniSEED file and its matching StationXML file in the browser.
- The browser may inspect one NSLC channel, a maximum 10-minute window, a maximum 100,000 samples, and a maximum 2 MiB waveform file.
- The preview may draw bounded **raw values/counts** only when the local StationXML contains a matching response and InstrumentSensitivity and the user supplies visible attribution.
- The preview retains only an exact-byte SHA-256, non-identifying summary metadata, and downsampled in-memory points. It does not upload, cache, proxy, download, export, persist, catalog, or publish waveform data.
- Unsupported MiniSEED encodings (including Steim-1/Steim-2 in this first slice), truncated records, and gaps/overlaps stay blocked with an explicit reason. No response correction, physical-unit conversion, event detection, magnitude, alert, warning, or health/engineering interpretation is performed.

The resulting state is HOLD even when the local checks pass: it is an unadmitted browser preview, not a KFM observation.

## Provider-term reconciliation

The official boundaries are recorded here so that an implementation cannot silently broaden the use class:

| Gate | Current disposition | Implementation consequence |
|---|---|---|
| Use class | **HOLD** for a KFM provider integration; local file inspection only | No Raspberry Shake URL, FDSN query builder, SeedLink client, or source activation is in the browser path. |
| Caching / proxy | **DENY** for KFM raw or digital redistribution | No server route, proxy, service worker, IndexedDB/localStorage cache, R2/D1 storage, or raw-byte handoff. |
| Attribution | **Required before local drawing** | The UI requires an explicit visible attribution string; it is carried into the redacted audit. |
| Redistribution permission | **DENY by this slice** | No raw waveform, sample array, downloadable file, derived asset, or public URL leaves the browser. |
| Response metadata | **Required** | Matching StationXML response plus InstrumentSensitivity is a blocking gate. The preview is raw counts/values only and never performs deconvolution. |\n| Record continuity | **Required** | A gap or overlap between records blocks drawing instead of connecting discontinuous samples into a false trace. |
| Provenance | **PASS for local inspection** | Exact waveform bytes receive a SHA-256; NSLC, time, sample rate, encoding, StationXML filename, and inspection time are retained in the audit. |
| Correction / rollback | **HOLD** | There is no correction, supersession, evidence, release, or rollback lane for a local preview, so it cannot become a claim-bearing record. |
| Real-time / operational use | **DENY** | No live feed, warning, event catalog, or action-oriented output is added. |

These dispositions reflect the provider's current public materials: the FDSN service is historical rather than real-time, has bounded request limits, and exposes StationXML and MiniSEED [in the FDSN manual](https://manual.raspberryshake.org/fdsn.html). The license requires attribution for Cloud FDSN use and says that digital waveform redistribution through another FDSN service, data center, or server is prohibited; visual redistribution is treated separately [in the Raspberry Shake license](https://raspberryshake.org/license/). The terms also prohibit reproducing, copying, selling, or exploiting service content without express written permission and prohibit scraping/crawling [in the Terms of Service](https://raspberryshake.org/terms-of-service/). The AM network identity and DOI are recorded by [FDSN's AM network record](https://www.fdsn.org/networks/detail/AM/).

No statement here grants KFM permission to use, cache, redistribute, commercialize, or integrate the provider service. Written provider permission remains a prerequisite for any broader use class.

## KFM architecture fit

The slice stays inside the existing renderer-neutral local-import boundary:

1. `apps/kansas-frontier-matrix-explorer/app/waveform-preview.ts` parses only bytes and XML supplied by the user.
2. `buildLocalWaveformPreview` emits `UNADMITTED_BROWSER_PREVIEW`, `publicEffect: NONE`, and a finite gate trace.
3. The existing Import utility displays the gate trace and a compact raw-value sparkline; its copy action emits only the redacted audit.
4. No layer registry, `SourceDescriptor`, `SourceArtifact`, EvidenceBundle, connector, public API, report, export, saved workspace, or deployment state is changed.
5. The current station metadata context feed remains metadata-only. A station marker is not upgraded to a waveform or observation by this slice.

This preserves the source-role and release membrane: a browser preview is inspectable context, not admitted source data.

## Review and rollback

A reviewer can reject the slice by reverting the branch commits or removing the preview file and Import-panel additions. No provider-side state changes are needed. If a future change adds a remote URL, raw cache, server route, response correction, source registry entry, evidence/release reference, or deployment, it must be reviewed as a new use class rather than treated as a continuation of this preview.

Before any future provider integration, require a new record with:

- written permission and exact use class (browser-direct, server retrieval, cache/proxy, derived products, commercial use);
- provider request/window/rate-limit and attribution requirements;
- StationXML response handling and units policy;
- correction, supersession, provenance, evidence, release, and rollback contracts;
- a negative-only test proving that unknown rights, missing response metadata, stale/corrected data, and unsupported encodings fail closed.

## Verification checklist

- `npm run build` and focused waveform tests pass in the repository source context.
- No changed file contains a Raspberry Shake runtime URL, `fetch(`, proxy handler, cache writer, or source activation call.
- The UI labels the output `HOLD` or `BLOCK`, never `ANSWER`, `PUBLISHED`, or `LIVE`.
- The audit omits exact samples and exact geometry-like location data; it carries only the digest and bounded summary.
- The branch remains unmerged, unreleased, and undeployed until an independent review accepts the gate.
