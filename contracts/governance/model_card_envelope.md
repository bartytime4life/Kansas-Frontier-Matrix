<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/model-card-envelope
title: ModelCardEnvelope Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED; fixture-first
owners:
  - OWNER_TBD model-governance steward
  - OWNER_TBD schema steward
  - OWNER_TBD release steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; governance; model-card; no-network; non-authoritative
owning_root: contracts/
responsibility: Define the shared semantic meaning and trust boundary of a machine-extractable governed model-card envelope.
truth_posture: CONFIRMED source and repository boundaries; PROPOSED object family; UNKNOWN production adoption and model inventory.
related:
  - ../../schemas/contracts/v1/governance/model_card_envelope.schema.json
  - ../../tools/validators/governance/model_card_envelope_core.py
  - ../../tools/validators/governance/validate_model_card_envelope.py
  - ../../fixtures/contracts/v1/governance/model_card_envelope/README.md
  - ../../tests/validators/governance/test_validate_model_card_envelope.py
  - ../../.github/workflows/model-card-envelope.yml
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `ModelCardEnvelope`

> A deterministic governance envelope that makes a model card machine-extractable without turning the card, model, evaluation, signature, or validator result into evidence or release authority.

## Status and evidence basis

**CONFIRMED source pressure.** `New Ideas 2.pdf` repeatedly describes model cards with stable model/document identity, review cadence, FAIR+CARE labels, STAC/DCAT/PROV profile references, commit and prior-version identity, signatures, attestations, SBOMs, telemetry, provenance chains, allowed uses, prohibited uses, and AI-transform permission/prohibition lists. The source also gives model-specific boundaries: environmental reconstruction is not forecasting or emergency alerting; governed narrative output requires citations, masking, and human review; sensitive spatial alignment must not expose protected coordinates.

**CONFIRMED repository fit.** Current repository evidence contains the accepted Directory Rules decision, governance contracts and schemas, deterministic RFC 8785 hashing support, generated-receipt validation, and domain model-card doctrine. The AI schema directory is explicitly a compatibility/index lane, so this first shared machine shape is placed with governance objects rather than creating a parallel canonical schema under `schemas/contracts/v1/ai/`.

**PROPOSED implementation.** This packet defines `kfm.governance.model-card-envelope.v1` as a fixture-first, inactive profile. It does not assert that any named model, artifact, review, signature, attestation, or release exists.

## Purpose

The envelope binds a human-facing model-card reference to:

- deterministic model and document identity;
- model kind and output source role;
- training-run, model-run-receipt, uncertainty, evidence, provenance, and output bindings;
- evaluation, drift, explainability, telemetry, signature, attestation, SBOM, and release-manifest bindings;
- rights, sensitivity, FAIR+CARE, sovereignty, review, citation, correction, and rollback posture;
- allowed and prohibited uses;
- allowed and prohibited AI transforms;
- explicit no-authority and non-effect declarations; and
- an RFC 8785 JCS plus SHA-256 `spec_hash`.

The object is a governance descriptor. It is not the model, model card prose, source evidence, evaluation report, policy decision, review record, release manifest, proof pack, or published output.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2 and makes `docs/doctrine/directory-rules.md` the writable human placement authority. This slice follows existing responsibility roots:

| Responsibility | Path |
|---|---|
| Semantic meaning | `contracts/governance/model_card_envelope.md` |
| Machine shape | `schemas/contracts/v1/governance/model_card_envelope.schema.json` |
| Synthetic examples | `fixtures/contracts/v1/governance/model_card_envelope/base.json` and `cases/` |
| Executable validation | `tools/validators/governance/model_card_envelope_core.py` and `validate_model_card_envelope.py` |
| Enforceability | `tests/validators/governance/test_validate_model_card_envelope.py` |
| Hosted orchestration | `.github/workflows/model-card-envelope.yml` |
| AI authoring provenance | `data/receipts/generated/genrec-model-card-envelope-20260807.json` |

No `mcp/` root, model store, training pipeline, release lane, evidence store, policy home, or public route is created.

## Required identity

For a model ID `kfm:model:<slug>` and version `<semver>`, the validator derives:

```text
model_card_id              = kfm:model-card:<slug>:v<semver>
semantic_document_id       = kfm-modelcard-<slug>
doc_uuid                    = urn:kfm:modelcard:<slug>:v<semver>
event_source_id             = urn:kfm:modelcard:<slug>
```

A mismatch is a blocking finding. The final `spec_hash` covers the entire envelope except the `spec_hash` member itself.

## Model kinds and reality boundary

