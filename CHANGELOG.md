# Changelog

All notable changes to the **Kansas Frontier Matrix (KFM)** repository will be documented in this file.

This changelog is intended to support traceability across the full KFM pipeline:
**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

The format is based on *Keep a Changelog*, and the project aims to follow *Semantic Versioning* (SemVer).

## [Unreleased]

### Added
- `CHANGELOG.md` (initial changelog scaffold).

### Changed

### Deprecated

### Removed

### Fixed

### Security

---

## Changelog entry guidance (recommended)

When adding entries, group changes by the pipeline stage(s) they impact:

- **ETL**: ingestion, parsing, normalization, deterministic transforms
- **Catalog**: STAC/DCAT/PROV outputs, mapping docs, catalog validation
- **Graph**: ontology updates, ingest fixtures, migrations
- **AI**: model cards, evidence products, prompt-gate behavior, evaluation harness
- **API**: OpenAPI/GraphQL contracts, endpoints, auth/redaction, contract tests
- **UI**: layer registry, map rendering, Focus Mode UX, accessibility
- **Story**: Story Node template/content, citations, publish workflow
- **Governance/Security**: review gates, scanning/CI policy, sensitive-data handling

Where applicable, include identifiers and provenance such as:
- DCAT dataset identifiers
- STAC Collection/Item IDs
- PROV activity/run IDs (and/or run manifests)
- contract/schema versions (old → new), plus migration notes for breaking changes

