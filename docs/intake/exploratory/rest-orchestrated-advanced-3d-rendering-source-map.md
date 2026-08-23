# REST-Orchestrated Advanced 3D Rendering and LLM-Ingestible PDF Carriers

> **Status:** DRAFT research reconciliation; non-authoritative; source-verified; no runtime, schema, policy, release, deployment, or publication effect  
> **Truth posture:** cite-or-abstain; source material is an idea source, not KFM authority  
> **Repository:** `bartytime4life/Kansas-Frontier-Matrix`  
> **Inspection baseline:** `main@d760932e3be8f2cfedd7ece7e9a6f53aa0f18226`  
> **Prepared:** 2026-08-23  
> **Owning lane:** `docs/intake/exploratory/` because this file reconciles an external research source against current repository evidence; it does not define semantic, schema, policy, API, renderer, or release authority

## 1. Purpose and bounded outcome

This source map reconciles the Google Drive PDF **“Designing an LLM-Ingestible PDF Resource on REST-Orchestrated Advanced 3D Rendering”** against the current KFM repository and current primary technical standards. It expands the useful ideas into a buildable control-plane model, identifies what the repository already supports, records drift and missing evidence, and defines small follow-on slices without pretending that proposed routes, contracts, or implementations already exist.

The source PDF is identified by:

- file name: `Designing an LLM-Ingestible PDF Resource on REST-Orchestrated Advanced 3D Rendering.pdf`;
- Google Drive file ID: `1jmkDEI3BK-WESlc29HLZ727da1Rk-qPg`;
- byte length: `116254`;
- SHA-256: `d5cd2e88854f3291dbeae5e609a423cce5bbf40e36172efdd2921127e2d8399d`;
- pages: `23`;
- PDF profile observed: PDF 1.7, untagged, no XMP metadata stream, no JavaScript, no embedded files, and not linearized;
- role: read-only idea source;
- authority: none;
- exact page-level content map: **CONFIRMED** in section 2.1 from direct inspection of the identified source bytes.

This document deliberately stops at research reconciliation. It does **not**:

- add a renderer dependency;
- implement `MapLibreAdapter` or any other concrete renderer adapter;
- establish a REST route or OpenAPI operation;
- admit a 3D source, asset, scene, or external service;
- create a machine contract or schema;
- promote a candidate object;
- release, deploy, or publish a scene or rendered artifact;
- make an LLM-generated summary authoritative.

## 2. Evidence method

The reconciliation used four evidence classes, in descending order of authority for repository claims:

1. current repository files and merged change evidence;
2. existing KFM contracts, receipts, architecture notes, and publication guardrails;
3. the supplied PDF as a proposal and research prompt;
4. current primary standards and official project documentation for HTTP, API description, geospatial 3D carriers, provenance, accessibility, and renderer behavior.

A statement is labeled:

- **CONFIRMED** when verified from the inspected repository or source-artifact evidence;
- **PROPOSED** when it is a design candidate not yet admitted into implementation;
- **UNKNOWN** when the inspected evidence does not resolve it;
- **NEEDS VERIFICATION** when a bounded check can resolve it but has not yet been completed strongly enough to act as fact.

Memory and architectural plausibility are not evidence.

### 2.1 Verified page-level source map

The following page map was checked against the 23-page PDF identified above. It records material content locations; it does not promote the source into KFM doctrine.

| PDF pages | Material content |
|---|---|
| 1 | Metadata example, executive summary, and definitions of REST rendering |
| 2 | Goals, audiences, scope, success criteria, and architecture-pattern introduction |
| 3 | Client-side, server-side, and hybrid patterns |
| 4 | Baseline architecture diagram; HTTP semantics, byte ranges, and caching |
| 5–8 | Resource model, OpenAPI examples, asset/artifact/render-job vocabulary, and finite compute states |
| 8–10 | Client polling, caching, and format guidance |
| 11–12 | Format comparison, LOD, compression, streaming, and progressive loading |
| 13 | Conversion pipeline, engines, trade-offs, and validation |
| 14 | Performance, observability, and deployment dimensions |
| 15 | Cost guidance and PDF 3D capability/security discussion |
| 16–18 | PDF compatibility/accessibility, JSON-LD, XMP, and metadata design |
| 18–19 | Corpus/build layout and export workflow |
| 20 | Checklists, validation, pitfalls, and security risks |
| 21–23 | Legal/licensing and references |

