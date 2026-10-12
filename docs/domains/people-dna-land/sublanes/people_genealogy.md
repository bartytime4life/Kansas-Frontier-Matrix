<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr/sublanes-docs-convention
title: ADR-NNNN — Domain sublane documentation convention (docs/domains/<domain>/sublanes/)
type: adr
version: v1
status: proposed
owners: <docs steward — TODO>, <People/DNA/Land domain steward — TODO>, <architecture reviewer — TODO>
created: 2026-06-06
updated: 2026-06-06
policy_label: public
related:
  # NEEDS VERIFICATION — paths PROPOSED until checked against a mounted repo
  - directory-rules.md
  - ai-build-operating-contract.md
  - docs/domains/people-dna-land/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
notes:
  # CONTRACT_VERSION = "3.0.0"
  # ADR number is UNRESOLVED. Use NNNN until docs/adr/ is enumerated. Slots into Atlas §24.12 backlog as ADR-S-16 (PROPOSED).
  # Resolves OQ-PEOPLE-SUB-01 (convention), -02 (sublane count/names), -13 (filename form), -14 (land duplicate), -15 (sibling scheme).
  # ADR-light: documentation-only; creates NO parallel schema/policy/test/data authority home (§2.4 not triggered on those grounds).
[/KFM_META_BLOCK_V2] -->

# ADR-NNNN — Domain sublane documentation convention (`docs/domains/<domain>/sublanes/`)

## Status

**Proposed.**

> [!NOTE]
> **The ADR number is UNRESOLVED.** `ADR-0001` (schema home) is the only ADR CONFIRMED accepted in the corpus; `ADR-0002`/`ADR-0003` are PROPOSED/unverified, and `docs/adr/` has not been enumerated against a mounted repo. This document uses `ADR-NNNN`; assign the next free integer at merge. In the Atlas §24.12 Open-ADR backlog it slots as a new entry, suggested **ADR-S-16** (PROPOSED). [DIRRULES §18.c; deep-research-report ADR index]

> [!IMPORTANT]
> **Authority class — ADR-light.** This is a *documentation-placement* decision under `docs/`. It does **not** add, remove, or rename a canonical root; does **not** change the schema-home rule; does **not** split or merge a lifecycle phase; and does **not** create a parallel authority home for schemas, contracts, policy, sources, registries, releases, proofs, or receipts. Directory Rules §2.4 triggers (1)–(6) are therefore **not** met on those grounds. Like OPEN-DR-02 (runbook subfolders) and OPEN-DR-04 (standards casing), this is the kind of convention that a per-root README or a one-line ADR may freeze. It is filed as a full ADR only because five separate sublane docs already depend on the unresolved convention and contradict one another in print, which makes a single recorded decision the cheapest way to stop the drift. [DIRRULES §2.4, §6.1.b, §18.b]

---

## Context

An active People/DNA/Land documentation sprint authored five sublane documents under a proposed `docs/domains/people-dna-land/sublanes/` segment. The segment is **not** described in Directory Rules §12, and the docs that depend on it have diverged into mutually inconsistent structural forms. The conflict is now visible in print across multiple files:

| Concern | Variants now in the tree | Open question |
|---|---|---|
| Does `sublanes/` exist as a sanctioned segment? | Used by all five docs; not in DIRRULES §12. | OQ-PEOPLE-SUB-01 |
| How many sublanes, and their names? | 2-axis (`people_genealogy` + `dna`); 3-axis (`people`/`dna`/`land`); 4-axis (adding `genealogy`). | OQ-PEOPLE-SUB-02 |
| Flat vs subfolder filename form? | `people.md` (flat) and `people/README.md` (subfolder); `land.md`, `land_ownership.md`. | OQ-PEOPLE-SUB-13 |
| Duplicate land docs. | `land.md` and `land_ownership.md` cover the same slice. | OQ-PEOPLE-SUB-14 |
| Duplicate people docs / sibling scheme. | `people.md`, `people/README.md`, and a proposed merged `people_genealogy.md`. | OQ-PEOPLE-SUB-15 |

Two further facts frame the decision:

