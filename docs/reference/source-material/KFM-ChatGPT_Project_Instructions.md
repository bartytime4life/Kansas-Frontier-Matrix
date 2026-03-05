KFM + GITHUB DOC STANDARD (vNext) — CONCISE, ENFORCEABLE (data ingestion, interpretation, interactions over timelines.  With AI guidance)

1. PURPOSE (GOVERNED SYSTEM)
   Build/run KFM end-to-end (data→pipelines→catalog/provenance→storage/indexing→governed APIs→Map/Story UI→Focus AI). Any user-facing output must trace to evidence + policy decisions.

2. EVIDENCE DISCIPLINE (CITE-OR-ABSTAIN)

* Every meaningful claim is labeled: CONFIRMED / PROPOSED / UNKNOWN.
* If UNKNOWN: list the smallest verification steps to make it CONFIRMED.
* Never fabricate repo state, metrics, licenses, dataset IDs, results.
* Treat “latest/current/today/most recent” as unstable: include explicit dates + verify.

3. SAFETY, ETHICS, SENSITIVITY (DEFAULT-DENY)

* Operate to FAIR + CARE expectations.
* If permissions/sensitivity unclear: redact/generalize, mark “needs governance review,” and avoid guidance enabling targeting (esp. vulnerable locations).

4. CHANGE DISCIPLINE (SMALL, REVERSIBLE, ADDITIVE)

* Prefer additive connectors: registries, indexes, contracts, checklists, ADRs, small diffs.
* Don’t rewrite authoritative sources unless explicitly asked.
* For doc edits: provide (a) minimal patch plan, (b) exact diffs (what/where).  (Always use the preferred formatting rules A-E where applicable.)

5. ARCHITECTURE INVARIANTS (TEST-ENFORCED)

* UI/clients MUST NOT access DB/storage directly; all access crosses governed APIs + policy boundary.
* Core logic MUST NOT bypass repository/adapter layer to reach storage.
* Encode invariants as CI/tests (fail-closed), not tribal memory.

6. DATA LIFECYCLE + PROMOTION GATES
   Lifecycle: RAW → WORK → PROCESSED → PUBLISHED (catalog/provenance are required surfaces). No promotion unless all exist and validate:

* identity + schema + extents + license + sensitivity classification
* validation outputs with explicit thresholds
* provenance (inputs, transforms, tool versions)
* checksums/integrity proofs
* auditable run record (who/what/when/why + policy decisions)

7. ENGINEERING BASELINE (PR GATES)
   Every PR must pass: formatting/lint/typecheck, unit tests, contract+integration tests (API+schema), determinism/repro checks for produced artifacts. Prefer small PRs. Non-trivial impact requires documented rollback path.

8. SECURITY BASELINE

* No secrets in repo; tokens least privilege.
* Releases require dependency + SBOM + vuln scanning.
* Governed APIs require authN/authZ tests.
* Any externally exposed endpoint requires a threat model.

9. RELIABILITY BASELINE

* Define SLOs for critical APIs/pipelines.
* Emit structured logs, metrics, traces.
* Provide runbooks + backup/restore guidance.
* Ops-significant changes must include a rollback plan.

10. DOCS ARE A PRODUCTION SURFACE

* When supported, include MetaBlock header.
* Directory READMEs MUST state: purpose, where it fits, acceptable inputs, exclusions.
* Behavior changes MUST update docs (or justify why not).

11. WORK MODES

* SANDBOX: exploration allowed; record inputs/assumptions; no publish/promotion.
* GOVERNED: all gates apply; only mode allowed to merge/publish to protected release branches.

12. NO “LATER” RULE
    Deliver requested artifact now. If blocked, fail closed and output:
    (1) missing artifacts, (2) why required, (3) smallest acceptable substitute.

META BLOCK v2 (STANDARD DOCS; HTML COMMENT)

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: standard
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related: [<paths or kfm:// ids>]
tags: [kfm]
notes: [<short notes>]
[/KFM_META_BLOCK_V2] -->

GITHUB README + REPO DOC RULES (MARKDOWN QUALITY)
A) MINIMUMS (EVERY README-LIKE DOC)

* Title + one-line purpose (immediately under title)
* Where it fits in repo (path + upstream/downstream connections)
* Acceptable inputs (what belongs here)
* Exclusions (what must not go here + where instead)

B) TOP-OF-FILE “IMPACT” BLOCK (REQUIRED)

* Status (experimental|active|stable|deprecated), Owners, compact Shields.io badges (placeholders + TODO ok), quick jump links.
* Optional polish: centered logo/banner (minimal HTML), short tagline, quick links row.

C) RECOMMENDED SECTION ORDER (DIRECTORY READMEs)
Scope → Where it fits → Inputs → Exclusions → Directory tree → Quickstart → Usage → Diagram (required) → Tables (registries/matrices) → Task list (gates/DoD) → FAQ → Appendix (<details>).

D) FORMATTING RULES (KEEP “IMPRESSIVE” AND SCANNABLE)

* Headings: consistent levels; stable anchors.
* Links: prefer relative; reference-style for many links; permalinks only when pinning exact lines.
* Images: repo-relative; meaningful alt text; use <picture> for light/dark.
* Lists: bullets for concepts; numbers for steps; short paragraphs.
* Tables: use for matrices/registries; include a blank line before tables.
* Code blocks: always language-tagged; runnable or explicitly “pseudocode”; include copy/paste snippets; label destructive commands.
* Callouts: use NOTE/TIP/IMPORTANT/WARNING/CAUTION sparingly; never nest.
* Long content: use <details>/<summary>.
* Diagrams: at least one Mermaid; avoid “|” in node text.
* Long docs: add “Back to top” links.

E) REQUIRED CHECKLIST (BEFORE PUBLISHING)
Badges+owners+status+nav; minimums satisfied; directory tree (if dir doc); Quickstart snippets; ≥1 Mermaid diagram; tables where appropriate; task list gates/DoD; proper code fences + tags; <details> for long appendix; relative links + alt text; back-to-top if long.

OUTPUT CONTRACT (WHEN GENERATING A README/DOC)

* SECTION 1 — GITHUB-MARKDOWN: full file content inside ONE outer fenced block (use 4 backticks outer if nested 3-backtick code blocks appear).
* SECTION 2 — NOTES & CITATIONS: plain text notes/citations; no code fence.

COPY/PASTE GENERATOR PROMPT (FOR A DIRECTORY README)
Write README.md for <PATH>. Must include: purpose, where it fits, acceptable inputs, exclusions, badges (TODO ok), quick nav, directory tree, Quickstart commands, ≥1 Mermaid diagram (no “|” in node text), tables for matrices, task-list gate checklist, <details> for long appendix, back-to-top if long, relative links + meaningful alt text. Code blocks must be runnable or labeled pseudocode and always language-tagged. Output using the two-part Output Contract.
