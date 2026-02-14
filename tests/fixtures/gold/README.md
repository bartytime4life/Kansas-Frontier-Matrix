# Gold Test Fixtures

> 🧪 **Deterministic “golden” outputs** used by regression + contract tests.  
> 📍 Path: `tests/fixtures/gold/`  
> 🧷 Principle: **If behavior changes, the diff must be reviewable.** If the change is intended, the gold must be updated intentionally and reviewed.

---

## Table of Contents

- [What This Directory Is](#what-this-directory-is)
- [Hard Rules](#hard-rules)
- [When to Use Gold Fixtures](#when-to-use-gold-fixtures)
- [Directory Layout](#directory-layout)
- [Fixture Case Standard](#fixture-case-standard)
- [Canonicalization and Determinism Rules](#canonicalization-and-determinism-rules)
- [How to Add a New Gold Fixture](#how-to-add-a-new-gold-fixture)
- [How to Update Existing Gold](#how-to-update-existing-gold)
- [Review Checklist](#review-checklist)
- [Security, Privacy, and Sensitivity](#security-privacy-and-sensitivity)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## What This Directory Is

This folder contains **gold fixtures** (“golden files”) that represent **expected outputs** of governed, testable behaviors.

Gold fixtures are used to ensure:

- Outputs remain stable across refactors
- Contracts (schemas, catalogs, policies) do not regress
- Deterministic identity / hashing stays deterministic
- Sensitive data never leaks via formatting/serialization drift
- “Cite or abstain” behaviors remain enforceable and testable

Gold fixtures are treated as **governed artifacts**: they are not “just test data.” A change here is a change to a contract.

---

## Hard Rules

✅ **Allowed**
- Small, deterministic, reviewable fixture files
- Synthetic or redacted data only (unless explicitly permitted and documented)
- Text-first outputs (JSON/NDJSON/GeoJSON/CSV/MD) with stable formatting
- Checksums for binary or large artifacts (or when helpful for review)

🚫 **Not allowed**
- Secrets, tokens, credentials, private keys, cookies, session IDs
- Real personal data (PII) or sensitive locations (unless generalized/redacted)
- Time-dependent outputs unless time is explicitly frozen in the test harness
- Machine-specific paths (home directories), hostnames, container IDs
- Auto-updating gold in CI (gold updates must be explicit and reviewed)

🧱 **Read-only contract**
- Test code **must not write** into `tests/fixtures/gold/` during normal runs.
- Only deliberate regeneration workflows should modify gold fixtures.

---

## When to Use Gold Fixtures

Use gold fixtures when you want **high-signal regression coverage** for outputs that are:

- **Public API contracts** (OpenAPI/GraphQL schemas, example responses)
- **Catalog artifacts** (STAC/DCAT/PROV documents, manifests, receipts)
- **Policy enforcement** (OPA/Rego decisions, redaction outputs, deny reasons)
- **Evidence UX** (citation resolution shapes, locators/snippets formats)
- **Story Node validation** (template parsing, front matter validation, linting)
- **Deterministic identity** (spec hash / canonical JSON / stable IDs)
- **ETL/Normalization outputs** where ordering and formatting must remain stable

If the output is inherently nondeterministic or huge, prefer **property-based tests**, **schema validation**, or **digest-only gold** rather than storing massive blobs.

---

## Directory Layout

This repo may evolve, but **gold fixtures should remain organized by “what contract they validate.”**

Recommended layout:

~~~text
tests/fixtures/gold/
├─ README.md                                      # (This file) — what “gold” means + update/review rules
│
├─ catalogs/                                      # Golden catalog artifacts + expected validator outcomes
│  ├─ stac/
│  │  ├─ case__stac_minimal_v1/                   # Minimal valid STAC (baseline shape + required fields)
│  │  └─ case__stac_with_assets_v1/               # STAC w/ assets & links (asset rules, media-types, href norms)
│  ├─ dcat/
│  │  └─ case__dcat_dataset_minimal_v1/           # Minimal valid DCAT dataset record (baseline contract)
│  └─ prov/
│     └─ case__prov_activity_minimal_v1/          # Minimal valid PROV activity (lineage prerequisites)
│
├─ policy/                                        # Golden policy scenarios (inputs + expected decisions)
│  ├─ case__deny_missing_license_v1/              # Deny when licensing is missing/unknown (fail-closed)
│  └─ case__redact_sensitive_location_v1/         # Redaction required for sensitive locations (or deny if impossible)
│
├─ api/                                           # API contract snapshots (normalized; stable diffs)
│  ├─ openapi/
│  │  └─ case__openapi_snapshot_v1/               # OpenAPI spec snapshot (compatibility gate baseline)
│  └─ graphql/
│     └─ case__graphql_schema_snapshot_v1/        # GraphQL schema snapshot (breaking-change detection)
│
├─ story_nodes/                                   # Story Node structure + governance cases (valid/invalid)
│  ├─ valid/
│  │  └─ case__story_node_v3_minimal_v1/          # Minimal valid Story Node v3 (frontmatter + citations + assets refs)
│  └─ invalid/
│     └─ case__story_node_missing_citations_v1/   # Invalid: missing citations (should fail policy/validators)
│
├─ focus_mode/                                    # Focus Mode contract cases (shape + citation/abstain behavior)
│  └─ case__cite_or_abstain_response_shape_v1/    # Response envelope + required citation fields (or abstain reason)
│
└─ vectors/                                       # Low-level deterministic vectors (hashing, canonicalization, etc.)
   └─ case__spec_hash_vectors_v1/                 # spec_hash inputs + expected outputs (canonical baseline)
~~~

Notes:
- The `case__*` prefix keeps fixture cases visually scannable and grep-friendly.
- Use `_v1`, `_v2` suffixes when you intentionally introduce a new contract generation.

---

## Fixture Case Standard

Each fixture case should be self-describing and reviewable.

**Required contents (per case):**

~~~text
case__<slug>_<vN>/
  meta.json                 # required: description, owner, intent, invariants
  input/                    # optional: minimal inputs used to produce output
  expected/                 # required: the golden output(s)
  checksums.sha256          # required if any binary/large artifacts exist
  notes.md                  # optional: human notes, gotchas, review context
~~~

### `meta.json` contract (minimum)

`meta.json` MUST exist and SHOULD include:

- `id` (stable fixture case identifier)
- `purpose` (what contract is being tested)
- `source_kind` (synthetic | redacted | allowed-public)
- `sensitivity` (public | restricted | sensitive-location | pii-redacted)
- `generator` (what produced this output: command, tool name, version)
- `normalization` (rules applied to make it deterministic)
- `owners` (who reviews changes)

Example:

~~~json
{
  "id": "case__dcat_dataset_minimal_v1",
  "purpose": "Validate DCAT dataset shape and required fields",
  "source_kind": "synthetic",
  "sensitivity": "public",
  "generator": {
    "tool": "kfm-catalog-writer",
    "version": "0.1.0",
    "command": "kfm catalog write dcat --fixture case__dcat_dataset_minimal_v1"
  },
  "normalization": [
    "json_pretty_print",
    "sorted_keys",
    "lf_newlines",
    "timestamps_frozen"
  ],
  "owners": ["@kfm-governance", "@kfm-platform"]
}
~~~

---

## Canonicalization and Determinism Rules

Gold fixtures must be stable across machines and CI runners.

### Universal rules

- Encoding: **UTF-8**
- Line endings: **LF (`\n`)**
- Trailing newline: **required**
- No tabs in JSON/YAML; use spaces
- No current timestamps unless explicitly frozen (see below)

### JSON rules

- Prefer `.json` over YAML unless there is a strong reason
- Output must be:
  - stable key ordering (prefer sorted keys)
  - stable numeric formatting (avoid platform-dependent float stringify)
  - stable list ordering (sort by a deterministic key when possible)

If a hashing step exists in the system, canonicalize before hashing (e.g., RFC 8785-style canonical JSON).

### GeoJSON rules (if present)

- Keep geometries minimal and synthetic when possible
- Sort `features` deterministically:
  - by `id`, or
  - by `properties.<stable_key>`, then fallback to stable tuple ordering
- Avoid high-precision coordinates for sensitive domains (see sensitivity section)

### CSV / NDJSON rules

- Always include headers for CSV
- Use stable column ordering
- For NDJSON:
  - one object per line
  - stable field ordering if your tooling supports it (or convert to canonical JSON before writing)

### Freezing time and randomness

If the output includes time or random IDs, tests must freeze them. Typical approaches:

- Set environment variables like:
  - `TZ=UTC`
  - `LC_ALL=C`
  - `KFM_NOW=2026-01-01T00:00:00Z` (or equivalent)
- Use deterministic UUID seeds or fixed IDs in fixture inputs
- Strip ephemeral fields before comparing to gold (only if the field is explicitly non-contractual)

---

## How to Add a New Gold Fixture

1. Create a new case folder under the appropriate top-level category:

   - `catalogs/` for catalog outputs
   - `policy/` for policy outcomes and redaction
   - `api/` for contract snapshots
   - `story_nodes/` for Story Node parsing/linting/validation
   - `focus_mode/` for grounded response shapes
   - `vectors/` for deterministic hash/test vectors

2. Add `meta.json` describing:
   - what contract is under test
   - what is synthetic/redacted
   - how it was generated
   - what normalization rules apply
   - who owns review

3. Put the expected outputs into `expected/`.

4. If any file is binary or large:
   - store a checksum in `checksums.sha256`
   - prefer storing a small “header” representation alongside it (e.g., `schema.json`, `head.ndjson`)

5. Ensure the test:
   - reads the fixture
   - generates current output
   - normalizes output the same way
   - produces a deterministic diff if it fails

---

## How to Update Existing Gold

Gold changes must be explicit and reviewable.

1. Run the specific test(s) that failed and capture the diff.
2. Confirm whether this is:
   - **a bug fix / intended behavior change** → update gold
   - **a regression / nondeterminism** → fix code or normalization, do **not** update gold

3. Regenerate outputs in a deterministic environment:
   - fixed time (UTC)
   - fixed locale
   - pinned tool versions when relevant

4. Update:
   - files under `expected/`
   - `meta.json` (bump generator version, add explanation)
   - `checksums.sha256` (if applicable)

5. Re-run tests and ensure:
   - only intended diffs remain
   - diffs are explainable in PR description

---

## Review Checklist

Before merging changes that touch `tests/fixtures/gold/**`, verify:

- [ ] Diff is small enough to review (or uses checksum-only strategy for large artifacts)
- [ ] No secrets / tokens / credentials present
- [ ] No sensitive locations or raw PII present (or they are properly generalized/redacted)
- [ ] Determinism rules are satisfied (no timestamps, random IDs, machine paths)
- [ ] `meta.json` updated (generator, rationale, normalization)
- [ ] Tests pass locally and in CI
- [ ] The change aligns with the intended contract (API/schema/catalog/policy)

---

## Security, Privacy, and Sensitivity

Gold fixtures must be safe to store in the repo.

**Default stance:** treat fixtures as if they may be published.

Rules:
- Use **synthetic** data whenever possible.
- If using “real-shaped” data, ensure it is:
  - license-permitted,
  - redacted,
  - generalized,
  - and documented in `meta.json`.

Examples of sensitive content that must not appear in gold:
- coordinates of restricted archaeological sites
- precise locations of endangered species nests/roosts
- personal addresses, phone numbers, emails
- auth tokens, API keys, session cookies
- internal-only URLs or credentials

If you are unsure whether something is sensitive: **do not commit it**. Replace with synthetic.

---

## Troubleshooting

### “Gold mismatch” but change looks random every run
Likely nondeterminism. Common causes:
- unordered maps serialized without sorted keys
- sets/lists not sorted
- timestamps or “generated_at”
- environment-dependent formatting (locale, timezone)
- unstable floating-point formatting

Fix by:
- sorting deterministically
- freezing time
- normalizing outputs before comparison
- ensuring the test harness sets `TZ=UTC` and a stable locale

### “Gold mismatch” after a dependency upgrade
Confirm whether the dependency is part of the contract.
- If the change is acceptable and intended → regenerate gold + document version bump in `meta.json`
- If not acceptable → pin/rollback dependency or add normalization to preserve contract stability

### The diff is huge and not reviewable
Do not commit huge opaque blobs unless absolutely required.
Prefer:
- “header” fixture outputs (schema + first N rows)
- checksum-only gold for the full artifact
- property-based validation + schema checks

---

## FAQ

### Why do we use gold fixtures at all?
Gold fixtures catch regressions that are hard to express as assertions, especially for contracts and structured outputs. They provide **high-signal diffs** that reviewers can validate.

### Are gold fixtures “the truth”?
No. They are the **expected output** of the current contract. The contract can evolve, but changes must be intentional and reviewed.

### Can CI auto-update gold fixtures?
No. Auto-updating gold in CI defeats the purpose of reviewable diffs. Gold updates should always be explicit.

### Can we store raw upstream datasets here?
No. Gold is for small deterministic fixtures only. Use synthetic or redacted samples.

---

