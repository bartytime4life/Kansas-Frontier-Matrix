<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-templates-readme
title: configs/templates/ — Configuration Templates
type: readme
version: v0.3
status: repository-grounded; draft; non-authoritative
owners: "NEEDS VERIFICATION — .github/CODEOWNERS routes /configs/ to @bartytime4life; a separate configuration/docs steward and independent approval control were not verified"
created: 2026-06-16
updated: 2026-09-04
policy_label: public; commit-safe; non-secret; non-authoritative
current_path: configs/templates/README.md
owning_root: configs/
responsibility: commit-safe configuration templates and their boundary documentation
truth_posture: cite-or-abstain; tracked template bytes prove presence only unless a named consumer, contract, schema, policy, validation, and runtime or release evidence establish more
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ccc4f3a7518271fadb6461ded3258706dd5c7303
  target_blob: b1ab4ef69a6f5e74e7988ac8b3acb1ebb14cfcae
  direct_children: 6
  template_payloads: 5
related:
  - ../README.md
  - ../examples/README.md
  - ../local/README.md
  - ../dev/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../contracts/README.md
  - ../../schemas/README.md
  - ../../policy/README.md
  - ../../apps/README.md
  - ../../pipelines/README.md
  - ../../runtime/README.md
  - ../../release/README.md
  - ../../data/README.md
tags: [kfm, configs, templates, defaults, governance]
notes:
  - "This is a same-path documentation maintenance change; it does not alter any template payload."
  - "The six direct children and five payload bytes are confirmed at the pinned base."
  - "Template consumers, semantic adequacy, precedence, dedicated validators, and CI enforcement remain NEEDS VERIFICATION."
  - "Template names and fields never create schema, policy, source, release, runtime, lifecycle, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Configuration templates

`configs/templates/`

This lane contains small, commit-safe configuration templates under the canonical [`configs/`](../README.md) responsibility root. It is a review and authoring surface for structure and placeholders—not a source of semantic truth, policy, runtime behavior, release state, lifecycle state, or generated output.

> [!IMPORTANT]
> **Current posture:** draft / `NEEDS VERIFICATION` for consumer binding and validation. The directory listing and five payload files are `CONFIRMED` at `main@ccc4f3a7518271fadb6461ded3258706dd5c7303`. No template-specific consumer or validator is claimed by this README.

## Purpose

Use this lane for reusable templates that are safe to commit and straightforward to review. A template may show expected keys, placeholder values, and a likely configuration role. It does not prove that an application, package, pipeline, runtime adapter, policy gate, release process, or viewer loads or accepts it.

The governing separation is:

| Question | Owning surface | What this lane may do |
|---|---|---|
| What does a field mean? | [`contracts/`](../../contracts/README.md) | Point toward the meaning; do not redefine it |
| What shape is valid? | [`schemas/`](../../schemas/README.md) | Provide a candidate shape; do not become schema authority |
| May a source, operation, or exposure proceed? | [`policy/`](../../policy/README.md) | Keep policy-significant decisions outside templates |
| What code consumes the configuration? | [`apps/`](../../apps/README.md), [`pipelines/`](../../pipelines/README.md), [`runtime/`](../../runtime/README.md), packages, tools, tests, or workflows | Name a consumer only when verified |
| What is the lifecycle or release state? | [`data/`](../../data/README.md) and [`release/`](../../release/README.md) | Never turn a template into an instance, receipt, proof, release, or publication record |

## Directory fit and authority boundary

`configs/templates/` is an established sublane of `configs/`. The accepted Directory Rules route placement by responsibility, and [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) identifies [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) as the writable human authority for that decision.

Templates here must remain:

- non-secret and safe to commit to the public repository;
- placeholder-oriented rather than environment-bound;
- separable from contracts, schemas, policy, source admission, runtime wiring, release decisions, and lifecycle records;
- explicit about unresolved consumers, loaders, precedence, validation, rights, and sensitivity;
- reversible to the prior same-path README when the documentation is corrected.

Do not place application source, pipeline logic, durable pipeline specifications, runtime adapter code, infrastructure controls, schemas, policy rules, receipts, proofs, registry rows, release decisions, or generated outputs here. Use the owning roots named above.

## Current tracked inventory

The current `main` directory listing contains exactly six direct children: this README and five template payloads.

```text
configs/templates/
├── README.md
├── dataset_manifest.template.yaml
├── layer_manifest.template.yaml
├── release_manifest.template.yaml
├── source_descriptor.template.yaml
└── viewer_style.template.json
```

### Payload map

The following map records observed names and fields. It is an inventory, not a schema or consumer registry.

