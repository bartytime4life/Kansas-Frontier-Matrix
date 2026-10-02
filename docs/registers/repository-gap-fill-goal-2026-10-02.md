<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://register/repository-gap-fill-goal-2026-10-02
title: KFM Repository Gap-Fill Goal — 2026-10-02
type: goal-and-procedure-ledger
version: v1.0
status: draft; repository-grounded; non-authoritative
owner: "NEEDS VERIFICATION — review routes through current CODEOWNERS (@bartytime4life)"
created: 2026-10-02
updated: 2026-10-02
policy_label: repository-facing
owning_root: docs/
responsibility: "State a measurable goal for closing repository gaps, record the gaps observed in a full-tree audit, define repeatable fill procedures, and point each gap at its existing machine projection or validator without creating source, policy, lifecycle, release, or publication authority."
truth_posture: "CONFIRMED local command results, file presence, parse results, link census, and scaffold/backlog counts on the evidence snapshot / PROPOSED goal targets, procedure order, and gap dispositions / UNKNOWN hosted workflow results for the snapshot / NEEDS VERIFICATION steward decisions on every HOLD named below"
evidence_snapshot: "main@6c12d36c57beb0a4162ee65e43b40283ab458de2; audit Python 3.13 (outside the CI matrix of 3.11 and 3.12); hosted workflow results UNKNOWN because the GitHub API was not reachable from the audit session"
related:
  - docs/registers/README.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
  - control_plane/verification_backlog.yaml
  - tools/qa/README.md
  - tools/qa/gap_scan.py
  - tools/qa/scaffold_inventory.py
  - tools/qa/completion_queue.py
  - docs/doctrine/README.md
  - docs/doctrine/directory-rules.md
notes:
  - "This ledger adds one census helper (tools/qa/gap_scan.py) and fixes defects with direct evidence; it does not resolve any DOC-DOC conflict, ADR status, or steward HOLD."
  - "Counts are snapshot facts. Re-run the commands in the Procedures section before citing them later."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Repository Gap-Fill Goal — 2026-10-02

> [!IMPORTANT]
> **Goal.** Every gap in the repository is either *filled with tested behavior*, *held with a named reason and owner*, or *retired* — and no class of gap can grow without a failing check.
>
> This ledger is a review aid. It records what the audit saw and how to close it. It does not approve, admit, release, or publish anything.

---

## 1. Definition of done

The goal is met when all of these hold on `main`. Targets marked PROPOSED need steward agreement.

| ID | Measure | Command | Snapshot | Target |
|---|---|---|---|---|
| `DOD-01` | Structured data parse errors outside negative fixtures | `python tools/qa/gap_scan.py --check` | 2 → **0** (fixed here) | 0, enforced |
| `DOD-02` | `tests/` packages shadowing an imported root | `python tools/qa/gap_scan.py --check` | 1 → **0** (fixed here) | 0, enforced |
| `DOD-03` | Broken local Markdown links (excluding `docs/archive/`) | `python tools/qa/gap_scan.py` | 466 → **456** | PROPOSED: < 100, then 0 |
| `DOD-04` | Placeholders outside scaffold surfaces | `python tools/qa/gap_scan.py` | 10 | PROPOSED: 0 (moved onto a ratchet or retired) |
| `DOD-05` | Scaffold findings | `make scaffold-inventory` | 925 findings, 732 files | Ratchets down only |
| `DOD-06` | Backlog entries still `NOT_INSPECTED` | `python tools/qa/completion_queue.py --check` | 732 of 747 | PROPOSED: all P1 (95) inspected first |
| `DOD-07` | Make targets failing for code reasons (HOLD exits excluded) | Section 4.1 battery | 1 → **0** on Python 3.13 with the geo profile | 0 on every supported Python |
| `DOD-08` | Full-suite collection errors with the `all-local-test` and `water-pilot` profiles installed | `python -m pytest --co -q tests` | 9 → **4** | 0, or each error mapped to a named installer |

