<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ahgp-readme
title: connectors/ahgp/ — AHGP Source Connector Lane
type: readme; directory-readme; implementation-status-boundary
version: v0.2
status: repository-grounded; connector-placeholder; source-admission-unproved; non-publisher
owners: NEEDS VERIFICATION — source, connector, people/genealogy, rights, sensitivity, data, and independent review stewards
created: 2026-06-16
updated: 2026-09-05
current_path: connectors/ahgp/README.md
owning_root: connectors/
policy_label: repository-facing; source-admission-only; no-network-by-default; non-publisher
base_commit: 10be9a177fc88333c983bb1b428ce20a32b22c76
prior_blob: 9ff3e956f69ca8c97b43de732ba8ee54f481ced5
truth_posture: CONFIRMED tracked scaffold and documentation / PROPOSED future implementation / UNKNOWN live operation and source activation
related:
  - ../README.md
  - ./src/README.md
  - ./src/ahgp/README.md
  - ./tests/README.md
  - ../../docs/sources/catalog/ahgp.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This same-path revision corrects the AHGP name and stale inventory; it changes no connector implementation or source state."
  - "The local descriptor is unresolved placeholder metadata, not an admitted SourceDescriptor or permission to use personal data."
  - "Source payload handoff is limited to RAW or QUARANTINE; receipt-ready metadata uses a caller-owned governed sink."
  - "Existing document identity and section anchors are retained; no schema, registry, test-placement, or source-identity migration is performed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AHGP Connector

