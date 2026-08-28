<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-probes-readme
title: tools/probes README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-domain-stewards
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; diagnostic-probes; dry-run
owning_root: tools/
responsibility: parent boundary and index for diagnostic probes under tools/
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ./comid_huc12/README.md
  - ../ingest/README.md
  - ../joins/README.md
notes:
  - "This parent README documents the diagnostic-probe lane. It does not confirm probe executables."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/probes

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-diagnostic--probes-informational)
![mode](https://img.shields.io/badge/mode-dry--run-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/probes/` is the parent lane for small dry-run diagnostic probes that exercise KFM rules against fixtures, sidecars, and controlled sample inputs.

---

## Purpose

A probe is a diagnostic helper. It checks whether a rule or fixture behaves as expected before maintainers depend on that behavior in a larger governed workflow.

A probe report is a review signal. It is not acceptance of a record, join, crosswalk, catalog entry, or release artifact.

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/probes/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent probe lane | **PROPOSED / draft** | Boundary documented; executable layout remains unverified. |
| `comid_huc12/` | **CONFIRMED README / executable PROPOSED** | First documented child probe lane. |
| Probe executables | **PROPOSED-to-create / NEEDS VERIFICATION** | No script is claimed by this parent README. |

---

## Authority boundary

`tools/probes/` inherits the `tools/` root boundary. It is for diagnostic support only.

| Responsibility | Home |
|---|---|
| Diagnostic probes | `tools/probes/` |
| Repo tooling | `tools/` |
| Validators of record | `tools/validators/` or accepted validator home |
| Ingest helpers | `tools/ingest/` |
| Join helpers | `tools/joins/` |
| Connectors | `connectors/` |
| Pipelines | `pipelines/` |
| Contracts, schemas, and policy | `contracts/`, `schemas/`, `policy/` |
| Source registry | `data/registry/sources/` |
| Receipts, proofs, catalog, graph, and releases | dedicated `data/` and `release/` roots |

---

## Child lanes

| Child lane | Type | Status |
|---|---|---|
| `comid_huc12/` | Hydrology crosswalk diagnostic probe | README confirmed; executable proposed. |

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PROBE_PASS` | Fixture result matched expectation. |
| `PROBE_FAIL` | Fixture result differed from expectation. |
| `ABSTAIN` | Probe could not decide with available evidence. |
| `ERROR` | Probe could not safely complete. |

---

## Review checklist

- [ ] Probe is diagnostic only.
- [ ] Probe is deterministic.
- [ ] Probe is dry-run by default.
- [ ] Inputs and outputs are explicit.
- [ ] Missing evidence fails closed.
- [ ] Executable claims are backed by current repo evidence.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft parent README replacement for existing empty file. |
| Next smallest safe change | Add `tests/probes/README.md` and shared fixture/report conventions. |
