# Implementation review packet contract

**Profile status:** PROPOSED / INACTIVE  
**Execution mode:** `LOCAL_NO_NETWORK`  
**Authority:** `NONE`

## Purpose

The implementation review packet is a deterministic reviewer view over two
existing KFM governance profiles:

1. one validated `ImplementationChangeContext`, which declares immutable Git
   range metadata and changed paths without raw diff or file content; and
2. zero or more validated `ImplementationDecisionRecord` documents, which
   contain explicitly authored rationale, alternatives, reviewer questions,
   support references, and rollback instructions.

The packet closes the mechanical review-context gap between those profiles. It
does not create a new truth-bearing record, infer why code changed, replace the
pull-request template, or grant review authority.

## Inputs

The command accepts exactly one context JSON path followed by zero or more
decision-record JSON paths:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_implementation_review_packet.py \
  path/to/implementation-change-context.json \
  path/to/decision-0001.json \
  path/to/decision-0002.json
```

Add `--render` to emit deterministic Markdown when the packet outcome is
`READY` or `HOLD`. An `ERROR` packet is never rendered; the command emits a
bounded JSON diagnostic instead.

The renderer admits at most 256 decision inputs. Input documents remain subject
to their own smaller schema and file-size bounds.

## Required validation order

An implementation MUST apply these checks in order:

1. validate the context with the canonical
   `ImplementationChangeContext` validator;
2. validate each decision with the canonical
   `ImplementationDecisionRecord` validator, including duplicate record-ID
   detection;
3. require exact set equality between
   `context.implementation_decision_refs` and the supplied decision
   `record_id` values;
4. require every decision `change_ref` to equal the context `context_id`; and
5. require every decision `scope.paths` entry to appear as either a changed
   destination path or a declared previous path in the context.

A decision record may cover a subset of the changed destination paths. Uncovered
paths are rendered as review information, not treated as a failure: a decision
record explains a material choice and is not a file manifest.

## Outcomes

| Outcome | Meaning | Exit code |
|---|---|---:|
| `READY` | Every input is internally ready and every cross-object binding is exact. | `0` |
| `HOLD` | Inputs are structurally valid, but the context or at least one decision remains held by its canonical validator. | `3` |
| `ERROR` | An input is invalid, the decision count is excessive, or an exact binding invariant fails. | `2` |

Input `HOLD` findings remain `HOLD`; the packet MUST NOT upgrade them to
`READY`. Any input or binding `ERROR` fails closed and suppresses Markdown
rendering.

## Deterministic reviewer view

For renderable inputs, the Markdown view contains only declared fields and
mechanically derived coverage:

- packet and input outcomes;
- repository, full base and head SHAs, context identity, and generation time;
- file counts, line-count metadata, binary count, top-level roots, signal codes,
  score, and decision-capture recommendation;
- a sorted changed-path table without diff hunks or file content;
- decision coverage and informational uncovered destination paths;
- held or less-confirmed decisions before ready, confirmed decisions;
- the chosen mechanism, rationale, alternatives, reviewer questions, evidence
  and validation references, governance links, and rollback for each record;
- consolidated reviewer questions; and
- an explicit trust boundary.

Input order and local filesystem locations are not meaning-bearing and MUST NOT
appear in the rendered packet. Reversing the same decision inputs MUST produce
identical bytes.

## Finding codes added by the packet

| Code | Classification | Meaning |
|---|---|---|
| `DECISION_LIMIT_EXCEEDED` | `ERROR` | More than 256 decision paths were supplied. |
| `DECISION_REFERENCE_SET_MISMATCH` | `ERROR` | Context references and supplied decision IDs are not the same set. |
| `DECISION_CHANGE_REF_MISMATCH` | `ERROR` | A decision does not bind to the validated context identity. |
| `DECISION_PATH_OUTSIDE_CHANGE` | `ERROR` | A decision claims a path absent from the changed or previous-path set. |
| `CONTEXT_<input-code>` | inherited | A canonical context finding, namespaced without changing its severity. |
| `DECISION_<input-code>` | inherited | A canonical decision finding, namespaced without changing its severity. |

Finding payloads are value-minimized. Decision findings identify the stable
`record_id`, not the local input filename or absolute path.

## Content and privacy boundary

The packet reads the closed JSON fields supplied by the two canonical
validators. It MUST NOT:

- run `git diff`, read changed-file contents, or include raw hunks;
- infer, summarize, or reconstruct a rationale from repository content;
- store prompts, session transcripts, hidden reasoning, or person profiles;
- authenticate evidence or validation references;
- call a model, network service, GitHub API, or external executable; or
- write to the repository, a pull request, an issue, or a governed data lane.

Authored decision prose is rendered because it is an explicit field of a
validated decision record; it is not inferred from the changed files.

## Authority and non-effects

`READY` means only that the supplied records are internally valid and exactly
bound for human review. It does not:

- create or resolve evidence;
- prove the declared rationale;
- make a policy or review decision;
- authorize mutation, merge, promotion, release, deployment, or publication;
- replace `ReviewRecord`, ADR, release, rollback, or publication controls; or
- convert the proposed input profiles into adopted repository policy.

## Fixtures and validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_implementation_review_packet.py \
  --cases

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/validators/governance/test_implementation_review_packet.py
```

The fixture suite contains exact `READY`, `HOLD`, and `ERROR` polarity for
valid binding, inherited holds, reference mismatch, context-ID mismatch,
out-of-change scope, and invalid decision input.

## Rollback

Revert the review-packet contract, validator, fixtures, tests, workflow, source
map, and generated authoring receipt as one dependency-closed slice. The two
underlying profiles and their existing workflows remain unchanged, and no data
migration or publication rollback is required.