1. **There is a direct precedent.** Directory Rules §6.1.b and §18 OPEN-DR-02 already resolve the *same shape* of question for runbooks — `docs/runbooks/<domain>/` (Pattern A, subfolder) vs `docs/runbooks/<domain>_<topic>.md` (Pattern B, flat) — recommending **Pattern A** pending an ADR, on the grounds that the subfolder scales better as artifacts-per-domain accumulate. This ADR should not invent a new framing; it should extend that precedent to `docs/domains/<domain>/`. [DIRRULES §6.1.b, §18 OPEN-DR-02]

2. **The bounded context is singular.** Atlas Ch. 16 (`[DOM-PEOPLE]`) defines People/Genealogy/DNA/Land as **one** bounded context that owns a single object-family spine (Person Assertion, Genealogy Relationship, FamilyGroup, LifeEvent, Residence/Migration Event, DNA Match Evidence, DNASegment, Land Ownership Assertion, Deed/Title Instrument, Assessor Record, TaxRecord, Parcel Version, Ownership Interval, …). There is **no** doctrinal sub-partition of that spine. "Sublanes" are therefore a *documentation-navigation* device, not new bounded contexts — which constrains how far the convention may go (it may organize prose; it may not fork authority). [Atlas Ch. 16 §B/§E; DDD Reference — one model per bounded context]

The status quo is the §2.5 conflict state: paths are `PROPOSED / CONFLICTED`, and the standing instruction is to *not create divergent siblings* until resolved. Five divergent siblings now exist. This ADR exists to close that.

---

## Decision

This ADR makes four linked decisions and one cleanup.

### D1 — Ratify `sublanes/` as a documentation-only segment

`docs/domains/<domain>/sublanes/` is **accepted** as a sanctioned navigation segment under the human-facing control plane, for domains large enough to warrant intra-domain decomposition of prose. It is a `docs/`-only device. It **MUST NOT** be mirrored into any other responsibility root: schemas, contracts, policy, tests, fixtures, pipelines, data, and release artifacts continue to use the **whole-domain** slug (`schemas/contracts/v1/domains/people-dna-land/`, `policy/domains/people-dna-land/`, etc.) with **no** sublane segment. This preserves §12 and the §2.4(5) no-parallel-home rule. [DIRRULES §3, §12]

> A domain SHOULD only adopt `sublanes/` when it has genuinely separable documentation axes (as People/DNA/Land does); small domains keep flat `docs/domains/<domain>/*.md`.

### D2 — Filename form: subfolder + `README.md` (Pattern A), mirroring OPEN-DR-02

Each sublane is a folder containing a `README.md`:

```text
docs/domains/people-dna-land/sublanes/
├── README.md            # sublanes index
├── people/README.md
├── dna/README.md
└── land/README.md
```

This matches the runbook Pattern A recommendation (OPEN-DR-02) and scales as a sublane accumulates companion docs (e.g., a sublane-specific runbook pointer or worked-example file) without producing long flat filenames. Flat `sublanes/<x>.md` and underscore forms (`land_ownership.md`, `people_genealogy.md`) are **rejected** for this segment. [DIRRULES §6.1.b]

### D3 — Sublane set: three (`people`, `dna`, `land`); genealogy folds into `people`

The People/DNA/Land domain is decomposed into **exactly three** documentation sublanes:

- **`people/`** — Person Assertion, PersonCanonical, NameAssertion, Person Identity Candidate, LifeEvent, Residence Event, Migration Event, **and** the genealogy object families (Genealogy Relationship, FamilyGroup, Relationship Hypothesis). Identity resolution and relationship modeling both live here, because both operate on the person spine and share the same evidence and review surfaces.
- **`dna/`** — DNA Match Evidence, DNASegment, DNAKitToken, consent, redaction, restricted access.
- **`land/`** — Land Ownership Assertion, Deed/Title Instrument, Assessor Record, TaxRecord, Parcel Version, Ownership Interval, LandParcel, chain-of-title.

