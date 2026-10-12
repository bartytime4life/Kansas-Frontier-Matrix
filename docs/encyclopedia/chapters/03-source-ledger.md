<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/03-source-ledger
title: "Source ledger and evidence method"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain source ledger and evidence method and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Source ledger and evidence method

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

Use a source ledger to make a research result repeatable. One row describes one identified product/version and access path, rather than a provider's entire website.

## Minimum useful record

| Field | What to record | Common mistake to avoid |
|---|---|---|
| Identity | Provider, product, native ID, edition and exact artifact or endpoint | Treating a provider name as a station-scoped descriptor |
| Spatial scope | Bounding box, geometry support, CRS and resolution | Treating a pixel, point and polygon as equal support |
| Time | Observation/valid interval, provider publication and local retrieval separately | Calling retrieval time the observation time |
| Meaning | Observation, model, forecast, interpretation, imagery or inventory | Presenting forecasts as observations |
| Bytes | Size, local digest, provider digest when available, receipt location | Calling a local digest provider verification |
| Access and limits | Terms source, permitted use, sensitivity and unresolved conditions | Treating public download availability as admission |
| Review | Candidate disposition, validation scope and required reviewer | Inferring review from a green badge |

## Repository entry points

- [Source catalog](../../sources/catalog/README.md): human descriptions of candidate products.
- [Source descriptor standard](../../sources/SOURCE_DESCRIPTOR_STANDARD.md): descriptor vocabulary and required context.
- [Local data tools](../../../tools/local_data/README.md): capture, manifests and verification.
- [Acquisition receipts](../../../apps/site/source/docs/acquisition-receipts.md): UI-facing capture and verification states.
- [Water pilot](../../runbooks/water-pilot.md): a bounded example with station/time identity and explicit lifecycle holds.

## Work sequence

Begin with the research question and the smallest useful area/time selection. Inspect existing local inventory before selecting new bytes. Review declared size and unknown-length handling, prepare the source-specific plan, and capture only the intended selection. Preserve originals and receipts outside the checkout. Verify captured bytes before interpreting the data.

Record exclusions and partial results with their denominators. If only some dates were returned, describe that coverage directly. A blank map, failed request or empty interval is not proof of absence. Link later transformations to their inputs and exact code version; keep display derivatives distinct from the source record and governed evidence.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
