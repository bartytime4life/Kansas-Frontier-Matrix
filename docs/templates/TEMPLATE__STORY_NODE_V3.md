<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://story/<uuid>@v1
title: <Story title>
type: story
version: v3
status: draft|review|published
owners: <names/teams>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<dataset_version_id>
tags:
  - kfm
  - story-node
notes:
  - "Template: docs/templates/TEMPLATE__STORY_NODE_V3.md"
[/KFM_META_BLOCK_V2] -->

<!--
AUTHORING NOTES
- Story Nodes bind narrative to map state and citations; a Story Node has a markdown file + a sidecar JSON file.
- Publishing gate: all citations must resolve through /api/v1/evidence/resolve.
- Evidence discipline: label each claim as CONFIRMED / PROPOSED / UNKNOWN and include citations (CITE-OR-ABSTAIN).
-->

# <Story title>

## Summary

<Short summary of the story, including scope and time window.>

- **Time window:** <YYYY-MM-DD> → <YYYY-MM-DD>
- **Geography:** <place name / bbox / admin area>
- **Primary dataset(s):** kfm://dataset/<slug>@<dataset_version_id>

## Claims

1. **[CONFIRMED]** <Claim text.> [CITATION: doc://...]
2. **[PROPOSED]** <Claim text.> [CITATION: stac://...]
3. **[UNKNOWN]** <Claim text.> [CITATION: TBD]  
   _Verification steps_: <Smallest concrete steps to make this claim CONFIRMED.>

## Narrative

<Full narrative with inline citations.>

## Evidence

- [CITATION: dcat://...]
- [CITATION: prov://...]

<details>
<summary>Sidecar JSON template (map state + citations)</summary>

> Save this JSON as a separate “sidecar” file associated with this Story Node.

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
    "layers": [
      { "layer_id": "<layer_id>", "dataset_version_id": "<dataset_version_id>" }
    ],
    "time_window": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }
  },
  "citations": [
    { "ref": "dcat://<dataset_slug>@<dataset_version_id>", "kind": "dcat" },
    { "ref": "prov://run/<run_id>", "kind": "prov" }
  ]
}
```

</details>

<!--
AUTHOR CHECKLIST (delete this block when done)
- [ ] Replace all <placeholders>.
- [ ] Claims are labeled (CONFIRMED / PROPOSED / UNKNOWN) and each has at least one citation.
- [ ] Sidecar JSON story_id + version_id match the Story Node doc_id.
- [ ] All citations resolve via /api/v1/evidence/resolve (fail-closed).
-->