The source is text-extractable and useful as research input. It is not a conformance exemplar for the packaging profile it proposes because the inspected bytes are untagged and contain no XMP stream, associated machine files, embedded 3D assets, or interactive 3D annotation.

## 3. Repository reconciliation

### 3.1 Current bounded state

| Concern | Status | Repository evidence | Consequence |
|---|---|---|---|
| Renderer-neutral runtime seam | **CONFIRMED** | `packages/maplibre/src/map-runtime-port.ts`, `packages/maplibre/src/null-map-runtime.ts`, and exports from `packages/maplibre/src/index.ts` were added by merged PR #3433 | KFM has a dependency-free boundary for serializable map camera, selection, runtime state, and validation. This is not a concrete renderer. |
| Concrete MapLibre implementation | **CONFIRMED ABSENT from the merged slice** | PR #3433 explicitly bounded out a `MapLibreAdapter`, `maplibre-gl` dependency admission, browser runtime probes, lockfile changes, and viewer integration | No claim may be made that the browser renderer path is implemented or admitted. |
| Renderer architecture decisions | **CONFIRMED ACCEPTED / implementation held** | ADR-0006 accepts the package-owned port/adapter seam; ADR-0007 accepts the renderer family while separating exact dependency and runtime admission | Architecture acceptance does not add a version, package, plugin, worker, adapter, browser proof, release, deployment, or publication authority. |
| 3D admission vocabulary | **CONFIRMED, PROPOSED-INACTIVE** | `contracts/map/three_d_admission_decision.md` | `ALLOW_RENDER_CANDIDATE` is not publication or policy authority. Fixture use does not admit real 3D data. |
| Representation process memory | **CONFIRMED** | `contracts/receipts/representation_receipt.md` | A representation receipt may record how a view or artifact was made; it does not make the output true or released. |
| Scene contract lane | **CONFIRMED as a guardrail, not an active schema family** | `schemas/contracts/v1/scene/README.md` | A README reserve does not establish machine-valid scene semantics. |
| Published scene lane | **CONFIRMED empty/guarded at the inspected architecture baseline** | `data/published/layers/scene/README.md` and `docs/architecture/planetary-3d.md` | No released 3D scene may be inferred from directory presence. |
| Planetary 3D architecture narrative | **CONFIRMED stale on the pinned base / corrected in the #3436 candidate** | The base document predates PR #3433 and ADR-0006/0007 acceptance; the same-path candidate updates only those current-state facts | The parent remains the carrier-architecture authority. This source map records lineage and does not compete with it. |
| Promoted REST/3D architecture companion | **CONFIRMED merged** | PR #3434 added `docs/architecture/rest-orchestrated-3d-derivatives.md` as a subordinate companion | Detailed orchestration/PDF guidance belongs in the companion, not in this source-lineage file or a fourth explanatory surface. |
| REST render-orchestration contract | **NEEDS VERIFICATION** | No dedicated contract was established by the bounded evidence set inspected for this reconciliation | Route names and state objects below remain examples and proposals. A repo-wide contract inventory is required before selecting a home. |
| LLM-ingestible PDF build profile | **NEEDS VERIFICATION** | No accepted KFM profile was established by the bounded evidence set inspected for this reconciliation | The profile in section 7 is a candidate quality and safety checklist, not a publication standard. |

### 3.2 Authority and lineage relationship

The merged and candidate documents now have distinct responsibilities:

1. `docs/intake/exploratory/rest-orchestrated-advanced-3d-rendering-source-map.md` — noncanonical source lineage and verification record, introduced by PR #3435;
2. `docs/architecture/planetary-3d.md` — parent carrier architecture and current implementation boundary;
3. `docs/architecture/rest-orchestrated-3d-derivatives.md` — narrow promoted companion for REST orchestration, derivatives, and PDF packaging, introduced by PR #3434.

No one of these files creates a semantic contract, machine schema, policy decision, renderer dependency, release, deployment, or publication state.

### 3.3 Drift finding and bounded correction

`docs/architecture/planetary-3d.md` correctly preserves the separation between evidence, policy, representation, and publication, but its base snapshot predates merged PR #3433 and the accepted ADR-0006/0007 transitions. The #3436 candidate applies the smallest truthful correction:

