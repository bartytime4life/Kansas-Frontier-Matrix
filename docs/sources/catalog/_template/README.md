<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-template-readme
title: docs/sources/catalog/_template README
type: readme
version: v0.1
status: draft
owners: ["@kfm/maintainers"]
created: 2026-07-16
updated: 2026-07-16
policy_label: public
owning_root: docs/
responsibility: documentation-only templates for human-authored source-catalog pages
truth_posture: repository inventory confirmed; template content remains proposed until completed and reviewed
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/_examples/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
notes:
  - "The four template files listed here were present in the repository on 2026-07-16."
  - "This folder is documentation-only and does not define machine contracts, schemas, policy, source admission, or release authority."
[/KFM_META_BLOCK_V2] -->

# `_template`

## Purpose

This folder owns reusable Markdown starting points for human-authored pages in `docs/sources/catalog/`. It helps authors keep source-family, source-product, crosswalk, and rights-note documentation consistent without creating a second source of machine authority.

## Authority level

`exploratory` — documentation-only, non-authoritative scaffolding. The templates may explain repository contracts, schemas, policy, and source records, but they cannot replace or amend them.

## Status

`CONFIRMED` as a repository folder containing the four templates inventoried below. Each template is marked `draft` or `PROPOSED`; a copied page remains draft until its placeholders, links, source facts, and review requirements are resolved.

## What belongs here

Only Markdown templates for source-catalog documentation and this routing README belong here.

| Template | Intended destination | Current role |
|---|---|---|
| [`SOURCE_FAMILY_TEMPLATE.md`](./SOURCE_FAMILY_TEMPLATE.md) | `<family>/README.md` | Source-family orientation and routing. |
| [`SOURCE_PRODUCT_TEMPLATE.md`](./SOURCE_PRODUCT_TEMPLATE.md) | `<family>/<product-name>.md` | Product-level catalog-profile, provenance, temporal, geometry, rights, and sensitivity notes. |
| [`CROSSWALK_TEMPLATE.md`](./CROSSWALK_TEMPLATE.md) | An authored crosswalk page | Explanatory field mapping between two standards. |
| [`RIGHTS_NOTE_TEMPLATE.md`](./RIGHTS_NOTE_TEMPLATE.md) | A rights note beside a family or product page | Per-source rights and sensitivity documentation that points to policy and source records. |

Copying rules:

1. Copy the closest matching template to its intended authored destination; do not use `_template/` as the home for a real source or product page.
2. Give the destination one unique, destination-specific `KFM_META_BLOCK_V2`. Do not reuse the template asset's `doc_id`, and remove the literal `<KFM Meta Block v2 — ...>` instruction line.
3. Replace every angle-bracket token and every `PLACEHOLDER`. Resolve each `NEEDS VERIFICATION`, `PROPOSED`, and `UNKNOWN` marker with repository or cited source evidence, or retain the marker when uncertainty is real.
4. Rebase relative links for the destination directory. A link that works from `_template/` may not work from a family directory or product page.
5. Do not invent identifiers, checksums, endpoint URLs, license terms, rights grants, sensitivity tiers, source roles, or catalog support. Link to the owning machine or policy artifact instead.
6. Keep the original template unchanged unless the change is an intentional improvement for every future copy.

## What does NOT belong here

- Completed source-family, source-product, crosswalk, or rights-note pages.
- `SourceDescriptor` records or source-admission decisions.
- Contracts, JSON Schemas, policy rules, validator code, fixtures, catalog artifacts, receipts, proofs, or release manifests.
- Source facts copied from a template without current verification.
- Filled examples; illustrative payloads belong in [`_examples/`](../_examples/README.md).
- Alternate template copies that drift from one of the four inventoried templates.

## Inputs

- Manual authoring based on the lane rules in [`docs/sources/catalog/README.md`](../README.md).
- Placement and folder-README requirements from [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md).
- Object meaning from `contracts/`, machine shapes from `schemas/contracts/v1/`, decisions from `policy/`, and source records from `data/registry/sources/`.
- Current repository evidence for links, validators, fixtures, and workflow status.

## Outputs

- Human-readable Markdown drafts placed under `docs/sources/catalog/`.
- Cross-links from those drafts to their owning contracts, schemas, policy, source records, connectors, validators, and catalog lanes.
- No machine-authoritative artifact and no publication or source-admission decision.

## Validation

For a template or copied page:

- run `git diff --check` for whitespace and patch errors;
- verify that every local link resolves from the authored destination;
- search the authored file for unresolved angle-bracket tokens and `PLACEHOLDER` text;
- when the page names a `SourceDescriptor`, validate the machine record with `python tools/validators/validate_source_descriptor.py --fixtures` or the fixture-backed aggregate runner `python tools/validators/_common/run_all.py`.

The confirmed source-descriptor validator checks `schemas/contracts/v1/source/source_descriptor.schema.json` against `fixtures/contracts/v1/source/source_descriptor/`; it does **not** validate these Markdown templates. The current `docs-build`, `link-check`, and `source-descriptor-validate` GitHub workflows are present but execute `echo TODO ...`, so they are not evidence of an implemented template or documentation gate. No executable dedicated to validating this template folder is confirmed.

## Review burden

`.github/CODEOWNERS` has no narrower rule for `docs/sources/` or this folder, so the repository-wide fallback assigns changes to `@kfm/maintainers`. A copied page that changes source, rights, sensitivity, schema, or catalog claims also needs review from the relevant owner before its draft labels can be strengthened, even though that additional routing is not encoded in the current `CODEOWNERS` file.

## Related folders

- [`docs/sources/catalog/`](../README.md) — parent human-facing source-catalog lane.
- [`docs/sources/catalog/_examples/`](../_examples/README.md) — illustrative payloads, explicitly non-authoritative.
- [`docs/sources/`](../../README.md) — parent source-documentation lane.
- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — current machine schema family referenced by the source-descriptor validator.
- [`fixtures/contracts/v1/source/source_descriptor/`](../../../../fixtures/contracts/v1/source/source_descriptor/) — current source-descriptor fixtures.
- [`tools/validators/validate_source_descriptor.py`](../../../../tools/validators/validate_source_descriptor.py) — confirmed fixture-backed SourceDescriptor validator entrypoint.
- [`data/registry/sources/`](../../../../data/registry/sources/) — source-record lane; its contents, not these templates, carry repository source records.

## ADRs

No accepted ADR is confirmed as assigning authority to `_template/` itself. The following present ADR files are `proposed` and inform authored destinations without making these templates machine authority:

- [`ADR-0001 — Schema Home`](../../../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) — proposed separation of semantic contracts from machine-checkable schemas.
- [`ADR-0017 — Source Descriptor Admission Process`](../../../adr/ADR-0017-source-descriptor-admission-process.md) — proposed source-admission and descriptor discipline.
- [`ADR-0022 — Catalog Matrix`](../../../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) — proposed STAC, DCAT, and PROV catalog-closure agreement.

## Last reviewed

2026-07-16
