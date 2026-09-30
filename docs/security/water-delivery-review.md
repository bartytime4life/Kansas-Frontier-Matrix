# Water delivery security and repository-control review

Status: proposed settings correction; no GitHub rule, host service or Site
publication was changed. This document supports review, not an approval record.

Pinned repository: 6994a65843c4999313fda01183b63333213134f3.
Pinned Site security baseline: v126 / 02500808ce96081db3613ca7200abdf67334b343.
The unpublished delivery candidate is based on v129 and includes separate
changed-area inspection and tests. The baseline reviews are partial: 86
monorepo files and 178/236 Site files (all 141 app TypeScript/TSX files).
No full-repository clean-security claim is made.

The validated Site baseline finding is low-severity owner-import KML text
CPU exhaustion. Linear text stripping before entity decoding and bounded text
fields repair it in the candidate, with CDATA/entity regressions. No browser
exploit timing was measured. Dependency reconciliation yields zero npm audit
findings in the candidate: Next/eslint-config-next 16.3.7, Undici 7.29.1 and
fast-uri 3.1.8. Vendored Vinext's next/og shim and application imports were
inspected; package presence did not establish deployed advisory reachability.
Generated production output built successfully; no runtime penetration test is
claimed. The live v129 Site has not received these candidate repairs.

New water serving checks reject tampered artifacts, inconsistent evidence,
missing approvals, expiry and withdrawal. Exact-query checks and fixed storage
keys prevent caller-directed upstream access. Ordinary reads cannot write the
activation store. Local activation mechanics assume trusted operator metadata;
they do not establish human review authenticity from arbitrary reference strings.
Hosted owner staging/review/activation remains open. Log fields exclude arbitrary
query text and raw errors. Mocked D1/R2 failures are tested; deployed D1/R2
integration and browser acceptance remain unverified.

The Qwen bridge now allows exactly 127.0.0.1:4173; a live temporary bridge probe
returned ready for that origin and 403 for port 41730. No model request was
needed. The installed original bridge was not restarted. Ollama's host override
explicitly sets 0.0.0.0:11434; only loopback consumers were observed in the
bounded connection snapshot. Remote reachability and future consumer dependency
remain unknown. Review the loopback drop-in example before any host restart.

## Ruleset correction for owner review

Live readback of ruleset 15484585 (`Protect`) found deletion/non-fast-forward
protection, zero approving reviews, no required status checks and an always
bypass for the owner. CONTRIBUTING records retirement of the old transition
authorization check; this proposal does not reinstate it.

Preserve the current default-branch condition and allowed merge methods.
The proposed replacement review/check parameters are:

```json
{
  "bypass_actors": [],
  "rules": [
    {"type":"deletion"},
    {"type":"non_fast_forward"},
    {"type":"pull_request","parameters":{
      "allowed_merge_methods":["merge","squash","rebase"],
      "dismiss_stale_reviews_on_push":true,
      "require_code_owner_review":false,
      "require_last_push_approval":true,
      "required_approving_review_count":1,
      "required_review_thread_resolution":true
    }},
    {"type":"required_status_checks","parameters":{
      "strict_required_status_checks_policy":true,
      "required_status_checks":[
        {"context":"scaffold-inventory"},
        {"context":"governed-api-tests"},
        {"context":"envelope-shape-tests"},
        {"context":"water-conformance"}
      ]
    }}
  ]
}
```

The first existing check contexts were observed or verified against their
workflow job IDs. `water-conformance` is introduced by this candidate; require
it only after a successful exact-head GitHub execution confirms its emitted name.
A separate reviewer must be available: a sole author cannot satisfy independent
review of their own pull request. Removing owner bypass changes emergency
operations; the owner must explicitly approve the complete settings change.
No settings-write command is run by the acquisition/monitoring jobs.

Non-merging verification after approval: preserve the exact ruleset JSON;
use a temporary canary PR to observe an unapproved revision blocked, one required
check failing blocked, and all required checks plus independent current-head
review eligible. Never merge the canary. Re-read rule enforcement and bypass
actors, then close the canary. A ruleset configuration read or local mock is
not proof of GitHub enforcement. Restore the preserved JSON if the authorized
rehearsal fails. This live positive/negative rehearsal remains pending.
