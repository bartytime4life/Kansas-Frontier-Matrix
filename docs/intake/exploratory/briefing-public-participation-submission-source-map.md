# Briefing public-participation submission source map

Status: **PROPOSED**
Scope: evidence map for an inactive, fixture-only assessment candidate

## Source claims

| Claim | Truth label | Evidence |
|---|---|---|
| A `CommentWindow` is a time-bounded period during which an authority accepts public input. It does not prove that any particular submission was accepted or acted upon. | CONFIRMED | `KFM_Briefing_to_System_Integration_Architecture.docx`, sections 15.1–15.3; Google Drive file `1UnJ3dl9ZFvWHM01pYnqdoh0OOWinSFUg` |
| A `Submission` is a received comment, testimony, or document with privacy and publication posture. It does not imply endorsement or decision. | CONFIRMED | Same briefing, sections 15.1–15.3 |
| Only released, public-safe submissions may be shown publicly; personal information and restricted attachments require protection. | CONFIRMED | Same briefing, Lane D public-participation requirements |
| Announcement, receipt, review, recommendation, decision, implementation, and outcome must remain separate states or objects. | CONFIRMED | Same briefing, required transition sequence |
| Accepted directory governance assigns contracts to meaning, schemas to shape, fixtures to examples, validators to deterministic checks, tests to behavior, workflows to orchestration, intake docs to source adaptation, and receipts to generated process memory. | CONFIRMED | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`; `docs/doctrine/directory-rules.md` |

## Repository assay at base `7d3b894deeb82d3ecb0ddf3daeec9158f266edb1`

The current `GovernanceEvent` profile already supplies the umbrella event
identity and keeps `comment_window_refs` and `submission_refs` distinct. This
proposal does not redefine that authority object. It fills the next sourced
idea listed in `docs/intake/exploratory/briefing-governance-event-source-map.md`:
an assessment of comment-window timing plus submission privacy/publication
posture.

Searches across contracts, schemas, validators, tests, workflows, exploratory
source maps, and open pull requests found no dedicated profile with this exact
boundary. Adjacent release, consent, redaction, and governance-event artifacts
remain authoritative in their own domains.

## Implemented proposal

The packet adds:

- one normative meaning document under `contracts/governance/`;
- one closed Draft 2020-12 schema under `schemas/contracts/v1/governance/`;
- one synthetic exact-polarity fixture matrix;
- one deterministic, no-network validator with value-free diagnostics;
- focused tests and a read-only GitHub Actions workflow; and
- one generated authorship receipt.

The candidate stores reference identifiers and a payload digest only. It cannot
store submission content or submitter contact data. `RELEASE_REFERENCE_ONLY`
can acknowledge an already governed release reference, but all release,
publication, public-use, acceptance, review-approval, recommendation, and
decision effects remain false.

## Explicit non-goals

- No comment intake endpoint, mailbox, web form, or calendar integration.
- No acceptance, moderation, endorsement, recommendation, or decision engine.
- No privacy classification engine or redaction transformation.
- No release creation, publication, map layer, API route, or UI.
- No database migration, source activation, or existing contract mutation.

## Activation gates

Activation is future work and requires an accepted ADR, named governance and
privacy owners, protected-content threat review, migration and rollback plan,
release-policy integration, representative non-sensitive fixtures, and explicit
human approval. Until then, every artifact in this packet remains proposed or
fixture-confirmed only.