| Model kind | Required output role | Additional minimum prohibitions |
|---|---|---|
| `ENVIRONMENTAL_RECONSTRUCTION` | `MODELED` | forward climate projection, emergency alerting, uncited narrative use; fabricated results, dataset IDs, license rights |
| `GOVERNED_NARRATIVE` | `INTERPRETIVE` | autonomous publishing, sensitive heritage narrative, unreviewed historical claims, culturally sensitive reconstruction; fabricated facts/citations, genealogy and sacred-site inference |
| `SPATIAL_ALIGNMENT` | `MODELED` | archaeological precision mapping, cadastral correction, sensitive cultural alignment |
| `DOMAIN_MODEL` | `MODELED` | baseline governance prohibitions |
| `OTHER` | `MODELED` | baseline governance prohibitions |

Every model kind must prohibit fabrication of provenance, governance override, sensitive-coordinate exposure, deanonymization, and publication without human review.

The reality-boundary block declares that model outputs are modeled, synthetic, or interpretive derivatives. It always denies observation, operational, and publication authority.

## Bindings

Every referenced object is represented as:

```json
{
  "ref": "kfm:evidence-bundle:example:v1.0.0",
  "digest": "sha256:<64 lowercase hex>",
  "role": "EVIDENCE_BUNDLE"
}
```

The validator requires role-correct, sorted, digest-pinned bindings for:

- training data;
- training run and model-run receipt;
- uncertainty;
- model-card document;
- EvidenceBundles and citations;
- provenance and output artifacts;
- evaluation, drift, and explainability reports;
- signature, attestation, SBOM, manifest, and release manifest;
- telemetry and its schema;
- governance, ethics, and sovereignty policies;
- review records, correction, and rollback records.

A reference with traversal segments, backslashes, placeholders, or all-zero digest material is rejected.

## Governance state

The declared model-card state uses independent fields:

- decision: `ALLOW`, `HOLD`, or `DENY`;
- review: `PENDING`, `APPROVED`, `CHANGES_REQUESTED`, or `REJECTED`;
- release: `DRAFT`, `CANDIDATE`, `RELEASED`, or `WITHDRAWN`.

These fields do not create the underlying decisions. They make claims about external records that later release tooling must authenticate.

A declared `RELEASED` state requires:

- `ALLOW`;
- approved and completed human review;
- a review record and review timestamp;
- verified rights;
- correction and rollback references; and
- completed sovereignty review when sensitive or sovereignty-scoped material is allowed.

## Validation outcomes and exit codes

| Outcome | Meaning | Candidate CLI exit |
|---|---|---:|
| `PASS` | Shape and semantics conform; declared state is `ALLOW` + approved + released. | `0` |
| `HOLD` | Shape and semantics conform; declared state is intentionally pending or held. | `3` |
| `DENY` | Shape and semantics conform; declared state is denied, rejected, or withdrawn. | `4` |
| `FAIL` | Schema, identity, reference, permission, use-boundary, governance, or hash conformance failed. | `1` |
| `ERROR` | Input could not be read or parsed safely. | `2` |

`--fixtures` returns `0` only when the shared `base.json` plus every named file under `cases/` exactly matches the reviewed case ID, outcome, and finding set.

A `PASS` is validation evidence for this inactive profile only. It is not proof of model quality, source truth, rights, human approval, signature validity, attestation validity, release readiness, publication, deployment, or public-use authority.

## Determinism and safety

The validator:

- uses bounded duplicate-free UTF-8 JSON loading from the shared hashing package;
- validates Draft 2020-12 shape locally;
- computes RFC 8785 JCS plus SHA-256 identity;
- makes no network request;
- emits stable finding codes and JSON paths without echoing untrusted values;
- orders findings and fixture reports deterministically; and
- treats unknown fields as invalid.

## Focused validation

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_validate_model_card_envelope.py' \
  --verbose

python tools/validators/governance/validate_model_card_envelope.py \
  --fixtures
```

Validate one candidate:

```bash
python tools/validators/governance/validate_model_card_envelope.py \
  --candidate path/to/model-card-envelope.json
```

## Non-goals

This first slice does not:

- create or train a model;
- generate human model-card prose;
- fetch training data or resolve remote catalog records;
- verify model metrics, drift, explainability, signatures, attestations, SBOMs, or telemetry;
- establish a complete repository-wide model registry;
- activate the compatibility AI schema lane;
- add a public API, graph node, MapLibre layer, Focus Mode implementation, or Story Node;
- promote, release, deploy, publish, or authorize public use.

## Correction and rollback

Before merge, close the draft pull request and delete its feature branch. If later merged, revert the implementation commit. That removes the additive contract, schema, fixture family, validator, tests, workflow, and generated authoring receipt.

No model, evidence object, policy decision, release record, published artifact, or external registry entry needs restoration because this packet creates none.

## Next bounded candidates

After this object family is reviewed, separate slices may add:

1. an adapter that projects approved human model-card metadata into this envelope;
2. signature, SBOM, SLSA, and telemetry resolvers that authenticate referenced artifacts;
3. a model-card registry projection;
4. a governed Focus Mode consumer that accepts only released, policy-safe model cards; and
5. domain profiles for hydrology, climate, habitat, and spatial alignment.

Each remains a separate review and rollback boundary.
