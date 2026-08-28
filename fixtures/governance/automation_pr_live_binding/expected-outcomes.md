# Expected live-binding outcomes

The temporary-Git test harness is the executable fixture surface. Expected outcomes are:

| Case | Expected outcome | Required reason |
|---|---|---|
| exact declared base/head/path/blob binding | `PASS` | none |
| declared digest differs from live candidate blob | `ERROR` | `ARTIFACT_DIGEST_MISMATCH` |
| live diff contains an undeclared candidate path | `ERROR` | `LIVE_CHANGED_PATH_MISMATCH` |
| live diff contains a path outside `data/work/automation/` | `ERROR` | `UNSAFE_LIVE_CHANGED_PATH` |
| current base moved after the proposal base SHA | `ERROR` | `BASE_SHA_MISMATCH` and `HEAD_NOT_BASED_ON_CURRENT_MAIN` |
| proposal policy outcome is not `PASS` | `ERROR` | `PROPOSAL_NOT_WRITE_ELIGIBLE` |
| candidate blob is executable rather than ordinary `100644` data | `ERROR` | `UNSAFE_CANDIDATE_BLOB_MODE` |

These are synthetic conformance expectations. They do not authorize a live GitHub mutation.