1. `MapRuntimePort` and `NullMapRuntime` are recorded as renderer-neutral package exports.
2. The seam remains dependency-free and serializable.
3. ADR-0006 and ADR-0007 are recorded as accepted architecture decisions.
4. No concrete `MapLibreAdapter`, admitted `maplibre-gl` dependency, browser proof, viewer route, REST render coordinator, or released scene follows from those facts.
5. All existing 3D admission, sensitivity, receipt, and release restrictions remain in force.

The correction is same-path and does not add another architecture authority file.

## 4. Research synthesis: the control plane is not the renderer

The useful core of REST-orchestrated advanced 3D rendering is a strict separation of responsibilities:

- **evidence plane:** source identity, rights, sensitivity, lineage, spatial and temporal extent, and validation;
- **decision plane:** policy and admission outcomes;
- **orchestration plane:** immutable requests, validated plans, job state, retries, cancellation, and receipts;
- **render plane:** renderer-specific execution behind an admitted adapter;
- **delivery plane:** controlled access to artifacts and representations;
- **publication plane:** review, release, correction, withdrawal, and rollback.

A renderer can produce pixels while every higher-order claim remains false. Render success is therefore not evidence success, policy approval, source admission, release, or publication.

### 4.1 Candidate semantic objects

The following object model is **PROPOSED**. Names are descriptive and do not reserve contract paths.

| Candidate object | Responsibility | Must not imply |
|---|---|---|
| `RenderIntent` | Records the bounded user or system request: viewport, time, representation type, output purpose, and requested quality | That inputs are admissible or that rendering will occur |
| `RenderPlan` | Resolves an admitted intent to immutable candidate inputs, renderer capability requirements, transformations, and budgets | That a renderer dependency or source is approved |
| `RenderJob` | Records asynchronous execution state, attempt history, idempotency, timeouts, cancellation, and terminal outcome | That a successful job is releasable |
| `RenderArtifact` | Identifies bytes or a stream by media type, content digest, dimensions, extent, and generation lineage | That the artifact is canonical truth |
| `RepresentationReceipt` | Records source versions, transformations, renderer build, parameters, and limitations | That representation choices have policy authority |
| `ReleaseDecision` | Records human/policy authorization for a specific artifact or manifest version | That a technical job may self-publish |
| `CorrectionRecord` | Connects superseded or withdrawn outputs to causes, replacements, and rollback targets | That replacement erases prior audit history |

KFM already has a representation-receipt concept. New work should extend or reference that authority rather than create a parallel receipt family.

### 4.2 Candidate job state machine

A render coordinator should expose a finite, monotonic state model. The following is **PROPOSED**:

```text
RECEIVED
  -> VALIDATING
      -> HELD
      -> DENIED
      -> READY
          -> QUEUED
              -> RUNNING
                  -> SUCCEEDED
                  -> FAILED
                  -> CANCELLED
                  -> EXPIRED
```

Required distinctions:

- `HELD` means the request is not safe or complete enough to proceed, but may become actionable after bounded evidence, rights, sensitivity, or capability work.
- `DENIED` means policy or authority forbids the requested execution or disclosure.
- `FAILED` means execution failed after admission; it must not conceal a policy hold or denial.
- `SUCCEEDED` means the technical job produced an artifact matching the accepted render plan. It does not mean the artifact is correct, reviewed, released, or published.
- `CANCELLED` is an explicit terminal outcome with actor, reason, and timing.
- `EXPIRED` records a bounded time or lease failure rather than silently deleting the job.

Outward-facing APIs should map internal detail to KFM’s finite public response posture—such as answer, abstain, deny, or error—without leaking protected policy reasoning or sensitive source detail.

## 5. Candidate REST orchestration profile

All route names in this section are **PROPOSED examples**. They do not establish repository behavior.

### 5.1 Resource-oriented shape

```text
POST   /v1/render-jobs
GET    /v1/render-jobs/{job_id}
DELETE /v1/render-jobs/{job_id}
GET    /v1/render-jobs/{job_id}/attempts
GET    /v1/render-artifacts/{artifact_id}
GET    /v1/render-artifacts/{artifact_id}/receipt
```

A safe asynchronous submission profile should:

