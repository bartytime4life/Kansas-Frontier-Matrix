<a id="top"></a>

# `fixtures/infrastructure-generalized/` — generalized-infrastructure fixture compatibility boundary

> **One-line purpose.** `fixtures/infrastructure-generalized/` is a transitional compatibility and routing lane for legacy top-level generalized-infrastructure fixture references; it is not a third reusable fixture authority.

> [!IMPORTANT]
> Route new domain-owned infrastructure fixtures to the working domain path [`fixtures/domains/settlements-infrastructure/`](../domains/settlements-infrastructure/README.md). That lane is currently scaffold-only, so new payloads still require reviewed contracts, schemas, policy, tests, and an accepted fixture structure.

> [!CAUTION]
> A generalized fixture is safe only when its geometry, attributes, joins, time fields, and surrounding context cannot disclose or reconstruct protected infrastructure detail. “Public source,” “coarse display,” “synthetic label,” and “passes a fixture check” are not substitutes for sensitivity review.

> [!WARNING]
> Never place live operational status, exact critical-asset geometry, condition or vulnerability detail, dependency topology, restricted operator fields, private person or parcel joins, credentials, emergency instructions, or real source payloads in this public repository lane.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs here](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

---

## Purpose

This README prevents the top-level path from evolving into a parallel infrastructure fixture authority. It helps maintainers:

- route reusable Settlements/Infrastructure examples to the working domain segment;
- distinguish reusable fixtures from test-local wrappers and cross-cutting renderer inputs;
- preserve the existing public-safe, generalized, synthetic-only posture;
- keep exact geometry, condition, vulnerability, dependency, operator, and service information fail closed;
- identify and retire legacy consumers without silently breaking them;
- preserve object ownership across Settlements/Infrastructure, Roads/Rail/Trade, Hydrology, Hazards, People/DNA/Land, Archaeology, and Spatial Foundation;
- record generalization, redaction, aggregation, correction, and rollback expectations; and
- keep inventory, ownership, validation, and migration gaps visible.

This lane is not an intake bucket for infrastructure-shaped material whose responsibility is unclear. Unclear ownership or sensitivity is a reason to stop, classify, and review the fixture.

### Routing rule

| Fixture purpose | Preferred home |
|---|---|
| Reusable Settlements/Infrastructure fixture | [`fixtures/domains/settlements-infrastructure/`](../domains/settlements-infrastructure/README.md), after its scaffold is replaced through a reviewed domain-fixture design |
| Existing generalized-infrastructure domain alias | [`fixtures/domains/infrastructure-generalized/`](../domains/infrastructure-generalized/README.md), treated as **CONFLICTED / NEEDS VERIFICATION**, not as an authority shortcut |
| One-test-only wrapper or parametrization | [`tests/fixtures/settlements-infrastructure/`](../../tests/fixtures/settlements-infrastructure/README.md) or the owning test subtree |
| Small cross-cutting renderer input whose infrastructure meaning is incidental | [`fixtures/slim/`](../slim/README.md) |
| Scale-dependent cross-cutting stress corpus | [`fixtures/heavy/`](../heavy/README.md), subject to its storage and admission rules |
| Cross-cutting expected output with no domain owner | [`fixtures/golden/`](../golden/README.md) |
| Verified legacy reference to this top-level path | Temporary pointer or wrapper here, with a canonical target and retirement plan |
| Real source, lifecycle, evidence, proof, release, or publication material | Not a fixture; use the governed responsibility root and lifecycle |

[Back to top](#top)

## Authority level

**Compatibility / transitional fixture-routing lane; non-authoritative for infrastructure meaning, machine shape, sensitivity, policy, source admission, evidence, proof, release, operational status, emergency guidance, or publication.**

The live contribution guide directs placement preflight to [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md). Directory Rules place domain-owned fixtures at `fixtures/domains/<domain>/`, and the Settlements/Infrastructure path registry names `fixtures/domains/settlements-infrastructure/` as the working domain fixture path.

Repository evidence is not fully reconciled:

- [`fixtures/README.md`](../README.md) lists this top-level lane as a public-safe generalized runtime fixture lane;
- [`fixtures/domains/infrastructure-generalized/`](../domains/infrastructure-generalized/README.md) is a second documented generalized-infrastructure fixture lane;
- [`fixtures/domains/settlements-infrastructure/`](../domains/settlements-infrastructure/README.md) matches the working domain segment but remains a four-line greenfield stub with placeholder child families; and
- the domain workflow inspects `fixtures/domains/settlements-infrastructure/`, not either generalized-infrastructure alias.

This README therefore narrows the requested path to compatibility and routing without moving, deleting, or silently declaring another path authoritative. Resolving the duplicate lanes requires a complete inventory, consumer graph, stewardship decision, migration plan, and—if authority or path identity changes—an accepted ADR or equivalent governed decision.

| Responsibility | Owning surface | Boundary for this lane |
|---|---|---|
| Settlements/Infrastructure meaning | [`contracts/domains/settlements-infrastructure/`](../../contracts/domains/settlements-infrastructure/README.md) | Fixtures may exercise accepted meaning but never define it. |
| Machine shape | [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Examples never become schema authority. |
| Domain policy | [`policy/domains/settlements-infrastructure/`](../../policy/domains/settlements-infrastructure/README.md) | An expected denial does not create a policy rule. |
| Reusable domain fixtures | [`fixtures/domains/settlements-infrastructure/`](../domains/settlements-infrastructure/README.md) | Working placement; currently scaffold-only and not proof of executable fixtures. |
| Generalized domain alias | [`fixtures/domains/infrastructure-generalized/`](../domains/infrastructure-generalized/README.md) | Existing candidate duplicate or compatibility lane; authority remains unresolved. |
| Domain tests | [`tests/domains/settlements-infrastructure/`](../../tests/domains/settlements-infrastructure/README.md) | Tests consume fixtures; fixtures are not assertions. |
| Test-local fixtures | [`tests/fixtures/settlements-infrastructure/`](../../tests/fixtures/settlements-infrastructure/README.md) | Keep unit-test-scoped wrappers there. |
| Source identity and admission | [`data/registry/sources/settlements-infrastructure/`](../../data/registry/sources/settlements-infrastructure/README.md) | Synthetic source-shaped examples do not admit or activate sources. |
| Candidate review and release | [`release/candidates/settlements-infrastructure/`](../../release/candidates/settlements-infrastructure/README.md) and release authority | Fixture success never approves promotion or release. |
| Public maps, APIs, exports, and AI | Governed public surfaces | Public clients do not read fixtures as infrastructure truth. |

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Fixtures do not enter, shortcut, or substitute for this lifecycle. A commit, pull request, merge, passing check, generalized render, or generated explanation is not KFM publication.

[Back to top](#top)

## Status

| Evidence field | Current bounded result |
|---|---|
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` at `main@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566` |
| Prior README blob | `73a09c9bc55d10ae9a66706e8caa07a532eaac6f` |
| Requested path | **CONFIRMED** — the directory and README exist. |
| Placement class | **PROPOSED / CONFLICTED** — transitional compatibility is the narrow safe classification pending lane reconciliation. |
| Working domain path | **CONFIRMED present** — `fixtures/domains/settlements-infrastructure/README.md` exists as a greenfield stub. |
| Working domain child families | **CONFIRMED placeholders** — `valid/`, `invalid/`, and `golden/` contain `PLACEHOLDER.md` files. |
| Generalized domain alias | **CONFIRMED present / authority unresolved** — `fixtures/domains/infrastructure-generalized/README.md` exists with substantial guidance. |
| Direct top-level payload inventory | **NARROWED / NEEDS VERIFICATION** — the connector confirmed a directory but did not expose a recursive listing. |
| Indexed top-level consumers | **NOT ESTABLISHED** — bounded indexed search surfaced only this README for the exact top-level path. |
| Domain workflow | **CONFIRMED readiness workflow** — it reads the working domain path, uses read-only contents permission, and holds semantic validation, proof production, and release dry-run readiness. |
| Review route | **CONFIRMED** — `.github/CODEOWNERS` maps `/fixtures/` to `@bartytime4life`; enforcement and semantic ownership remain **UNKNOWN**. |
| Fixture regeneration | **CONFIRMED TODO-only** — the root `Makefile` fixture target prints a readiness marker. |
| Dedicated compatibility validation | **NOT ESTABLISHED**. |
| Release or public dependency | **UNKNOWN**. |

### Current safe conclusions

- **CONFIRMED:** three infrastructure-related fixture paths exist, but they do not have one reconciled authority story.
- **CONFIRMED:** Directory Rules and the domain path registry use the `settlements-infrastructure` domain segment.
- **CONFIRMED:** the domain workflow inspects the working `settlements-infrastructure` fixture lane and explicit readiness holds; it does not consume this top-level lane.
- **PROPOSED:** stop admitting new payloads here and treat this path as a temporary compatibility router.
- **CONFLICTED:** the parent fixture index recognizes this top-level lane, a populated `domains/infrastructure-generalized/` lane also exists, and the working domain path remains scaffold-only.
- **UNKNOWN:** exhaustive child inventories, active consumers, ignored or generated files, external stores, migration dependencies, required-review enforcement, and release coupling.
- **NEEDS VERIFICATION:** which lane owns existing payloads, whether either alias can retire, and whether compatibility wrappers are needed.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Directory README | `CONFIRMED` | This revision supplies the required ordered contract. |
| Compatibility classification | `PROPOSED` | Safe posture; acceptance and migration owner remain unverified. |
| Recursive child inventory | `NOT ESTABLISHED` | No byte-complete listing was available. |
| Active consumers | `NOT ESTABLISHED` | No indexed executable consumer surfaced for the exact top-level path. |
| Working canonical placement | `CONFIRMED doctrine / scaffold-only implementation` | The domain path exists but does not yet contain an accepted reusable fixture corpus. |
| Alias reconciliation | `CONFLICTED` | Two generalized-infrastructure aliases exist outside the working domain segment. |
| Migration manifest | `NOT ESTABLISHED` | Required if payloads or consumers are discovered. |
| Pointer or wrapper validator | `NOT ESTABLISHED` | No executable compatibility enforcement was confirmed. |
| Deterministic regeneration | `NOT ESTABLISHED` | Root fixture command is a TODO marker. |
| Dedicated CI collection | `NOT ESTABLISHED` | The domain workflow does not reference this path. |
| Infrastructure truth authority | `DENIED` | Fixtures never establish real infrastructure state. |
| Operational or emergency authority | `DENIED` | Fixtures never provide instructions or live status. |
| Release authority | `DENIED` | Fixtures never approve promotion or publication. |

[Back to top](#top)

## What belongs here

Until inventory, consumers, and lane ownership are reconciled, admission is intentionally narrow:

- this README and human-readable routing notes required to explain the compatibility boundary;
- a small compatibility manifest pointing to one reviewed fixture under the working domain lane, only when a named executable consumer still requires this path;
- a temporary wrapper that is synthetic, deterministic, public-safe, generalized, non-reconstructable, and not a divergent copy;
- deprecation, migration, correction, and retirement notes tied to exact old and new paths;
- finite expected-outcome and reason-code notes that make unsafe or stale compatibility behavior fail visibly; and
- immutable hashes or target identifiers needed to prove that a pointer resolves to the intended fixture.

### Compatibility admission contract

Every retained item must declare:

| Field | Required meaning |
|---|---|
| `compatibility_id` | Stable toy identifier for the compatibility item. |
| `canonical_fixture_ref` | Exact reviewed target under the accepted fixture lane. |
| `consumer` | Exact executable consumer that still requires the old path. |
| `reason` | Why the consumer cannot use the accepted path yet. |
| `owner` | Accountable migration owner; `OWNER_TBD` requires a review reason. |
| `introduced_at` | Commit or version that created the dependency, when known. |
| `expires_or_reviews_on` | Date or concrete trigger for re-evaluation. |
| `expected_outcome` | Bounded result such as `PASS`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `source_role` | Must be `synthetic`; any imitated domain role remains explicit and subordinate. |
| `geometry_posture` | `toy`, `generalized`, `aggregated`, `redacted`, or `withheld`; never ambiguous. |
| `reconstruction_posture` | Evidence that joins, zoom changes, tiles, attributes, or adjacent fixtures cannot recover protected detail. |
| `transform_ref` | Synthetic transform or review note explaining generalization, aggregation, redaction, or suppression. |
| `network` | `disabled` by default. |
| `content_hash` | Hash of the canonical target or manifest when identity matters. |
| `uses_real_source_data` | Must be `false`. |
| `authorizes_publication` | Must be `false`. |
| `removal_plan` | Consumer update, verification, correction, rollback, and retirement steps. |

An item without a canonical target, real consumer, accountable owner, sensitivity posture, non-reconstruction rationale, and removal trigger does not belong here.

[Back to top](#top)

## What does NOT belong here

- New reusable Settlements/Infrastructure fixtures; place them under the reviewed working domain lane.
- New material under `fixtures/domains/infrastructure-generalized/` merely to avoid resolving the domain-path conflict.
- Unsorted, speculative, or “temporarily public” infrastructure payloads.
- Copies of working-domain fixtures, test-local wrappers, or expected outputs.
- Real source exports, live API responses, operational feeds, current observations, production snapshots, caches, logs, or source-registry records.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data.
- Actual SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReviewRecords, release manifests, correction notices, withdrawal notices, or rollback cards.
- Contracts, schemas, policy rules, validators, executable tests, pipelines, connector code, renderer code, API code, UI code, or AI runtime code.
- Generated CI reports, screenshots, rendered tiles, map exports, build products, or public artifacts.
- Exact or realistically recoverable locations of dams, levees, bridges, pump stations, treatment plants, substations, towers, network nodes, utility segments, vulnerable facilities, or other critical assets.
- Condition ratings, vulnerability fields, inspection detail, outage state, service availability, maintenance state, operator-sensitive fields, security controls, or emergency readiness information.
- Full dependency edges, private service topology, named-party access detail, facility-to-facility reliance, or cross-fixture combinations that reconstruct them.
- Private operator-as-person data, precise parcel joins, living-person identifiers, title assertions, or restricted community, cultural, archaeological, ecological, or tribal context.
- Alerts, advisories, evacuation instructions, navigation guidance, emergency decisions, engineering conclusions, insurance determinations, regulatory findings, or public-safety claims.
- Mutable remote URLs, ambient credentials, current-clock dependencies, live-network fallbacks, or third-party tracking surfaces.
- A second fixture registry, schema home, contract home, policy home, source authority, proof home, release home, or publication surface.

[Back to top](#top)

## Inputs

Compatibility material may derive only from:

- a verified legacy consumer that still resolves `fixtures/infrastructure-generalized/`;
- a reviewed synthetic fixture under the accepted domain fixture lane;
- accepted semantic contracts and machine schemas referenced by that fixture;
- reviewed sensitivity, source-role, rights, temporal, evidence, policy, and release expectations;
- deterministic generation, generalization, aggregation, redaction, or normalization notes; and
- a migration decision that preserves correction and rollback.

### Infrastructure invariant set

Any compatibility item must preserve these boundaries:

1. **Generalized is not exact with fewer pixels.** Geometry, attributes, labels, IDs, tiles, zoom behavior, and context must not recover a protected location.
2. **Joins must not reconstruct precision.** Multiple public-safe fixtures cannot be combined to infer critical detail, dependency edges, vulnerable endpoints, or private property relations.
3. **Condition and vulnerability fail closed.** Full condition, inspection, vulnerability, outage, and security-relevant detail never becomes a public fixture.
4. **Dependency detail fails closed.** Full reliance graphs and sensitive endpoints remain denied; only reviewed toy or coarse summaries may appear.
5. **Operator identity stays bounded.** Public organization names do not authorize operator-sensitive data, private agreements, credentials, or living-person details.
6. **Service area is not service guarantee.** A toy or aggregate polygon does not establish availability, reliability, eligibility, jurisdiction, or current coverage.
7. **Cross-lane ownership survives composition.** Roads/Rail owns transport-graph meaning; Hydrology owns water evidence; Hazards owns hazard events and warnings; People/Land owns person, parcel, title, and consent constraints; Archaeology and cultural lanes retain their sensitivity controls.
8. **Source role never upgrades by normalization or display.** Administrative, observed, regulatory, modeled, aggregate, candidate, and synthetic roles remain distinct.
9. **Temporal roles remain separate.** Source, observed, valid, retrieval, release, expiry, stale, correction, and withdrawal times do not collapse.
10. **Evidence resolves before claim-like answers.** A synthetic `ANSWER` case must model `EvidenceRef -> EvidenceBundle` closure; otherwise use `ABSTAIN`, `DENY`, or `ERROR`.
11. **The most restrictive sensitivity posture wins.** Cross-lane joins, precise geometry, critical assets, dependency detail, and person/parcel proximity fail closed or generalize.
12. **No-network is the default.** Fixtures never silently call operator systems, GIS portals, source APIs, map services, model runtimes, public APIs, or release services.
13. **Release stays independent.** A valid fixture, generalized render, or green check never creates review, release, or publication state.

### Family routing

| Scenario | Destination and posture |
|---|---|
| Positive reusable domain case | [`fixtures/domains/settlements-infrastructure/valid/PLACEHOLDER.md`](../domains/settlements-infrastructure/valid/PLACEHOLDER.md) currently marks a placeholder; replace it only through reviewed domain-fixture work. |
| Negative or fail-closed domain case | [`fixtures/domains/settlements-infrastructure/invalid/PLACEHOLDER.md`](../domains/settlements-infrastructure/invalid/PLACEHOLDER.md) currently marks a placeholder. |
| Stable domain expected output | [`fixtures/domains/settlements-infrastructure/golden/PLACEHOLDER.md`](../domains/settlements-infrastructure/golden/PLACEHOLDER.md) currently marks a placeholder. |
| Existing generalized-domain material | [`fixtures/domains/infrastructure-generalized/`](../domains/infrastructure-generalized/README.md), pending inventory and authority reconciliation. |
| Test-local case | [`tests/fixtures/settlements-infrastructure/`](../../tests/fixtures/settlements-infrastructure/README.md). |
| Cross-cutting small, heavy, or expected-output case | [`slim/`](../slim/README.md), [`heavy/`](../heavy/README.md), or [`golden/`](../golden/README.md), only when no domain owner applies. |

[Back to top](#top)

## Outputs

This lane may support only:

- human-readable routing from the old top-level path to an accepted fixture;
- a bounded compatibility pointer or wrapper for a named legacy consumer;
- explicit migration, deprecation, correction, and retirement signals;
- deterministic identity and checksum evidence for a reviewed target;
- public-safe transform notes that explain why a synthetic wrapper is generalized and non-reconstructable; and
- finite compatibility outcomes that fail visibly when target identity, sensitivity posture, consumer contract, or safety boundaries are missing.

It does not emit or authorize:

- an infrastructure observation, legal status, condition finding, vulnerability assessment, dependency claim, service guarantee, operational status, regulatory conclusion, engineering conclusion, or emergency message;
- source admission, activation, freshness approval, rights clearance, or sensitivity downgrade;
- an EvidenceBundle, receipt, proof, PolicyDecision, ReviewRecord, or release decision;
- lifecycle promotion;
- a map layer, tile set, API response, AI answer, alert, public export, or operational instruction;
- release, deployment, publication, correction execution, or rollback execution; or
- public-capacity, resilience, safety, insurance, eligibility, navigation, ownership, or title conclusions.

Generated comparison reports or migration diagnostics belong in accepted temporary or non-authoritative artifact locations. They do not become fixtures, proofs, or releases because a workflow produced them.

[Back to top](#top)

## Validation

### Current executable boundary

- The root `make fixtures` target is a TODO readiness marker and does not regenerate or validate this lane.
- [`domain-settlements-infrastructure.yml`](../../.github/workflows/domain-settlements-infrastructure.yml) runs on pull requests with read-only contents permission and no persisted checkout credentials.
- That workflow checks `fixtures/domains/settlements-infrastructure/`, its placeholder families, and broader domain readiness; it does not reference this top-level path or `fixtures/domains/infrastructure-generalized/`.
- The workflow explicitly reports semantic validation, proof production, and release-dry-run holds. A green hold job does not create proof or release authority.
- No dedicated compatibility-pointer validator, recursive inventory check, reconstruction-resistance test, orphan detector, migration check, or consumer-backlink gate was confirmed.

### Required compatibility checks

1. **Inventory:** enumerate every tracked, ignored, generated, LFS-backed, and externally stored child in all three fixture paths.
2. **Consumer graph:** identify every inbound reference, executable consumer, generated mirror, documentation backlink, and runtime dependency.
3. **Authority resolution:** accept one reusable domain fixture path and classify the other paths as compatibility, migration, or retirement surfaces.
4. **Canonical target:** require every retained compatibility item to resolve to one exact reviewed fixture.
5. **No duplication:** compare hashes and semantics so wrappers do not become divergent copies.
6. **Synthetic-only:** reject real observations, source responses, identities, restricted fields, operational material, and source-derived sensitive geometry.
7. **Geometry posture:** require explicit toy, generalized, aggregated, redacted, or withheld state and reject unexplained precision.
8. **Reconstruction resistance:** test joins, tiles, labels, attributes, zoom levels, adjacent fixtures, and repeated releases for precision recovery.
9. **Condition and dependency denial:** reject vulnerability, inspection, outage, security, and sensitive topology detail.
10. **No-network:** fail if a loader reaches live sources, operator systems, map services, public APIs, model runtimes, or release services.
11. **Cross-lane ownership:** reject transport-as-infrastructure duplication, model-as-observation, hazard-context-as-alert, or person/parcel authority collapse.
12. **Temporal separation:** reject collapsed observed, valid, retrieval, release, expiry, stale, correction, and withdrawal times.
13. **Evidence and policy:** require synthetic evidence closure for claim-like `ANSWER`; otherwise return a finite fail-closed outcome.
14. **Rights and sensitivity:** require reviewable synthetic posture and the most restrictive applicable boundary.
15. **Backlinks and expiry:** reject orphan pointers, missing consumers, missing owners, expired review dates, or absent removal triggers.
16. **Non-vacuity:** zero collected cases, all skipped cases, missing targets, or unsupported consumers are not success.
17. **Correction and rollback:** prove replacement and reversion leave consumers visibly correct or fail closed.
18. **Retirement:** after consumers migrate, remove compatibility material through a reviewed, history-preserving change.

### Outcome vocabulary

| Vocabulary | Meaning here | Boundary |
|---|---|---|
| `PASS` | Compatibility pointer or wrapper satisfies its bounded test contract. | Does not mean infrastructure information is true or safe to release. |
| `ANSWER` | Synthetic runtime example models evidence-resolved, policy-allowed output. | Does not create a real infrastructure answer or release. |
| `ABSTAIN` | Evidence, identity, time, freshness, citation, ownership, or review support is insufficient. | Preferred over inference. |
| `DENY` | Policy, rights, sensitivity, precision, reconstruction, operational, emergency, or release boundary blocks exposure. | Fail-closed governance outcome. |
| `ERROR` | Fixture, pointer, loader, schema, transform, or runtime setup is malformed, missing, nondeterministic, or network-dependent. | Operational failure, not policy denial. |

Do not collapse test pass/fail, runtime outcomes, policy decisions, review states, release states, and lifecycle states into one status field.

### README validation performed for this revision

- Verified one H1 and the twelve required folder-README H2 headings in the mandated order.
- Verified every repository-relative file link used by the revision against the pinned base.
- Checked balanced fenced blocks, unique heading anchors, final newline, and absence of trailing whitespace.
- Reviewed the proposed content for secrets, private data, exact sensitive locations, operational detail, real infrastructure data, and new external dependencies.
- Compared the remote branch against the pinned base and required exactly one changed path.
- Did not claim fixture regeneration, recursive inventory, consumer execution, sensitivity-policy execution, infrastructure correctness, or release validation.

[Back to top](#top)

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life`. This is a verified GitHub review route, not proof of semantic ownership, independent review, sensitivity approval, completed review, or branch-protection enforcement.

Review should cover every materially affected responsibility:

- fixture stewardship for placement, compatibility, deterministic identity, and retirement;
- Settlements/Infrastructure domain stewardship for asset, facility, operator, service-area, condition, and dependency meaning;
- the exact consumer owner for any retained compatibility item;
- schema and contract owners when a fixture claims conformance;
- sensitivity, rights, security, privacy, evidence, policy, temporal, and release reviewers when those concerns appear;
- Roads/Rail, Hydrology, Hazards, People/Land, Archaeology, cultural, ecological, or tribal reviewers for cross-lane cases; and
- security review for archives, decompression, parsers, paths, network access, credentials, generated outputs, precision recovery, or sensitive topology.

| Change class | Minimum review concern |
|---|---|
| README-only clarification | Fixture, domain, and sensitivity documentation boundary. |
| New compatibility pointer | Consumer owner, accepted target, expiry, non-duplication, and removal plan. |
| New synthetic wrapper | Fixture, consumer, domain, reproducibility, no-network, rights, sensitivity, and reconstruction review. |
| Geometry or attribute change | Precision, generalization, reconstruction, redaction receipt, and cross-fixture joins. |
| Condition or dependency scenario | Default denial, named-party boundaries, logging, reason codes, and negative counterpart. |
| Operator, service-area, or parcel-adjacent case | Privacy, time scope, authority, and person/land review. |
| Cross-lane fixture | Every owning domain plus evidence, policy, and sensitivity review. |
| Expected outcome change | Contract, consumer, policy, evidence rationale, and rollback target. |
| Path migration or retirement | Complete inventory, reference update, compatibility window, drift or migration note, and rollback. |
| Release-gating use | Separate release authority and independently reviewed failure behavior. |

Do not preserve a legacy path merely for symmetry, and do not retire it merely because indexed search was empty. Both decisions require a sufficiently complete inventory and consumer audit.

[Back to top](#top)

## Related folders

| Path | Relationship |
|---|---|
| [`fixtures/README.md`](../README.md) | Parent fixture-root scope; currently recognizes this top-level lane. |
| [`fixtures/domains/settlements-infrastructure/`](../domains/settlements-infrastructure/README.md) | Working reusable domain placement; currently a greenfield stub. |
| [`fixtures/domains/infrastructure-generalized/`](../domains/infrastructure-generalized/README.md) | Existing generalized-domain alias; authority and migration relationship remain unresolved. |
| [`tests/fixtures/settlements-infrastructure/`](../../tests/fixtures/settlements-infrastructure/README.md) | Unit-test-scoped fixture lane. |
| [`tests/domains/settlements-infrastructure/`](../../tests/domains/settlements-infrastructure/README.md) | Domain test boundary. |
| [`docs/domains/settlements-infrastructure/README.md`](../../docs/domains/settlements-infrastructure/README.md) | Parent domain dossier and evidence boundary. |
| [`CANONICAL_PATHS.md`](../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | Domain path registry naming the working `settlements-infrastructure` segment. |
| [`ARCHITECTURE.md`](../../docs/domains/settlements-infrastructure/ARCHITECTURE.md) | Domain architecture and lifecycle boundary. |
| [`infrastructure.md`](../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md) | Infrastructure object-family dossier at a path whose own metadata records placement conflict. |
| [`DENY_BY_DEFAULT.md`](../../docs/domains/settlements-infrastructure/DENY_BY_DEFAULT.md) | Critical-asset fail-closed guidance. |
| [`contracts/domains/settlements-infrastructure/`](../../contracts/domains/settlements-infrastructure/README.md) | Semantic contract lane. |
| [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Machine-shape lane. |
| [`policy/domains/settlements-infrastructure/`](../../policy/domains/settlements-infrastructure/README.md) | Domain policy home. |
| [`data/registry/sources/settlements-infrastructure/`](../../data/registry/sources/settlements-infrastructure/README.md) | Governed source-registry boundary. |
| [`release/candidates/settlements-infrastructure/`](../../release/candidates/settlements-infrastructure/README.md) | Pre-publication candidate-review boundary. |
| [`NO_NETWORK_TEST_RUNBOOK.md`](../../docs/runbooks/settlements-infrastructure/NO_NETWORK_TEST_RUNBOOK.md) | Draft no-network test guidance; commands remain evidence-bounded. |
| [`tools/validators/facilities/`](../../tools/validators/facilities/README.md) | Proposed cross-domain facility-validator documentation; not proof of executable validation. |
| [`tools/validators/hazard-exposure/`](../../tools/validators/hazard-exposure/README.md) | Proposed hazard-exposure validator documentation; not emergency authority. |
| [`docs/domains/roads-rail-trade/SENSITIVITY.md`](../../docs/domains/roads-rail-trade/SENSITIVITY.md) | Transport-adjacent sensitivity and publication guidance. |
| [`domain-settlements-infrastructure.yml`](../../.github/workflows/domain-settlements-infrastructure.yml) | Current read-only readiness workflow and explicit holds. |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Live contribution-preflight placement and required README contract. |
| [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Drift register; no entry for the three fixture paths was found at the evidence snapshot. |

[Back to top](#top)

## ADRs

No accepted ADR authorizing this top-level lane or `fixtures/domains/infrastructure-generalized/` as a second reusable Settlements/Infrastructure fixture authority was established.

Relevant ADR files are present but remain draft or proposed:

| ADR | Status at the evidence snapshot | Relevance |
|---|---|---|
| [`ADR-0010 — Deny-by-Default for DNA, Rare Species, Archaeology, and Critical Infrastructure`](../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | `draft` / `proposed`; ADR number and topic overlap are conflicted | Proposes fail-closed handling for critical infrastructure; supports caution but does not settle fixture placement. |
| [`ADR-0025 — Public Client Never Reads Canonical or Internal Stores`](../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md) | `draft` / `proposed`; acceptance needs verification | Proposes public trust-membrane enforcement; does not authorize fixtures as a public data path. |

An accepted ADR or equally explicit governed migration decision is required before a change:

- creates or ratifies a parallel domain fixture authority;
- changes the working `settlements-infrastructure` domain segment;
- retires or repurposes either generalized-infrastructure alias in a way that changes compatibility obligations;
- establishes a new schema, contract, policy, source-registry, proof, release, or publication home;
- weakens critical-infrastructure sensitivity, reconstruction resistance, trust-membrane, or public-path controls; or
- changes object meaning rather than supplying a bounded synthetic example.

Routine README correction and removal of an unused compatibility wrapper may use a focused reviewed change when complete inventory and consumer evidence show no authority or safety change. An actual move must preserve history, references, tests, validation, correction, and rollback.

[Back to top](#top)

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-21` |
| Evidence base | `main@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566` |
| Review scope | Target and parent fixture READMEs; both domain fixture paths; placeholder families; domain and test-local fixture guidance; domain architecture, object-family, path, denial, contract, schema, policy, source-registry, candidate, ADR, drift, contribution, CODEOWNERS, Makefile, and workflow evidence; bounded indexed searches. |
| Inventory limit | No byte-complete recursive listing, ignored-file inventory, external-store inventory, branch-protection proof, runtime trace, source-data review, or release dependency graph was available. |
| Next scheduled review | By `2027-01-21`, or earlier on any trigger below. |

Review this README immediately when:

- any payload, pointer, wrapper, manifest, consumer, generator, validator, or workflow begins using this path;
- the working domain fixture scaffold is replaced with accepted fixture families;
- the generalized-domain alias changes, migrates, freezes, or retires;
- the parent fixture index or domain path registry resolves the three-path conflict;
- sensitivity, geometry, reconstruction, condition, vulnerability, dependency, operator, service-area, or cross-lane posture changes;
- CI begins collecting this lane, stops collecting it, reports zero cases, or changes required-check status;
- a relevant ADR is accepted, superseded, renumbered, merged, or rejected; or
- six months pass without a documented review.

### Correction, migration, and rollback

For a documentation-only revision, rollback is a transparent revert of the scoped commit. If compatibility material exists:

1. identify the exact item, consumer, accepted target, hashes, sensitivity posture, transform, and affected revisions;
2. stop unsafe or ambiguous consumers from resolving the item;
3. quarantine prohibited real, sensitive, rights-unclear, reconstructable, or operational material through the appropriate governed incident path;
4. restore the last reviewed synthetic wrapper or fail closed if none is safe;
5. update the accepted fixture, compatibility pointer, consumer, expected outcome, and backlinks together;
6. record correction reason, precision and reconstruction impact, source-role and temporal impact, and retirement state;
7. rerun deterministic, no-network, geometry, reconstruction, condition/dependency denial, cross-lane, evidence, policy, sensitivity, and nonempty-collection checks; and
8. remove the compatibility item only after consumer migration and rollback are verified.

Do not rewrite shared history or casually delete external objects. If secrets, restricted infrastructure detail, protected data, exact sensitive locations, or live operational content enter Git history, stop normal fixture work and use the repository’s private-first security, credential-revocation, legal, and incident-response procedures.

### Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Complete inventory of all three fixture paths | `NEEDS VERIFICATION` | Byte-complete recursive listing plus ignored, generated, LFS, and external-store review. |
| Active consumers and inbound references | `NEEDS VERIFICATION` | Complete code, workflow, docs, generated-source, and runtime dependency graph. |
| Accepted reusable domain fixture authority | `NEEDS VERIFICATION` | Fixture and domain steward decision consistent with Directory Rules and accepted ADRs. |
| Generalized-domain alias classification | `CONFLICTED / NEEDS VERIFICATION` | Migration, compatibility, mirror, or retirement decision with backlinks. |
| Top-level compatibility classification | `PROPOSED / NEEDS VERIFICATION` | Parent README reconciliation and consumer evidence. |
| Migration owner, deadline, and compatibility window | `NEEDS VERIFICATION` | Accepted stewardship record and dated migration plan. |
| Canonical target for every retained item | `NEEDS VERIFICATION` | Manifest and remote hash validation. |
| No-duplication and deterministic identity | `NEEDS VERIFICATION` | Clean no-network pointer-resolution or regeneration checks with matching hashes. |
| Geometry and reconstruction resistance | `NEEDS VERIFICATION` | Collected tests across attributes, joins, tiles, zooms, adjacent fixtures, and releases. |
| Condition, vulnerability, and dependency denial | `NEEDS VERIFICATION` | Collected negative tests with stable reason codes. |
| Operator, service-area, person, and parcel safeguards | `NEEDS VERIFICATION` | Reviewed synthetic cases and fail-closed policy/test evidence. |
| Cross-lane ownership and sensitivity | `NEEDS VERIFICATION` | Collected tests preserving domain ownership and the most restrictive posture. |
| Temporal and stale-state coverage | `NEEDS VERIFICATION` | Collected tests preserving observed, valid, retrieval, release, expiry, and correction time. |
| Dedicated compatibility validation | `NEEDS VERIFICATION` | Named CI job rejects orphan, duplicate, missing target, network use, reconstruction, zero collection, and expired wrapper. |
| Semantic ownership and required review | `NEEDS VERIFICATION` | Accepted owner assignments and verified branch-protection behavior. |
| Release or public dependency | `UNKNOWN` | Accepted release contract or complete consumer inventory proving presence or absence. |

[Back to top](#top)