[Back to top](#top)

---

## 2. Fixes applied with this ledger

Each fix has direct evidence and a one-commit rollback.

| Gap | Change | Evidence before | Evidence after |
|---|---|---|---|
| `G-TEST-01` | Removed empty `tests/pipelines/__init__.py` | With pytest's default `prepend` import mode, `tests/pipelines` became a top-level package named `pipelines` and hid the real `pipelines/` namespace. Collecting `tests/pipelines` with hydrology water tests raised `ModuleNotFoundError: pipelines.domains.hydrology.normalize` | With the same installed profiles, `pytest --co tests` collects 7,889 tests instead of 7,810 and collection errors drop from 9 to 4 |
| `G-TEST-02` | `test_no_network_proof.py` skips the IPv6 `connect` case only when the host cannot create an `AF_INET6` socket | `OSError: [Errno 97] Address family not supported` happened at socket creation, before the guarded `connect`, so `make offline-pipeline-check` failed for a host reason, not a guard defect | `198 passed, 2 skipped`; the IPv4 `connect` case still proves the guard |
| `G-DATA-01` | `fixtures/domains/fauna/valid/{range_polygon,seasonal_range}.geojson` rewritten as parseable, empty `FeatureCollection` slots that declare `kfm:placeholder` | Both files held one `#` comment line under a `.geojson` name in a `valid/` folder: not JSON | Valid GeoJSON with no features or coordinates; still reported as `UNRATCHETED_PLACEHOLDER` until a reviewed fixture replaces it |
| `G-DOC-01a` | 3 broken links in `docs/atlases/` repointed to `docs/atlas/master-api-surface.md`; across the three atlas files, 9 quick-jump anchors corrected to the existing heading slugs and 8 links to absent ADRs and to `decision-outcome-envelope.md` made plain text marked "(not present)"; the three files' related lists keep every resolving entry, redirect renamed targets, and drop entries that resolve to nothing | The target had moved from `docs/atlases/` to `docs/atlas/`. The audit found 32 more repoints (flat `schemas/contracts/v1/*.schema.json` → family subfolders, wrong `../` depth), but they are held under `G-DOC-04` | 466 → 456 broken links |
| `G-QA-01` | Added `tools/qa/gap_scan.py`, `tools/qa/gap_scan_baseline.json`, `tests/qa/test_gap_scan.py`, `make gap-scan`, and `.github/workflows/gap-scan.yml` | No check covered parse errors in fixtures, test-package shadowing, broken links repo-wide, or placeholders outside scaffold surfaces | Run against the unfixed `main`, the scan fails on all three defect classes above; on this branch it passes |

Deliberately **not** changed, because the repository already records them as held decisions:

- Links to `docs/doctrine/corrections-are-first-class.md` (`DOC-DOC-003`, 54 references) — the doctrine README says not to mass-rewrite without identity review.
- Links to root `ai-build-operating-contract.md` (`DOC-DOC-002`, 19 references) — the in-repo `docs/doctrine/` copy has a conflicting identity, so repointing would imply authority.
- Links to `docs/doctrine/trust-posture.md` (`DOC-DOC-004`, 24 references) — no intended target may be inferred.
- Source-specific `IDENTITY.md` / `RIGHTS-AND-SENSITIVITY-MAP.md` links under `docs/sources/catalog/{ahgp,blm}/` — the catalog-level files are different documents.

[Back to top](#top)

---

## 3. Gap register

`Status` uses the repository truth labels. `Disposition` is PROPOSED unless marked FIXED.

| ID | Gap | Evidence (snapshot) | Status | Disposition | Owner route |
|---|---|---|---|---|---|
| `G-TEST-01` | Test package shadowed `pipelines/` | Section 2 | CONFIRMED | FIXED | tests/ |
| `G-TEST-02` | IPv6 guard test depended on host kernel | Section 2 | CONFIRMED | FIXED | tests/ + CI steward |
| `G-DATA-01` | Unparseable fauna `valid/` fixtures | Section 2 | CONFIRMED | FIXED (slot remains placeholder) | Fauna steward |
| `G-DOC-01` | 456 broken local links to 214 distinct targets | `gap_scan.py`: 283 into `docs/`, 86 into `apps/` (retired Explorer Web), 19 to root contract, 21 into `schemas/` | CONFIRMED | Procedure P-03 | Docs steward |
| `G-DOC-02` | Doctrine filename conflicts drive 97 of the broken links | `DOC-DOC-002/003/004` in `docs/doctrine/README.md` | CONFIRMED | Needs steward naming decision, then a scripted rewrite (P-03 step 4) | Doctrine steward |
| `G-DOC-03` | Retired `apps/explorer-web` still linked from ADR-0004, ADR-0007, and domain feature READMEs | 86 references | CONFIRMED | Point at the live Site source or mark as historical; ADRs need append-only notes, not rewrites | Docs + ADR steward |
| `G-DOC-04` | Link repairs blocked by pre-existing metadata defects | The diff-scoped docs checks (`check_links.py`, `check_meta_blocks.py`, `check_document_graph.py`) fail any changed document whose metadata block is invalid or whose other links are broken. The audit's 32 held repoints are in `docs/doctrine/{ai-as-assistant,map-first,trust-membrane,truth-posture}.md` (invalid `doc_id` or missing fields; `truth-posture.md` is byte-identical to `trust-membrane.md`), `docs/domains/habitat/PRESERVATION_MATRIX.md` and `docs/sources/catalog/manual_curation/README.md` (missing fields; remaining broken links), and `docs/sources/catalog/usfws_ecos/{README,critical-habitat}.md` (shared `doc_id`) | CONFIRMED | Repair each document's metadata, then apply the held repoints | Document owners |
| `G-ENV-01` | `requires-python = ">=3.11"` is unbounded, but CI locks cover 3.11 and 3.12 only | `install_python_ci.py geo-transforms` fails on 3.13 with a hash mismatch: no `cp313` wheel hashes in `tools/ci/python-geo.lock` | CONFIRMED | Choose: cap `requires-python` at `<3.13`, or add 3.13 to the CI matrix and its wheel hashes | CI steward |
| `G-ENV-02` | No single documented profile installs everything the full suite imports | 4 collection errors remain after `all-local-test` + `water-pilot`: three `tests/packages/kfm_cli` modules need `tools/ci/install_kfm_cli.py`; `tests/release/test_geoparquet_2_rc_pyarrow_carriers.py` needs the `geoparquet-pyarrow-25` profile | CONFIRMED | Add a `full-local-test` profile or document the profile per test folder | CI steward |
| `G-SITE-01` | Site mirror receipt drift on `main` | `python tools/qa/site_mirror.py --check` → `MIRROR_FILE_SET_DRIFT`: 6 unrecorded mirror paths, 15 changed files. `water-pilot.yml` runs this step | CONFIRMED locally; hosted result UNKNOWN | Reviewed mirror receipt refresh; do not regenerate unreviewed | Site/source owner |
| `G-PLACE-01` | Three PROPOSED-scaffold `.rego` files at the `release/` root | `release/{hydrology_publication,public_safe_geometry,source_role_anti_collapse}.rego` — policy source outside `policy/`, and outside the scaffold ratchet | CONFIRMED | Migrate under `policy/` or retire, via migration note per Directory Rules §9.3 | Policy steward |
| `G-SCAF-01` | Scaffold backlog is uninspected | 747 backlog entries: 732 `NOT_INSPECTED`, 15 `PARTIAL`; priorities P1 95 / P2 513 / P3 139; by root: `schemas` 387, `policy` 112, `tests` 89 | CONFIRMED | Procedure P-05 | Owning-root stewards |
| `G-SCAF-02` | Placeholders outside scaffold surfaces | 10 files: `CITATION.cff`, `artifacts/build/env/tool-versions.yaml`, `artifacts/qa/lint/mypy.txt`, 2 fauna fixtures, `infra/compose/docker-compose.yml`, 3 `release/*.rego`, `runtime/model_adapters/OllamaAdapter.py` | CONFIRMED | Now counted by `gap_scan.py`; fill or retire each | Root owners |
| `G-DOM-01` | Two domain lanes are documentation-only | `planetary-3d` and `spatial-foundation`: one file under `docs/domains/`, nothing under `schemas/`, `contracts/`, `policy/`, `pipelines/`, `packages/`, `tests/`, or `fixtures/` | CONFIRMED | Decide: real lane (scaffold through P-06) or fold into existing lanes | Domain steward |
| `G-ADR-01` | Most ADRs remain proposed | `docs/adr/INDEX.md`: 5 accepted, 38 proposed | CONFIRMED | Prioritise ADRs that block P1 backlog entries | ADR steward |
| `G-POL-01` | Policy readiness lane cannot run without OPA | `make policy` → HOLD `OPA_BINARY_UNAVAILABLE` in the audit environment | CONFIRMED locally | Document the OPA install for local runs; hosted lane UNKNOWN | Policy steward |

### 3.1 Domain coverage snapshot

Tracked files per domain under each owning root, and scaffold-baseline findings whose path names the domain.

| Domain | docs | schemas | contracts | policy | pipelines | packages | tests | fixtures | scaffold |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agriculture | 31 | 27 | 11 | 6 | 8 | 5 | 30 | 38 | 47 |
| archaeology | 35 | 41 | 32 | 18 | 7 | 10 | 18 | 46 | 71 |
| atmosphere | 32 | 74 | 44 | 14 | 6 | 5 | 29 | 110 | 96 |
| fauna | 29 | 37 | 21 | 8 | 2 | 9 | 30 | 40 | 62 |
| flora | 35 | 41 | 38 | 24 | 11 | 16 | 32 | 102 | 74 |
| geology | 43 | 43 | 30 | 16 | 7 | 10 | 23 | 62 | 44 |
| habitat | 47 | 40 | 29 | 29 | 6 | 5 | 35 | 57 | 66 |
| hazards | 26 | 25 | 10 | 10 | 8 | 6 | 29 | 67 | 58 |
| hydrology | 32 | 47 | 37 | 9 | 27 | 5 | 28 | 118 | 49 |
| people-dna-land | 42 | 24 | 12 | 14 | 3 | 6 | 27 | 46 | 20 |
| planetary-3d | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| roads-rail-trade | 38 | 21 | 31 | 17 | 18 | 11 | 23 | 40 | 85 |
| settlements-infrastructure | 24 | 20 | 17 | 6 | 2 | 5 | 11 | 25 | 33 |
| soil | 23 | 39 | 28 | 7 | 14 | 5 | 11 | 134 | 27 |
| spatial-foundation | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

File counts show presence, not maturity. A domain with many files and a high scaffold count (atmosphere, roads-rail-trade, flora, archaeology) has the most placeholder surface to inspect.

[Back to top](#top)

---

## 4. Fill procedures

Run these in order. Each ends with a command whose result can be cited.

### 4.1 P-01 — Establish a clean local baseline

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py all-local-test
python tools/ci/install_python_ci.py water-pilot
python tools/ci/install_python_ci.py geo-transforms   # Python 3.11/3.12 only (G-ENV-01)
git fetch --unshallow 2>/dev/null || true             # baseline validators read pinned commits
for t in scaffold-inventory gap-scan deny-suites offline-pipeline-check local-data-check \
         schemas test validator-full repository-guardrails trust-spine-baseline \
         program-baseline control-plane-registry-packet trust-spine-fixture-slice \
         ci-conformance-report repository-governance-parity release-dry-run publish-check \
         evidence-resolver deny-test governed-api-smoke boundary-guards hazards-validate \
         normalized-summary-check docs-critical-structure; do
  make "$t" >/dev/null 2>&1; echo "$? $t"
done
```

Run targets one at a time. Parallel runs leave `__pycache__` files that make `release-dry-run` fail its clean-tree check. Exit `3` is a named HOLD (`policy`, `fixtures`, `catalog`, `ui-build`, `native-explorer-check`) and is not a failure or a pass.

### 4.2 P-02 — Keep invariant classes at zero

`make gap-scan` and the `gap-scan` workflow fail on any parse error outside negative fixtures and on any `tests/<root>/__init__.py` that shadows an imported root. Negative fixtures live under `invalid/`, `malformed/`, `negative/`, `bad/`, or `broken/` folders, or carry one of those words in the file stem.

### 4.3 P-03 — Burn down broken links

1. `python tools/qa/gap_scan.py --list` and group findings by `detail` (the missing target).
2. **Moved target** — the file exists under one unambiguous new path, or the link has the wrong `../` depth: repoint it.
3. **Retired target** (`apps/explorer-web`): point at the current Site source or mark the sentence historical. In accepted ADRs, add an append-only note instead of editing the decision text.
4. **Held identity** (`DOC-DOC-002/003/004`): wait for the steward's naming decision, then rewrite every reference in one scripted commit.
5. **Planned target** (for example `docs/architecture/release-and-publication.md`, `docs/runbooks/RB-ROLLBACK-EXECUTION.md`): write the document, or change the link to plain text marked PROPOSED.
6. `python tools/qa/gap_scan.py --write-baseline` so the count can only fall.

### 4.4 P-04 — Retire stray placeholders

For each `UNRATCHETED_PLACEHOLDER`: implement it, move it to the owning root with a migration note (Directory Rules), or delete it. Then tighten the baseline.

### 4.5 P-05 — Work the scaffold backlog by priority

1. `python tools/qa/completion_queue.py --check` must stay `PASS`.
2. Take P1 entries first (95; hydrology, governed API, catalog, release, policy runtime, evidence resolver, workers).
3. For each entry: inspect the consumer, then implement with a changed-area test, make it fail closed with a named HOLD, or retire it.
4. `python tools/qa/scaffold_inventory.py --write-baseline` once markers are gone, so the ratchet tightens.

### 4.6 P-06 — Bring a domain lane to minimum coverage

A lane is at minimum coverage when it has, under the owning roots from Directory Rules: a domain README, at least one schema and contract pair, a deny-by-default policy with a test, one synthetic valid and one invalid fixture, and a test that runs both. Apply to `planetary-3d` and `spatial-foundation` only after `G-DOM-01` is decided.

### 4.7 P-07 — Close environment gaps

Decide `G-ENV-01` (supported Python range) and `G-ENV-02` (full-suite profile). Then the full suite should collect with zero errors:

```bash
python -m pytest --co -q -p no:cacheprovider tests apps/governed-api/tests
```

[Back to top](#top)

---

## 5. Open questions

| ID | Question | Blocks |
|---|---|---|
| `OQ-GAP-01` | Is Python 3.13 supported? If not, should `requires-python` say `<3.13`? | `G-ENV-01`, `DOD-07` |
| `OQ-GAP-02` | Should a `full-local-test` install profile exist, or is per-folder profiling the contract? | `G-ENV-02`, `DOD-08` |
| `OQ-GAP-03` | Who reviews the Site mirror receipt refresh, and is the `water-pilot` workflow currently red on `main`? | `G-SITE-01` |
| `OQ-GAP-04` | Do `release/*.rego` scaffolds move under `policy/`, or are they retired? | `G-PLACE-01` |
| `OQ-GAP-05` | Are `planetary-3d` and `spatial-foundation` full domain lanes? | `G-DOM-01` |
| `OQ-GAP-06` | What is the target date for the `DOC-DOC-002/003/004` naming decisions? | `G-DOC-02`, `DOD-03` |

---

## 6. Verification backlog

- NEEDS VERIFICATION: hosted results for the `gap-scan` workflow on the branch carrying this ledger.
- NEEDS VERIFICATION: hosted `water-pilot` result on `main` at the snapshot commit (`G-SITE-01`).
- NEEDS VERIFICATION: `make offline-pipeline-check` on a GitHub-hosted runner, where IPv6 sockets are expected to exist and the skipped case should run.
- OBSERVED: a full `pytest -n 8 tests` run (7,886 passed, 3 skipped) had one failure, `test_validate_repository_governance_parity::test_current_profile_passes_without_claiming_conformance` (`LANE_OUTCOME_MISMATCH`), which passes when run alone and under `make repository-governance-parity`. The parity check reads working-tree state that other tests write concurrently, so it is not safe under `pytest-xdist`. No repository workflow runs the suite in parallel today.

## 7. Rollback

Revert the commit that adds this ledger. That restores `tests/pipelines/__init__.py`, the original fauna placeholder bytes, the 3 atlas link targets and related lists, and removes the gap scan, its baseline, test, make target, and workflow. No receipts, registers, ADRs, or release records are touched.

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-02 | First audit snapshot, five fixes, gap scan, and procedures P-01 to P-07. |

[Back to top](#top)