| File | Observed placeholder shape | Bounded role | Consumer / validator status |
|---|---|---|---|
| `dataset_manifest.template.yaml` | `id`, `spec_hash`, `valid_time`, `provenance` | Dataset identity, temporal extent, and provenance placeholders | No direct consumer or dedicated validator verified |
| `layer_manifest.template.yaml` | `id`, `release_id`, `proof_refs`, `rights`, `sensitivity` | Layer identity plus release, proof, rights, and sensitivity placeholders | No direct consumer or dedicated validator verified |
| `release_manifest.template.yaml` | `release_id`, `spec_hash`, `candidates`, `rollback_target`, `signatures` | Candidate release and rollback/signature shape | Does not create a release; consumer and validator remain unverified |
| `source_descriptor.template.yaml` | `id`, `domain`, `role`, `authority`, `rights`, `sensitivity_floor`, `update_cadence`, `access_posture`, `citation_template` | Source-description and citation placeholders | Does not admit a source; consumer and validator remain unverified |
| `viewer_style.template.json` | `version: 8`, `name`, empty `sources`, empty `layers` | Minimal viewer-style scaffold | Viewer/runtime binding and validation remain unverified |

The fields above are transcribed from the five tracked files at the pinned base. `TBD`, `null`, empty objects, empty arrays, and empty strings are incomplete placeholders; they are not evidence that a value is valid, safe, current, rights-cleared, or ready for publication.

## Placeholder and safety rules

1. Keep examples synthetic, public-safe, and minimal.
2. Never add credentials, tokens, private keys, cookies, signed URLs, confidential endpoints, private identifiers, restricted source details, exact sensitive locations, living-person records, DNA/genomic material, or culturally controlled information.
3. Do not replace a placeholder with a live value merely because a file parses. Rights, sensitivity, source role, contract, policy, review, release, and rollback remain separate checks.
4. Do not use a template as a shortcut for a source descriptor instance, release manifest, evidence record, registry row, or generated artifact.
5. If a new consumer or validator is discovered, document the exact path and validation scope before upgrading the status language.

## Using a template safely

Before a template is consumed, verify the complete path from shape to behavior:

- identify the named consumer, loader, environment scope, and deterministic precedence;
- resolve the applicable contract and schema, if any;
- check policy, rights, sensitivity, source-admission, and public-path constraints;
- exercise positive and negative validation, including missing, malformed, unknown, and unsafe values where the consumer makes those distinctions;
- record the exact test, workflow, or runtime evidence and the failure behavior;
- preserve correction and rollback instructions for any real consumer binding.

This README update does not establish any of those bindings. A future payload change should include the smallest corresponding contract, schema, validator, test, or consumer documentation needed to make its claim inspectable.

## Validation for changes in this lane

### Documentation-only changes

For a README-only change, review the complete diff, confirm same-path placement, check headings and relative links, inspect whitespace, and read the remote file back from the resulting branch. Repository-wide runtime or release checks are not implied by a documentation-only change.

### Template payload changes

When a payload changes, add proportional checks for syntax and machine shape, then verify the named consumer, precedence, semantic contract, policy boundary, rights/sensitivity handling, negative cases, and rollback path. No dedicated template validator or config-wide CI enforcement was verified for this lane at the pinned base.

Do not call a template valid, consumed, deployed, released, published, or runtime-proven from its presence, filename, parse result, or an unrelated green check.

## Migration and correction posture

If material is misplaced here:

1. classify the material by responsibility and lifecycle;
2. identify the owning root and any existing consumer;
3. make the smallest reviewable move or compatibility correction;
4. preserve owner notes, rights/sensitivity decisions, and rollback instructions;
5. record drift if the old location was consumed or referenced.

For a documentation correction, restore the prior same-path README or revert the single documentation commit. Payloads remain unchanged unless a later, separately scoped change is authorized and validated.

## Definition of done

- [x] The established `configs/templates/` path is retained.
- [x] The current six-entry inventory is re-pinned to an exact `main` commit.
- [x] All five payload names and observed placeholder shapes are documented.
- [x] Template, schema, policy, source, release, lifecycle, runtime, and publication boundaries are explicit.
- [x] Consumer, validator, precedence, rights, sensitivity, and CI uncertainty is labeled rather than inferred.
- [ ] A responsible configuration/docs steward is independently confirmed.
- [ ] Each template has a verified named consumer and validation path.
- [ ] Config-wide precedence and CI enforcement are verified.

## Status summary

At `main@ccc4f3a7518271fadb6461ded3258706dd5c7303`, `configs/templates/` contains this README and five small placeholder templates. Their tracked presence and observed bytes are `CONFIRMED`. Consumer binding, semantic adequacy, schema alignment, precedence, dedicated validation, CI enforcement, runtime use, release effect, and publication readiness remain `NEEDS VERIFICATION` or `UNKNOWN`.

This lane is a commit-safe authoring surface. It is not a source of runtime truth, schema truth, policy truth, evidence truth, lifecycle truth, release truth, implementation truth, or generated-output authority.

<p align="right"><a href="#top">Back to top</a></p>