The **2-axis** scheme (`people_genealogy` + `dna`, with land absent) and the **4-axis** scheme (standalone `genealogy/`) are **rejected**. Rationale: the domain name lists genealogy, but the *object families* give genealogy no separable spine from people — splitting them forces an artificial `people ↔ genealogy` identity/relationship boundary that the doctrine does not draw, while merging keeps the natural seam at `dna` (restricted) and `land` (title/parcel) where the doctrine *does* draw hard rules. Three sublanes match the three places the domain's deny-default and anti-collapse rules actually bite. [Atlas Ch. 16 §B/§E/§I; UNIFIED §10.14]

### D4 — Cross-root naming stays whole-domain

No `…/people-dna-land/people/`, `…/people-dna-land/dna/`, or `…/people-dna-land/land/` sub-segments are created in `schemas/`, `contracts/`, `policy/`, `tests/`, `fixtures/`, or `data/`. Validators, schemas, and policy that need to distinguish sublane concerns do so by **object family** or **file naming inside the whole-domain lane**, not by a directory sub-segment. [DIRRULES §12, §2.4(5)]

### D5 — Retire the duplicates and divergent forms

The following drafts are **superseded** by the canonical three-folder set and MUST be retired (kept only as redirects or deleted, with a DRIFT_REGISTER entry recording the supersession):

| Retired draft | Superseded by | Disposition |
|---|---|---|
| `sublanes/people.md` (flat) | `sublanes/people/README.md` | merge content, delete flat file |
| `sublanes/land.md` (flat) | `sublanes/land/README.md` | rename to subfolder form |
| `sublanes/land_ownership.md` | `sublanes/land/README.md` | merge content into `land/README.md`, delete |
| `sublanes/genealogy/README.md` (standalone) | `sublanes/people/README.md` | fold genealogy content into `people/README.md`, delete folder |
| `sublanes/people_genealogy.md` (proposed, not yet created) | — | do not create |

The DNA draft (`sublanes/dna/README.md`) is already in canonical form and is retained as-is.

---

## Evidence basis

- **DIRRULES §3** (the deeper rule — domains live as lanes inside responsibility roots, not as roots), **§6.1.b** (runbook subfolder placement contract; Pattern A/B), **§12** (Domain Placement Law — `people-dna-land` is a named slug; per-domain artifacts live under responsibility roots with a domain segment), **§2.4** (ADR-required triggers; none met on parallel-home grounds), **§2.5** (conflict procedure — PROPOSED/CONFLICTED, no divergent siblings), **§18 OPEN-DR-02 / OPEN-DR-04** (precedent for documentation-convention freezes). CONFIRMED in attached `directory-rules.md`.
- **Atlas Ch. 16 `[DOM-PEOPLE]` §B/§E/§I** — single bounded context; object-family spine with no sub-partition; living-person/DNA deny-default; assessor/tax-not-title and parcel-not-boundary hard rules. CONFIRMED.
- **UNIFIED §10.14** — People/genealogy/DNA/land coverage; land ownership as temporal evidence-bound assertion. CONFIRMED.
- **Operating contract §28 / `.github/ISSUE_TEMPLATE/adr.md`** — ADR skeleton this document follows; §2.4 trigger list. CONFIRMED.
- **DDD Reference** — one model per bounded context; sublanes-as-navigation is consistent with keeping a single model. CONFIRMED (general principle).
- **No mounted repo, CI, workflow, or runtime evidence was inspected.** Every repo path here is PROPOSED / NEEDS VERIFICATION.

---

## Directory Rules basis

This decision is anchored in **§3** (responsibility-rooted structure), **§6.1** (`docs/` is the human-facing control plane that *explains*), **§6.1.b** (the runbook-subfolder precedent it mirrors), and **§12** (Domain Placement Law). It explicitly does **not** invoke §2.4(1)–(6): no canonical root changes, no schema-home change, no lifecycle-phase change, **no parallel authority home** (D1/D4 forbid exactly that). The convention is confined to the layer §6.1 reserves for explanation.

---

## Consequences

**Positive**