1. validate request syntax before accepting work;
2. bind the request to an immutable canonical request digest;
3. require an idempotency key for creation;
4. return `202 Accepted` only when work has been accepted for asynchronous processing;
5. return a status-resource URI using `Location` or an equivalent typed link;
6. include `Retry-After` when polling guidance is known;
7. expose `ETag` on mutable status resources and require `If-Match` for state-changing operations where lost updates matter;
8. represent errors with RFC 9457 Problem Details or an equivalent governed envelope;
9. distinguish requester-visible status from protected internal diagnosis;
10. never return an artifact URL that bypasses rights, sensitivity, release, or expiry checks.

### 5.2 Idempotency and replay

An idempotency record should bind at least:

- authenticated principal or service identity;
- route and API version;
- normalized request body digest;
- idempotency key;
- first-seen time and bounded retention window;
- resulting job identifier;
- mismatch outcome when the same key is reused with different bytes.

A repeated request with the same key and same canonical request must resolve to the same logical job or an explicitly versioned replay result. Reuse with different request bytes must fail safely rather than silently start different work.

Replay has two meanings and they must remain separate:

- **semantic replay:** the same admitted scene graph, source versions, transformations, policy context, and renderer profile are reconstructed;
- **pixel replay:** the same output bytes are produced.

Pixel replay may be impossible across GPU, driver, browser, shader compiler, font, or codec changes. KFM should require semantic replay evidence first and make pixel determinism an explicitly bounded capability claim.

### 5.3 Cancellation, retry, and partial failure

Cancellation should be modeled as a state transition, not a transport disconnect. The coordinator should record who requested it, when it became effective, which side effects completed, and whether temporary outputs were destroyed or quarantined.

Retries should create an attempt record under the same logical job when inputs and plan are unchanged. A changed source version, renderer profile, policy context, or transform parameter should produce a new logical job or a clearly versioned successor. Attempt history must not be overwritten.

Multi-artifact jobs need explicit partial-success semantics. A coordinator should not convert “one tile failed” or “one view omitted” into an unqualified success. Candidate terminal detail may include:

- `complete`;
- `complete_with_omissions`;
- `failed_before_artifact`;
- `failed_after_partial_artifact`;
- `cancelled_with_temporary_artifacts`.

Only the finite public outcome should be exposed to ordinary clients; protected diagnostics remain behind governed access.

### 5.4 Caching and correction

Cache keys must include all representation-significant inputs, including source version, style or material version, renderer profile, coordinate reference assumptions, time slice, transform parameters, sensitivity generalization, and output media profile.

A cached artifact must not survive a source withdrawal, policy change, rights expiry, correction, or release revocation merely because its byte digest is stable. Cache invalidation should therefore be driven by both content identity and governance state.

## 6. 3D carrier and scene boundaries

### 6.1 Carriers are not truth

3D Tiles, glTF, terrain meshes, point clouds, voxels, rasters, vector tiles, and rendered images are representation carriers. Each can preserve some properties and discard others. No carrier should become the sovereign store of source meaning.

A candidate scene assembly should reference, rather than absorb without trace:

- source object identifiers and versions;
- evidence references;
- coordinate reference and vertical datum assumptions;
- temporal validity or observation time;
- transforms and generalization;
- rights and sensitivity decisions;
- renderer capability requirements;
- representation limitations;
- correction and rollback targets.

### 6.2 3D Tiles and glTF

The OGC 3D Tiles standard provides a spatial hierarchy and streaming model for large heterogeneous 3D geospatial content. glTF provides a runtime transmission format for 3D scenes and models. Their technical compatibility does not settle KFM admission, provenance, rights, sensitivity, semantic identity, or publication.

A governed profile should pin:

- accepted specification and extension versions;
- extension allowlists and unknown-extension behavior;
- external URI policy;
- bounding-volume and geometric-error validation;
- coordinate and vertical-reference handling;
- metadata preservation and mapping;
- compression and decoder versions;
- content-size, hierarchy-depth, and traversal budgets;
- validation tooling and expected diagnostics.

Unknown extensions, remote dependencies, malformed hierarchies, non-finite coordinates, impossible bounding volumes, and missing vertical-reference information should fail closed or enter quarantine.

### 6.3 MapLibre relationship

`MapRuntimePort` is a renderer-neutral application boundary. A future `MapLibreAdapter` may implement it, but the port must not acquire renderer-specific types merely to simplify one implementation. Advanced 3D execution should remain behind capability negotiation and bounded adapter interfaces.

