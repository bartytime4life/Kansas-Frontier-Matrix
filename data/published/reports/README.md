# Published Reports

Released KFM report payload lane under `data/published/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: published" src="https://img.shields.io/badge/lifecycle-published-success">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

## Purpose

`data/published/reports/` is for report payloads that have passed KFM publication gates.

This is separate from [`../../../docs/reports/`](../../../docs/reports/README.md), which is the steward-facing generated narrative lane.

Reports here are downstream carriers. They do not replace source records, processed data, catalog records, EvidenceBundles, proofs, receipts, review records, release manifests, or correction records.

## Repo fit

| Field | Value |
|---|---|
| Path | `data/published/reports/` |
| Responsibility root | `data/` |
| Lifecycle phase | `published` |
| Counterpart | `docs/reports/` |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Catalog authority | `data/catalog/`, not this directory |

## Allowed contents

- Released report payloads.
- Release-local report indexes.
- Report manifests and citation indexes.
- Evidence-reference summaries.
- Digest files.
- `latest.json` only when generated from release state.

## Not allowed here

| Item | Use instead |
|---|---|
| Source material | `data/raw/` |
| Draft or working report files | `data/work/` |
| Held material | `data/quarantine/` |
| Processed domain objects | `data/processed/` |
| Catalog or EvidenceBundle state | `data/catalog/` or `data/proofs/` |
| Proofs and receipts | `data/proofs/` and `data/receipts/` |
| Release decisions | `release/` |
| Steward-facing report narratives | `docs/reports/` |
| Contracts, schemas, or policy rules | `contracts/`, `schemas/`, `policy/` |

## Directory sketch

```text
data/published/reports/
├── README.md
├── <release_id>/
│   ├── report.<slug>.md
│   ├── report.manifest.json
│   ├── citation_index.json
│   ├── evidence_refs.json
│   ├── report.<slug>.sha256
│   └── README.md
└── latest.json
```

## Required checks

- [ ] Confirm this is the right published lane.
- [ ] Confirm release approval.
- [ ] Confirm citation and evidence closure.
- [ ] Confirm proof and receipt closure.
- [ ] Confirm digest and rollback support.
- [ ] Confirm no report is treated as root truth.

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub. | **CONFIRMED authored** |
| The path existed as a stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Actual report payloads exist here. | **UNKNOWN** |
| Release manifests approve report payloads here. | **UNKNOWN** |
| Validators and CI checks enforce this lane. | **NEEDS VERIFICATION** |

## Related files

- [`../README.md`](../README.md)
- [`../layers/README.md`](../layers/README.md)
- [`../pmtiles/README.md`](../pmtiles/README.md)
- [`../../README.md`](../../README.md)
- [`../../../docs/reports/README.md`](../../../docs/reports/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a released report payload lane only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, policy authority, or root truth.
