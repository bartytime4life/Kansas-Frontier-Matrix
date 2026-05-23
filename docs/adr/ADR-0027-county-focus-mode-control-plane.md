# ADR-0027 — County Focus Mode Control Plane

> **Status:** PROPOSED · **Last reviewed:** 2026-05-22 · **Owners:** `<OWNER:focus-mode-steward>`, `<OWNER:directory-rules-steward>`
>
> **ADR number is `0027`.** Several corpus documents informally reserve `ADR-0003` for different topics; the user has flagged this conflict separately. Assign the next available ID from `docs/adr/`.

---

## Status

PROPOSED — not yet accepted. This ADR ratifies the county Focus Mode control plane as a governed subsystem of `docs/focus-modes/` and resolves the singular/plural naming question.

---

## Context

Eleven county Focus Mode Build Plans are in `status: draft` per `directory-rules.md` v1.2 §0 (CONFIRMED), and ≥30 (the actual enumeration shows 34) are in the corpus per `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` Appendix C (CONFIRMED corpus presence, dated 2026-05-21). Without a control plane the work is becoming a growing collection of Markdown files: there is no master index, no standardized metadata, no validator, and no documented bridge from a county plan to a `FocusModePayload`.

Three specific problems motivate this ADR:

1. **No navigability.** New collaborators cannot tell which counties are in flight, planned, or untouched. Duplicate selection is possible (no lookup gate).
2. **No standard metadata.** Each county build plan can drift in shape, making cross-county reasoning and validation impossible.
3. **No payload bridge.** The doctrine repeatedly states "a Focus Mode is not a publication target by itself" (`directory-rules.md` §6.7; `kfm_repository_structure_guiding_document.md` §8.3), but no document anywhere in the corpus declares the **path** by which a county plan becomes a governed UI payload. The slice can become an indefinite-residence Markdown collection by default.

Compounding these: the user's prompt references `docs/focus-mode/` (singular hyphen), while `directory-rules.md` v1.2 §6.7.2 specifies `docs/focus-modes/` (plural hyphen) as canonical and §13.5 lists singular variants as drift candidates. The live-repo state of these folders is **NEEDS VERIFICATION**.

---

## Decision

Establish a six-artifact control plane that gates further per-county work:

1. `docs/focus-modes/README.md` — lane doctrine, the lifecycle (`not-started → planned → draft → validated → payload-ready → released → rolled-back/deprecated`), the add-a-county procedure, and the per-area required-file set.
2. `docs/focus-modes/COUNTY_INDEX.md` — the master index of all 105 Kansas counties with status, lane path, owner, priority, sensitivity hot lanes, and validation state.
3. `docs/focus-modes/_template/county-build-plan.md` — the standardized template, including a YAML front-matter spec that the validator parses.
4. `tools/validators/validate_focus_mode_index.py` — a lightweight, stdlib-only Python validator that runs twelve checks (parsing, 105-county presence, no duplicates, lane folder presence, required-file presence, front-matter shape, ui-shell correctness, no schema-home violation, no `apps/web/` drift, lane naming, acceptance items, link resolution).
5. `contracts/focus_mode/focus_mode_payload.md` — the semantic contract that crosswalks a county plan into a `FocusModePayload`, gates the finite outcome envelope (`ANSWER | ABSTAIN | DENY | ERROR`), and lists required companion objects.
6. This ADR.

Resolve the singular/plural naming question:

- **Canonical name is `docs/focus-modes/` (plural, hyphen).** This matches `directory-rules.md` v1.2 §6.7.2 and the rest of the corpus's cross-host-root placement table.
- If the live tree contains `docs/focus-mode/` (singular), it is **drift** and must be migrated to `docs/focus-modes/` under this ADR. Migration is a structural move per `directory-rules.md` §2.4 and `ai-build-operating-contract.md` §28; the migration script lives at `migrations/<date>-focus-mode-singular-to-plural.py` (PROPOSED) with `git_sha_before`/`git_sha_after`.

Out-of-scope of this ADR (deferred):