A future adapter proof should demonstrate at least:

- renderer version and dependency integrity;
- style loading and restoration;
- terrain and raster-dem handling;
- custom-layer lifecycle and graphics-context restoration;
- camera and selection serialization;
- stable feature identity and feature-state behavior;
- resize, context loss, and error handling;
- cleanup and listener disposal;
- accessibility and reduced-motion behavior;
- performance budgets under representative fixtures;
- no direct path from browser input to an ungoverned model or canonical store.

The port seam alone proves none of these items.

## 7. Candidate LLM-ingestible PDF profile

“LLM-ingestible” must not mean “LLM-authoritative.” A PDF may be easier to extract, chunk, search, and cite while still containing errors, stale claims, prompt injection, inaccessible diagrams, unresolved rights, or unsupported conclusions.

A KFM PDF carrier should be treated as a derived representation whose claims resolve back to evidence and governing records.

### 7.1 Document control block

Every governed PDF candidate should make the following visible near the beginning:

- stable document identifier;
- title, version, status, and effective or observation date;
- owning responsibility lane;
- authority level and explicit non-authorities;
- source and evidence references;
- repository commit or release manifest when applicable;
- rights and sensitivity status;
- correction contact and supersession relationship;
- build-tool and profile version;
- content digest or a resolvable manifest reference;
- truth labels used in the document.

A PDF without this block may still be useful research, but should not be treated as a governed KFM artifact.

### 7.2 Logical structure and extraction

A candidate build profile should require:

1. tagged logical reading order;
2. real Unicode text rather than text flattened into images;
3. bookmarks that mirror the heading hierarchy;
4. stable section and claim identifiers visible in text;
5. page headers and footers marked as artifacts so they do not pollute extraction;
6. descriptive link text and preserved target URIs;
7. table headers, simple table structures, and text alternatives for complex tables;
8. alternative text and extended descriptions for diagrams, maps, and 3D views;
9. no reliance on color, animation, hover, or spatial placement alone;
10. code blocks with language labels and unambiguous line wrapping;
11. explicit units, coordinate systems, time zones, and temporal scope;
12. selectable citations and bibliography entries;
13. a text equivalent for every material conclusion shown only in a figure.

The accessible reading order should also be the extraction order. Visual polish must not be achieved by fragmenting sentences into separately positioned text boxes.

### 7.3 Claim cards

Material claims should be expressible as compact, self-contained records. The following shape is **illustrative**, not an accepted schema:

```json
{
  "claim_id": "KFM-3D-CLAIM-0001",
  "status": "CONFIRMED",
  "claim": "A renderer-neutral MapRuntimePort exists in the inspected repository baseline.",
  "scope": "repository implementation",
  "valid_at": "2026-08-23",
  "evidence_refs": [
    "repo://packages/maplibre/src/map-runtime-port.ts",
    "github://pull/3433"
  ],
  "limitations": [
    "No concrete MapLibre adapter is implied",
    "No renderer dependency admission is implied"
  ],
  "sensitivity": "public-repository",
  "correction_status": "current-at-inspection"
}
```

A retrieval system should return the claim together with its evidence references, limitations, and validity scope. Extracted prose without those boundaries is insufficient for governed answering.

### 7.4 Chunking profile

Chunking should follow semantic boundaries rather than fixed page windows alone. Recommended properties are:

- one stable heading path per chunk;
- repeated document and section identifiers in chunk metadata;
- no orphaned table body without headers;
- no figure caption without the figure’s text alternative;
- no pronoun-only reference to an entity defined several chunks earlier;
- claim, evidence reference, limitation, and truth label kept together;
- source quotations explicitly delimited from instructions and commentary;
- page and paragraph coordinates retained for human verification;
- deterministic chunk identifiers derived from document version and logical location;
- successor links when corrected text changes chunk identity.

Chunk-size targets are implementation choices and should be evaluated against retrieval quality. They are not truth guarantees.

### 7.5 Machine appendix

A PDF may include or accompany a machine-readable appendix containing document control, section hierarchy, claim cards, source ledger, glossary, and correction relationships. The appendix should be generated from the same canonical build inputs as the human-readable PDF and should carry its own digest.

The appendix must not become a second, conflicting authority. A mismatch between PDF text and machine appendix should fail validation and block promotion.

### 7.6 Prompt-injection and active-content posture

