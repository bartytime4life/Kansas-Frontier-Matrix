<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-templates-readme
title: configs/templates/ — Configuration Templates
type: readme
version: v0.4
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
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  prior_blob: 7a0d642589a6d622929f4e67fa77b9cbb209fe2e
  base_tree: b17f061592f3da0b1903c5252bc1d12437fe3575
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
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
  - "v0.4 preserves v0.3 guidance and anchors, documents concrete public-valued defaults, and adds a read-only syntax check; template payloads are unchanged."
  - "The six direct children and five payload bytes are confirmed at the pinned base."
  - "Template consumers, semantic adequacy, precedence, dedicated validators, and CI enforcement remain NEEDS VERIFICATION."
  - "Template names and fields never create schema, policy, source, release, runtime, lifecycle, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Configuration templates

`configs/templates/`

This lane contains small, commit-safe configuration templates under the canonical [`configs/`](../README.md) responsibility root. It is a review and authoring surface for structure and placeholders—not a source of semantic truth, policy, runtime behavior, release state, lifecycle state, or generated output.

> [!IMPORTANT]
> **Current posture:** draft / `NEEDS VERIFICATION` for consumer binding and validation. The directory listing and five payload files are `CONFIRMED` at `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`. The inspection recipe below checks syntax only; no production consumer, template schema conformance, or template-specific validation gate is established.