- The machine schema `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` is **PROPOSED** by this ADR but not authored in this PR. Emission belongs to a follow-up PR (PR-1b) with its own ADR-cited Directory-Rules-basis.
- Per-county `policy/sensitivity/<area>/` override files. Authored only when a county justifies a default override; deny-fixture required.

---

## Evidence basis

CONFIRMED:

- `directory-rules.md` v1.2 §6.7 (Focus Modes placement contract); §6.7.2 (per-host-root casing); §6.7.6 (four-PR sequence); §13.5 (drift register); §15 (README contract); §2.4 (ADR triggers).
- `kfm_repository_structure_guiding_document.md` §8 (Focus Mode placement contract); §8.4 (recommended first-PR sequence); §8.5 (eleven counties in flight); §3 (root-stays-boring).
- `kfm_unified_doctrine_synthesis.md` Part III (cite-or-abstain); Part V (finite outcome envelope); Part VI (promotion gates A–G); Part VII (publication/sensitivity); Part XI (validator worked example).
- `ai-build-operating-contract.md` §10 (AI is interpretive); §26 (governed loop); §27 (PR discipline); §28 (ADR triggers); §29 (object-family guardrails).
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3 COUNTY-01..04; Appendix C county Build Plan index (≥30 corpus presence).

PROPOSED: every file path emitted by this ADR. No live repo was mounted in the authoring session, so every path is `PROPOSED` pending verification. The first run of `validate_focus_mode_index.py` against the live tree will produce a verification snapshot.

---

## Directory Rules basis

| Artifact | Host root | Casing | Authority cited |
|---|---|---|---|
| `docs/focus-modes/README.md` | `docs/` | kebab-case plural | §6.1, §6.7, §15 |
| `docs/focus-modes/COUNTY_INDEX.md` | `docs/` | kebab-case plural; SCREAMING_SNAKE for the index file matches existing register conventions (e.g., `docs/registers/DRIFT_REGISTER.md`) | §6.1, §6.7.2 |
| `docs/focus-modes/_template/county-build-plan.md` | `docs/` | `_template/` leading-underscore is **PROPOSED**; alternative is `template/` without underscore. Decided here: leading underscore signals "not a county lane; do not consume from validators." | §6.7.2 |
| `tools/validators/validate_focus_mode_index.py` | `tools/` | flat naming under `tools/validators/`; orchestrated by `tools/validate_all.py` | §7.5, §7.5.a |
| `contracts/focus_mode/focus_mode_payload.md` | `contracts/` | singular snake_case for the focus-mode family; matches `contracts/{source,evidence,…}/` | §6.3, §6.7.2 |
| `docs/adr/ADR-0027-county-focus-mode-control-plane.md` | `docs/adr/` | ADR naming convention | §6.1, §2.4 |

---

## Consequences

**Positive:**

- The county subsystem becomes navigable in O(1) (the index) instead of O(N) (grep the corpus).
- Duplicate county claims are caught before merge.
- Build plans must declare their front-matter; non-conforming plans fail validation.
- The plan-to-payload bridge has a citable contract.
- The validator becomes a single discoverable artifact (`tools/validators/validate_focus_mode_index.py`) orchestrated by the canonical `tools/validate_all.py`.

**Negative / cost:**

- Existing markdowns under `docs/focus-mode/` (if any) must be migrated.
- Existing 34 corpus draft plans must be normalized to the front-matter spec; un-normalized plans fail validation.
- Adding a new scope suffix beyond `-county`/`-region`/`-corridor` now requires an ADR.

**Reversibility:** Removing the six artifacts and the validator returns the repo to pre-control-plane state. No lifecycle data is touched. No published payloads exist yet to roll back.

---

## Alternatives considered

1. **Do nothing; keep producing per-county build plans.** Rejected: the user explicitly asked for the control plane before more plans, and the doctrine warns against "a Focus Mode … remaining only a document."
2. **Put everything in `contracts/focus_mode/` and let `docs/focus-modes/` be human-facing only.** Rejected: planning and acceptance documents are not contracts; they are control-plane carriers. They must remain in `docs/` per §6.3 boundary.
3. **Use the singular `docs/focus-mode/` to match the user's prompt phrasing.** Rejected: contradicts `directory-rules.md` v1.2 §6.7.2 canonical pattern and the rest of the corpus's cross-host-root placement table.
4. **Make the validator require a third-party YAML parser (PyYAML).** Rejected: makes CI bootstrap brittle. The stdlib-only validator handles 90% of cases; deep YAML parsing is a follow-up validator if needed (ADR-class).
5. **Emit per-county schema files at `schemas/contracts/v1/focus_mode/<area>/`.** Rejected: violates schema-home convention (ADR-0001) — schemas are area-agnostic; per-area variation is a payload-instance concern, not a schema concern.

