<!--
================================================================================
KFM Meta Block v2
--------------------------------------------------------------------------------
document_id:        kfm-adr-0007-maplibre-sole-browser-renderer
title:              ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer
class:              architecture decision record (ADR)
adr_id:             ADR-0007
adr_status:         PROPOSED
truth_posture:      cite-or-abstain
governance_layer:   UI/AI plane · Planetary/3D domain (Atlas §18)
proposed_path:      docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md
directory_rule:     directory-rules.md §5 (canonical roots — `docs/adr/`);
                    directory-rules.md §2.4 (ADR required for reversing a
                    previously canonical rule, and for bending a §3 invariant);
                    directory-rules.md §17 (reversing a previously canonical
                    rule requires ADR + supersession notice + drift register
                    entry).
supersedes:         KFM-P2-FEAT-0012 (Pass 23 / Pass 32 idea-index card —
                    prior dual-renderer posture for 3D scene rendering).
                    The card is retained in the register with
                    `superseded_by: ADR-0007` and a forward link.
related_adrs:       ADR-0001 — Schema home (NEEDS VERIFICATION of accepted
                    text against the live ADR set);
                    ADR-0003 — `policy/` singular is canonical (PROPOSED per
                    user-memory; NEEDS VERIFICATION against the live ADR set);
                    Build Manual §30 Recommended ADR Queue informally lists
                    different topics under the ADR-0007 / ADR-0008 slots —
                    see §10 Open Questions, OQ-A7-01.
related_docs:       docs/architecture/maplibre-3d.md  (PROPOSED)
                    docs/architecture/master-maplibre-components-functions-features.md
                    KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas (§18)
                    KFM_Unified_Implementation_Architecture_Build_Manual.md
                    ai-build-operating-contract.md (§7 publication; §28 ADR
                    skeleton; §29 object-family guardrails; §31 security)
                    docs/doctrine/directory-rules.md (v1.2)
spec_hash:          NEEDS VERIFICATION (emit via canonical JCS+SHA-256 at PR
                    acceptance; do not invent before release).
last_reviewed:      <YYYY-MM-DD — set on PR>
owner:              <PLACEHOLDER — UI/AI plane steward; do not invent>
================================================================================
-->

<a id="top"></a>

# ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer

![adr](https://img.shields.io/badge/ADR-0007-blue?style=flat-square)
![status](https://img.shields.io/badge/status-PROPOSED-orange?style=flat-square)
![truth--posture](https://img.shields.io/badge/truth--posture-cite--or--abstain-success?style=flat-square)
![doctrine](https://img.shields.io/badge/doctrine-CONFIRMED-success?style=flat-square)
![implementation](https://img.shields.io/badge/implementation-PROPOSED-orange?style=flat-square)
![repo--depth](https://img.shields.io/badge/repo--depth-UNKNOWN-lightgrey?style=flat-square)
![renderer](https://img.shields.io/badge/renderer-MapLibre%20GL%20JS-blueviolet?style=flat-square)
![trust--membrane](https://img.shields.io/badge/trust%20membrane-single-success?style=flat-square)
![supersedes](https://img.shields.io/badge/supersedes-KFM--P2--FEAT--0012-yellow?style=flat-square)
![rollback](https://img.shields.io/badge/rollback-additive%20via%20exception--ADR-informational?style=flat-square)
<!-- CI badge URL left as a placeholder; no mounted workflow was verified this session.
![ci](https://img.shields.io/github/actions/workflow/status/<OWNER>/<REPO>/<WORKFLOW>.yml?branch=main)
-->

> **One-line decision.** MapLibre GL JS is KFM's **default and sole browser-side renderer.** Every 2D, 2.5D, true-3D, point-cloud, globe, and visualization-overlay surface in KFM lives inside MapLibre's API surface — native capabilities plus an explicitly admitted plugin set governed by a `PluginAdmission` PolicyDecision. Any introduction of a browser-side rendering technology beyond the admitted plugin set requires an accepted **exception-ADR** with attached supply-chain attestation and an explicit, scoped use case.

---

## Mini Table of Contents

- [1. Status](#1)
- [2. Context](#2)
- [3. Decision](#3)
- [4. Evidence basis](#4)
- [5. Directory Rules basis](#5)
- [6. Consequences](#6)
- [7. Alternatives considered](#7)
- [8. Validation](#8)
- [9. Rollback](#9)
- [10. Open questions](#10)
- [11. Migration plan](#11)
- [12. Truth-label summary](#12)

---

<a id="1"></a>

## 1. Status

**PROPOSED.**

Accepts when:

- the numbering conflict with the Build Manual §30 Recommended ADR Queue (OQ-A7-01) is resolved against the **live** `docs/adr/` set;
- `KFM-P2-FEAT-0012` is marked `superseded_by: ADR-0007` in the Idea Index Master, with a forward link to this document;
- a supersession entry is recorded in `docs/registers/DRIFT_REGISTER.md`;
- the `PluginAdmission` contract is named in `contracts/` with a machine schema under `schemas/contracts/v1/...`;
- `docs/architecture/maplibre-3d.md` updates its meta block to reference this ADR by accepted number.

Supersedes (per directory-rules §17): **`KFM-P2-FEAT-0012`** — Pass 23 / Pass 32 idea-index card carrying the prior dual-renderer posture for 3D scene rendering. The card is **retained** with `superseded_by: ADR-0007` and is **not deleted**.

[↑ Back to top](#top)

---

<a id="2"></a>

## 2. Context

### 2.1 The architectural commitment this ADR makes

KFM's UI/AI plane has, in the corpus, more than one architectural sketch for how 3D scenes are rendered in the browser. Doctrine has not previously named a single renderer as the system's commitment. This ADR makes that commitment.

The choice is **MapLibre GL JS** — and only MapLibre GL JS, augmented by a small set of explicitly admitted plugins — as KFM's browser-side rendering surface. The decision rests on three things, in order:

1. **MapLibre 5.x's capability surface is sufficient for every 3D need KFM has identified** at Kansas focus-mode and state-wide working scales. The capability matrix in §2.2 enumerates this.
2. **A single renderer upholds the trust membrane by construction.** One `ViewState` model, one `CameraPath`, one `RepresentationReceipt` stream, one supply chain, one `PluginAdmission` surface, one set of plugin pins, one reviewer burden.
3. **The corpus already classifies 3D rendering as a conditional overlay.** Master MapLibre v2.1 Category W normalizes 3D and globe surfaces as *conditional overlays that must preserve evidence identity and performance limits.* A single renderer is the most direct way to uphold that condition.

### 2.2 MapLibre 5.x capability map

Every 3D capability KFM has identified in the Planetary/3D domain (Atlas §18) is reachable inside MapLibre's API surface — natively where possible, and through a small named plugin set otherwise. *(CONFIRMED at external-tech level against MapLibre's official documentation, plugins page, and the MapLibre 3D Tiles via three.js example dated 2026-03-03 — see `docs/architecture/maplibre-3d.md` §§2.4, 2.8.)*

| KFM 3D requirement | MapLibre 5.x path | Status |
|---|---|---|
| 3D terrain mesh | `raster-dem` source + `Map.setTerrain` | **CONFIRMED native** |
| Hillshade / shaded relief | `hillshade` layer | **CONFIRMED native** |
| Globe projection + sky / atmosphere | `setProjection({type:'globe'})` + `sky` block (MapLibre 5.0+, Jan 2025) | **CONFIRMED native** |
| 2.5D extruded geometry | `fill-extrusion` (evidence-bearing height attributes) | **CONFIRMED native** |
| Camera control / cinematic ViewStates | `setPitch` / `setBearing` / `setVerticalFieldOfView` (`maxPitch ≈ 85°`) | **CONFIRMED native** |
| Custom WebGL hosting | `type: 'custom'` layers (foundation for plugin paths) | **CONFIRMED native** |
| OGC 3D Tiles (b3dm, i3dm, pnts) | `3d-tiles-renderer` via three.js custom layer | **CONFIRMED — MapLibre example dated 2026-03-03** |
| glTF assets | `maplibre-three-plugin` or three.js custom layer | **CONFIRMED plugin ecosystem** |
| LAS / LAZ / COPC point clouds | `maplibre-gl-lidar` (deck.gl-based) | **CONFIRMED plugin** |
| EPT (Entwine) streaming point clouds | `maplibre-gl-lidar` | **CONFIRMED plugin** |
| Massive vector / large-scale aggregation viz | `deck.gl` interleaved (`MapboxOverlay`, WebGL2, MapLibre ≥ 3) | **CONFIRMED integration** |
| COG-as-source | `maplibre-cog-protocol` | **CONFIRMED plugin** |
| PMTiles | `pmtiles` via `addProtocol` | **CONFIRMED plugin** |
| Vector text protocols (CSV/TSV/Topojson/KML/GPX/TCX) | `maplibre-gl-vector-text-protocol` | **CONFIRMED plugin** |
| Contour generation from vector | `maplibre-contourmap` | **CONFIRMED plugin** |
| Babylon.js scenes (alternative to three.js) | MapLibre custom layer | **CONFIRMED advertised** |

What MapLibre **does not** do, and what this ADR does **not** promise:

- **Subsurface volumetric stratigraphy** at production quality. This is **UNKNOWN regardless of approach** — no browser-side renderer covers this today. If it ever becomes in-scope it transits §3.5 (exception path).
- **Planetary-scale terrain quality beyond zoom 18.** Irrelevant at Kansas focus-mode and state-wide scales (Atlas §18 working envelope).
- **Free orbital camera beyond ~85° pitch.** No current KFM use case requires orbital views; if one emerges it transits §3.5.

### 2.3 Why this needs to be an ADR, not an architecture note

Per directory-rules §2.4 / §17, naming a single renderer is an **architecturally canonical commitment** and reversing the prior multi-renderer posture (carried in `KFM-P2-FEAT-0012`) is an §17-class rule reversal. Both require an ADR + supersession notice + drift register entry. This document is that ADR.

[↑ Back to top](#top)

---

<a id="3"></a>

## 3. Decision

### 3.1 Sole renderer

**MapLibre GL JS is KFM's default and sole browser-side renderer.** It hosts:

- 2D vector and raster layers (Master MapLibre v2.1 Categories K, M).
- 2.5D `fill-extrusion` (evidence-bearing height attributes only; `geometry_label: '2.5D'` per Atlas §18 invariant `I-3D-4`).
- 3D terrain (`raster-dem` + `setTerrain`) with hillshade as a context layer.
- Globe projection and sky / atmosphere.
- OGC 3D Tiles via `3d-tiles-renderer` + three.js custom layer.
- glTF assets via `maplibre-three-plugin` or direct three.js custom layer.
- LiDAR point clouds via `maplibre-gl-lidar`.
- Visualization overlays via `deck.gl` interleaved (`MapboxOverlay`).

### 3.2 Admitted plugin set is the boundary of "the renderer"

The phrase *"the renderer"* in this ADR is defined as **MapLibre GL JS + the admitted plugin set.** The admitted plugin set is enumerated in `contracts/3d/plugin-dependencies.md` (PROPOSED) and pinned per-release by `PluginAdmission` PolicyDecisions emitted from `policy/maplibre/plugin-admission.rego` (PROPOSED).

A plugin's appearance in this ADR's §2.2 capability map does **not** constitute admission. Admission is a per-plugin, per-version PolicyDecision, satisfying:

- License clearance (`OQ-A7-02`).
- Version pin in `packages/maplibre-runtime/src/plugin-registry.ts` (PROPOSED).
- Supply-chain attestation (per AI Build Operating Contract §31).
- Schema-checked round-trip of the plugin's contribution to `LayerManifest.plugin_dependencies` (per Atlas §18 invariant `I-3D-7`).

### 3.3 Default-path commitments

The following are **canonical** as of acceptance (PROPOSED locations; **NEEDS VERIFICATION** against a mounted repo):

| Commitment | Surface |
|---|---|
| All default-path map components import MapLibre GL JS and never an alternative browser-side renderer SDK. | `apps/*`, `packages/*` |
| All 3D-capable contracts are defined inside the MapLibre family of contracts. | `contracts/maplibre/`, `contracts/3d/` |
| All 3D-capable schemas live under the MapLibre / 3D family. | `schemas/contracts/v1/maplibre/`, `schemas/contracts/v1/3d/` |
| All 3D-capable policy bundles live under the MapLibre family. | `policy/maplibre/` |
| All `MapReleaseManifest` layers carry `renderer: "maplibre"` by default. | `release/manifests/` |

### 3.4 Default-deny on additional rendering technology

For any browser-side rendering technology **outside the admitted plugin set** — including any second WebGL/WebGPU rendering SDK, any alternative 3D engine, any external scene-streaming runtime, or any plugin not yet listed in `contracts/3d/plugin-dependencies.md`:

- **DENY** at `policy/maplibre/plugin-admission.rego` if the technology appears in a `LayerManifest.plugin_dependencies`, a `SceneManifest`, or a `MapReleaseManifest` without an accepted exception-ADR reference.
- **DENY** at `policy/release/renderer-boundary.rego` for any `MapReleaseManifest` layer whose `renderer` field is not `maplibre` and which does not reference an accepted exception-ADR id.
- **DENY** at lockfile validator (`tools/validators/validate_plugin_admission.py`, PROPOSED) for any package matching an unadmitted renderer-family identifier.
- **DENY** in CI bundle-analyzer guardrail if a default-path bundle includes code paths from an unadmitted renderer family.

These DENY surfaces are the operational meaning of *sole renderer*. They make the commitment in §3.1 testable rather than aspirational.

### 3.5 Exception path

An additional browser-side rendering technology MAY be admitted by a **follow-on accepted ADR** that:

1. Names the specific use case and dataset that requires it.
2. Documents the alternative MapLibre + admitted-plugin paths considered and explains why each fails for that use case.
3. Names the edition / variant of the technology, its license, and its rights posture.
4. Pins versions and attaches supply-chain attestation (DSSE / cosign / Rekor or equivalent).
5. Defines or references a `PluginAdmission` PolicyDecision for that admission.
6. Defines a rollback path that does **not** break the MapLibre-only default-path deployment.
7. Is scoped to the named use case and does **not** promote the additional technology to default-path status.

An admitted exception **does not modify this ADR.** It is a scoped, named amendment recorded in the register and forward-linked from this document.

[↑ Back to top](#top)

---

<a id="4"></a>

## 4. Evidence basis

> *Priority order: corpus doctrine + workspace evidence first, then authoritative external research where versions or capabilities are version-sensitive.*

### 4.1 Doctrine evidence (CONFIRMED)

- **`KFM-P2-FEAT-0012`** — Pass 23 / Pass 32 idea-index card recording the prior dual-renderer posture for 3D scene rendering. The card itself carries `NEEDS VERIFICATION` on an unresolved edition-selection question and a `tension` entry on sustainable scene-authoring workflow. This ADR's supersession of the card resolves both by removing the dual-renderer posture from the default path. *(CONFIRMED in `Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md`, §8.6.30.)*

- **Master MapLibre v2.1, Category W** — entries `ML-W-072` through `ML-W-075` normalize 3D and globe surfaces as **conditional overlays that must preserve evidence identity and performance limits.** A single renderer is the most direct construction-level guarantee of evidence identity across all overlays. *(CONFIRMED in `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`.)*

- **Master MapLibre v2.1, Category W — `ML-W-006` through `ML-W-010`** — entries about shared artifacts, point clouds, terrain layers, and overlay synchronization are each marked as cumulative expansions requiring revalidation against mounted-repo tests, manifests, release receipts, and source-ledger checks. A single renderer reduces the number of such revalidation surfaces to one. *(CONFIRMED.)*

- **AI Build Operating Contract** — §§7 (publication, rights, sensitivity), 29 (object-family guardrails), 31 (security and exposure rules). Each of these is easier to satisfy with a single renderer's single supply chain than with two parallel chains. *(CONFIRMED in `ai-build-operating-contract.md`.)*

- **Directory Rules v1.2** — §§2.4(2)/(5)/(6), §13.5, §17. The "two parallel schema / contract / policy / source / registry / release / proof homes" anti-pattern (§13.5) directly applies to dual-renderer architectures, which would require parallel contracts, schemas, policies, and release surfaces. This ADR closes that latent parallel-home risk. *(CONFIRMED in `directory-rules.md`.)*

- **`docs/architecture/maplibre-3d.md` (PROPOSED)** — the companion architecture document. This ADR is the canonical decision that the architecture document's recommendation depends on; the architecture document is the implementation reference. *(CONFIRMED at doctrine rank; implementation PROPOSED.)*

### 4.2 External-tech evidence (CONFIRMED)

> *KFM's authoritative-research clause (operating-contract §1.3) permits and expects external research for version-sensitive capabilities. The following are CONFIRMED against MapLibre's own published documentation and examples, not asserted from memory.*

- **MapLibre GL JS 5.0** released January 2025 — native globe projection (`Map.setProjection({type:'globe'})`) and `GlobeControl`. *(CONFIRMED — MapLibre release notes and docs.)*
- **MapLibre Style Spec** — `terrain`, `hillshade`, `sky`, `light`, `fill-extrusion`, `projection` are first-class in the published style spec. *(CONFIRMED.)*
- **MapLibre 3D Terrain example** — uses two `raster-dem` sources (one for `terrain`, one for `hillshade`) for render quality. *(CONFIRMED — `maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/`.)*
- **MapLibre 3D Tiles via three.js example**, dated **2026-03-03** — `three@^0.183.0`, `3d-tiles-renderer@^0.4.21`, `GLTFLoader`, `DRACOLoader`. *(CONFIRMED — `maplibre.org/maplibre-gl-js/docs/examples/add-3d-tiles-using-threejs/`.)*
- **MapLibre Plugins page** lists `maplibre-three-plugin`, `maplibre-gl-lidar`, `pmtiles`, `maplibre-cog-protocol`, `maplibre-gl-vector-text-protocol`, `maplibre-contourmap`. *(CONFIRMED — MapLibre plugins page.)*
- **deck.gl `MapboxOverlay` interleaved mode** with WebGL2 supports MapLibre ≥ 3. *(CONFIRMED — deck.gl docs.)*

### 4.3 What this ADR does **not** rely on

- It does **not** rely on any performance benchmark beyond Kansas focus-mode and state-wide working envelopes. Performance is monitored via `RenderReceipt` budgets, not by this ADR.
- It does **not** rely on any specific plugin version. Each plugin pin is the job of a per-release `PluginAdmission` PolicyDecision, not this ADR.
- It does **not** rely on the maturity of any single plugin to be permanent. If a plugin regresses, it leaves the admitted set via the `PluginAdmission` flow; the renderer commitment remains.

[↑ Back to top](#top)

---

<a id="5"></a>

## 5. Directory Rules basis

### 5.1 Why an ADR is required at all

- **§2.4(6) — Bending an invariant from §3.** Naming a single renderer reinforces the *single trust membrane* invariant. The reversal of `KFM-P2-FEAT-0012`'s prior posture is itself an §17-class rule reversal.
- **§17 — "Reversing a previously canonical rule"** — requires ADR + supersession notice + drift register entry. All three are produced by this ADR.

### 5.2 Why this ADR lives at `docs/adr/`

- **§5 canonical roots** — `docs/adr/` is the canonical home for accepted and superseded ADRs.
- The filename pattern `ADR-NNNN-<kebab-case-decision>.md` matches the precedents of `ADR-0001-schema-home.md` and `ADR-0003-policy-singular-is-canonical.md`. *(PROPOSED — mounted ADR set NEEDS VERIFICATION.)*

### 5.3 Why `docs/architecture/maplibre-3d.md` is the companion document, not this ADR

- **§6 docs lane — `docs/architecture/<topic>.md`** is the canonical home for cross-domain architecture doctrine.
- **§12 Domain Placement Law** — 3D is a cross-cutting carrier, not a domain root. The architecture document belongs at `docs/architecture/`; this decision document belongs at `docs/adr/`.

### 5.4 Compatibility-root posture

This ADR does **not** create new compatibility roots, **does not** promote any compatibility root to canonical, **does not** change the schema-home rule, and **does not** add a lifecycle phase. It satisfies the §2.4 "no parallel home" anti-pattern by **closing** a latent parallel-renderer family rather than opening one.

[↑ Back to top](#top)

---

<a id="6"></a>

## 6. Consequences

### 6.1 Positive

- **One trust membrane.** One renderer to govern; one set of receipts to emit; one `ViewState` and `CameraPath` model; no cross-renderer drift to specify, monitor, or test.
- **Evidence identity by construction.** The same tiles drive 2D, 2.5D, globe, 3D Tiles, glTF, and point-cloud views. Master MapLibre v2.1 Category W's *evidence identity* requirement is structurally upheld.
- **Single supply chain.** AI Build Operating Contract §31 attestation discipline applies to one chain, not two; SBOM, signing, and lockfile checks are simpler and more comprehensive.
- **Smaller bundle, simpler stack.** No dual-renderer infrastructure, no cross-renderer camera sync, no shared-layer-manifest translation overhead, no reviewer burden duplication.
- **Easier to test and to govern.** One `PluginAdmission` surface, one `RepresentationReceipt` schema, one lockfile guardrail, one bundle-analyzer rule.
- **Reversible by exception.** The §3.5 exception path means this commitment is firm but not absolute — KFM keeps the ability to admit additional rendering technology under a scoped, attested ADR if a use case ever truly requires it.

### 6.2 Negative / accepted risks

- **Maturity dependency on the admitted plugin set.** Some plugins in §2.2 are younger than the corresponding capabilities in mature alternative engines. KFM accepts this risk at Kansas-scale working envelopes; the risk is re-evaluated per use case via §3.5.
- **`maxPitch ≈ 85°`.** Sufficient for all current KFM use cases; orbital cases transit §3.5.
- **Plugin-version drift becomes a real governance surface.** Mitigated by `PluginAdmission` per-release and CI lockfile checks. *(PROPOSED implementation.)*
- **An exception-ADR carries non-trivial cost.** This is a feature of the governance, not a bug — the cost of admitting an additional rendering technology is the same as the cost of upholding the trust membrane against it.

### 6.3 Carried-forward, **unchanged** by this ADR

- The **2.5D vs. true-3D label discipline** (`KFM-P9-FEAT-0011`, `KFM-P9-FEAT-0013`) remains in effect.
- The Atlas §18 object families — **Scene Manifest, Layer Manifest, Style Manifest, Terrain Model, View State, Camera Path, Representation Receipt, 3D Admission Decision, Reality Boundary Note** — remain in effect.
- The **CARE-grade generalization** rule for archaeology terrain-linked layers (`≥5 km`; `ML-059-055`) remains in effect.
- The **cite-or-abstain** posture and **EvidenceBundle** discipline are untouched.
- The **deny-by-default release gate** is untouched.
- The 3D invariants `I-3D-1` through `I-3D-7` (governed tile-host endpoints; evidence parity; no cross-renderer drift; 2.5D ≠ true-3D; CARE / sensitivity generalization; living-person / DNA exclusion; pinned plugin admission) are upheld by construction.

[↑ Back to top](#top)

---

<a id="7"></a>

## 7. Alternatives considered

### 7.1 Multi-renderer architecture (the prior posture)

**Rejected.** A multi-renderer architecture requires parallel contracts, schemas, policy bundles, release surfaces, and supply chains — exactly the "two parallel homes" anti-pattern that directory-rules §13.5 names. It doubles the reviewer burden and creates a standing cross-renderer drift risk that the corpus's evidence-identity requirement (`ML-W-072`–`ML-W-075`) cannot tolerate without significant additional discipline that no architecture document has yet specified. The prior posture in `KFM-P2-FEAT-0012` also carried unresolved governance items (edition selection, sustainable authoring workflow) that this ADR does not attempt to resolve in-place; it resolves them by removing the multi-renderer posture from the default path.

### 7.2 Use `deck.gl` as the primary renderer; treat MapLibre as a basemap host

**Rejected.** `deck.gl` on its own does not provide the vector style spec, native terrain mesh, hillshade layer, globe projection, sky / atmosphere, or `fill-extrusion` API that KFM's 2D and 2.5D surfaces depend on (Master MapLibre v2.1 Categories K, M, Q). `deck.gl` **is** admitted as an interleaved overlay (`MapboxOverlay`, `interleaved: true`) per `docs/architecture/maplibre-3d.md` — that integration is consistent with this ADR. The rejected option is making `deck.gl` *primary*, not making it *admitted*.

### 7.3 Adopt a hand-rolled three.js scene as the primary renderer

**Rejected.** A hand-rolled three.js scene would lose the MapLibre style spec, the governed source families (`pmtiles`, `cog-protocol`, vector text protocols), the globe projection, the terrain-and-hillshade pair, and the existing `RepresentationReceipt` plumbing. three.js **is** admitted as the host for OGC 3D Tiles and glTF rendering inside MapLibre custom layers, which is consistent with this ADR. The rejected option is making three.js *primary*, not making it *admitted*.

### 7.4 Adopt MapLibre as default but leave the renderer commitment unstated

**Rejected.** Silence is not reversal. Per directory-rules §17, a previously canonical rule must be **explicitly** reversed; per §2.5, drift between doctrine and repo must be raised as a drift-register entry and resolved by ADR. An unstated commitment would leave the corpus in contradiction with the architecture and would leave the §13.5 anti-pattern latent rather than closed.

### 7.5 Defer the decision until a mounted repo is inspected

**Rejected as the default.** The decision is doctrine-level; it does not depend on mounted-repo evidence to be **correct**. It depends on mounted-repo evidence to be **operational** (file paths, validator names, CI workflows). The two concerns are separated in this ADR — the decision sits in §3, the operational paths sit in §3.3 and §8 as PROPOSED — so acceptance of the decision is not blocked on a mounted-repo inspection. The mounted-repo inspection drives §11 migration scope, not the §3 decision.

[↑ Back to top](#top)

---

<a id="8"></a>

## 8. Validation

> *Per directory-rules §2.4 and operating-contract §28, every ADR carries a validation surface. Each item below is **PROPOSED** until backed by a mounted test, fixture, or CI run.*

### 8.1 Contract / schema tests

- `schemas/contracts/v1/policy/plugin_admission.schema.json` validates a `PluginAdmission` instance with `renderer: "maplibre"` (default) and accepts an `additional_renderer` field only when paired with an `exception_adr_id` referencing an accepted ADR. **PROPOSED.**
- `schemas/contracts/v1/maplibre/scene_manifest.schema.json` defines a single-renderer `SceneManifest` with no cross-renderer bridge fields. **PROPOSED.**
- `schemas/contracts/v1/release/map_release_manifest.schema.json` validates `MapReleaseManifest.layers[*].renderer == "maplibre"` by default and accepts other values only when paired with an `exception_adr_id`. **PROPOSED.**
- `schemas/contracts/v1/maplibre/layer_manifest.schema.json` validates `plugin_dependencies[*]` against the admitted plugin set. **PROPOSED.**

### 8.2 Policy tests (Rego or chosen DSL)

- `policy/maplibre/plugin-admission.rego` — DENIES `LayerManifest` whose `plugin_dependencies` include any identifier not in the admitted set and without an accepted `exception_adr_id`. **PROPOSED.**
- `policy/release/renderer-boundary.rego` — DENIES `MapReleaseManifest` whose layers carry a `renderer` value outside the admitted set without an accepted `exception_adr_id`. **PROPOSED.**
- CARE / sensitivity / archaeology / living-person / DNA policies remain in effect across all layers; admission via the §3.5 exception path does **not** relax sensitivity gates. **PROPOSED.**

### 8.3 Validator tests

- `tools/validators/validate_plugin_admission.py` — fails closed on missing or unknown `exception_adr_id` for any non-admitted renderer family. **PROPOSED.**
- `tools/validators/validate_scene_manifest.py` — fails closed on any cross-renderer bridge field appearing in a `SceneManifest`. **PROPOSED.**
- `tools/validators/validate_layer_manifest.py` — fails closed on unadmitted `plugin_dependencies` entries. **PROPOSED.**

### 8.4 Build / CI tests

- Lockfile (`package-lock.json` or equivalent) check fails closed if a package matching an unadmitted renderer-family identifier appears without an accepted `exception_adr_id`. **PROPOSED.**
- Bundle-analyzer guardrail flags any default-path bundle that includes code paths from an unadmitted renderer family. **PROPOSED.**
- 3D smoke test: `setTerrain` succeeds, `terrain` event fires, `RenderReceipt` emitted within budget. **PROPOSED.**
- 2D fallback test: terrain-admission failure → 2D render with visible reason. **PROPOSED.**
- Globe toggle test: `setProjection({type:'globe'})` succeeds at MapLibre 5.0+. **PROPOSED.**
- 3D Tiles via three.js smoke test: tileset loads, first tile renders within budget, `RenderReceipt` records `3d-tiles-renderer` version. **PROPOSED.**
- LiDAR EPT smoke test: point cloud streams, point budget respected, classification filter passes. **PROPOSED.**

### 8.5 Documentation tests

- `docs/architecture/maplibre-3d.md` meta block references `ADR-0007` after acceptance (no `<NNNN>` placeholder remains). **PROPOSED.**
- `docs/registers/DRIFT_REGISTER.md` carries an entry recording the supersession of `KFM-P2-FEAT-0012`. **PROPOSED.**
- The `KFM-P2-FEAT-0012` card in the Idea Index Master gains `superseded_by: ADR-0007` and a forward link. **PROPOSED.**
- Master MapLibre v2.1 Category W entries that referenced cross-renderer assumptions are refreshed to reference this ADR. **PROPOSED.**

[↑ Back to top](#top)

---

<a id="9"></a>

## 9. Rollback

> *Per operating-contract §1.5 and §28, every ADR names a rollback path. KFM's preference is **reversible, additive** rollback whenever possible.*

### 9.1 Rollback is additive

If a future KFM use case demonstrates a genuine need for a browser-side rendering technology outside the admitted plugin set, this ADR is rolled back **by amendment**, not by deletion:

1. Author a follow-on **exception-ADR** that satisfies the seven §3.5 conditions.
2. Mark this ADR (`ADR-0007`) as **amended** (not superseded) with a forward link to the new ADR. The default-off, gated posture for everything outside the named exception remains in effect.
3. Add an amendment entry to `docs/registers/DRIFT_REGISTER.md`.

### 9.2 Full reversal

A full reversal — restoring a multi-renderer default-path posture — requires a superseding ADR (`status: accepted`, with this ADR's `status: superseded` and a forward link) and would itself be an §17-class rule reversal. This path is documented for completeness; it is not anticipated.

### 9.3 What rollback never restores

- An exception-ADR **must** resolve the governance items that this ADR's supersession of `KFM-P2-FEAT-0012` left behind (edition selection, licensing posture, sustainable authoring workflow, sustainable supply-chain attestation). Rollback does **not** restore the prior posture *with those open items still open.*

[↑ Back to top](#top)

---

<a id="10"></a>

## 10. Open questions

### OQ-A7-01 — Numbering conflict (NEEDS VERIFICATION)

The Build Manual §30 Recommended ADR Queue informally lists different topics under the ADR-0007 and ADR-0008 slots than this ADR uses. The user-supplied path for this decision is `docs/adr/ADR-0007-maplibre-is-the-sole-browser-renderer.md`.

**Treatment in this draft:** the user-supplied number is honored. The Build Manual queue is itself a recommendation table (PROPOSED), not an accepted ADR set. The numbering conflict is recorded here for resolution against the **live** `docs/adr/` directory at PR time.

**Resolution paths (any of):**

- **(a)** Accept this ADR as `0007` and renumber the Build Manual queue's reservations.
- **(b)** Renumber this ADR to the lowest free slot in the live `docs/adr/` set (e.g., `0008` if `0007` is already taken in the accepted set).
- **(c)** Renumber the Build Manual queue's reservations to align with this ADR.

**Status:** NEEDS VERIFICATION against the mounted `docs/adr/` directory.

### OQ-A7-02 — Admitted plugin licensing inventory (PROPOSED)

Several MapLibre plugins listed in §2.2 carry licenses marked `NEEDS VERIFICATION` in `docs/architecture/maplibre-3d.md` Appendix A. This ADR does not block on those entries — they are governed at `PluginAdmission` time — but the licensing inventory should be completed before the first release that depends on any of them. Plugins in scope: `3d-tiles-renderer`, `maplibre-three-plugin`, `maplibre-gl-lidar`, `maplibre-cog-protocol`, `maplibre-gl-vector-text-protocol`, `maplibre-contourmap`.

### OQ-A7-03 — `PluginAdmission` schema home (PROPOSED)

`schemas/contracts/v1/policy/plugin_admission.schema.json` is the PROPOSED home. If `ADR-S-03` (Receipt schema layout) is decided in favor of per-domain schema homes, the path may move to `schemas/contracts/v1/maplibre/plugin_admission.schema.json`. **Resolution required by** `ADR-S-03` or a follow-on ADR.

### OQ-A7-04 — Pre-existing artifacts from the prior posture (NEEDS VERIFICATION)

If the mounted repo already contains artifacts authored under the prior dual-renderer posture (`KFM-P2-FEAT-0012`), they must be enumerated, evaluated, and either removed in the migration PR (§11) or admitted under an exception-ADR. **NEEDS VERIFICATION** against the live repo. Default treatment in the migration PR is removal with a drift-register entry; admission would require the §3.5 exception path.

### OQ-A7-05 — Subsurface stratigraphy (UNKNOWN — independent of this ADR)

Subsurface volumetric stratigraphy remains **UNKNOWN** for browser rendering at production quality. This ADR does not promise to solve that case; if it ever becomes in-scope it is handled under §3.5 exception path with a `geometry_label` outside the current 2D / 2.5D / 3D set.

### OQ-A7-06 — Effect on Master MapLibre v2.1 Category W (PROPOSED)

Category W entries `ML-W-006` through `ML-W-010` and `ML-W-072` through `ML-W-075` carry assumptions about multi-renderer artifacts and overlay synchronization. Once this ADR is accepted, Category W should be refreshed to align with the single-renderer commitment and mark the affected rows `superseded_by: ADR-0007`. This is a Master MapLibre v2.x edition concern, not a blocker on acceptance of this ADR.

### OQ-A7-07 — `RepresentationReceipt` schema completeness (PROPOSED)

`schemas/contracts/v1/maplibre/representation_receipt.schema.json` should carry `renderer`, `renderer_version`, `plugin_versions[]`, `view_state_id`, `camera_path_id`, and `spec_hashes[]` at minimum. A complete shape is the job of `ADR-S-03` and follow-on contract work, not this ADR.

[↑ Back to top](#top)

---

<a id="11"></a>

## 11. Migration plan

> *PROPOSED migration steps. Each step lands as a separate PR or a clearly-scoped section of a single PR; none of these steps modifies trust-bearing receipts after the fact.*

| # | Step | Affected path (PROPOSED) | Type |
|---|---|---|---|
| 1 | Mark `KFM-P2-FEAT-0012` `superseded_by: ADR-0007` with a forward link. | Idea Index Master (location NEEDS VERIFICATION) | doctrine update |
| 2 | Add drift register entry recording the supersession. | `docs/registers/DRIFT_REGISTER.md` | governance ledger |
| 3 | Update `docs/architecture/maplibre-3d.md` meta block to reference `ADR-0007`; remove the `<NNNN>` placeholder; align §0.1 framing with this ADR. | `docs/architecture/maplibre-3d.md` | doctrine update |
| 4 | Refresh Master MapLibre v2.1 Category W to align with single-renderer commitment. | `docs/architecture/master-maplibre-components-functions-features.md` (PROPOSED path) | doctrine update |
| 5 | Author the `PluginAdmission` contract and machine schema. | `contracts/3d/plugin-dependencies.md`, `schemas/contracts/v1/policy/plugin_admission.schema.json` | contract + schema |
| 6 | Author `policy/maplibre/plugin-admission.rego` and `policy/release/renderer-boundary.rego`. | `policy/maplibre/`, `policy/release/` | policy |
| 7 | Author `tools/validators/validate_plugin_admission.py`, `validate_scene_manifest.py`, `validate_layer_manifest.py`. | `tools/validators/` | validator |
| 8 | Author or extend `packages/maplibre-runtime/` with `terrain.ts`, `hillshade.ts`, `sky.ts`, `globe.ts`, `fill-extrusion.ts`, `camera-path.ts`, `custom-layer-host.ts`, `tiles3d-three.ts`, `gltf-three.ts`, `lidar-decklike.ts`, `deckgl-interleaved.ts`, `admission.ts`, `plugin-registry.ts`, `receipts.ts`. | `packages/maplibre-runtime/src/` | runtime |
| 9 | Add CI lockfile guardrail (deny unadmitted renderer-family identifiers without exception-ADR). | `.github/workflows/` (PROPOSED) | CI |
| 10 | Add CI bundle-analyzer guardrail. | `.github/workflows/` (PROPOSED) | CI |
| 11 | Enumerate and act on any pre-existing artifacts from the prior posture (per OQ-A7-04). | repo-wide | cleanup |
| 12 | Confirm no default-path package, contract, schema, policy, or release manifest references an unadmitted renderer family. | repo-wide | conformance check |

Every step preserves reversibility per operating-contract §1.5.

[↑ Back to top](#top)

---

<a id="12"></a>

## 12. Truth-label summary

- **CONFIRMED at doctrine level.** The single-renderer commitment is supported by Master MapLibre v2.1 Category W's evidence-identity normalization (`ML-W-072`–`ML-W-075`), by directory-rules §13.5's "two parallel homes" anti-pattern, and by AI Build Operating Contract §§7, 29, 31. The supersession of `KFM-P2-FEAT-0012` is supported by the card's own unresolved governance items.
- **CONFIRMED at external-tech level.** MapLibre GL JS 5.0 native globe (January 2025), MapLibre 3D Tiles via three.js example (2026-03-03), MapLibre plugins page entries, and deck.gl `MapboxOverlay` interleaved mode are each verified against MapLibre's own published documentation and examples.
- **PROPOSED at implementation level.** Every file path, schema URI, package name, validator name, CI workflow name, plugin pin, owner, `spec_hash`, and `last_reviewed` date in this ADR is **PROPOSED** or a **PLACEHOLDER** until verified against a mounted repository.
- **NEEDS VERIFICATION.** The ADR-0007 numbering conflict with the Build Manual Recommended ADR Queue (OQ-A7-01); any pre-existing artifacts from the prior posture in the live repo (OQ-A7-04); the live `docs/adr/` set and acceptance status of `ADR-0001` and `ADR-0003`; the location of the Idea Index Master for `superseded_by` updates.
- **UNKNOWN.** Subsurface volumetric stratigraphy for browser rendering at production quality (OQ-A7-05) — independent of this ADR's renderer commitment.

This ADR is a **doctrine-level** instrument. It does **not** imply that the contracts, schemas, policies, validators, CI workflows, or apps it names exist in the mounted repo; it specifies what **must** exist for the decision to be operational, and what **must not** exist (default-path artifacts from unadmitted renderer families) for the decision to remain in effect.

[↑ Back to top](#top)

---

<sub>**Document control.** ADR id `ADR-0007` is treated as binding per the user-supplied path; numbering conflict with the Build Manual §30 Recommended ADR Queue is recorded in OQ-A7-01 and to be reconciled against the live `docs/adr/` set at PR time. `spec_hash` is `NEEDS VERIFICATION` — emit via canonical JCS+SHA-256 of the frontmatter + body once the hashing tool is wired. Owner is a `<PLACEHOLDER>` per operating-contract §28; do not invent. Acceptance moves this document from `PROPOSED` to `accepted` and emits a forward link from `KFM-P2-FEAT-0012`.</sub>

[↑ Back to top](#top)
