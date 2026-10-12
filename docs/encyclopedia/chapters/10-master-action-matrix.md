<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/10-master-action-matrix
title: "Master action matrix"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain master action matrix and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Master action matrix

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

Actions that look adjacent in the UI can have very different effects. Use this matrix to plan work and to state exactly what completed.

| Action | Preconditions | Output | Completion evidence |
|---|---|---|---|
| Inspect a source | Product identity and question | Metadata and suitability notes | Source page or pinned repository descriptor |
| Preview acquisition | Explicit selection, bounds and destination | Transfer/storage plan | Plan result including unknown lengths and limits |
| Capture originals | Valid plan and permitted local store | Bytes, manifest and receipt | Capture result plus verification |
| Render context | Supported source/configuration and access | Map or chart | Source labels, coverage state and actual render |
| Save a view/draft | Chosen area, time and content | Local or application draft | Readback and known persistence scope |
| Validate candidate | Contract/profile and fixture/tool scope | Findings | Exact command, inputs and exit/result |
| Submit PR | Isolated reviewed diff | Proposed repository change | PR URL and exact head |
| Merge | Required repository review/checks | Main-branch change | GitHub merge state and commit |
| Deploy | Exact saved source/artifact and audience | Hosted version | Sites deployment result |
| Admit or release source | Required rights, sensitivity, policy and human decisions | Governed lifecycle transition | The owning decision and release records |

## Operator sequence

Start with inspection and planning. Use bounded reads to resolve source identity, current inventory and storage effects. Carry out only the chosen action. Read its result before deciding whether another step is warranted. Do not silently turn a metadata lookup into a bulk transfer or a display into a release.

For local capture, the [local-PC runbook](../../runbooks/local-pc-data-store.md) distinguishes `plan`, `sync` and `verify`. For repository changes, the [PR reliability guide](../../runbooks/pr-reliability-guide.md) explains how to attribute failures and retain review state.

## Failure reporting

Report partial work at the level that failed: selection, transfer, checksum, validation, review or publication. Preserve successful immutable captures and their receipts where the operator contract requires it. Do not describe a retry plan as a completed recovery. Include the next actionable check and any needed input.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
