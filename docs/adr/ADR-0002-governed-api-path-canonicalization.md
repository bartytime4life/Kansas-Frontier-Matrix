# ADR-0002: Governed API path canonicalization (`governed_api` vs `governed-api`)

![status](https://img.shields.io/badge/status-accepted-2ea44f)
![decision-area](https://img.shields.io/badge/decision%20area-repository%20structure-1f6feb)
![boundary](https://img.shields.io/badge/boundary-governed%20API-8250df)
![policy](https://img.shields.io/badge/policy-shim--only%20legacy-b60205)

- **Status:** accepted
- **Date accepted:** 2026-04-25
- **Last updated:** 2026-04-27
- **Decision area:** repository structure / import boundaries / compatibility
- **Primary owner:** governed API maintainer
- **Applies to:** Python implementation paths under `apps/governed_api/...` and legacy file-path compatibility under `apps/governed-api/...`
- **CI guard:** `tools/ci/check_governed_api_path_policy.py`

> [!IMPORTANT]
> `apps/governed_api/...` is the canonical implementation path.
> `apps/governed-api/...` is legacy compatibility only.
> Legacy files may re-export canonical modules, but they must not contain primary implementation logic.

---

## 1. Decision summary

KFM will use `apps/governed_api/...` as the canonical governed API implementation path.

The historical hyphenated path, `apps/governed-api/...`, remains only as a compatibility surface for legacy path references, old documentation, migration notes, and narrowly scoped tooling that still expects those files to exist.

The legacy path must not become a second implementation home. Any behavior, route handler, resolver, policy bridge, runtime adapter, evidence resolver, or DTO implementation belongs in the canonical underscore path.

---

## 2. Context

The repository has used two near-identical governed API path spellings:

| Path | Role | Import posture | Status |
|---|---:|---:|---:|
| `apps/governed_api/...` | canonical implementation | Python-importable dotted package path | authoritative |
| `apps/governed-api/...` | legacy compatibility path | not a normal Python dotted import path because of the hyphen | shim-only |

This dual-path state creates maintenance risk unless one path is declared authoritative.

The risk is not cosmetic. KFM’s governed API boundary is a trust-bearing membrane between public/steward-facing clients and internal evidence, policy, release, correction, and runtime state. Duplicated API code can create divergent behavior at exactly the layer where KFM needs deterministic routing, stable envelope contracts, citation discipline, policy checks, release-state visibility, and auditable runtime outcomes.

The path decision also intersects with repo-facing documentation. Earlier planning material and UI/governed-AI implementation plans used `apps/governed-api/...` in places where later Python implementation references and runtime-proof slices used `apps/governed_api/...`. This ADR settles the file-home decision without pretending every historical reference has already been rewritten.

---

## 3. Problem statement

KFM needs exactly one governed API implementation home.

Without this ADR, contributors can accidentally:

- add new Python logic under the legacy hyphenated path;
- patch a shim while the canonical implementation remains unchanged;
- import from a path that is not a normal Python package path;
- create tests that pass against one path while runtime code uses another;
- update documentation in a way that presents the legacy path as canonical;
- weaken the governed API trust membrane by allowing two outward-response regimes to evolve.

That is unacceptable for a system whose public unit of value is an inspectable claim and whose public clients must use governed interfaces rather than internal stores or ad hoc runtime outputs.

---

## 4. Decision

1. **Canonical implementation path:** `apps/governed_api/...`
2. **Legacy compatibility path:** `apps/governed-api/...` remains shim-only.
3. **Legacy shim rule:** files under the legacy compatibility path may only re-export canonical modules or canonical symbols.
4. **No primary logic in legacy path:** no domain logic, route logic, policy logic, evidence resolution, runtime envelope construction, source access, validation, data loading, mutation, or persistence may live under `apps/governed-api/...`.
5. **CI enforcement:** `tools/ci/check_governed_api_path_policy.py` enforces the policy.
6. **New implementation work:** new governed API implementation files must be created under `apps/governed_api/...`.
7. **Documentation default:** new documentation must refer to `apps/governed_api/...` as canonical. References to `apps/governed-api/...` must be explicitly labeled as legacy compatibility.
8. **Removal requires a new decision:** deleting the legacy compatibility path requires a later ADR or ADR amendment, plus migration notes and validation evidence.

---

## 5. Scope

### 5.1 In scope

This ADR governs:

- Python implementation files under `apps/governed_api/...`;
- legacy compatibility files under `apps/governed-api/...`;
- import and re-export boundaries between those paths;
- CI policy for canonical/legacy mapping;
- documentation wording about the two paths;
- compatibility behavior for existing path references.

### 5.2 Out of scope

This ADR does not decide:

- public URL paths;
- OpenAPI route naming;
- FastAPI, Flask, or other framework selection;
- schema-home authority between `schemas/` and `contracts/`;
- runtime envelope field structure;
- app registration of specific routes;
- production deployment topology;
- whether legacy path references in all historical documents are immediately rewritten.

---

## 6. Canonical path rules

### 6.1 Canonical files

Canonical governed API implementation files live under:

```text
apps/governed_api/
```

A canonical file may contain:

- route definitions;
- runtime adapters;
- EvidenceRef-to-EvidenceBundle resolution boundaries;
- response-envelope builders;
- request/response DTO shaping;
- integration with policy and citation validation;
- tests fixtures or helper code if the repository’s app convention places them there;
- normal implementation code.

A canonical file must not import implementation logic from the legacy path.

### 6.2 Legacy files

Legacy compatibility files live under:

```text
apps/governed-api/
```

A legacy file may contain only:

- a module docstring explaining that it is a compatibility shim;
- imports from the matching canonical module;
- re-export assignments from the imported canonical module;
- `__all__` declarations when needed;
- comments.

A legacy file must not contain:

- function definitions;
- class definitions;
- route registration logic;
- runtime envelope construction;
- evidence resolution logic;
- source loading or file I/O;
- policy checks;
- schema definitions;
- persistence or mutation logic;
- direct calls into RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED stores;
- test-only behavior hidden in production paths;
- business logic of any kind.

---

## 7. Accepted shim shapes

The preferred shim form is explicit re-export:

```python
"""Legacy compatibility shim.

Canonical implementation lives in apps.governed_api.ecology.routes.
"""

from apps.governed_api.ecology.routes import router

__all__ = ["router"]
```

A star re-export is allowed only when the canonical module intentionally defines `__all__` and the repository linter policy allows the import waiver:

```python
"""Legacy compatibility shim.

Canonical implementation lives in apps.governed_api.ecology.routes.
"""

from apps.governed_api.ecology.routes import *  # noqa: F401,F403
```

Importing from the legacy path is not allowed:

```python
# Forbidden: legacy path must never be the implementation source.
# from apps.governed-api.ecology.routes import router
```

Because `governed-api` contains a hyphen, it is not a normal Python dotted package path. Compatibility is file/path compatibility, not endorsement of a Python import namespace.

---

## 8. Enforced mapping

The initial enforced mapping is:

| Canonical implementation file | Legacy compatibility shim |
|---|---|
| `apps/governed_api/ecology/evidencebundle_resolver.py` | `apps/governed-api/ecology/evidencebundle_resolver.py` |
| `apps/governed_api/ecology/routes.py` | `apps/governed-api/ecology/routes.py` |
| `apps/governed_api/ecology/fastapi_routes.py` | `apps/governed-api/ecology/fastapi_routes.py` |

This list is a minimum enforcement set, not permission to add ungoverned logic elsewhere under `apps/governed-api/...`.

When new legacy compatibility files are retained or created, the checker must be updated so CI knows the canonical counterpart and can verify the shim contract.

---

## 9. CI enforcement requirements

`tools/ci/check_governed_api_path_policy.py` must fail when any of the following are true:

1. A required canonical file is missing.
2. A required legacy shim file is missing while the compatibility path is still in force.
3. A legacy shim contains primary logic.
4. A legacy shim imports from anything other than its canonical counterpart, except for narrow typing/linter-safe imports approved by the checker.
5. A canonical file imports implementation from the legacy path.
6. A legacy file defines functions, classes, route handlers, validators, policy branches, source readers, persistence behavior, or runtime envelope builders.
7. A new Python file appears under `apps/governed-api/...` without being registered as a shim mapping or explicitly denied by the checker.
8. A documentation or test fixture asserts `apps/governed-api/...` as canonical without labeling it legacy compatibility, if that documentation scan is enabled in CI.

The checker should be deterministic, no-network, read-only, and small enough to be reviewed as part of normal CI maintenance.

---

## 10. Recommended checker strategy

The checker should combine path mapping with AST/text checks.

Minimum recommended checks:

- verify every canonical path exists;
- verify every legacy shim path exists for the enforced mapping;
- parse every legacy shim with `ast.parse`;
- allow only docstrings, import statements, `__all__`, and simple alias/re-export assignments;
- reject `FunctionDef`, `AsyncFunctionDef`, `ClassDef`, `If`, `For`, `While`, `With`, `Try`, `Call`-bearing executable logic, file I/O, and route decorators;
- reject imports that reference `apps.governed-api` or other legacy modules as an implementation source;
- scan canonical files for textual references to `apps/governed-api` except comments or ADR references;
- exit non-zero with file-specific reason codes.

Reason-code examples:

```text
missing.canonical
missing.legacy_shim
legacy.non_shim_ast
legacy.bad_import
canonical.imports_legacy
legacy.unregistered_file
docs.legacy_presented_as_canonical
```

---

## 11. Contributor rules

### 11.1 Adding new governed API logic

When adding governed API logic:

1. Create or update the canonical file under `apps/governed_api/...`.
2. Add tests against the canonical path.
3. Add or update a legacy shim only when backward file-path compatibility is still required.
4. Update `tools/ci/check_governed_api_path_policy.py` with the mapping.
5. Update docs so the canonical path is the default reference.
6. Run the path-policy checker before merging.

### 11.2 Editing legacy shim files

Legacy shim edits should be rare.

Allowed reasons:

- update the canonical import target after a canonical rename;
- adjust `__all__` to match canonical exports;
- improve the shim docstring;
- remove the shim after a later ADR authorizes deprecation/removal.

Disallowed reasons:

- quick-fix route behavior;
- bypass tests on canonical modules;
- add fallback logic;
- load fixtures or files directly;
- add policy or citation behavior;
- hide divergent behavior from the canonical path.

### 11.3 Updating docs

New or revised docs should use:

```text
apps/governed_api/...
```

When mentioning the legacy path, use wording like:

```text
apps/governed-api/... is a legacy compatibility path and must remain shim-only.
```

Do not write examples that direct contributors to place new implementation logic under `apps/governed-api/...`.

---

## 12. Compatibility posture

The legacy path exists only to avoid immediate breakage from historical references and transitional tooling.

Compatibility does not mean behavioral independence. Any behavior reachable through the legacy file path must be behavior defined by the canonical module.

The compatibility path may be removed only when all of the following are true:

- historical references are migrated or clearly labeled;
- downstream tooling no longer requires the legacy file path;
- CI has a removal check or migration check;
- docs include the removal decision;
- rollback is documented;
- a later ADR or ADR amendment approves the removal.

---

## 13. Relationship to KFM governance

This ADR preserves KFM’s trust posture by preventing the governed API from splitting into two implementation regimes.

The path decision supports these KFM invariants:

- public/steward-facing clients use governed interfaces, not internal stores;
- AI and UI surfaces consume governed envelopes, not raw model or source output;
- EvidenceBundle, policy, review, release, and correction state remain upstream of runtime-facing claims;
- generated summaries and map/UI outputs remain downstream carriers, not sovereign truth;
- compatibility must be visible, bounded, and reversible.

This ADR does not authorize direct client access to canonical/internal stores. It only settles repository path ownership for governed API code.

---

## 14. Consequences

### 14.1 Positive

- Python import behavior is deterministic.
- Implementation ownership is clear.
- Legacy path references can continue to resolve during migration.
- CI can detect accidental split-brain implementation.
- Documentation can migrate gradually without blocking implementation clarity.
- The governed API trust membrane has one implementation owner.

### 14.2 Negative / tradeoffs

- Temporary duplicate file paths remain visible.
- CI must maintain a canonical-to-legacy mapping.
- Contributors must learn the underscore/hyphen distinction.
- Historical documents may still mention the legacy path until updated.
- Removal of the legacy path is deferred and requires later governance work.

### 14.3 Accepted tradeoff

KFM accepts short-term visible duplication to avoid breaking historical path references, but rejects long-term duplicated implementation logic.

---

## 15. Alternatives considered

### Alternative A: keep both paths as peer implementation homes

Rejected.

This creates divergent code ownership and raises the risk of conflicting runtime behavior at the governed API boundary.

### Alternative B: immediately delete `apps/governed-api/...`

Rejected for now.

Immediate removal could break historical references and transitional tooling before documentation and migration state are complete.

### Alternative C: make `apps/governed-api/...` canonical

Rejected.

The hyphenated path is not a normal Python dotted import path. It is unsuitable as the canonical Python implementation home.

### Alternative D: move governed API implementation to a third path

Rejected for this decision.

A broader move may be considered in a later architecture decision, but it would be a larger migration and does not solve the immediate underscore/hyphen ambiguity.

---

## 16. Validation

### 16.1 Required CI validation

At minimum, CI must run:

```bash
python tools/ci/check_governed_api_path_policy.py
```

If the repository has a test wrapper for the checker, CI should also run the relevant test target, for example:

```bash
pytest tests/ci/test_governed_api_path_policy.py
```

If the test file does not exist, the checker itself remains the required guard until a test wrapper is added.

### 16.2 Recommended local validation

Before opening a PR that touches either path, run:

```bash
python tools/ci/check_governed_api_path_policy.py

git grep -n "apps/governed-api" -- . \
  ':!docs/adr/ADR-0002*' \
  ':!tools/ci/check_governed_api_path_policy.py'

git grep -n "from apps\.governed-api\|import apps\.governed-api" -- '*.py'
```

Interpretation:

- direct implementation references should use `apps/governed_api/...`;
- remaining `apps/governed-api/...` references should be migration notes, legacy labels, or checker mappings;
- Python imports from the hyphenated path should not exist.

### 16.3 Acceptance criteria

A PR satisfies this ADR when:

- all governed API implementation logic is under `apps/governed_api/...`;
- every retained `apps/governed-api/...` Python file is shim-only;
- CI path-policy check passes;
- docs label the legacy path correctly;
- tests target canonical implementation behavior;
- no public/steward UI, Focus Mode, route, or runtime envelope relies on the legacy path as a truth source.

---

## 17. Rollback

Rollback of this ADR’s implementation is straightforward if a path-policy change breaks the repository unexpectedly:

1. Revert the PR that changed the checker or shim mapping.
2. Restore the last passing canonical and legacy shim files.
3. Re-run `python tools/ci/check_governed_api_path_policy.py`.
4. Re-run governed API route/runtime tests affected by the reverted change.
5. Record the failed migration attempt in the PR notes or ADR amendment log.

Rollback must not move implementation logic into the legacy path. If compatibility is broken, restore shims; do not duplicate canonical behavior.

---

## 18. Documentation impact

Required documentation updates:

- this ADR should be placed in the repository ADR folder;
- governed API README files should identify `apps/governed_api/...` as canonical;
- migration notes should explain that `apps/governed-api/...` is shim-only;
- future route/runtime docs should use canonical paths;
- any exception must link back to this ADR.

Suggested ADR filename:

```text
docs/adr/ADR-0002-governed-api-path-canonicalization.md
```

If the repository uses a different ADR home, place the file in the existing ADR convention and preserve the ADR number.

---

## 19. Open verification items

The following are not decided by this ADR and should be verified in the mounted repository before making stronger implementation claims:

- whether all listed canonical files are present on the active branch;
- whether all listed legacy shim files are present on the active branch;
- whether `tools/ci/check_governed_api_path_policy.py` currently covers only the listed files or the full legacy path tree;
- whether a test wrapper exists for the checker;
- whether CI workflow YAML already runs the checker;
- whether docs still present `apps/governed-api/...` as canonical;
- whether app route registration imports only canonical modules.

---

## 20. Final rule

Use this rule when uncertain:

> Implementation goes in `apps/governed_api/...`; `apps/governed-api/...` only points back to it.
