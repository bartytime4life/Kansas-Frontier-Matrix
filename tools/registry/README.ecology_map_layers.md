<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: Ecology Map Layer Registry Tooling
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS_VERIFICATION_CREATED_DATE>
updated: 2026-04-24
policy_label: <NEEDS_VERIFICATION_POLICY_LABEL>
related: [
  ./ecology_map_layer_registry.py,
  ./ecology_map_layer_registry_cli.py,
  ./tests/test_ecology_map_layer_registry.py,
  ./tests/test_ecology_map_layer_registry_cli.py,
  ../../schemas/ecology/ecology_map_layer_binding.schema.json,
  ../../contracts/ui/ecology_maplibre_layer_binding.md,
  ../../data/registry/ecology/map_layers/README.md
]
tags: [kfm, ecology, registry, maplibre, layer-binding, evidencebundle]
notes: [
  "Proposed README for ecology map-layer registry tooling.",
  "Active-branch file existence, schema home, policy label, and CI wiring remain NEEDS VERIFICATION.",
  "Documents proposed registry loader, validator, CLI, test surface, and fail-closed rules."
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ecology Map Layer Registry Tooling

Validate and resolve ecology map-layer bindings so MapLibre interactions stay tied to governed evidence.

<div align="left">

![status](https://img.shields.io/badge/status-experimental-orange)
![truth posture](https://img.shields.io/badge/truth--posture-PROPOSED-blue)
![renderer](https://img.shields.io/badge/renderer-MapLibre-2c7cd6)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![repo verification](https://img.shields.io/badge/repo--verification-needed-lightgrey)

</div>

**Owners:** @bartytime4life  
**Suggested path:** `tools/registry/README.ecology_map_layers.md`  
**Status:** `experimental` README surface / `draft` document metadata  
**Truth posture:** `PROPOSED` until active-branch verification confirms files, schema home, CLI behavior, and CI gates.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Flow](#binding-flow) · [CLI](#cli) · [Fail-closed rules](#fail-closed-rules) · [Tests](#tests-and-ci) · [Done](#definition-of-done)

> [!IMPORTANT]
> This README describes the intended registry tooling boundary. It does **not** claim that the loader, CLI, schema, tests, or CI enforcement already exist on the active branch.

---

## Scope

This tooling validates the map-side evidence chain for ecology layers. It is designed to answer a narrow question before the UI draws or explains a layer:

> Can this `layer_id` resolve to a schema-valid, hash-matching, evidence-bound layer binding that is safe for the governed MapLibre shell to consume?

The intended chain is:

```text
layer_id
  -> registry entry
  -> binding_ref
  -> binding schema validation
  -> candidate_id / evidence reference
  -> EvidenceBundle resolution by governed API
  -> Evidence Drawer payload
```

The registry output should keep renderer state subordinate to governed evidence. A MapLibre layer may be visible, clickable, styled, or filtered, but consequential explanation remains evidence-backed and policy-mediated.

[Back to top](#top)

## Repo fit

| Surface | Path or dependency | Truth label | Role |
|---|---|---:|---|
| README | `tools/registry/README.ecology_map_layers.md` | PROPOSED | Maintainer-facing guide for the registry tooling. |
| Loader | `tools/registry/ecology_map_layer_registry.py` | NEEDS VERIFICATION | Loads registry JSON, resolves binding files, validates shape and hash agreement. |
| CLI | `tools/registry/ecology_map_layer_registry_cli.py` | NEEDS VERIFICATION | Exposes list and single-layer resolve operations for local checks and CI. |
| Tests | `tools/registry/tests/` | NEEDS VERIFICATION | Unit and CLI tests for fail-closed behavior. |
| Binding schema | `schemas/ecology/ecology_map_layer_binding.schema.json` | NEEDS VERIFICATION | Machine contract for one evidence-bound ecology map layer binding. |
| UI contract | `contracts/ui/ecology_maplibre_layer_binding.md` | PROPOSED | Human-readable contract for what MapLibre and the Evidence Drawer may consume. |
| Registry data | `data/registry/ecology/map_layers/registry.json` | PROPOSED | Layer index containing `layers[]` entries and `binding_ref` pointers. |

### Upstream and downstream

| Direction | Surface | Boundary rule |
|---|---|---|
| Upstream | Source descriptors, processed ecology candidates, catalog records, proof/release state | Registry entries must not become source truth. They point to governed artifacts; they do not replace them. |
| Upstream | `ecology_map_layer_binding.schema.json` | Binding shape is schema-owned. README examples are illustrative unless the schema confirms them. |
| Downstream | MapLibre layer setup | MapLibre consumes released source/layer metadata and visual treatment only. It does not assemble evidence truth. |
| Downstream | Governed API | EvidenceRef / EvidenceBundle resolution happens through governed service boundaries, not browser-side registry parsing. |
| Downstream | Evidence Drawer | Clicks and drill-throughs should open trust-visible evidence, review, policy, freshness, and provenance context. |
| Downstream | CI / promotion checks | Registry validation should become a release gate before public layer publication. |

[Back to top](#top)

## Accepted inputs

| Input | Required | Expected role |
|---|---:|---|
| Registry JSON | Yes | A JSON object with `layers[]` entries. Each active layer should identify a `layer_id`, `binding_ref`, and `spec_hash`. |
| Binding JSON | Yes | One schema-valid binding per evidence-bound ecology layer. |
| Binding schema | Yes | The JSON Schema used to validate binding files. |
| `layer_id` | Optional | Resolves one layer when supplied; otherwise validates listed active bindings. |

> [!NOTE]
> Field names beyond `layer_id`, `binding_ref`, `spec_hash`, and `candidate_id` are intentionally not treated as confirmed here. Let the schema define the exact machine contract.

[Back to top](#top)

## Exclusions

This registry tooling is deliberately small. It does **not** do the following work:

| Excluded behavior | Where it belongs instead |
|---|---|
| Render MapLibre layers | UI runtime / MapLibre adapter. |
| Fetch or build proof packs | Promotion, proof, or release tooling. |
| Resolve EvidenceBundle payloads | Governed API / evidence resolver. |
| Generate Evidence Drawer payloads | UI contract adapter after evidence resolution. |
| Publish layer artifacts | Promotion gate and release workflow. |
| Validate source datasets | Ingest, processing, and source-specific validators. |
| Decide sensitivity or rights policy | Policy engine and release review. |
| Turn a style expression into policy logic | Backend promotion and governed API state. |

[Back to top](#top)

## Binding flow

```mermaid
flowchart LR
    A[MapLibre layer_id] --> B[registry.json layers[]]
    B --> C[binding_ref]
    C --> D[Binding JSON]
    D --> E[JSON Schema validation]
    E --> F{layer_id + spec_hash match?}
    F -- no --> X[Fail closed]
    F -- yes --> G[candidate_id / evidence ref]
    G --> H[Governed API resolves EvidenceBundle]
    H --> I[Evidence Drawer]

    B -. must not read .-> RAW[(RAW / WORK / QUARANTINE)]
    I -. trust-visible .-> J[policy + review + freshness + provenance]
```

The loader validates registry and binding consistency. The governed API remains responsible for EvidenceBundle resolution and policy-aware explanation.

[Back to top](#top)

## CLI

The commands below are **PROPOSED** examples. Run them only after active-branch verification confirms the module paths.

### Validate active bindings

```bash
python -m tools.registry.ecology_map_layer_registry_cli \
  --registry data/registry/ecology/map_layers/registry.json \
  --schema schemas/ecology/ecology_map_layer_binding.schema.json
```

### Resolve one layer

```bash
python -m tools.registry.ecology_map_layer_registry_cli \
  --registry data/registry/ecology/map_layers/registry.json \
  --schema schemas/ecology/ecology_map_layer_binding.schema.json \
  --layer-id kfm.ecology.vegetation.ndvi_change.v1 \
  --out /tmp/ndvi.binding.json
```

### Exit codes

| Exit | Meaning |
|---:|---|
| `0` | Registry and bindings validated. |
| `1` | Invalid registry, missing layer, invalid binding, malformed JSON, or consistency failure. |
| `2` | Registry file missing. |
| `3` | Schema file missing or invalid. |
| `5` | Unexpected internal error. |

[Back to top](#top)

## Fail-closed rules

Registry resolution should fail when any of these conditions are true:

| Check | Failure condition | Exit |
|---|---|---:|
| Registry shape | Registry document is not a JSON object. | `1` |
| Registry shape | `registry.layers` is missing or not an array. | `1` |
| Lookup | Requested `layer_id` is absent. | `1` |
| Entry completeness | `binding_ref` is missing. | `1` |
| Binding file | Binding file is missing. | `1` |
| Binding shape | Binding JSON fails schema validation. | `1` |
| Identity | Binding `layer_id` differs from registry entry. | `1` |
| Integrity | Binding `spec_hash` differs from registry entry. | `1` |
| Evidence binding | Binding lacks the schema-required evidence/candidate pointer. | `1` |
| 3D burden | Cesium / 3D layer lacks explicit justification. | `1` |

> [!CAUTION]
> 3D or Cesium-backed ecology views should be opt-in and burden-bearing. A 3D layer that does not explain why 2D MapLibre is insufficient should fail validation until the schema and review state support it.

[Back to top](#top)

## Registry output expectations

A successful resolve should produce one binding object that is safe for downstream governed runtime use. The object should be schema-valid and should preserve enough identity and evidence pointers for the governed API to continue the chain.

The CLI should not silently repair bad bindings. Prefer explicit failure over inferred correction.

<details>
<summary>Illustrative registry and binding examples</summary>

These examples are placeholders for reviewer discussion. The schema is the authority once verified.

```json
{
  "layers": [
    {
      "layer_id": "kfm.ecology.vegetation.ndvi_change.v1",
      "status": "active",
      "binding_ref": "./bindings/kfm.ecology.vegetation.ndvi_change.v1.json",
      "spec_hash": "sha256:<NEEDS_VERIFICATION_SPEC_HASH>"
    }
  ]
}
```

```json
{
  "layer_id": "kfm.ecology.vegetation.ndvi_change.v1",
  "spec_hash": "sha256:<NEEDS_VERIFICATION_SPEC_HASH>",
  "candidate_id": "kfm://candidate/<NEEDS_VERIFICATION_ID>",
  "evidence_ref": "kfm://evidence-bundle/<NEEDS_VERIFICATION_ID>",
  "renderer": {
    "surface": "maplibre",
    "source_id": "<NEEDS_VERIFICATION_SOURCE_ID>",
    "layer_id": "kfm.ecology.vegetation.ndvi_change.v1"
  },
  "policy": {
    "evidence_drawer_required": true,
    "public_release_state": "<NEEDS_VERIFICATION>"
  }
}
```

</details>

[Back to top](#top)

## Tests and CI

### Unit test targets

| Test family | Expected assertion |
|---|---|
| Happy path | Valid registry + valid binding exits `0`. |
| Registry shape | Non-object registry and missing `layers[]` fail. |
| Missing file | Missing registry exits `2`; missing schema exits `3`; missing binding exits `1`. |
| Lookup | Unknown `layer_id` fails closed. |
| Schema validation | Malformed binding and schema-invalid binding fail. |
| Identity | Binding `layer_id` mismatch fails. |
| Integrity | `spec_hash` mismatch fails. |
| 3D burden | 3D/Cesium binding without justification fails. |
| Output | `--out` writes only after validation succeeds. |

### Proposed CI check

```bash
python -m tools.registry.ecology_map_layer_registry_cli \
  --registry data/registry/ecology/map_layers/registry.json \
  --schema schemas/ecology/ecology_map_layer_binding.schema.json
```

CI should treat a nonzero exit as a release-blocking validation failure once the registry is promoted from `PROPOSED` to active enforcement.

[Back to top](#top)

## Implementation notes

- Keep style JSON, source descriptors, layer metadata, and evidence bindings separate.
- Do not store policy decisions only in MapLibre paint/layout expressions.
- Do not let browser-side feature-state or filters become the truth source for consequential ecology claims.
- Prefer deterministic IDs and `spec_hash` checks wherever practical.
- Keep public output downstream of released artifacts and governed API resolution.
- Treat `registry.json` as an index, not as a canonical ecology store.

[Back to top](#top)

## Definition of done

- [ ] Registry loader exists.
- [ ] CLI exists.
- [ ] Binding schema exists.
- [ ] Unit tests pass.
- [ ] CLI tests pass.
- [ ] Active registry fixture exists.
- [ ] Invalid registry and invalid binding fixtures exist.
- [ ] MapLibre consumes registry output through a governed adapter.
- [ ] Layer click opens Evidence Drawer through governed API resolution.
- [ ] CI enforces registry validation.
- [ ] README truth posture updated from `PROPOSED` with evidence.

[Back to top](#top)

## Open verification items

| Item | Current label | Needed evidence |
|---|---:|---|
| Target path | NEEDS VERIFICATION | Active repo checkout confirms `tools/registry/` convention. |
| Schema home | NEEDS VERIFICATION | Active repo confirms whether ecology schemas live under `schemas/`, `contracts/`, or another canonical home. |
| Policy label | NEEDS VERIFICATION | Project policy registry confirms `public`, `restricted`, or another label. |
| CLI module path | NEEDS VERIFICATION | Source file exists and imports cleanly. |
| Exit-code contract | PROPOSED | CLI tests confirm behavior. |
| EvidenceBundle resolver boundary | PROPOSED | Governed API contract confirms request/response names. |
| CI enforcement | NEEDS VERIFICATION | Workflow YAML or equivalent release gate confirms validation is blocking. |

[Back to top](#top)