`connectors/ahgp/` is the source-specific implementation lane for the
**American History and Genealogy Project (AHGP)**. The name follows the
[AHGP homepage](https://ahgp.org/) and the repository's
[source-catalog navigation page](../../docs/sources/catalog/ahgp.md).

> [!IMPORTANT]
> **Current capability: scaffold, not an operational connector.** At
> `main@10be9a177fc88333c983bb1b428ce20a32b22c76`, the fetch and admission
> modules contain comments only, the package initializer is empty, and the
> connector test directory contains only a README. No retrieval command,
> implemented admission gate, or AHGP-specific test result is established.

**Navigate:** [Inventory](#canonical-fit) · [Authority](#authority-boundary) ·
[Admission](#ahgp-admission-posture) · [Validation](#validation-expectations) ·
[Next change](#safe-change-pattern) · [Completion gates](#definition-of-done)

## Purpose

This lane is intended to preserve source-native AHGP material for governed
intake, including historically relevant people, locality, census, cemetery,
newspaper, and family-history context. It does not resolve identities, establish
kinship, verify historical claims, or authorize reuse.

Its owning root is `connectors/`. The [parent connector contract](../README.md)
limits source acquisition to bounded capture and admission support. Normalization,
evidence resolution, policy decisions, review, release, and public delivery
remain separate responsibilities. This README documents that boundary; it does
not implement or activate it.

## Canonical fit

**CONFIRMED tracked inventory at the pinned base:**

```text
connectors/ahgp/
├── README.md
├── pyproject.toml
├── src/
│   ├── README.md
│   └── ahgp/
│       ├── README.md
│       ├── __init__.py
│       ├── admit.py
│       ├── descriptor.yaml
│       └── fetch.py
└── tests/
    └── README.md
```

| Surface | Observed bytes and safe interpretation |
|---|---|
| [Project metadata](./pyproject.toml) | `kfm-connector-ahgp`, version `0.0.0`; no build backend, dependencies, or entry point declared. Installation is not verified. |
| [Package initializer](./src/ahgp/__init__.py) | Empty; no exported API. |
| [Fetcher](./src/ahgp/fetch.py) and [admission module](./src/ahgp/admit.py) | Comment-only placeholders; no endpoint, transport, parser, admission function, or output implemented. |
| [Local descriptor](./src/ahgp/descriptor.yaml) | `name: ahgp`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`; incomplete package-local metadata, not an activation record. |
| [Source-tree guide](./src/README.md) | Detailed inventory and intended import/I/O boundary; documentation is not execution evidence. |
| [Package guide](./src/ahgp/README.md) | Older design guidance; its name expansion and inventory are stale. Read the pinned files above for implementation facts. |
| [Test boundary](./tests/README.md) | README-only directory; no local executable tests or fixtures. Local-versus-root test placement remains unresolved. |
| [Source-catalog navigation](../../docs/sources/catalog/ahgp.md) | Routes to existing family/product guidance and proposed registry material; no longer a stub or an activation authority. |

This is a tracked-tree inspection, not a workstation, deployed-runtime,
ignored-file, or external-storage audit. The `ahgp` path and package identifier
are preserved; correcting the display name does not register a new source ID.

### Directory Rules basis

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts [Directory Rules](../../docs/doctrine/directory-rules.md), whose
§10.1 / `DIR-EXEC-002` places source/provider implementation under `connectors/`.
§12.3 / `DIR-SOURCE-003` separates connector code from human source guidance in
`docs/sources/` and machine source identities in `data/registry/sources/`.

This update retains an existing file in its owning root. It does not migrate the
catalog's flat/directory paths, the existing proposed registry material, or the
local descriptor into a second authoritative home.

## Authority boundary

The intended handoff is limited to source payload candidates and process metadata:

```text
explicit caller + admitted source/configuration + bounded transport
  -> AHGP capture/admission implementation (not implemented here yet)
  -> RAW candidate or QUARANTINE candidate
  -> receipt-ready metadata through a caller-owned governed sink
```

The full KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A connector must not directly write WORK, PROCESSED, CATALOG, TRIPLET, PROOF,
PUBLISHED, or release decisions. Receipt construction is not proof or approval;
durable process records belong to `data/receipts/`, not this source tree.
Promotion is a governed transition, not a file move, successful fetch, validation
pass, pull request, or merge.

Public maps, search, exports, and AI use governed APIs and released artifacts,
never direct connector results or RAW/WORK/QUARANTINE stores. Consequential
claims must resolve `EvidenceRef -> EvidenceBundle`; otherwise narrow or abstain.
AI, indexes, graph projections, and map layers remain interpretive carriers.

## Allowed contents

The following are **allowed responsibilities, not implemented features**:

| Content | Boundary |
|---|---|
| Source-specific fetch and parsing helpers | Explicit invocation; bounded configuration; preserve source-native identifiers, wording, locators, and caveats. |
| Endpoint, cadence, and source-role notes | Link to reviewed source/configuration decisions; do not infer access permission from a URL. |
| Digest, retrieval, and admission metadata helpers | Candidate RAW/QUARANTINE handoff and receipt-ready metadata only. |
| Connector and package documentation | State implementation limits; do not duplicate source catalog, policy, schema, or registry authority. |
| Test-routing and fixture guidance | Follow the existing [test boundary](./tests/README.md); do not establish parallel local and root suites. |

## Forbidden contents

Do not commit source payloads, credentials, cookies, real-person fixtures,
private addresses, sensitive burial locations, or copied volunteer family trees
under this lane. Do not add unbounded crawling, network/credential/filesystem
side effects on import, automatic identity or kinship resolution, or publication.

| Material or responsibility | Owning boundary outside this lane |
|---|---|
| Machine source identity and activation | Governed source registry and reviewed activation decisions; local `descriptor.yaml` is not a substitute. |
| Contracts, machine shape, and admissibility | `contracts/`, `schemas/`, and `policy/`, respectively. |
| Reusable domain logic and transformations | `packages/` and `pipelines/`; declarative run definitions belong to `pipeline_specs/`. |
| Lifecycle records and evidence support | Their governed `data/` lanes; no authority follows from a path alone. |
| Release, withdrawal, correction, and rollback decisions | `release/`; a connector cannot approve itself. |
| Non-authoritative QA outputs | The owning validation/output profile; compatibility `artifacts/` is not a blanket storage permission. |

## AHGP admission posture

> [!CAUTION]
> The checked-in `sensitivity_floor: public` is a **placeholder value, not a
> clearance decision**. With `role` and `rights` still `TBD`, that file must not
> authorize fetching, source admission, public-safe classification, redistribution,
> or disclosure of living-person information. This revision does not change it.

Keep the hosting project, contributor/transcriber, underlying record, and
specific claim distinct. A name match is not an identity decision; a
transcription is not the original record; and a locality reference is not a
verified coordinate or current land-title claim.

The [AHGP Census Index Project](https://ahgp.org/census/) describes its index
as a discovery aid rather than transcribed census data and asks readers to link
rather than copy webmaster work. Its scope must not be generalized to every
AHGP product. The [homepage](https://ahgp.org/) also carries a rights-reserved
notice. These are source statements, not a KFM legal determination: page,
contribution, image, compilation, underlying-record, caching, and redistribution
rights still require their own review before live connector use.

A future intake must preserve the source/product identity, exact locator,
contributor and underlying-record reference where available, source wording and
uncertainty, capture digest, and retrieval time. Keep historical event time,
source publication/update time, and KFM retrieval time separate. Missing or
ambiguous dates and locations remain unresolved; do not silently geocode,
merge people, or invent precision.

Living-person, family-linkage, obituary, cemetery, cultural/Indigenous, private-land,
and exact-location sensitivity must be evaluated before exposure, including
sensitivity introduced by joins. Prefer no retrieval when permission is absent;
where retention is permitted, use governed quarantine, minimization, redaction,
or generalization with recorded reasons. Public web availability is not a
blanket reuse or disclosure decision.

## Endpoint and rate-limit posture

**UNKNOWN / not implemented:** approved AHGP endpoint configuration, host and
redirect allowlist, authentication, robots/access policy, cadence, rate limits,
retry policy, source-head handling, persistence, and live source activation.
The two official links above are documentation references, not configured feeds
or crawl authorization. No live connector invocation is provided.

Before any later live invocation, require a resolvable descriptor and activation
decision; page-specific rights and sensitivity review; explicit timeouts,
redirect/retry/request/byte limits and cancellation; and deterministic no-network
transport tests. Do not bypass denial, authentication, rate limiting, or access
restrictions. Define finite failure outcomes in the owning contract; this
README does not mint executable enums or turn a transport success into admission.

## Validation expectations

### Read-only scaffold checks

From an actual repository checkout, these commands inspect the present files
without importing AHGP, installing it, or contacting a source:

```bash
git ls-tree -r --name-only HEAD -- connectors/ahgp
git diff --check -- connectors/ahgp/README.md
python - <<'PY'
import ast
import tomllib
from pathlib import Path

root = Path("connectors/ahgp")
metadata = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
assert metadata["project"]["name"] == "kfm-connector-ahgp"
assert metadata["project"]["version"] == "0.0.0"
for name in ("__init__.py", "admit.py", "fetch.py"):
    module = ast.parse((root / "src" / "ahgp" / name).read_text(encoding="utf-8"))
    assert not module.body, f"Scaffold changed: inspect {name} before relying on this README"
print("Scaffold metadata and empty-module assertions passed; no connector behavior tested.")
PY
```

The Python check requires Python 3.11 or later (`tomllib`). It checks only the
listed metadata and absence of executable statements in three files. It does
not prove package installation, import isolation for future code, runtime
confinement, source access, admission, receipt persistence, or publication safety.
If it fails after implementation advances, inspect the change and update the
README; do not delete implementation to preserve the scaffold assertion.

There is no executable test in `connectors/ahgp/tests/` to report as passing.
Shared connector checks are not AHGP coverage unless they exercise AHGP code.
Run repository-native documentation/link and applicable connector/policy checks
at the actual review head; record unrun, skipped, pending, and failing checks
separately. This README supplies no current CI pass or enforcement claim.

### Before claiming an implemented connector

Use the [test boundary](./tests/README.md) for placement and collection review.
The first actual adapter needs synthetic, no-network positive and negative
cases for import safety, unresolved descriptor/rights refusal, bounded transport,
malformed or partial responses, timeout/rate limiting, captured-byte identity,
RAW/QUARANTINE-only handoff, receipt metadata, replay, and forbidden downstream
writes. Passing syntax checks or an empty test collection is not this proof.

## Migration posture

Do not relocate the local descriptor, proposed registry material, catalog pages,
or test lane merely to match a directory example. Inspect accepted placement,
consumers, identity, and applicable ADRs first; preserve references and rollback
in a separate, narrowly scoped migration. Retain historical receipts unchanged.

The older [package guide](./src/ahgp/README.md) still uses the superseded name
expansion and an outdated inventory. That documentation drift is explicitly
left outside this parent-README update; it must not override the pinned module
bytes or be mistaken for an active connector.

## Safe change pattern

The **PROPOSED next implementation slice** is one explicit, dependency-closed,
no-network capture/admission boundary using synthetic inputs, after selecting
one reviewed test-collection route. Reuse existing shared contracts and connector
primitives where their current code and interfaces support it. Do not add a
second descriptor/schema/policy home or use live pages as fixtures.

For this documentation revision, keep the existing document ID, path, headings,
and source identifier; change only the README plus its generated-work provenance
receipt. Re-pin `main`, inspect task-branch and open-PR overlap, validate the final
bytes and links, and deliver through an eligible draft-PR path under current
[contribution guidance](../../CONTRIBUTING.md). Human review is separate from
authoring and validation. No merge, activation, settings, release, deployment,
promotion, or publication is authorized by the README.

## Definition of done

Documentation completion and operational completion are different gates:

| Gate | Status at this revision |
|---|---|
| Tracked connector contents inventoried and linked | **CONFIRMED** at the pinned base. |
| Correct source name and catalog navigation | **CONFIRMED** in this page; older child-guide drift remains disclosed. |
| Source, connector, rights, sensitivity, and independent stewards | **NEEDS VERIFICATION**; a repository review route is not evidence of those roles. |
| Accepted descriptor, product coverage, rights, access, and activation | **NOT ESTABLISHED** by the inspected scaffold. |
| Implemented endpoint, parser, admission, bounded I/O, and receipts | **NOT IMPLEMENTED** in the inspected modules. |
| AHGP-specific tests, fixtures, collection, and exact-head CI | **NEEDS VERIFICATION**; local test directory is documentation-only. |
| Evidence closure, policy/review, correction, release, and rollback | **NOT PROVED**; must remain separate from connector success. |

### Rollback

For this documentation-only change, leave the draft unmerged or revert its
README and companion generated-work receipt together in a reviewed corrective
change. Preserve existing source bytes, historical receipts, and review history.
No runtime, registry, descriptor, policy, source activation, or public state was
changed by this revision and none should be changed to roll it back.

## Status summary

**Last reviewed: 2026-09-05 UTC**, against
`main@10be9a177fc88333c983bb1b428ce20a32b22c76`. This page is a
repository-grounded connector boundary with confirmed scaffold inventory and
explicit future gates, not evidence of an operational AHGP service. Re-review
when module bytes, package metadata, descriptor state, test placement, source
terms, activation, or caller-owned sinks change.

[Back to top](#top)
