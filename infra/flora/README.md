# Flora infrastructure placement hold

`infra/flora/`

Status: **CONFLICTED / DOCUMENTATION ONLY / NO INFRASTRUCTURE PAYLOAD**

This README records the tracked state and placement hold for the direct
`infra/flora/` child. It does not establish this path as an accepted
infrastructure family, authorize Flora deployment, or provide evidence of a
running service or environment.

## Current repository state

At `main@4f1a3087facf259db058733728cb3d2187f7ef9b`, this directory contains
exactly two tracked files:

| Path | Evidence | Safe interpretation |
|---|---|---|
| `README.md` | Human-maintained Markdown boundary | Documents the hold; not infrastructure configuration |
| `.gitkeep` | Zero-byte placeholder | Preserves the directory only; not adoption or implementation evidence |

No Dockerfile, Compose file, proxy or firewall rule, service unit, Kubernetes
manifest, Terraform configuration, environment template, route inventory,
secret reference, test, validator, or deployment payload is tracked here.
Whether externally managed Flora infrastructure exists is **UNKNOWN**.

## Placement status

[Directory Rules](../../docs/doctrine/directory-rules.md), adopted through
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md),
assign deployment, network, host, access, secret-reference, and exposure
configuration to `infra/`. They also require the owning root and artifact
family to be known before adding a scope segment.

The current [infrastructure root](../README.md) explicitly classifies this
direct domain-named child as **CONFLICTED / NEEDS VERIFICATION**. It says not to
use the path as precedent or expand it until a reviewed placement decision,
migration note, or ADR resolves the boundary.

The [Flora domain README](../../docs/domains/flora/README.md) and
[Flora file-system plan](../../docs/domains/flora/FILE_SYSTEM_PLAN.md) describe
Flora as a segment inside responsibility roots, but both documents are drafts.
They do not admit deployment payloads here or override the accepted
infrastructure root.

The safe current conclusion is therefore:

- the tracked direct child exists;
- its placement is unresolved;
- it contains no implementation-bearing payload;
- it is not a canonical pattern for another `infra/<domain>/` directory; and
- this documentation change neither retains nor rejects the path permanently.

## Admission hold

Do not add infrastructure payloads under this directory until a review packet
closes all applicable questions:

1. What concrete service, environment, or exposure change needs the file?
2. Which standard infrastructure family owns it—such as
   [Docker](../docker/README.md), [Compose](../compose/README.md), or
   [firewall](../firewall/README.md)?
3. Why is a direct `infra/flora/` segment necessary instead of placement
   inside that established family or in Flora documentation/runbooks?
4. What accepted decision, migration note, or ADR authorizes the chosen path?
5. Who is accountable for the payload and its operational validation?
6. What public/private routes, identities, mounts, secrets, data phases,
   positive checks, required denials, and rollback steps apply?

If those questions cannot be answered from current evidence, leave the payload
out of this lane and record the unresolved placement rather than guessing.

## Authority and safety boundary

This lane does not own Flora meaning, source admission, machine schemas,
contracts, policy, lifecycle data, proofs, receipts, release decisions, or
published artifacts.

- Public clients must use governed interfaces or released public-safe
  artifacts, not canonical stores or this directory.
- RAW, WORK, QUARANTINE, unpublished candidates, source credentials, direct
  model runtimes, proofs, receipts, and release material must not become public
  paths or default mounts through Flora infrastructure.
- Where Flora material includes rare-species locations or other sensitive
  geometry, the applicable policy and release decision—not infrastructure
  prose—controls whether and how it may be disclosed.
- A build, scan, open port, health check, merge, or deployment does not prove
  Flora truth, evidence closure, policy approval, release, or publication.

## Evidence map

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| [Infrastructure root](../README.md) | Canonical `infra/` responsibility and the direct-child conflict | Final placement for Flora infrastructure |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | Accepted root and segment-placement rules through ADR-0029 | A specific Flora deployment topology |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption of Directory Rules v2 | Adoption of this child lane |
| [Flora domain README](../../docs/domains/flora/README.md) | Draft domain-lane context | Infrastructure implementation or deployment authority |
| [Flora file-system plan](../../docs/domains/flora/FILE_SYSTEM_PLAN.md) | Draft candidate placement and recorded conflicts | Accepted resolution of this path |
| `.gitkeep` | The empty placeholder is tracked | A service, owner, validator, environment, or operational state |

## Maintenance and validation

Recheck this README when:

- a child file is added, removed, or proposed;
- the parent infrastructure root changes this path's classification;
- an accepted ADR or migration note resolves the placement;
- a real Flora service, environment, route, or deployment consumer appears; or
- a standard infrastructure lane admits Flora-scoped payloads.

For a documentation-only change, validate the complete diff, GFM structure,
relative links, and exact tracked inventory. If a future payload is admitted,
run the tool-specific checks required by its owning standard infrastructure
lane and retain separate runtime, environment, release, and rollback evidence.

## Open questions

- Should the direct child be retained, moved, or removed?
- If retained, what artifact family and placement rule make it necessary?
- Are any Flora services or environments implemented outside this tracked lane?
- Who holds accountable infrastructure and Flora operational stewardship?
- What validation and rollback evidence would be required for the first
  implementation-bearing payload?

Until those questions are resolved, the lane remains a documentation-only
placement hold.

## Rollback

Before merge, close the documentation PR. After merge, revert the scoped
Markdown commit without rewriting shared history. No operational rollback is
implied because this directory contains no tracked infrastructure payload.