**Quick navigation:** [Inventory](#current-tracked-inventory) · [Concrete defaults](#concrete-defaults-are-not-permissions) · [Safe use](#using-a-template-safely) · [Read-only check](#read-only-syntax-check) · [Rollback](#migration-and-correction-posture)

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

At the pinned snapshot, the complete directory listing contains exactly six files and no child directories: this README and five template payloads. This describes tracked Git content, not ignored workstation files, runtime loading, or external storage.

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

| File | Observed fields and scaffold | Bounded role | Consumer / validator status |
|---|---|---|---|
| [`dataset_manifest.template.yaml`](dataset_manifest.template.yaml) | `id`, `spec_hash`, `valid_time`, `provenance` | Dataset identity, temporal extent, and provenance placeholders | No direct consumer or dedicated validator verified |
| [`layer_manifest.template.yaml`](layer_manifest.template.yaml) | `id`, `release_id`, `proof_refs`, `rights`, `sensitivity` | Layer identity plus release, proof, rights, and sensitivity placeholders | No direct consumer or dedicated validator verified |
| [`release_manifest.template.yaml`](release_manifest.template.yaml) | `release_id`, `spec_hash`, `candidates`, `rollback_target`, `signatures` | Candidate release and rollback/signature shape | Does not create a release; consumer and validator remain unverified |
| [`source_descriptor.template.yaml`](source_descriptor.template.yaml) | `id`, `domain`, `role`, `authority`, `rights`, `sensitivity_floor`, `update_cadence`, `access_posture`, `citation_template` | Source-description scaffold with concrete `public` defaults; see warning below | Does not admit a source; consumer and validator remain unverified |
| [`viewer_style.template.json`](viewer_style.template.json) | `version: 8`, `name`, empty `sources`, empty `layers` | Minimal viewer-style scaffold | Viewer/runtime binding and validation remain unverified |

The fields above are transcribed from the five tracked files at the pinned base. These scaffolds mix unresolved placeholders with concrete example values. Neither kind establishes a complete, valid, safe, current, rights-cleared, or publishable instance. Whether a null or empty value is permitted is a question for the applicable schema and consumer, not a blanket rule supplied by this README. The `greenfield` comments in three templates are historical scaffold labels, not a claim that the repository is empty.


### Exact payload identities

Git blob IDs identify the exact inspected bytes; they are not schema versions or policy approvals. No payload changes in this revision.

| Template | Git blob at the pinned base |
|---|---|
| `dataset_manifest.template.yaml` | `9d750cc5bbe5c17ae985f5370aa28f768592bf4a` |
| `layer_manifest.template.yaml` | `ffd7b964e851ca7e6d26805f86a30bbf477cf488` |
| `release_manifest.template.yaml` | `d72c63aace042f2ba3856d7e20252b75fe20ac45` |
| `source_descriptor.template.yaml` | `f4dae75173aa07eae3c9f09f3f08223de4ae2095` |
| `viewer_style.template.json` | `0e14e644bacb66f8e8e0e18925b50b8a22108b15` |

### Concrete defaults are not permissions

> [!WARNING]
> `source_descriptor.template.yaml` contains **`sensitivity_floor: public` and `access_posture: public`**, while `rights.license` is still `TBD` and `citation_template` is empty. These are observed template values, **not an evaluated sensitivity classification, access decision, license grant, or source-admission record**. Never carry them into a real source instance without the governing evidence and review. Unresolved rights or sensitivity must keep admission and exposure held or denied; this documentation does not invent replacement enum values or change the payload.

`rights.attribution_required: true` does not resolve the missing license or citation. Likewise, empty `proof_refs`, `candidates`, `signatures`, and `provenance` do not establish evidence closure, approval, or lineage. The viewer file's `version: 8` with empty `sources` and `layers` proves only that those fields are present; it does not demonstrate a working map or an admitted renderer dependency.

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

**Keep authoring separate from activation.** Select a destination by the resulting object's responsibility and verified consumer, not by copying a filename into a canonical store. Directory Rules §10.4 places shared non-secret templates under `configs/`; §11.2 (`DIR-DATA-005`) excludes placeholder instances from canonical trust-instance lanes. An edited template is still candidate input. It cannot skip `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`, resolve `EvidenceRef -> EvidenceBundle` by itself, or expose internal stores or a model endpoint to public clients.

Do not assume every template belongs in `configs/local/`, is automatically loaded, or has a common overlay order. Confirm the destination, loader, precedence, ignored-local-file handling, and rollback before any real use. Secrets remain outside Git, including outside these templates.

## Validation for changes in this lane

### Documentation-only changes

For a README-only change, review the complete diff, confirm same-path placement, check headings and relative links, inspect whitespace, and read the remote file back from the resulting branch. Repository-wide runtime or release checks are not implied by a documentation-only change.

### Read-only syntax check

Run from the repository root with Python 3 and PyYAML already available in an isolated development environment. This recipe reads the **five named files**, prints their SHA-256 digests, and exits nonzero on a missing/unreadable file, invalid UTF-8, or a parser error. It writes no files, fetches no sources, installs no dependencies, and starts no service.

```bash
python - <<'PYCODE'
from hashlib import sha256
from pathlib import Path
import json

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required; use the project's development environment.")

root = Path("configs/templates")
names = (
    "dataset_manifest.template.yaml",
    "layer_manifest.template.yaml",
    "release_manifest.template.yaml",
    "source_descriptor.template.yaml",
    "viewer_style.template.json",
)
for name in names:
    path = root / name
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        raise SystemExit(f"PARSE_ERROR {name}: {type(exc).__name__}") from None
    print(f"PARSE_ONLY {name} sha256:{sha256(raw).hexdigest()}")
print("Syntax check finished; schema, policy, consumer, and release checks NOT performed.")
PYCODE
```

The pinned payloads parse with this recipe, **including the unresolved `public` defaults**. That is deliberate evidence of the distinction between syntax and admissibility, not a passing source-admission test. The recipe does not validate required keys, duplicate-key policy, identifiers, digest references, schema compatibility, rights, sensitivity, citations, signatures, or consumer behavior. It is not a parser for arbitrary untrusted or oversized intake. Re-run after changes; do not copy this snapshot's result into a later receipt as a new execution.

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

For a documentation correction, restore the prior same-path README (`7a0d642589a6d622929f4e67fa77b9cbb209fe2e` for this revision) through a reviewed revert, and record the resulting generated-work provenance. Preserve earlier receipts as history rather than rewriting them to match new bytes. Payloads remain unchanged unless a later, separately scoped change is authorized and validated.

## Definition of done

- [x] The established `configs/templates/` path is retained.
- [x] The current six-entry inventory is re-pinned to an exact `main` commit.
- [x] All five payload names and observed placeholder shapes are documented.
- [x] Template, schema, policy, source, release, lifecycle, runtime, and publication boundaries are explicit.
- [x] Consumer, validator, precedence, rights, sensitivity, and CI uncertainty is labeled rather than inferred.
- [x] Concrete `public` defaults and unresolved license/citation fields are distinguished from policy decisions.
- [x] A read-only syntax recipe and its non-authority limits are documented.
- [ ] A responsible configuration/docs steward is independently confirmed.
- [ ] Each template has a verified named consumer and validation path.
- [ ] Config-wide precedence and CI enforcement are verified.

## Status summary

At `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`, `configs/templates/` contains this README and five small placeholder templates. Their tracked presence, exact blob identities, concrete defaults, and bounded syntax-check result are `CONFIRMED`; syntax success is not source or release approval. Consumer binding, semantic adequacy, schema alignment, precedence, dedicated validation, CI enforcement, runtime use, release effect, and publication readiness remain `NEEDS VERIFICATION` or `UNKNOWN`.

This lane is a commit-safe authoring surface. It is not a source of runtime truth, schema truth, policy truth, evidence truth, lifecycle truth, release truth, implementation truth, or generated-output authority.

<p align="right"><a href="#top">Back to top</a></p>
