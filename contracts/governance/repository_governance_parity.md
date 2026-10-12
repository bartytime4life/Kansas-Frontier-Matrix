<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/repository-governance-parity/v1
title: Repository Governance Parity and Drift Classification Contract
type: semantic-contract
version: v1.0.0
status: proposed; repository-grounded; schema-backed; implementation-partial; non-authoritative
owners:
  - UNKNOWN
created: 2026-08-22
updated: 2026-08-22
policy_label: internal-governance; validation-projection-only; fail-closed; no-network
owning_root: contracts/
responsibility: define the MRTS-04 composition and classification boundary across existing registry path topology and public-boundary validators without redefining their rules expanding their baselines or turning inherited repository drift into conformance
truth_posture: CONFIRMED accepted Directory Rules existing 20-rule topology engine root and alias validators merged MRTS-02 registry packet merged MRTS-03 catalog and current inherited topology counts / PROPOSED this parity profile schema validator fixture test workflow and receipt packet / UNKNOWN accountable closure owners and required-check coupling / NEEDS VERIFICATION human review hosted exact-head results and eventual inherited-drift disposition
related:
  - ../../control_plane/repository_governance_parity.yaml
  - ../../schemas/contracts/v1/governance/repository_governance_parity.schema.json
  - ../../tools/validators/directory_governance/validate_repository_governance_parity.py
  - ../../tools/validators/directory_governance/validate_repository_topology.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "A green parity-profile check proves exact classification and validator coverage, not repository topology conformance."
  - "The current repository conformance outcome remains HOLD_INHERITED while the pinned 9/125/13 topology state persists."
[/KFM_META_BLOCK_V2] -->

# Repository Governance Parity and Drift Classification Contract

## Purpose

This contract defines the smallest MRTS-04 layer missing above the existing
governance validators: deterministic composition, exact coverage binding, and
feature-base comparison. It answers whether all required validator owners ran,
whether the topology baseline remained monotonic, and whether a change
introduced new topology findings.

It does not replace the owning validators. In particular, it does not copy the
20 topology rules or make their current failures disappear.

## Inputs and pinned authority

The canonical projection is
`control_plane/repository_governance_parity.yaml`. It binds a full Git commit
SHA and SHA-256 values for:

- the accepted Directory Rules and ADR-0029;
- the root and path-alias registries;
- the topology engine; and
- its exact inherited-drift baseline.

Canonical validation reads those bytes from the pinned Git tree. Mutable
working-tree bytes cannot satisfy a historical digest.

The projection is validation routing only. It cannot amend doctrine, accept an
ADR, create a root, activate an alias, assign authority, or authorize writes.

## Composed lanes

| Lane | Existing owner | Required result |
|---|---|---|
| Control-plane registry packet | MRTS-02 validator | `PASS` |
| Object-family register | MRTS-03 validator | `PASS` |
| Root registry | Existing directory-governance validator | `PASS` |
| Path-alias register | Existing directory-governance validator | `PASS` |
| Public boundary guards | Existing policy and governed-API boundary tests | `PASS` |
| Repository topology | Existing 20-rule engine | `HOLD_INHERITED` at this pinned checkpoint |

`NOT_RUN`, timeout, missing owner, or execution error can never be rewritten as
`PASS`.

## Acceptance-criterion coverage

The profile binds every MRTS-04 criterion to its owner lanes and, where
applicable, exact topology rule IDs:

- registry reference, digest, and stable-ID integrity;
- portable path grammar, registered roots, normalized planes, and alias state;
- duplicate schema and human authority IDs;
- policy-source placement and populated policy boundaries;
- trust-shaped object placement;
- deployable/public separation from internal lifecycle and direct model paths;
- generated artifact provenance;
- active alias expiry and closure;
- check-not-run separation; and
- monotonic topology-baseline transition.

The parity validator fails if a criterion, lane, owner path, or rule binding is
removed or substituted.

## Inherited-versus-introduced classification

The validator creates a temporary Git index for the exact `base_ref`, runs the
unchanged topology scanner against that tree, and compares finding
fingerprints with the current index. The temporary index is deleted after use.

- A current fingerprint absent from the feature base is introduced drift and
  fails the profile.
- A base fingerprint absent from current state is a resolved finding and is
  allowed, subject to the owning topology ratchet.
- An unchanged finding remains inherited; it is never called conformance.
- Any baseline addition, protected-metadata mutation, expiry extension, or
  non-shrinking evidence replacement fails closed through the existing
  topology transition validator.

At the pinned MRTS-04 base, the repository has 9 unbaselined drift findings,
125 baselined warnings, and 13 stale baseline fingerprints. Therefore the
repository-level outcome is `HOLD_INHERITED`, even when parity-profile integrity
is `PASS`.

## Output semantics

The JSON projection separates:

- `profile_integrity_outcome`: whether coverage, execution, pinned evidence,
  and classification are valid; and
- `conformance_outcome`: whether the repository is conforming, held by exact
  inherited drift, failed by introduced drift, or not evaluated.

A workflow may be green for exact profile integrity while its summary still
records `HOLD_INHERITED`. Consumers must never interpret that green check as a
passing topology result, waiver, migration approval, or release approval.

## Security and resource bounds

- No network request is made after declared dependency installation.
- Commands are repository constants; instance data cannot supply shell text,
  package names, URLs, or executable arguments.
- Git refs must be full commit SHAs.
- Git reads use argument arrays, timeouts, regular-file mode checks, and bounded
  blob sizes.
- Lane output is not echoed, preventing untrusted repository content from
  entering public diagnostics.
- Fixture and current reports emit stable codes and counts rather than source
  payloads or sensitive values.

## Fixtures and tests

The fixture matrix contains one valid inherited-hold case and negative cases
for:

- check not run;
- a failed validator lane;
- introduced topology drift;
- baseline growth;
- missing criterion coverage; and
- an inherited failure mislabeled as pass.

Focused tests also cover strict Draft 2020-12 schema validity, duplicate YAML
keys, exact lane/rule coverage, pinned-tree replay, non-authority output, and
no-echo behavior.

## Rollback and forward fix

Before merge, abandon the isolated change. After an authorized merge, revert
the profile, schema, validator, fixtures, tests, workflow, Make target, registry
entry, contract, and receipt as one packet, or forward-fix those same paths.
Never expand the topology baseline or alter an owning validator merely to make
this composition check green.

## Non-effects

This packet does not:

- accept or amend an ADR;
- activate a source, root, alias, policy, object family, or public route;
- assign owners or reviewers;
- mutate a governance registry or lifecycle state;
- waive, suppress, baseline, or resolve a topology finding;
- authorize migration or deletion;
- approve evidence, policy, review, release, correction, or rollback; or
- deploy, promote, publish, or change public-runtime behavior.