- Closes OQ-PEOPLE-SUB-01/02/13/14/15 in one recorded decision; ends the §2.5 conflict state for this tree.
- One unambiguous form (`sublanes/<x>/README.md`) for authors to follow; matches the runbook precedent, so the two `docs/` subfolder conventions are consistent.
- Authority stays singular: no schema/policy/test forks, so the §2.4(5) and trust-membrane guarantees are untouched.
- Generalizes cleanly to other large domains (e.g., a future `docs/domains/frontier-matrix/sublanes/`).

**Negative / costs**

- Requires a small migration: four drafts retired/merged (D5), with DRIFT_REGISTER entries and link-fixups across the surviving docs.
- Folding genealogy into `people/` makes `people/README.md` larger; mitigated by clear intra-doc sectioning.
- If a future need for a genuinely separate genealogy bounded context emerges, this ADR would need superseding — but that would be a doctrine change at the Atlas level, not just a docs move.

**Neutral**

- Back-to-top anchors and relative-link depths in the surviving docs must be re-verified after the rename (subfolder depth differs from flat).

---

## Alternatives considered

1. **Flat files, no `sublanes/` (`docs/domains/people-dna-land/people.md`, …).** Simpler; avoids the segment question entirely. Rejected because it does not scale once a sublane needs companion docs, and it contradicts the OPEN-DR-02 Pattern A direction the project already leans toward. Still the right choice for *small* domains.
2. **Flat files *inside* `sublanes/` (`sublanes/people.md`).** The form several drafts used. Rejected per D2 for the same scaling reason OPEN-DR-02 rejects flat runbooks.
3. **4-axis split (standalone `genealogy/`).** Matches the domain's name most literally. Rejected per D3: no separable object-family spine; forces an artificial people↔genealogy boundary.
4. **2-axis split (`people_genealogy/` + `dna/`, land elsewhere).** Rejected: drops `land` from the domain's own decomposition even though the domain owns the land spine and its hardest anti-collapse rules.
5. **Mirror `sublanes/` into schemas/policy/tests.** Rejected outright: this *is* the §2.4(5) parallel-home anti-pattern and would fork authority.

---

## Validation

- [ ] `docs/domains/people-dna-land/sublanes/` contains exactly `README.md`, `people/README.md`, `dna/README.md`, `land/README.md` after migration.
- [ ] No `sublanes/*.md` flat files, no `land_ownership.md`, no `people_genealogy.md`, no `genealogy/` folder remain.
- [ ] No `…/people-dna-land/<sublane>/` sub-segment exists under `schemas/`, `contracts/`, `policy/`, `tests/`, `fixtures/`, `data/`, or `release/` (whole-domain lanes only).
- [ ] DRIFT_REGISTER carries a supersession entry for each retired draft (D5).
- [ ] Surviving docs' relative links and back-to-top anchors resolve at the new subfolder depth.
- [ ] A `docs/domains/<domain>/sublanes/README.md` per-root note states the convention for future authors.
- [ ] Atlas §24.12 backlog updated with this ADR's assigned number (suggested ADR-S-16).

## Rollback

This is a documentation move; rollback is restoring the retired files from version control and reverting the DRIFT_REGISTER entries. No data, schema, policy, or release artifact is touched, so there is no lifecycle or trust-membrane state to unwind. If the three-sublane decision (D3) proves wrong, supersede this ADR with a new one rather than silently re-splitting.

## Open questions

- **Assigned ADR number** — pending `docs/adr/` enumeration (carries the broader OQ-KFM-01 ADR-inventory question).
- **Does `genealogy` ever need its own bounded context?** If genealogical reasoning grows a spine distinct from the person spine (e.g., a separate relationship-graph store with its own release surface), revisit D3 at the Atlas level.
- **Per-root README vs ADR for future convention freezes** — this ADR sets the precedent that a `docs/`-only convention *can* be ADR-frozen; whether future ones use a per-root README instead (cheaper, per OPEN-DR-04) is left to the docs steward.
- **Mounted-repo verification** — every path remains NEEDS VERIFICATION until the repo is inspected.

---

**Last updated:** 2026-06-06 · **Doc id:** `kfm://doc/adr/sublanes-docs-convention` · **Status:** proposed · `CONTRACT_VERSION = "3.0.0"`