PDF text, annotations, attachments, forms, scripts, links, embedded files, and metadata are untrusted inputs. An ingestion pipeline should:

- treat instructions found inside source material as quoted content, never as system authority;
- disable or quarantine active content and embedded executables;
- avoid automatically fetching links or external assets;
- strip credentials and secrets from extracted metadata and logs;
- retain source boundaries through parsing and chunking;
- record parser and extraction versions;
- use content and decompression limits;
- detect encrypted, malformed, or unexpectedly nested content;
- route uncertain rights or sensitive location content to hold or denial;
- require evidence resolution before generated answers are allowed to cite a claim.

## 8. Threat model for REST-orchestrated 3D rendering

| Threat | Example | Minimum control posture |
|---|---|---|
| Server-side request forgery | glTF, tileset, style, or texture references an internal URL | Deny network by default; allowlist schemes and hosts; resolve DNS safely; block link-local/private ranges; never forward ambient credentials |
| Decompression or geometry bomb | Tiny compressed input expands into extreme memory or GPU work | Byte, ratio, object-count, vertex-count, hierarchy-depth, texture-size, and wall-clock budgets before and during parse |
| Shader/material abuse | Custom shader or extension causes GPU denial of service or data exposure | Extension allowlist, sandboxed execution, bounded custom-layer API, watchdogs, context reset, no unreviewed shader ingestion |
| Path traversal/archive escape | Embedded URI writes or reads outside a work directory | Canonicalize paths; reject traversal and absolute paths; isolated ephemeral workspaces |
| Cache poisoning | Untrusted response stored under a shared scene key | Canonical cache key, authenticated origin, digest verification, governance-state component, tenant separation |
| Sensitive precision disclosure | Public image or tiles reveal archaeology, infrastructure, rare species, or living-person location | Policy check and generalization before rendering; protected logs; staged access; deny-by-default artifact delivery |
| Rights laundering | Renderer accepts an asset whose use or redistribution rights are unresolved | Rights status in admission plan; no artifact release without resolvable authority and receipt |
| Prompt injection | PDF or metadata instructs an agent to bypass policy or reveal protected data | Source instructions remain data; evidence-first retrieval; no tool execution from source text; bounded model permissions |
| Stale or corrected output | Old cache remains accessible after source correction or release revocation | Correction graph, release-state check on every delivery, cache purge receipt, rollback target |
| False determinism | Pixel hash is treated as proof of factual correctness | Separate semantic replay, pixel replay, evidence validity, and publication authority |

## 9. Validation and proof plan

No candidate should graduate from this research note on documentation alone. A dependency-closed implementation slice should define tests before claiming behavior.

### 9.1 Contract and schema validation

- valid and invalid examples for every finite state;
- rejection of unknown states and impossible transitions;
- canonical request-digest test vectors;
- idempotency-key replay and mismatch cases;
- receipt-to-artifact digest resolution;
- required evidence, rights, sensitivity, and temporal fields;
- backward-compatibility or explicit migration fixtures;
- no duplicate semantic home for existing receipt or runtime concepts.

### 9.2 HTTP behavior

- `202 Accepted` status-resource behavior;
- `Location`, typed links, and `Retry-After` semantics;
- `ETag` and `If-Match` lost-update protection;
- RFC 9457 error shape and content negotiation;
- cancellation races;
- timeout and expiry behavior;
- rate-limit and overload responses;
- no protected diagnostic leakage;
- exact handling of repeated requests and network retries.

### 9.3 Security-negative tests

- blocked private, loopback, link-local, and credential-bearing URLs;
- malicious redirects and DNS rebinding;
- oversized textures, vertex counts, archive depth, and compression ratio;
- malformed glTF/tileset hierarchies and non-finite coordinates;
- unsupported extensions and external-resource references;
- path traversal and archive escape;
- active PDF content, embedded files, encryption, and malformed object graphs;
- prompt-injection strings retained as source text and never executed;
- sensitive coordinate redaction/generalization before artifact creation.

### 9.4 Renderer and scene proof

- synthetic no-network fixtures first;
- capability negotiation without renderer import at the application seam;
- browser lifecycle, context loss, cleanup, and restoration;
- semantic scene hash and receipt reproducibility;
- visual regression used only as representation evidence;
- performance budgets recorded with hardware, browser, renderer, and driver context;
- artifact delivery blocked until explicit release fixture authorizes it.