---

## Validation

The control plane is itself validatable:

- `python tools/validators/validate_focus_mode_index.py docs/focus-modes/` runs the twelve checks.
- `python tools/validators/validate_focus_mode_index.py docs/focus-modes/ --emit-json artifacts/focus_mode_index.json` produces a machine-readable validation snapshot.
- Exit codes: `0` = all pass, `1` = at least one check failed, `2` = system error.
- CI MUST invoke via `tools/validate_all.py` (per `directory-rules.md` §7.5.a; OPEN-DR-07).

The plan-to-payload contract is validated indirectly via the schema and the per-area validators listed in `contracts/focus_mode/focus_mode_payload.md` §3 (most of those validators are PROPOSED follow-ups).

---

## Rollback

1. Delete the six artifacts (`docs/focus-modes/README.md`, `docs/focus-modes/COUNTY_INDEX.md`, `docs/focus-modes/_template/`, `tools/validators/validate_focus_mode_index.py`, `contracts/focus_mode/focus_mode_payload.md`, this ADR).
2. If a migration from `docs/focus-mode/` to `docs/focus-modes/` was performed, reverse it via the migration script's `--rollback` flag.
3. Remove the validator entry from `tools/validators/registry.yaml`.
4. No `git_sha_after` artifacts to invalidate; no released payloads to rescind.

---

## Open questions

| ID | Question | Action |
|---|---|---|
| OPEN-FM-01 | Live state of `docs/focus-mode/` (singular) vs `docs/focus-modes/` (plural) | Inspect; if singular present, run migration. |
| OPEN-FM-02 | Reconciliation of `eleven` (Directory Rules v1.2 §0) vs `≥30` (MapLibre v2.1 Appendix C) county counts | Resolved in COUNTY_INDEX.md by using the larger Appendix C set and marking the eleven as P1 priority. |
| OPEN-FM-03 (OPEN-DR-06) | Existing build plans referencing `apps/web/src/focus-modes/` | Revise on next plan iteration; validator catches new instances. |
| OPEN-FM-04 (OPEN-DR-07) | `tools/validate_all.py` (live) vs `tools/validators/validate_all.py` (doctrine) | This ADR keeps live path; separate ADR for permanent reconciliation. |
| OPEN-FM-05 | Existing `contracts/focus_mode/focus_mode_payload.md` and `schemas/contracts/v1/focus_mode/focus_mode_payload.schema.json` — do they exist in the live repo? | Verify; emit absent artifacts in PR-1b. |
| OPEN-FM-06 | ADR-S-05 sensitivity tier scheme (T0–T4) status | This ADR references but does not author; separate ADR pending. |
| OPEN-FM-07 | `ai_permitted_templates[]` field PROPOSED in front-matter; mirror in payload contract | Resolve in PR-1b alongside the AI Focus Mode template registry. |
| OPEN-FM-08 | ADR number assignment (corpus has informal `ADR-0003` reservations for several topics) | Assign next free number from live `docs/adr/` directory. |

---

## Cross-references

- `docs/focus-modes/README.md`
- `docs/focus-modes/COUNTY_INDEX.md`
- `docs/focus-modes/_template/county-build-plan.md`
- `tools/validators/validate_focus_mode_index.py`
- `contracts/focus_mode/focus_mode_payload.md`
- `directory-rules.md` v1.2 §6.7
- `kfm_repository_structure_guiding_document.md` §8
- `kfm_unified_doctrine_synthesis.md` Parts III, V, VI, VII, XI
- `ai-build-operating-contract.md` §§10, 26, 28, 29
- `Master_MapLibre_Components-Functions-Features_v2_1_FULL.md` §16.3, Appendix C
