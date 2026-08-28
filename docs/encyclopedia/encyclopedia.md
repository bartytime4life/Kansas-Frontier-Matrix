<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia-assembled-mirror
title: KFM Encyclopedia — Reserved Assembly Target
type: generated-target-placeholder
version: v0.1
status: proposed; placeholder; generated-target-hold; non-authoritative; no-publication
owners:
  - "@bartytime4life via the current CODEOWNERS review route"
created: 2026-05-15
updated: 2026-08-14
policy_label: public; planning-reference
owning_root: docs/
responsibility: >-
  Reserve the potential whole-manuscript assembly path while preventing hand-authored
  content or placeholder presence from becoming a competing encyclopedia source.
generated_from: PROPOSED docs/encyclopedia/chapters/ ordered by INDEX.md
generator: UNKNOWN
placement_outcome: HOLD
related:
  - README.md
  - INDEX.md
  - CHANGELOG.md
  - ../KFM-encyclopedia.md
  - ../doctrine/encyclopedia.md
  - ../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md
tags: [kfm, encyclopedia, generated, placeholder, hold]
notes:
  - "Do not hand-edit this path into a manuscript. ADR-0036 is proposed and no deterministic assembler is established."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Encyclopedia — Reserved Assembly Target

> [!IMPORTANT]
> **No assembled manuscript is established at this path.** Read the current planning index at [`docs/KFM-encyclopedia.md`](../KFM-encyclopedia.md), the scaffold inventory in [`INDEX.md`](./INDEX.md), and the lane boundary in [`README.md`](./README.md).

Proposed [`ADR-0036`](../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md) would make this file a deterministic, read-only assembly generated from the ordered structural chapter source.

Until that decision is accepted and a repository-owned assembler, manifest, tests, and drift checks exist:

- do not add manuscript prose here;
- do not treat this file as canonical;
- do not generate or copy source-PDF text into it;
- do not claim chapter completeness, release, or publication;
- preserve this explicit `HOLD` state.

[Back to top](#top)