### 9.5 PDF carrier proof

- logical extraction order matches visual reading order;
- headings, lists, tables, links, code, and captions survive two independent extractors;
- all material figures have text alternatives;
- every `CONFIRMED` claim resolves to at least one evidence reference;
- `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION` labels remain attached after chunking;
- machine appendix and rendered PDF are generated from the same inputs and have a verified relationship;
- correction and supersession links survive regeneration;
- retrieval evaluation measures exact claim/evidence pairing and appropriate abstention, not fluent summary quality alone.

## 10. Smallest coherent follow-on slices

The following order minimizes authority drift and keeps changes reversible.

### Slice A — current-state documentation correction

**Status:** IN REVIEW through issue #3436 and its same-path candidate branch.

Update only stale current-state statements in `docs/architecture/planetary-3d.md` so they reflect merged PR #3433 and accepted ADR-0006/0007. Preserve every existing hold, sensitivity, admission, receipt, and publication boundary. Do not add route names or runtime claims.

### Slice B — existing-contract inventory

**Status:** PROPOSED; exact paths for any new objects are **NEEDS VERIFICATION**.

Inventory current job, task, operation, receipt, runtime-envelope, error, and release contracts before naming a `RenderJob` semantic home. The output should classify overlap, reuse opportunities, and conflicts. No new contract should be created until this inventory shows that a distinct semantic responsibility remains.

### Slice C — fixture-only orchestration contract

**Status:** PROPOSED; blocked on Slice B.

Define the smallest finite-state, renderer-neutral job contract with valid and invalid synthetic fixtures. It should reference existing evidence, policy, receipt, and runtime-envelope authorities rather than copy them. No route, service, renderer, or source admission belongs in this slice.

### Slice D — API projection and no-network evaluator

**Status:** PROPOSED; blocked on accepted contract and placement review.

Project the accepted contract through the governed API boundary using synthetic, no-network fixtures. Verify HTTP status, finite outward outcomes, idempotency, conditional mutation, problem details, and protected-diagnostic redaction.

### Slice E — renderer dependency admission and concrete adapter

**Status:** HOLD until dependency, security, browser-probe, ownership, and rollback evidence exists.

A concrete renderer adapter should be admitted only after the dependency gate, exact-version integrity, browser lifecycle proof, accessibility checks, negative tests, and reviewer route are satisfied. The adapter remains a renderer implementation, not evidence, policy, or publication authority.

### Slice F — real source or scene candidate

**Status:** HOLD.

Real 3D sources, externally hosted tilesets, LiDAR, meshes, point clouds, or released scenes require separate identity, rights, sensitivity, provenance, validation, integrity, review, release, correction, and rollback evidence. None is admitted by this research note.

## 11. Primary-source research ledger

The following primary sources constrain the proposed design. A future implementation PR should pin the exact versions used by code and validation rather than infer them from this list.

