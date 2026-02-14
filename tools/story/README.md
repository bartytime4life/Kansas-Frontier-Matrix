# 🧭 KFM Story Tools

![Governance](https://img.shields.io/badge/governance-governed-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-brightgreen)
![Template](https://img.shields.io/badge/story%20template-v3-informational)
![CI](https://img.shields.io/badge/CI-fail--closed-important)

This folder contains the **governed tooling** for KFM Story Nodes:
- validating Story Node Markdown against the **v3 template + schema**
- enforcing **citation** and **link integrity** rules
- building **StoryNodeBundle** payloads for the API/UI
- producing a **story bundle index** suitable for deterministic story listing, caching, and governance review

> [!IMPORTANT]
> Story Nodes are not “just docs.” They are **governed content artifacts** that drive UI playback and must remain compatible with:
> - the KFM **trust membrane** (no UI direct DB access; policy enforced centrally)  
> - **evidence resolution** (every citation ref must be resolvable)  
> - **fail-closed** CI gates (invalid stories block merge/publish)

---

## Table of contents

- [What this folder is for](#what-this-folder-is-for)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Folder layout](#folder-layout)
- [Quickstart](#quickstart)
- [CLI contract](#cli-contract)
- [Story Node format](#story-node-format)
  - [Story Node v3 front matter](#story-node-v3-front-matter)
  - [Required Markdown sections](#required-markdown-sections)
  - [Citation format](#citation-format)
  - [Evidence bundle](#evidence-bundle)
- [Bundling format](#bundling-format)
- [Publishing workflow](#publishing-workflow)
- [CI integration](#ci-integration)
- [Governance and sensitivity](#governance-and-sensitivity)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [References](#references)

---

## What this folder is for

KFM Story Nodes are governed narratives authored in Markdown, validated in CI, and served to the UI through the API gateway so policy and access control can be enforced consistently.:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

The story toolchain exists to ensure Story Nodes:
- follow the **v3 template** and **front matter schema**
- include **citations for factual claims**
- reference only **resolvable evidence**
- remain safe to publish (sensitivity-aware, fail-closed)

---

## Non-negotiable invariants

These invariants are enforced by the validator and must remain true across all future work.

### Evidence-first

- Story Nodes **require citations** for factual claims and are **validated in CI**.:contentReference[oaicite:5]{index=5}
- Citations must resolve to evidence endpoints (doc/stac/dcat/prov/graph).:contentReference[oaicite:6]{index=6}

### Trust membrane compliance

- The frontend must not talk to databases directly.
- Policy evaluation occurs on every data/story/AI request.
- Backend logic uses repository interfaces and cannot bypass them.:contentReference[oaicite:7]{index=7}

> [!NOTE]
> Story tooling **must not** encourage workflows where the UI fetches raw story files directly from storage bypassing the API/policy boundary. If a local preview exists, it should remain a **developer-only** tool.

### Fail-closed

- CI must fail if required story sections are missing or if citations are missing/unresolvable.:contentReference[oaicite:8]{index=8}

---

## Folder layout

This README documents the **intended** structure for `tools/story`. If your repository layout differs, update this section and keep the invariants the same.

```text
tools/
└── story/
    ├── README.md                 # you are here
    ├── schemas/                  # governed JSON Schemas for story artifacts
    │   ├── story_front_matter_v3.json
    │   ├── story_bundle.schema.json
    │   └── citation.schema.json
    ├── rules/                    # deterministic validator rule inputs
    │   ├── banned_patterns.yml
    │   ├── allowed_citation_kinds.yml
    │   └── required_sections.yml
    ├── src/                      # implementation (language-agnostic)
    │   ├── validate.*            # parse+validate story nodes
    │   ├── bundle.*              # build StoryNodeBundle JSON
    │   ├── resolve.*             # resolve evidence refs (API or local catalogs)
    │   ├── index.*               # build story index + checksums
    │   └── export.*              # exports with embedded citation lists
    ├── fixtures/
    │   └── example.story.v3.md    # canonical test story for regression
    └── tests/
        ├── test_story_validator.*
        ├── test_citation_resolution.*
        └── test_bundle_determinism.*
```

> [!NOTE]
> The blueprint explicitly calls out a “verification step” to confirm the canonical v3 template path and schema in the repo and implement validators against that canonical file. Keep this README aligned with whatever is actually canonical in your repo.

---

## Quickstart

### 1) Author a Story Node in the governed location

Story Nodes are expected to live under governed documentation paths (commonly under `docs/…`). One documented convention is:

```text
docs/reports/story_nodes/
  ├── draft/
  ├── review/
  └── published/
```

(If your repo uses a different root such as `docs/stories/`, keep it consistent and update this README.):contentReference[oaicite:11]{index=11}

### 2) Validate locally

Run the story validator before opening a PR. CI will run the same checks and fail-closed if issues exist.:contentReference[oaicite:13]{index=13}

```bash
# Example CLI name. If your repo uses a different entrypoint, map it in the next section.
kfm-story validate docs/reports/story_nodes/draft/my_story.md
```

### 3) Resolve citations and links

```bash
kfm-story resolve docs/reports/story_nodes/draft/my_story.md \
  --evidence-base-url http://localhost:8000
kfm-story link-check docs/reports/story_nodes/draft/my_story.md
```

---

## CLI contract

This section defines the **expected interface** for story tooling. The implementation may be Python/Node/Go/etc., but the contract should remain stable so CI and contributors have a predictable workflow.

> [!TIP]
> If you already have an entrypoint (Make/NPM/Justfile), document the mapping here, for example:
> - `make story-validate` → `kfm-story validate`
> - `npm run story:validate` → `kfm-story validate`

### Commands

| Command | Purpose | Must be deterministic | Must fail-closed |
|---|---:|---:|---:|
| `kfm-story validate <paths…>` | Validate v3 template, schema, sections, citation usage | ✅ | ✅ |
| `kfm-story resolve <paths…>` | Resolve evidence refs against evidence endpoints or local catalogs | ✅ | ✅ |
| `kfm-story bundle <story.md>` | Build `StoryNodeBundle` JSON for API/UI | ✅ | ✅ |
| `kfm-story index <rootDir>` | Build story index + checksums + provenance refs | ✅ | ✅ |
| `kfm-story preview <story.md>` | Local preview of story playback (developer-only) | ✅ | ✅ |
| `kfm-story export <story.md>` | Export story with embedded citation list | ✅ | ✅ |

### Common flags

| Flag | Meaning |
|---|---|
| `--format json|text` | Output format (validation reports should support JSON) |
| `--report <path>` | Write machine-readable report to disk |
| `--evidence-base-url <url>` | API base URL for evidence resolution |
| `--offline` | Resolve using local catalogs only (no network) |
| `--strict` | Enable all checks; CI should use strict |

---

## Story Node format

Story Nodes follow a strict template and are validated in CI. Required sections include an overview and titled steps; factual statements require citations.

### Story Node v3 front matter

The Story Node v3 front matter schema requires at minimum:

- `story_id`, `title`, `template_version`, `status`
- `template_version` must be `"v3"` and `status` must be `draft|review|published`

Minimal example (aligned with the documented skeleton):

```yaml
---
story_id: "kfm.story.example.black_sunday.v1"
title: "Black Sunday and the Dust Bowl"
summary: "A short, cited narrative linking map states and evidence."
template_version: "v3"
status: "draft"
tags: ["dust-bowl", "kansas", "1930s"]
time_range: ["1935-04-01", "1935-04-30"]
bbox: [-102.05, 36.99, -94.59, 40.00]
evidence_bundle:
  stac: ["stac://…"]
  dcat: ["dcat://…"]
  prov: ["prov://…"]
  graph: ["graph://…"]
---
```

### Required Markdown sections

The documented skeleton defines the following canonical structure:

- `# Overview`
- `# Step 1: <title>` … (repeat for as many steps as needed)
- `# Evidence & Citations`

Validator expectations (minimum):
- Template version declared; required front matter keys present
- Overview exists
- Each step has a title and body text
- Citations exist and resolve
- Links are valid; banned patterns are absent

### Citation format

KFM uses Markdown footnotes to attach structured citations. The documented skeleton example is:

```md
Text… [^c1]

# Evidence & Citations
[^c1]: kind=prov ref="prov://…" locator="…" note="…"
```

Validator expectations:
- Every citation **must define** at least:
  - `kind` in `{dcat, stac, prov, doc, graph}`
  - `ref` matching the corresponding scheme (`dcat://…`, `stac://…`, etc.)
- Every `ref` must be resolvable via evidence endpoints (or local offline catalogs).:contentReference[oaicite:22]{index=22}

### Evidence bundle

The front matter can include an `evidence_bundle` listing relevant evidence URIs across STAC/DCAT/PROV/graph. This is part of the documented v3 skeleton and schema.

---

## Bundling format

The API contract defines a `StoryNodeBundle` with:

- `story_id`, `title`, `body_markdown`
- `steps[]` (each step includes `step_id`, `title`, `text_markdown`, and optional `view_state_patch`)
- `citations[]`
- `evidence_bundle`

A bundle build should be **deterministic**:
- identical inputs → identical JSON output bytes (canonical formatting), so checksums remain stable
- step IDs should be derived deterministically (recommended: slugged headings + ordering)

Example output shape:

```json
{
  "story_id": "kfm.story.example.black_sunday.v1",
  "title": "Black Sunday and the Dust Bowl",
  "body_markdown": "# Overview\n...\n",
  "steps": [
    {
      "step_id": "step-1-black-sunday",
      "title": "Black Sunday",
      "text_markdown": "Text…",
      "view_state_patch": {
        "bbox": [-102.05, 36.99, -94.59, 40.00],
        "time_range": ["1935-04-14", "1935-04-14"],
        "active_layers": ["kfm.layer.dust_storms.v1"]
      }
    }
  ],
  "citations": [
    {
      "id": "c1",
      "kind": "prov",
      "ref": "prov://…",
      "locator": "page=12",
      "note": "Lineage for dataset X"
    }
  ],
  "evidence_bundle": {
    "prov": ["prov://…"]
  }
}
```

---

## Publishing workflow

The documented workflow is:

1) Author creates story under template v3 referencing stable dataset/layer IDs  
2) Automated validator checks required sections, citations, disallowed content  
3) Peer review approves; governance review triggered as needed  
4) Publish step creates/updates story bundle index with checksums and provenance references:contentReference[oaicite:26]{index=26}

> [!IMPORTANT]
> Publishing is not a “copy file” operation. It is a governed promotion step that should record:
> - checksums
> - provenance references
> - any redaction/generalization decisions (if applicable)

### Suggested publish outputs

A typical publish step should produce:

- `story_bundle_index.json`  
  - list of story IDs
  - `sha256` checksums for each bundle
  - provenance refs (if tracked)
- `StoryNodeBundle` JSON artifacts (or a deterministic build from Markdown at runtime)

---

## CI integration

Minimum CI hardening includes:
- Docs: lint + link-check + template validator  
- Stories: v3 validator + citation resolution  
- Data: STAC/DCAT/PROV validation + checksums  
- Policy: OPA tests  
…and is intended to fail-closed.

Also, the governed documentation protocol expects markdown lint and link/reference checks for docs content.:contentReference[oaicite:28]{index=28}

### Example GitHub Actions job

```yaml
name: story-governance

on:
  pull_request:
    paths:
      - "docs/**"
      - "tools/story/**"
      - "policy/**"

jobs:
  story:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate Story Nodes
        run: |
          kfm-story validate docs/reports/story_nodes --strict --format json --report story.validation.json

      - name: Resolve citations
        run: |
          kfm-story resolve docs/reports/story_nodes --strict --format json --report story.resolve.json

      - name: Link check docs
        run: |
          kfm-story link-check docs/reports/story_nodes --strict
```

---

## Governance and sensitivity

KFM governance includes FAIR/CARE and explicit sensitivity handling. If content contains sensitive locations or culturally restricted knowledge, publish a generalized derivative for general audiences and store precise data under restricted access, with separate provenance chains documenting the transformation/redaction step.:contentReference[oaicite:29]{index=29}

> [!WARNING]
> Story Nodes must not disclose restricted coordinates or culturally restricted site details in public stories.
> If unsure, mark the story as `review` and route through governance review.

---

## Troubleshooting

### “Missing required sections”

- Ensure the file includes:
  - `# Overview`
  - at least one `# Step N: …`
  - `# Evidence & Citations`

### “Front matter schema invalid”

- Confirm `template_version: "v3"`
- Confirm `status` is one of `draft`, `review`, `published`
- Confirm required keys exist: `story_id`, `title`, `template_version`, `status`

### “Citation ref does not resolve”

- Ensure `kind` is one of: `dcat|stac|prov|doc|graph`
- Ensure `ref` uses a matching scheme (e.g., `prov://…`)
- If running online resolution, ensure the evidence resolver endpoint exists and is reachable.

The API blueprint proposes evidence resolver endpoints so every citation ref can be fetched and displayed:​:contentReference[oaicite:31]{index=31}

- `GET /api/v1/evidence/dcat/{id}`
- `GET /api/v1/evidence/stac/{id}`
- `GET /api/v1/evidence/prov/{id}`
- `GET /api/v1/evidence/doc/{id}?page=...&span=...`
- `GET /api/v1/evidence/graph/{id}`

---

## Contributing

### Definition of done for story tool changes

- [ ] Validator remains deterministic and fail-closed
- [ ] Schema changes update:
  - [ ] `schemas/story_front_matter_v3.json`
  - [ ] fixtures and regression tests
  - [ ] CI job expectations
- [ ] New rules include:
  - [ ] documented rationale
  - [ ] example failing fixture
  - [ ] example passing fixture
- [ ] No tooling bypasses the trust membrane:
  - [ ] no direct DB access patterns introduced
  - [ ] resolution uses API and/or governed local catalogs:contentReference[oaicite:32]{index=32}

---

## References

- KFM Next-Gen Blueprint:
  - Story Node publishing workflow and requirements:contentReference[oaicite:33]{index=33}
  - v3 Story Node template skeleton
  - Story front matter v3 schema excerpt
  - StoryNodeBundle schema excerpt
- Markdown governance conventions:
  - Story nodes folder conventions and doc checks:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}

