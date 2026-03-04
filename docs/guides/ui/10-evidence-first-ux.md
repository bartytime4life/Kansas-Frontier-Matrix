<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/6f3d7c8c-2b1c-4e5a-8f0a-33a4ac2b4e77
title: Evidence First UX
type: standard
version: v1
status: draft
owners: [ui-platform, governance, focus-mode]
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: [docs/guides/ui/, docs/architecture/, docs/governance/]
tags: [kfm, ui, evidence-first, provenance, policy, focus-mode]
notes: ["UI guidance that enforces 'No Source, No Answer' across Map, Timeline, Story, and Focus Mode."]
[/KFM_META_BLOCK_V2] -->

# Evidence First UX
One-line purpose: Define UI patterns and contracts so every user-visible claim is traceable to governed evidence and policy decisions.

---

## Impact
**Status:** draft (target: active)  
**Owners:** `@ui-platform` · `@governance` · `@focus-mode`  
**Applies to:** Map Explorer · Timeline · Story · Focus Mode  

**Badges (TODO):**  
![Status](https://img.shields.io/badge/status-draft-lightgrey)  
![Policy](https://img.shields.io/badge/policy-default--deny-red)  
![A11y](https://img.shields.io/badge/WCAG-2.1_AA%2B-blue)  

**Quick nav:**  
- [Scope](#scope)  
- [Where it fits](#where-it-fits)  
- [Evidence discipline](#evidence-discipline)  
- [Core invariants](#core-invariants)  
- [UI patterns](#ui-patterns)  
- [Focus Mode UX contract](#focus-mode-ux-contract)  
- [Failure modes](#failure-modes)  
- [Definition of done](#definition-of-done)  

---

## Scope
**PROPOSED**: This guide covers UX and UI contracts for “evidence-first” behavior across KFM front-ends: Map, Timeline, Story, and Focus Mode.

**PROPOSED**: It defines:
- what must be shown to users (citations, provenance, policy decisions),
- how to show it (components and microcopy),
- how the UI behaves when evidence is missing or restricted (abstain, reduce scope, mask).

---

## Where it fits
**PROPOSED**: Location: `docs/guides/ui/10-evidence-first-ux.md`

**PROPOSED**: Upstream dependencies (conceptual):
- `docs/architecture/*` for layering rules and system boundaries
- `docs/governance/*` for policy decisions, obligations, and sensitivity handling
- `contracts/*` for API response schemas (Focus answers, map feature queries, evidence bundles)

**PROPOSED**: Downstream readers:
- UI engineers (React/MapLibre/Cesium)
- API engineers (governed endpoints that return evidence + obligations)
- Product/design (interaction rules, microcopy, and escalation paths)

---

## Acceptable inputs
**PROPOSED**: This guide assumes the UI receives (directly or indirectly via the API) these artifacts:
- **Evidence references**: IDs/URIs pointing to immutable, versioned artifacts
- **Catalog metadata**: STAC/DCAT records and provenance (PROV/run receipts)
- **Policy decisions**: allow/deny + obligations (redactions, masking, “do not show”)
- **Quality signals**: validation status, freshness timestamps, and pipeline health

---

## Exclusions
**PROPOSED**: This guide does not define:
- ETL pipeline implementation details (fetch/normalize/tiling)
- policy authoring (Rego rules) beyond UI consumption and messaging
- database/storage internals (PostGIS/Neo4j/index implementation)

---

## Evidence discipline
### Claim labels
**CONFIRMED**: KFM outputs are expected to be “evidence-first,” meaning user-visible insights must trace back to governed, immutable evidence and pass policy checks.  
**PROPOSED**: In UI, every *meaningful claim* should carry one of these labels:

- **CONFIRMED** — Supported by resolvable evidence the user is allowed to inspect.
- **PROPOSED** — A hypothesis, plan, or interpretation presented as such; may point to supporting evidence but is not asserted as fact.
- **UNKNOWN** — Not supported by available admissible evidence; UI must not imply it is true.

### UI rule: No Source, No Answer
**CONFIRMED**: Focus Mode is designed as a governed loop: retrieve admissible evidence → synthesize → verify citations → emit receipts; if verification fails, the system abstains or reduces scope.  
**PROPOSED**: The UI must enforce the same semantics visually and interactionally:
- If a claim has no evidence, it must be labeled **UNKNOWN** and **not** presented as a factual answer.
- If policy blocks evidence access, the UI must disclose that **policy**, not “error,” is the cause (without leaking restricted details).

---

## Core invariants
### Layering
**CONFIRMED**: The UI is a pure client and must not directly call LLM runtimes or datastores; it calls governed APIs that orchestrate retrieval, generation, and policy checks.

### Policy membrane
**CONFIRMED**: Policy enforcement is default-deny / fail-closed: when evidence or permissions are missing, output scope must shrink, not expand.

### Observed vs derived
**PROPOSED**: UI must differentiate:
- **Observed** (measured/recorded) data
- **Derived** (processed, aggregated, modeled) data
- **Narrative** (human-authored Story Nodes) vs **Synthesis** (Focus answers)

---

## Mental model
**PROPOSED**: Treat UX as a “truth path”:
1) show what exists (datasets, features, timestamps),
2) show why it is trustworthy (provenance, validation),
3) only then show interpretation (summaries, narratives).

**PROPOSED**: Evidence-first UX optimizes for:
- **Auditability**: anyone can follow citations to sources.
- **Legibility**: users understand “what we know” vs “what we infer.”
- **Safety**: restricted data stays restricted; the UI does not “help users guess.”

---

## UI patterns

### Pattern 1: Evidence chips
**PROPOSED**: Any claim-bearing UI element (tooltip, panel paragraph, chart caption, Focus answer sentence) can attach an **Evidence Chip**.

**PROPOSED**: Evidence chip fields:
- label: `CONFIRMED | PROPOSED | UNKNOWN`
- citation count: `n sources`
- sensitivity icon (optional): `masked | redacted | restricted`
- open action: “View evidence”

**PROPOSED**: Chip placement rules:
- Map popups: chips near the first numeric claim.
- Timeline: chips near the event title and any “counts/impacts”.
- Story: chips inline at paragraph end, not buried in footers.
- Focus: chips per paragraph (not per sentence) unless high-stakes.

---

### Pattern 2: Evidence drawer
**PROPOSED**: A single consistent “Evidence Drawer” component across the app.

**PROPOSED**: Drawer tabs:
- **Sources**: resolvable artifacts and snippets
- **Provenance**: run receipt, transforms, tool versions
- **Policy**: allow/deny rationale category + obligations
- **Quality**: validation checks, freshness, known gaps

**PROPOSED**: Drawer UX principles:
- default collapsed, but never hidden
- supports keyboard navigation
- “copy citation” button emits stable reference (no transient URLs)

---

### Pattern 3: Provenance badge overlay on map
**PROPOSED**: Display per-feature pipeline status and provenance as small on-map badges (healthy/degraded/failing/running/unknown) with click-through to attestations and logs.

**PROPOSED**: This is especially useful when the user asks “why is this layer missing?” or “how fresh is this?”

---

### Pattern 4: Observed vs modeled label
**PROPOSED**: When a layer or metric is model-derived (e.g., anomaly surfaces, reconstructions), the UI must show a persistent “MODELED” label plus “not a forecast” where relevant.

**PROPOSED**: Tooltip microcopy:
- “Observed” → “Measured/recorded values.”
- “Modeled” → “Derived by a model from inputs listed in Evidence; not an alert system; not a forecast.”

---

### Pattern 5: Precision and masking controls
**PROPOSED**: If policy requires generalization, the UI should:
- show the fact that masking is applied,
- show the **effective precision** (e.g., “generalized to region level”),
- prevent “zooming in” past allowed precision (hard stop, not a soft warning).

**PROPOSED**: Avoid “security through obscurity” patterns:
- never show a blurred exact coordinate if it can be reconstructed
- never show “hinting” UI that reveals restricted locations by elimination

---

## Evidence surfaces matrix

**PROPOSED**: Minimum evidence artifacts per UX surface.

| UX surface | What user sees | Minimum evidence | Policy surface | Default behavior on missing evidence |
|---|---|---|---|---|
| Map popup | attribute claims, dates, counts | feature EvidenceRefs + dataset STAC/DCAT | obligations + masking note | abstain from numeric claims; show “UNKNOWN” |
| Layer panel | layer description + freshness | STAC collection + run receipt | allow/deny + sensitivity | hide layer or show masked preview |
| Timeline event | event title + date range | event EvidenceRefs + provenance | redaction list | show event shell; suppress restricted details |
| Story node | narrative paragraphs | citations per paragraph + source previews | obligations | block publish; require steward review |
| Focus answer | synthesized text | citation list + resolved bundles | policy decision + citation verification status | abstain or reduce scope |

---

## Focus Mode UX contract
### Interaction loop
**CONFIRMED**: Focus Mode is designed as a governed retrieval + synthesis loop with policy checks before returning answers.

~~~mermaid
flowchart LR
  U[User question] --> UI[UI sends request]
  UI --> API[Governed API]
  API --> P[Policy pre-check]
  API --> R[Retrieve admissible evidence]
  R --> E[Resolve evidence bundles]
  API --> L[LLM generation]
  L --> V[Citation verification gate]
  V -->|pass| A[Answer with citations]
  V -->|fail| X[Abstain or reduce scope]
  A --> UI2[UI renders answer and evidence]
  X --> UI2
~~~

### UI requirements for Focus results
**PROPOSED**: Focus answer UI must always render:
- an explicit claim label summary (e.g., “3 confirmed claims, 1 proposed interpretation, 2 unknowns”)
- a citation list that can be opened per paragraph
- a visible “policy applied” strip if redaction/masking occurred
- a “download receipt” action for audit workflows (if user role allows)

**PROPOSED**: Focus microcopy patterns:
- Abstain: “I can’t confirm this from admissible evidence. Try narrowing time/place or requesting access.”
- Reduce scope: “I can answer at county level, but not at parcel level due to policy.”

---

## API response shape
**UNKNOWN**: Exact KFM API schemas for EvidenceBundles and Focus answers are not confirmed in this guide.  
**Verification steps** (smallest path to CONFIRMED):
1) Identify the canonical OpenAPI/GraphQL schema for Focus responses.
2) Confirm EvidenceRef and EvidenceBundle shapes (fields + redaction model).
3) Confirm policy decision payload (obligations, reason codes, audit refs).

**PROPOSED**: Until schemas are finalized, use an additive, backward-compatible contract:

~~~json
{
  "answer_markdown": "…",
  "claim_summary": {
    "confirmed": 3,
    "proposed": 1,
    "unknown": 2
  },
  "citations": [
    {
      "id": "cite-1",
      "label": "NOAA Storm Events 1951",
      "evidence_ref": "kfm://evidence/…",
      "spans": [{"start": 120, "end": 210}]
    }
  ],
  "evidence_bundles": [
    {
      "evidence_ref": "kfm://evidence/…",
      "redactions": [{"field": "geometry", "reason": "policy.mask_precision"}],
      "artifacts": [
        {"type": "stac_item", "href": "…"},
        {"type": "prov_receipt", "href": "…"}
      ]
    }
  ],
  "policy": {
    "decision": "allow",
    "obligations": ["mask_precision", "no_sensitive_coords"],
    "audit_ref": "kfm://audit/…"
  },
  "run_receipt_ref": "kfm://prov/run/…"
}
~~~

---

## Failure modes
### Policy denial
**PROPOSED**: If policy denies, show:
- a denial banner (“Access restricted by policy”)
- reason category (high level, non-leaky)
- next action: “request access” or “open governance ticket”
- safe fallback view (aggregate, masked, or none)

### Evidence missing
**PROPOSED**: If evidence is missing:
- downgrade claim label to **UNKNOWN**
- show “what would be needed” (which source types) without implying facts
- offer scoped alternatives (“try county-level,” “try a different date range”)

### Stale or degraded pipelines
**PROPOSED**: If data freshness is outside SLO:
- show “stale” badge with last successful run timestamp
- disable “confirm” interactions (no confident language)
- allow browsing with explicit caution label

---

## Accessibility and trust cues
**PROPOSED**: Evidence-first UX must be accessible:
- evidence drawer keyboard reachable
- citations have accessible names (“Citation 2: USGS NWIS daily series”)
- color is never the only indicator (badges use icons + text)

**PROPOSED**: Avoid dark patterns:
- never auto-collapse citations permanently
- never hide policy-applied masking
- never present model-derived layers as “observed” data

---

## Telemetry and audit
**PROPOSED**: Emit privacy-preserving telemetry (PII-free):
- “evidence drawer opened”
- “citation copied”
- “policy denial viewed”
- “abstain shown”
- latency metrics per surface (map popup, focus answer render)

**PROPOSED**: Log as structured events with:
- request id
- role
- evidence ids (not raw content)
- policy audit ref

---

## Definition of done
**PROPOSED**: Evidence-first UX is “done” when:

- [ ] Every claim-bearing UI surface can render Evidence Chips.
- [ ] Evidence Drawer is available from Map, Timeline, Story, and Focus Mode.
- [ ] UI clearly differentiates observed vs derived vs narrative.
- [ ] Policy denials show a non-leaky reason category and safe next steps.
- [ ] Masking rules are enforced by interaction constraints (not just warnings).
- [ ] Focus Mode supports abstain/reduce-scope states with correct microcopy.
- [ ] Accessibility checks pass for citations and drawers (WCAG 2.1 AA+ target).
- [ ] Telemetry events are emitted without sensitive payloads.
- [ ] Regression tests exist for “no source, no answer” across core flows.

---

## Appendix
<details>
<summary>Microcopy pack (safe defaults)</summary>

**Abstain (no admissible evidence):**
- “I can’t confirm this from admissible evidence.”
- “Try narrowing the timeframe or widening the geography.”

**Policy deny (restricted access):**
- “Some details are restricted by policy.”
- “You can request access or view aggregated summaries.”

**Masked precision:**
- “Location has been generalized to protect sensitive sites.”
- “Zoom is limited to the allowed precision for this dataset.”

</details>

<details>
<summary>Component inventory (suggested)</summary>

~~~text
ui/
  components/
    EvidenceChip/
    EvidenceDrawer/
    PolicyBanner/
    ObservedModeledBadge/
    DataFreshnessBadge/
    ProvenanceLink/
~~~

</details>

---

## Back to top
[Back to top](#evidence-first-ux)