| Source | Governing use in this research | Repository effect |
|---|---|---|
| IETF RFC 9110, *HTTP Semantics* — `https://www.rfc-editor.org/rfc/rfc9110` | Status semantics, conditional requests, representation metadata, caching vocabulary | Research constraint only |
| IETF RFC 9457, *Problem Details for HTTP APIs* — `https://www.rfc-editor.org/rfc/rfc9457` | Machine-readable error projection without inventing a proprietary error transport | Research constraint only |
| IETF RFC 7240, *Prefer Header for HTTP* — `https://www.rfc-editor.org/rfc/rfc7240` | Optional asynchronous preference and response handling | Research constraint only |
| IETF RFC 8288, *Web Linking* — `https://www.rfc-editor.org/rfc/rfc8288` | Typed links among job, artifact, receipt, correction, and successor resources | Research constraint only |
| IETF RFC 9530, *Digest Fields* — `https://www.rfc-editor.org/rfc/rfc9530` | Content-integrity metadata for requests and artifacts | Research constraint only |
| IETF RFC 9421, *HTTP Message Signatures* — `https://www.rfc-editor.org/rfc/rfc9421` | Candidate authenticated-message profile where deployment requirements justify it | Research constraint only; not required or implemented |
| OpenAPI Specification 3.1.1 — `https://spec.openapis.org/oas/v3.1.1.html` | API description, JSON Schema alignment, operation and response documentation | No OpenAPI operation created |
| JSON Schema Draft 2020-12 — `https://json-schema.org/draft/2020-12/json-schema-core` | Candidate machine-validation vocabulary | No schema created |
| OGC 3D Tiles 1.1 — `https://docs.ogc.org/cs/22-025r4/22-025r4.html` | Hierarchical streaming, bounding volumes, metadata, and content rules for large 3D geospatial carriers | No carrier admitted |
| Khronos glTF 2.0 — `https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html` | Runtime 3D asset structure, buffers, images, materials, extensions, and external dependencies | No glTF profile admitted |
| MapLibre GL JS documentation — `https://maplibre.org/maplibre-gl-js/docs/` | Renderer capabilities and lifecycle to verify in a future adapter slice | No renderer dependency or adapter admitted |
| MapLibre Style Specification — `https://maplibre.org/maplibre-style-spec/` | Style/source/layer semantics that a concrete adapter must not misrepresent | No style profile admitted |
| W3C PROV-O — `https://www.w3.org/TR/prov-o/` | Provenance concepts for entities, activities, agents, derivation, and invalidation | Existing KFM evidence and receipt authorities remain sovereign |
| W3C WCAG 2.2 — `https://www.w3.org/TR/WCAG22/` | Accessible document and interface outcomes, including non-text alternatives, structure, and non-color cues | Research constraint only |
| PDF Association, *Well-Tagged PDF* resources — `https://pdfa.org/resource/tagged-pdf-best-practice-guide-syntax/` | Tagged structure, reading order, artifact handling, and extraction quality | No PDF build profile accepted |

## 12. Directory Rules basis

This file is placed under `docs/intake/exploratory/` because its responsibility is source reconciliation and candidate research. It does not belong under:

- `contracts/`, because it does not define semantic authority;
- `schemas/`, because it does not define machine shape;
- `policy/`, because it does not grant or deny permission;
- `packages/` or `apps/`, because it contains no implementation;
- `data/published/`, because it is not a released dataset or scene;
- a new root-level 3D or AI folder, because topic similarity does not justify a new authority boundary.

Existing compatibility roots remain unchanged. Future new paths are intentionally not selected here; they require a current inventory and placement check.

## 13. Non-effects and rollback

This source map changes documentation only. It has no runtime import, dependency, lockfile, route, schema, source, registry, policy, release, deployment, publication, or data effect.

Rollback for this same-path update is restoration of source-map blob `f8da2f3efd58197c95219728a5359d2f0ffd267e` or reversal of the candidate commit. No migration or data repair is required. Any future slice must define its own rollback target and must not rely on this note as authority.

## 14. Open verification register

| ID | Verification item | Status | Closure evidence |
|---|---|---|---|
| `REST3D-VER-001` | Extract and map the supplied PDF’s material claims to exact pages or section identifiers | **CONFIRMED CLOSED** | Section 2.1 page map reviewed against source SHA-256 `d5cd2e88854f3291dbeae5e609a423cce5bbf40e36172efdd2921127e2d8399d` |
| `REST3D-VER-002` | Re-run a repository-wide inventory for existing operation/job/idempotency/error contracts before naming a new semantic home | **NEEDS VERIFICATION** | Search record plus overlap classification |
| `REST3D-VER-003` | Correct stale current-state statements in `docs/architecture/planetary-3d.md` without expanding authority | **IN REVIEW** | Issue #3436 same-path candidate grounded in PR #3433 and accepted ADR-0006/0007; merge remains separate |
| `REST3D-VER-004` | Verify exact current renderer, 3D Tiles, glTF, OpenAPI, JSON Schema, PDF, and accessibility versions at dependency/profile admission time | **NEEDS VERIFICATION** | Pinned manifests, checksums, official specification references, and tests |
| `REST3D-VER-005` | Establish independent reviewer ownership for dependency, security, policy, and publication-significant slices | **NEEDS VERIFICATION** | Recorded reviewer route and approval evidence |
| `REST3D-VER-006` | Demonstrate LLM retrieval preserves claim, truth label, evidence reference, limitation, sensitivity, and validity together | **PROPOSED** | Synthetic evaluation suite with abstention and citation-resolution results |

Until these items are closed, the correct repository posture is: the research is useful, the control-plane model is buildable, the renderer-neutral seam and accepted architecture decisions are real, and the advanced REST/3D/PDF profiles remain proposals.