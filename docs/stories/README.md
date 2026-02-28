<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/d32015ca-3079-4341-9cee-697c744ac4fd
title: Story Nodes Directory Guide
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-24
updated: 2026-02-24
policy_label: public
related:
  - docs/stories/
tags: [kfm, stories, story-nodes, narrative]
notes:
  - Directory-level contract for Story Node v3 content and workflow.
[/KFM_META_BLOCK_V2] -->

![Status](https://img.shields.io/badge/status-draft-lightgrey) <!-- TODO: wire to releases/gates -->
![Story%20Node](https://img.shields.io/badge/story_node-v3-informational)
![Evidence](https://img.shields.io/badge/evidence-resolver_required-blueviolet)
![Policy](https://img.shields.io/badge/policy-cite_or_abstain-important)
![Owners](https://img.shields.io/badge/owners-TBD-orange)

# Story Nodes

Governed narrative units that bind **human-readable markdown** to **map state** and **resolvable evidence**.

> [!NOTE]
> This folder is the canonical home for Story Nodes in this repo *if* you are using `docs/stories/`.
> Some legacy documentation may refer to other locations (for example `docs/reports/story_nodes/`). If your repo differs, update this README to match the actual canonical path.

## Navigation
- [Purpose](#purpose)
- [How this fits in KFM](#how-this-fits-in-kfm)
- [Directory layout](#directory-layout)
- [Story Node v3 format](#story-node-v3-format)
- [Citations and evidence](#citations-and-evidence)
- [Governance and safety](#governance-and-safety)
- [Workflow](#workflow)
- [Definition of done](#definition-of-done)
- [Story registry](#story-registry)
- [Appendix](#appendix)

---

## Purpose

This directory exists to store **Story Nodes** as governed publications:

- **Narrative**: written in Markdown for humans
- **Map choreography**: encoded in a sidecar JSON file for machines
- **Evidence**: every claim is traceable and must be resolvable via the evidence resolver

Back to top: [Navigation](#navigation)

---

## How this fits in KFM

Story Nodes sit downstream of the trust membrane. A Story Node must not “skip the line” ahead of provenance, catalogs, and policy.

```mermaid
flowchart LR
  Raw[Raw] --> ETL[ETL and transforms]
  ETL --> Catalogs[STAC DCAT PROV]
  Catalogs --> Graph[Graph]
  Graph --> API[Governed API]
  API --> UI[Map and Story UI]
  UI --> Stories[Story Nodes]
  Stories --> Focus[Focus Mode]
```

Back to top: [Navigation](#navigation)

---

## Directory layout

This README documents **what belongs here** and **what must not**. The exact subfolders are a repo choice; below is a recommended structure that keeps drafts and published stories separate.

```text
docs/stories/                                    # Story Nodes: narratives + map state + citations
├─ README.md                                      # Authoring + review + publish rules (gates + invariants)
│
├─ _schemas/                                      # JSON Schemas (CI validates story packs + sidecars)
│  ├─ story_node.schema.json                      # story.md structural expectations (if you lint markdown)
│  ├─ story_sidecar.schema.json                   # story.json: map state + citations + policy labels
│  ├─ media_attribution.schema.json               # optional structured media attribution (if you adopt it)
│  └─ story_index.schema.json                     # schema for aggregated story indexes
│
├─ _registry/                                     # Lightweight catalog/index of stories for UI + discovery
│  ├─ stories.index.json                           # derived or hand-curated index (slug → title/status/tags)
│  ├─ tags.vocab.json                              # controlled tags (optional; helps filter/search UX)
│  └─ policy_labels.vocab.json                     # allowed labels + obligations vocab (optional)
│
├─ _lint/                                         # Repo-local lint config for story QA
│  ├─ linkcheck.allowlist.txt                     # allowlist for stable external domains (optional)
│  ├─ markdownlint.json                           # style rules (optional)
│  └─ story_rules.yaml                            # house rules: required sections, prohibited patterns, etc.
│
├─ _shared/                                       # Shared, non-story-specific assets (optional)
│  ├─ media/                                      # icons, logos, generic diagrams used across stories
│  └─ snippets/                                   # reusable markdown fragments (disclaimers, boilerplates)
│
├─ _templates/                                    # Copy/paste starters (keep aligned to Story Node v3)
│  └─ story_node_v3/
│     ├─ story.md                                 # template markdown (sections + citation pattern)
│     ├─ story.json                               # template sidecar (map state + refs placeholders)
│     ├─ media_attribution.md                     # template attribution notes (license + credits)
│     └─ review_checklist.md                      # reviewer checklist template
│
├─ draft/                                         # Proposed stories (NOT authoritative)
│  └─ <story_slug>/                               # kebab-case slug; stable once published
│     ├─ story.md                                 # narrative w/ claim anchors (claims must be cited)
│     ├─ story.json                               # sidecar: map state + citations + policy labels/obligations
│     ├─ story.lock.json                          # optional: frozen hashes of evidence/media for reproducibility
│     │
│     ├─ evidence/                                # optional: structured citation plumbing (still “draft”)
│     │  ├─ evidence_refs.json                    # EvidenceRef list (ids, sources, scope, policy label)
│     │  ├─ claim_map.json                        # claim_id → evidence_ref_id(s)
│     │  └─ notes.md                              # analyst notes; assumptions; “unknowns to verify”
│     │
│     ├─ map/                                     # optional split to reduce JSON diff noise
│     │  ├─ map_state.json                        # viewport, layers, filters, time slider defaults
│     │  ├─ layer_overrides.json                  # per-story layer styling/symbolization overrides
│     │  └─ bookmarks.json                        # named extents/steps used by scrollytelling
│     │
│     ├─ media/                                   # bounded story assets (licensed; no sensitive detail)
│     │  ├─ src/                                  # originals (as received)
│     │  ├─ derived/                              # resized/cropped/annotated derivatives
│     │  └─ thumbnails/                           # small preview images for UI listing cards
│     ├─ media_attribution.md                     # recommended in draft; required if licenses apply
│     │
│     ├─ review/                                  # WIP review artifacts (draft stage)
│     │  ├─ checklist.md                          # reviewer checklist instance
│     │  ├─ signoff.yaml                          # approvals + timestamps (optional)
│     │  └─ discussion.md                         # review notes + decisions
│     │
│     └─ exports/                                 # optional (usually generated; may be gitignored)
│        ├─ preview.html                          # rendered HTML preview
│        └─ figures/                              # exported charts/maps for PR review
│
├─ review/                                        # Stories in formal review (pre-publish freeze)
│  └─ <story_slug>/
│     ├─ story.md                                 # candidate content (RC)
│     ├─ story.json                               # candidate sidecar (RC)
│     ├─ story.lock.json                          # REQUIRED if you enforce reproducibility gates
│     ├─ review/                                  # REQUIRED: signoffs + checklist + decision record
│     │  ├─ checklist.md
│     │  ├─ signoff.yaml
│     │  └─ decision_log.md                       # what changed + why
│     └─ receipts/                                # REQUIRED: CI outputs proving gates passed
│        ├─ lint_report.json
│        ├─ linkcheck_report.json
│        ├─ schema_validation.json
│        └─ policy_check.json
│
├─ published/                                     # Published stories (authoritative)
│  └─ <story_slug>/
│     ├─ story.md                                 # latest published version (frozen)
│     ├─ story.json                               # latest sidecar (frozen; must match story.md refs)
│     ├─ story.manifest.json                      # REQUIRED: hashes of story.md/json + media set
│     ├─ story.receipt.json                       # REQUIRED: publish receipt (who/what/when/inputs/outputs)
│     ├─ media/
│     │  └─ …                                     # frozen published media (no sensitive detail)
│     ├─ media_attribution.md                     # REQUIRED when media licenses/attribution apply
│     │
│     ├─ versions/                                # REQUIRED if edits after publish are allowed at all
│     │  ├─ v1/                                   # immutable snapshot (first publish)
│     │  │  ├─ story.md
│     │  │  ├─ story.json
│     │  │  ├─ story.manifest.json
│     │  │  ├─ story.receipt.json
│     │  │  └─ media/…
│     │  └─ v2/                                   # immutable snapshot (republish)
│     │     └─ …
│     │
│     └─ CHANGELOG.md                             # human-readable summary of republish diffs (optional)
│
├─ withdrawn/                                     # Removed from publication (policy/quality/rights reasons)
│  └─ <story_slug>/
│     ├─ tombstone.md                             # why withdrawn + what users should do instead
│     ├─ withdrawal_receipt.json                  # who/when/why/policy decision record
│     └─ references/                              # optional: pointers to replacement story or redacted version
│
└─ _archive/                                      # Deprecated structures or retired templates (keep minimal)
   └─ …
```

### Acceptable inputs

- Story Node v3 artifacts:
  - `story.md` (markdown narrative)
  - `story.json` (sidecar metadata: map state + citations + policy + review)
- Supporting media **only when** rights are clear and attribution is captured
- Directory-level documentation and templates that support Story Node authoring

### Exclusions

Do **not** put these in `docs/stories/`:

- Raw or processed datasets (those belong in the data lifecycle zones)
- Pipeline code, ETL scripts, or schema contracts (those belong in code/contracts areas)
- Media with unclear rights or missing attribution
- Uncited narrative claims
- Sensitive location specifics that violate policy or sovereignty requirements

Back to top: [Navigation](#navigation)

---

## Story Node v3 format

A Story Node is a **pair** of files:

| Artifact | Required | Purpose |
|---|---:|---|
| `story.md` | ✅ | Human-readable narrative with explicit claims and inline citations |
| `story.json` | ✅ | Machine-readable story metadata: map state, citations list, policy label, review state |

### story.md expectations

- Must include a **MetaBlock v2** (as an HTML comment) so it can be treated as a governed document.
- Must include:
  - `Summary` section: scope + time window
  - `Claims` section: numbered claims with citations
  - `Narrative` section: prose with inline citations
  - `Evidence` section: a list of evidence references used

Minimal example:

```markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://story/<uuid>@v1
title: <Story title>
type: story
version: v3
status: draft
owners: <names or teams>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - kfm://dataset/<slug>@<dataset_version_id>
tags: [kfm, story]
notes:
  - Short note about scope or constraints
[/KFM_META_BLOCK_V2] -->

# <Story title>

## Summary
<What this story covers and the relevant time window.>

## Claims
1. <Claim text.> [CITATION: dcat://...]
2. <Claim text.> [CITATION: prov://...]

## Narrative
<Prose with inline citations.>

## Evidence
- [CITATION: dcat://...]
- [CITATION: stac://...]
- [CITATION: prov://...]
```

### story.json expectations

The sidecar JSON must declare Story Node v3 and include, at minimum:

- `kfm_story_node_version: "v3"`
- stable story identity (`story_id`) and story version (`version_id`)
- `status`, `policy_label`, and `review_state`
- `map_state` (bbox/zoom/layers/time window or equivalent)
- `citations[]` (scheme refs that can be resolved)

Minimal example:

```json
{
  "kfm_story_node_version": "v3",
  "story_id": "kfm://story/<uuid>",
  "version_id": "v1",
  "status": "draft",
  "policy_label": "public",
  "review_state": "needs_review",
  "map_state": {
    "bbox": [-102.0, 36.9, -94.6, 40.0],
    "zoom": 6,
    "layers": [],
    "time_window": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }
  },
  "citations": [
    { "ref": "dcat://<dataset>@<version>", "kind": "dcat" }
  ]
}
```

Back to top: [Navigation](#navigation)

---

## Citations and evidence

### Non-negotiable rules

- **Every claim must cite evidence.**
- Citations must use resolvable evidence references (examples):
  - `dcat://...` for dataset identity + licensing + distribution metadata
  - `stac://...` for spatial/temporal assets
  - `prov://...` for run receipts / lineage
  - `doc://...` for governed documents and extracts

> [!IMPORTANT]
> Publishing is blocked unless **all citations resolve through the evidence resolver**.
> Do not publish Story Nodes that rely on “dead links”, private URLs, or evidence that can’t be resolved.

### Practical authoring guidance

- Prefer **primary sources** and **cataloged** evidence.
- Inline citations close to the sentence they support.
- If a claim is uncertain or contested, state uncertainty and cite sources for the competing viewpoints.

Back to top: [Navigation](#navigation)

---

## Governance and safety

Story Nodes are not “just content”; they are governed outputs.

### Rights and licensing for media

> [!WARNING]
> Publishing must be blocked if rights are unclear for included media.

When adding images or other media:

- Ensure the license/rights are recorded
- Ensure attribution is included (recommended: `media_attribution.md`)
- Ensure policy labels match the sensitivity of the content

### Sensitive locations and sovereignty

If a story touches sensitive locations or culturally restricted knowledge:

- Default to generalization/redaction
- Use a restrictive policy label when required
- Do not embed precise coordinates unless policy explicitly allows it

Back to top: [Navigation](#navigation)

---

## Workflow

### Create a new Story Node

1. Create a folder under `draft/<story_slug>/`.
2. Add `story.md` and `story.json` as a pair.
3. Add any media under `media/` and include attribution notes.
4. Ensure:
   - MetaBlock v2 is present and complete
   - `doc_id` is stable (do not regenerate on edits)
   - `policy_label` is correct for the content
   - every claim has at least one resolvable citation

### Update an existing Story Node

- Bump `updated` date in MetaBlock on meaningful edits.
- Preserve `doc_id` stability.
- If policy label changes, treat it as a governance event and ensure review gates are applied.

Back to top: [Navigation](#navigation)

---

## Definition of done

A Story Node is ready to move from `draft/` to `published/` when:

- [ ] `story.md` contains MetaBlock v2 and required sections
- [ ] `story.json` declares `kfm_story_node_version: "v3"` and includes required keys
- [ ] Every claim has at least one citation
- [ ] All citations resolve through the evidence resolver
- [ ] Policy label is correct and consistent with evidence sensitivity
- [ ] Media rights are clear and attribution is recorded
- [ ] Sensitive content is handled according to governance playbooks
- [ ] Review state indicates approval for publishing

Back to top: [Navigation](#navigation)

---

## Story registry

> [!TIP]
> Keep this table updated so reviewers and UI builders can discover story nodes quickly.

| Story | Status | Policy | Time window | Notes |
|---|---|---|---|---|
| _(add stories here)_ | draft | public | YYYY–YYYY | |

Back to top: [Navigation](#navigation)

---

## Appendix

<details>
<summary>Recommended conventions and open questions</summary>

### Proposed conventions

- Keep drafts and published stories separate (`draft/` vs `published/`) to make “what ships” explicit.
- Store story media adjacent to the story and require explicit attribution notes.
- Consider adding a machine-readable registry file if the UI needs quick discovery.

### Unknown until repo verification

- Exact story discovery mechanism for the UI (directory scan vs registry file)
- Exact schema validation tooling and CI checks for Story Nodes
- Canonical location if the repo uses a different path than `docs/stories/`

</details>
