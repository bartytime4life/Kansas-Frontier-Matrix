# GitHubIssueInventoryRead Contract

Status: **PROPOSED_INACTIVE** authenticated read-only repository-state profile.

`GitHubIssueInventoryRead` is a value-minimized, read-only observation of GitHub issue state for one bound repository and default-branch ref. It exists to support the BriefingSignal issue-routing verification boundary without turning issue metadata into evidence, repository authority, or mutation permission.

## Purpose

The fixture-backed `IssueInventoryProjection` remains the deterministic contract-test profile. This live-read profile is separate: it may call GitHub only when explicitly invoked with a read credential, records repository/ref identity and rate-limit metadata, emits only issue number/state/update time, and fails closed when authentication, repository binding, freshness, or rate-limit safety is unresolved.

## Required behavior

- HTTP method is `GET` only.
- Credential comes from `KFM_GITHUB_READ_TOKEN` or `GITHUB_TOKEN`; it is never serialized or logged.
- Repository metadata binds `repository`, numeric `repository_id`, `default_branch`, and `default_branch_head_sha`.
- Requested issue numbers are unique, sorted, positive integers.
- Pull requests returned through the Issues API are rejected from this issue-only projection.
- Each issue row contains only `number`, `state`, and `updated_at`.
- `retrieved_at` and `stale_at` make freshness explicit; expired projections are unusable.
- Rate-limit remaining/reset values are recorded when supplied. A response with no remaining budget is a finite hold, not a successful routing input.
- `response_digest` and `receipt_id` deterministically bind the minimized result and transport metadata.
- `repository_mutation_allowed`, `authority_created`, `evidence_created`, `release_authorized`, `publication_authorized`, and `public_use_allowed` are always `false`.

## Finite outcomes

- `FRESH` — authenticated read succeeded, repository/ref binding is complete, requested issues were observed, freshness window is open, and rate-limit posture is usable.
- `STALE` — the projection exceeded its freshness window.
- `HOLD_AUTH` — no usable read credential or authentication failed.
- `HOLD_RATE_LIMIT` — rate-limit state does not permit a reliable read.
- `HOLD_BINDING` — repository/ref identity could not be established.
- `ERROR` — malformed response, unexpected pull-request object, transport failure, or internal validation failure.

## Trust boundary

A `FRESH` record proves only that the named GitHub API responses were observed through a read-only adapter at a recorded time. It does not authorize issue mutation, merge, branch writes, source admission, evidence, policy, review, proof, release, deployment, publication, or public truth. It does not prove that an issue body or comment is correct.

## Directory Rules basis

Semantic meaning is owned by `contracts/governance/`; the closed machine shape by `schemas/contracts/v1/governance/`; deterministic API-response fixtures by `fixtures/contracts/v1/governance/`; the diagnostic read adapter by `tools/probes/`; enforceability by `tests/governance/`; and CI orchestration by `.github/workflows/`. No new root or parallel authority home is introduced.
