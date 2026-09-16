# Evidence resolver validator

Repository-facing CLI wrapper for the package-local v1alpha1 evidence candidate
check. It inherits validator authority limits from
[`tools/validators/`](../README.md).

## Boundary contract

- Purpose: run one explicit input or the synthetic fixture suite, including
  the shared `VerificationStateHistory` validation and replay gate.
- Owner: evidence/proof and validation stewards — `OWNER_TBD`.
- Input: bounded JSON matching the internal candidate profile.
- Output: deterministic JSON for one input, or pass/fail fixture summaries.
- Exit codes: `0 RESOLVED`, `2 UNRESOLVED`, `3 DENIED`, `4 ERROR`;
  fixture mode returns `0` only when all selected expectations match.
- Prohibited: registry/network/store access, evidence creation, policy
  evaluation, review/release action, public response generation, or publishing.
- Exposure/retention: local/CI diagnostic only; nothing is persisted.
- Rollback: revert the validator with its package, fixture, test, Make, and
  workflow surfaces.
- Discovery: fixture-suite mode reads candidate cases only from the ratcheted
  `valid/` and `invalid/` lanes. It deliberately excludes the sibling
  `repository/` adapter configuration lane.

```text
tools/validators/evidence_resolver/
├── README.md
└── validate_candidate.py
```

Run through `make evidence-resolver` or `make evidence-resolver-deny`. A pass
means only that the declared internal fixture expectations matched. The
validator performs no filesystem history lookup: the bounded history and both
as-of instants must be supplied in the input.

## Reproduce the Atlas review candidate

From the repository root, with the repository's declared Python test dependencies
installed and that environment's `python` active:

```bash
git rev-parse HEAD
git status --short
make atlas-review
```

Record the displayed commit and any working-tree changes with the result.
The command does not assert that a modified worktree equals its commit. It
performs local checks only and does not fetch, install dependencies, request
reviews, dispatch hosted workflows, create a PR or change a Site.

The target runs these existing entrypoints in order:

1. Resolver package tests, verification-history/profile tests, native governed
   API tests and the Explorer adapter boundary test in one pytest invocation.
2. The verification-history fixture CLI, including the explicit synthetic
   Atlas profile and its mixed-version/wrong-subject negatives.
3. The complete evidence-candidate fixture CLI, including its negative cases.
4. The generated-receipt validator against this command's receipt,
   `data/receipts/generated/genrec-atlas-review-command-20260916.json`, then
   the profile receipt,
   `data/receipts/generated/genrec-atlas-verification-profile-20260916.json`,
   using the current worktree bytes.

`make atlas-review-tests` runs the first three steps when only technical replay
is needed. It makes no statement about the receipt or acceptance. The full
`atlas-review` target preserves every native failure: it stops on failed tests
or fixtures and does not suppress, reinterpret or whitelist receipt findings.
Receipt validation runs after its tests, including under `make -j`.

The expected disposition for profile parent
`6ad557c2f12d802d379ebcce5987a71440049993` is **tests PASS / receipt HOLD**.
The native receipt validator returns `POLICY_DECISION_REQUIRED` because the
canonical schema change has no applicable policy-decision reference recorded.
The validator exits `1`; GNU Make reports a nonzero failed target. This is a
real gate failure, not an expected-success test. Missing dependencies or another
finding must be diagnosed on its own evidence instead of being labeled the
known policy hold.

The profile's original 17 paths are preserved by this command-only follow-up.
Its fixture history is invented test input, not operational verification.
The fixed lookup remains on `atlas-lookup/verification-profile-review-required`;
an internal resolved result remains non-renderable.

To advance acceptance, the accountable policy/contract review must establish the
applicable decision, record its reference in a reviewed receipt follow-up and
rerun the full target. A nonempty reference alone is not proof of applicability,
authenticity or approval; those remain independent-review obligations. Hosted
checks, topology acceptance, server-owned same-subject records, positive real
API/browser transport and operational recovery remain separate gates.

The [semantic contract](../../../contracts/evidence/verification_state_history.md#explicit-subject-profiles)
and [issue #3381](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3381)
hold the detailed profile and acceptance boundary. Revert the Make targets and
this documentation together to remove the convenience command; no runtime or
stored state requires migration or rollback.
