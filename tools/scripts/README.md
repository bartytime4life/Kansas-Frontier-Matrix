<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-scripts-readme
title: tools/scripts README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-maintainers
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; script-adapters
owning_root: tools/
responsibility: bounded script-style entrypoint and adapter lane for durable tools workflows
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../qa/README.md
  - ../release/README.md
  - ../proof_pack/README.md
  - ../validators/README.md
  - ../generators/README.md
  - ../../scripts/
  - ../../tests/
notes:
  - "This README documents a bounded tools/scripts lane, not proof that executable scripts exist."
  - "Use this path for thin durable wrappers around tools/. One-off operational helpers belong under top-level scripts/ when that root is the better fit."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/scripts

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-script--adapters-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/scripts/` is a bounded lane for durable script-style entrypoints and adapters that invoke KFM tooling in a repeatable way.

---

## Purpose

`tools/scripts/` exists for small script-shaped entrypoints that are still part of the durable `tools/` surface.

A file belongs here only when it is a stable wrapper, compatibility entrypoint, or orchestration shim around other governed tooling. It should make common tool invocations easier without hiding the authority boundaries of the underlying tool.

The durable KFM question for this lane is:

> Does this script-shaped helper provide a stable, reviewable entrypoint into existing `tools/` behavior without becoming the owner of that behavior?

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/scripts/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Script adapter executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| `tools/` root authority | **CONFIRMED in repo evidence** | Parent README defines `tools/` as durable repo-wide executable support. |
| Relationship to top-level `scripts/` | **NEEDS VERIFICATION** | Parent guidance says one-off operational helpers belong in top-level `scripts/`, not `tools/`. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Thin wrappers for durable tools workflows | `tools/scripts/` |
| Validators of record | `tools/validators/` |
| Generators | `tools/generators/` |
| QA helpers | `tools/qa/` |
| Release support helpers | `tools/release/` |
| ProofPack support helpers | `tools/proof_pack/` |
| One-off operational helpers | top-level `scripts/` when present and accepted |
| Pipeline orchestration | `pipelines/` |
| Tests | `tests/` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** stable wrappers may live here when documented and backed by tests or clear manual validation.
- **NEEDS VERIFICATION:** exact executable names, current callers, CI usage, and whether top-level `scripts/` owns a better home.

[Back to top](#top)

---

## What belongs here

- Thin wrappers around `tools/qa/` commands.
- Stable entrypoints for release dry-runs.
- Compatibility shims that call renamed tool modules.
- Small CLI launchers that delegate to `tools/validators/`, `tools/generators/`, `tools/proof_pack/`, or `tools/release/`.
- Repo-wide wrapper scripts used by CI or maintainer workflows.
- Migration wrappers with explicit deprecation notes and removal plans.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/scripts/` | Correct home |
|---|---|
| One-off developer convenience scripts | top-level `scripts/` or local-only notes |
| Validators of record | `tools/validators/` |
| Generators with durable output contracts | `tools/generators/` |
| Pipeline orchestration | `pipelines/` |
| Source fetchers | `connectors/` |
| Tests | `tests/` |

[Back to top](#top)

---

## Script adapter posture

A script adapter should do very little by itself. Prefer this pattern:

```text
parse args -> call governed tool module -> emit structured result -> exit with documented code
```

Avoid this pattern:

```text
parse args -> inline unrelated governance logic -> write authority records directly
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SCRIPT_OK` | Wrapper completed and delegated successfully. |
| `SCRIPT_WARN` | Wrapper completed with review-worthy warnings. |
| `SCRIPT_FAIL` | Wrapped tool reported failure. |
| `DELEGATE_NOT_FOUND` | Expected underlying tool or module was not found. |
| `CONFIG_MISSING` | Required non-secret configuration is absent. |
| `UNSUPPORTED_MODE` | Caller requested a mode this wrapper does not support. |
| `ABSTAIN` | Wrapper cannot decide safely with available context. |
| `ERROR` | Wrapper could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/tools/scripts/
├── README.md
├── test_script_adapters.py
└── fixtures/
```

Suggested future command pattern:

```bash
pytest -q tests/tools/scripts
```

> [!NOTE]
> This is a proposed validation surface, not proof that `tests/tools/scripts/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] The script is a stable wrapper or adapter, not a one-off helper.
- [ ] The underlying governed tool is named.
- [ ] Inputs, outputs, and exit behavior are documented.
- [ ] The wrapper avoids duplicating the underlying tool logic.
- [ ] The script is tested or manually validated.
- [ ] If temporary, the deprecation/removal path is documented.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Inventory child files, then add tests or deprecation notes for any existing adapters. |
