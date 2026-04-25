<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-kansas-biodiversity-etl-validate-readme-uuid
title: Kansas Biodiversity ETL Validation Gate
type: standard
version: v1
status: draft
owners: TODO-confirm-biodiversity-validation-stewards
created: 2026-04-25
updated: 2026-04-25
policy_label: TODO-confirm-public-or-restricted
related: [
  ../README.md,
  ../Makefile,
  ../publish/README.md,
  ../attest/README.md,
  ../catalog/README.md,
  ../../../data/README.md,
  ../../../data/processed/README.md,
  ../../../data/receipts/README.md,
  ../../../data/proofs/README.md,
  ../../../data/catalog/README.md,
  ../../../tools/validators/README.md,
  ../../../tools/validators/promotion_gate/README.md
]
tags: [kfm, pipelines, kansas-biodiversity-etl, validation, promotion-gate, evidencebundle, spec-hash, receipts, proofs]
notes: [
  "Updated from an earlier broad validation README into the concrete promotion gate contract for promotion_gate_full.py.",
  "Branch-local file presence, owners, policy label, CI wiring, and exact shared-schema homes still NEED VERIFICATION.",
  "Documents JSONL, single-file Parquet, partitioned Parquet, metadata spec_hash, EvidenceBundle, and receipt-proof checks."
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Biodiversity ETL Validation Gate

Fail-closed validation boundary for Kansas biodiversity ETL candidates before catalog closure, publication, API use, map layers, export, or Focus Mode use.

<div align="left">

![status](https://img.shields.io/badge/status-experimental-orange)
![doc](https://img.shields.io/badge/doc-draft-lightgrey)
![surface](https://img.shields.io/badge/surface-validation-blue)
![truth](https://img.shields.io/badge/truth-evidence--first-5b6ee1)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![gate](https://img.shields.io/badge/gates-A--H-red)

</div>

| Impact field | Value |
| --- | --- |
| **Status** | `experimental` |
| **Owners** | `TODO-confirm-biodiversity-validation-stewards` |
| **Path** | `pipelines/kansas_biodiversity_etl/validate/README.md` |
| **Primary executable** | `promotion_gate_full.py` |
| **Trust posture** | fail-closed promotion gate |
| **Quick jumps** | [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Gate matrix](#gate-matrix) · [Diagram](#diagram) · [Failure reasons](#failure-reasons) · [Definition of done](#definition-of-done) · [FAQ](#faq) |

> [!IMPORTANT]
> `validate/` is a promotion boundary. It may return `PASS`, but it does **not** publish, repair, enrich, catalog, summarize, or make biodiversity claims on its own.

> [!WARNING]
> Unknown licenses, missing attribution, duplicate identities, invalid evidence, missing metadata, mismatched `spec_hash`, and unredacted restricted geometry must fail closed.

---

## Scope

This directory contains the Kansas biodiversity ETL lane-local validation gate.

The current concrete gate target is:

```text
pipelines/kansas_biodiversity_etl/validate/promotion_gate_full.py
```

It validates generated artifacts from the pipeline sequence:

```text
harvest -> normalize -> dedupe -> publish -> sign -> gate -> catalog
```

### What this lane validates

| Validation concern | Gate responsibility |
| --- | --- |
| **EvidenceBundle** | Must exist, parse, contain `spec_hash`, `items`, `source_uris`, license summary, and attribution summary. |
| **Dataset presence** | Dataset path must exist as JSONL, single Parquet file, or partitioned Parquet directory. |
| **Dataset metadata** | Parquet outputs must have `_dataset_metadata.json` with stable `spec_hash`. |
| **Identity** | EvidenceBundle `spec_hash` must match the expected dataset identity source. |
| **Record-level rights** | Records must not contain missing or `UNKNOWN` license values. |
| **Attribution** | `CC-BY-4.0` records must carry attribution. |
| **Sensitivity** | `restricted` records must not retain geometry. |
| **Receipt proof** | When wired through Makefile, receipt proof hash must match current receipt bytes. |

### Truth labels used here

| Label | Meaning |
| --- | --- |
| **CONFIRMED** | Present in the supplied old README or prior generated code in this conversation. |
| **INFERRED** | Conservative relationship derived from KFM lifecycle doctrine and adjacent pipeline paths. |
| **PROPOSED** | Recommended realization not yet verified in active branch. |
| **UNKNOWN** | Not proven strongly enough to state as current repo fact. |
| **NEEDS VERIFICATION** | Must be checked against active branch, CI, policy, schema, or workflow state before merge. |

[Back to top](#top)

---

## Repo fit

`validate/` sits inside the Kansas biodiversity ETL lane. It should stay execution-near and lane-specific.

| Relation | Surface | Use it for | Status |
| --- | --- | --- | --- |
| Parent lane | [`../README.md`](../README.md) | ETL stage ordering and evidence-first posture | NEEDS VERIFICATION |
| Makefile | [`../Makefile`](../Makefile) | canonical local execution path | PROPOSED / NEEDS VERIFICATION |
| Publisher | [`../publish/`](../publish/) | dataset, metadata, EvidenceBundle, receipt emission | PROPOSED / NEEDS VERIFICATION |
| Attestation helper | [`../attest/`](../attest/) | local receipt proof generation | PROPOSED / NEEDS VERIFICATION |
| Catalog closure | [`../catalog/`](../catalog/) | STAC/DCAT/PROV emission after gate pass | PROPOSED / NEEDS VERIFICATION |
| Processed data | [`../../../data/processed/README.md`](../../../data/processed/README.md) | processed dataset lifecycle placement | NEEDS VERIFICATION |
| Receipts | [`../../../data/receipts/README.md`](../../../data/receipts/README.md) | run receipt custody | NEEDS VERIFICATION |
| Proofs | [`../../../data/proofs/README.md`](../../../data/proofs/README.md) | proof artifact custody | NEEDS VERIFICATION |
| Catalog | [`../../../data/catalog/README.md`](../../../data/catalog/README.md) | catalog closure surfaces | NEEDS VERIFICATION |
| Shared validators | [`../../../tools/validators/README.md`](../../../tools/validators/README.md) | reusable validation doctrine | NEEDS VERIFICATION |
| Promotion gate doctrine | [`../../../tools/validators/promotion_gate/README.md`](../../../tools/validators/promotion_gate/README.md) | broader A–G gate semantics | NEEDS VERIFICATION |

### Upstream / downstream boundary

```text
data/work/kansas_biodiversity_etl/deduped.jsonl
  -> publish/
  -> data/processed/kansas_occurrences/
  -> data/proofs/.../evidence_bundle.json
  -> data/receipts/.../run_receipt.json
  -> data/proofs/.../receipt_proof.json
  -> validate/promotion_gate_full.py
  -> catalog/emit_catalog.py only after PASS
```

[Back to top](#top)

---

## Accepted inputs

Material belongs here only when it is needed to validate a generated Kansas biodiversity ETL candidate.

| Input | Example | Required posture |
| --- | --- | --- |
| Dataset candidate | `data/processed/kansas_occurrences/` | JSONL, single Parquet, or partitioned Parquet directory must be readable. |
| Dataset metadata | `data/processed/kansas_occurrences/_dataset_metadata.json` | Required for Parquet and partitioned Parquet. |
| EvidenceBundle | `data/proofs/kansas_biodiversity_etl/YYYYMMDD/evidence_bundle.json` | Must contain `evidenceBundle.spec_hash`. |
| Run receipt | `data/receipts/kansas_biodiversity_etl/YYYYMMDD/run_receipt.json` | Required when proof verification is enforced. |
| Receipt proof | `data/proofs/kansas_biodiversity_etl/YYYYMMDD/receipt_proof.json` | Required when `--proof` is supplied. |
| Synthetic sample outputs | generated from `make sample` | Allowed for offline validation only. |

[Back to top](#top)

---

## Exclusions

| Does **not** belong here | Better home | Why |
| --- | --- | --- |
| Raw source exports | `../../../data/raw/` | validators should not own raw custody |
| Work/intermediate transforms | `../../../data/work/` | validators consume candidates; they should not become transformation storage |
| Durable proof artifacts | `../../../data/proofs/` | proof custody is lifecycle storage |
| Run receipts | `../../../data/receipts/` | receipt custody is separate from validation code |
| Catalog records | `../../../data/catalog/` | catalog closure is downstream of validation |
| Published data | `../../../data/published/` | publication is a governed state transition |
| Policy source of truth | `../../../policy/` | validator enforces policy; it should not hide policy law |
| Canonical schemas/contracts | `../../../schemas/`, `../../../contracts/` | validators should not define parallel schema law |
| Secrets or signing keys | secret manager / untracked local config | never commit trust-root material |
| Public map/API payloads | governed API / UI contract surfaces | validation is not runtime serving |

[Back to top](#top)

---

## Directory tree

```text
pipelines/kansas_biodiversity_etl/
├── Makefile
├── attest/
│   ├── sign_receipt.py                 # PROPOSED / NEEDS VERIFICATION
│   └── verify_receipt_proof.py         # PROPOSED / NEEDS VERIFICATION
├── publish/
│   └── publish.py                      # PROPOSED / NEEDS VERIFICATION
└── validate/
    ├── README.md
    └── promotion_gate_full.py          # PROPOSED / NEEDS VERIFICATION
```

Expected validated output surfaces:

```text
data/
├── processed/
│   └── kansas_occurrences/
│       ├── _dataset_metadata.json
│       └── year=YYYY/
│           └── month=MM/
│               └── part-000.parquet
├── proofs/
│   └── kansas_biodiversity_etl/
│       └── YYYYMMDD/
│           ├── evidence_bundle.json
│           └── receipt_proof.json
└── receipts/
    └── kansas_biodiversity_etl/
        └── YYYYMMDD/
            └── run_receipt.json
```

[Back to top](#top)

---

## Quickstart

Run from:

```text
pipelines/kansas_biodiversity_etl/
```

### Full gate through Makefile

```bash
make gate
```

Expected success shape:

```json
{
  "decision": "PASS",
  "gates": ["A", "B", "C", "D", "E", "F", "G", "H"]
}
```

### Direct gate command

```bash
python validate/promotion_gate_full.py \
  --dataset ../../data/processed/kansas_occurrences \
  --metadata ../../data/processed/kansas_occurrences/_dataset_metadata.json \
  --evidence ../../data/proofs/kansas_biodiversity_etl/20260425/evidence_bundle.json \
  --receipt ../../data/receipts/kansas_biodiversity_etl/20260425/run_receipt.json \
  --proof ../../data/proofs/kansas_biodiversity_etl/20260425/receipt_proof.json
```

### Offline sample flow

```bash
make clean
make sample
```

> [!NOTE]
> `make sample` should remain no-network and fixture-driven. `make all` may use the GBIF harvest step when that harvester is present and network access is intended.

[Back to top](#top)

---

## Usage

### Supported dataset shapes

| Dataset argument | Supported | Identity source |
| --- | --- | --- |
| `*.jsonl` | yes | SHA-256 of dataset file bytes |
| `*.parquet` | yes | `_dataset_metadata.json` |
| partitioned directory | yes | `_dataset_metadata.json` |
| missing path | fail | `dataset_missing` |
| unsupported suffix | fail | `unsupported_dataset_format:<suffix>` |

### Makefile gate target

```makefile
gate:
	@echo "=== Promotion Gate (fail-closed) ==="
	python validate/promotion_gate_full.py \
		--dataset $(DATASET_ROOT) \
		--metadata $(METADATA) \
		--evidence $(EVIDENCE) \
		--receipt $(RECEIPT) \
