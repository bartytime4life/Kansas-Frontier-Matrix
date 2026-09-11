# Directory Governance Validators

Deterministic, no-network validators for the machine projections and decision records required by adopted KFM Directory Rules v2.

## Current slice

`validate_root_registry.py` validates:

- strict JSON-compatible YAML parsing;
- Draft 2020-12 schema conformance;
- the exact adopted Directory Rules digest and `ADR-0029` binding;
- canonical ordering and unique root identities/paths;
- class, status, target, activation, exit, and single-write invariants;
- canonical-root parity;
- top-level repository-root coverage at a pinned checkout;
- reviewed valid/invalid fixture polarity.

`validate_repository_topology.py` adds a twenty-rule, standard-library,
no-network ratchet over the tracked Git index. It covers root admission and root
files, safe path grammar and collisions, compatibility-root expansion,
collection spellings, speculative leaves, data and release lane placement,
policy-source singularity, trust-shaped artifacts, public/internal-store
separation, schema and document identities, generated-output provenance,
boundary READMEs, adopted-authority binding, and active-alias closure.

The 138 inherited finding groups recorded by ADR-0029's August 2026
checkpoint are historical, not a live inventory. Read the exact baseline's
`generated_from_ref`, entry set and expiry together with the validator's
`BOOTSTRAP_BASE_SHA` at the examined commit; obtain current counts from a fresh
run. Do not infer the bootstrap or current conformance from an old README count.

Baselined findings are warnings, not conformance claims: any addition or changed
fingerprint fails as new drift, any removed finding requires the baseline to
shrink in the same change, and invariant rules cannot be baselined.
In pull-request CI the proposed baseline is also compared with the trusted base
commit: waiver additions, waiver mutation, metadata changes, and deadline
extensions fail. These diagnostics do not authorize a new bootstrap or waiver.

`render_repository_topology_diagnostics.py` is a bounded diagnostic projection
for failed ratchet runs. It preserves the ratchet exit code and reports only the
failure disposition, rule id, subject, and fingerprint for new drift, invariant
findings, baseline mismatches, and stale baseline entries. It intentionally does
not emit evidence members or evidence digests, does not mutate the baseline, and
does not create path authority. Output is deterministically sorted and bounded
to 20 identities by default (maximum 50).

### Safe diagnostic identities

The diagnostic projection preserves ordinary ASCII identifier tokens. Other
values are rendered as reversible, ASCII-escaped JSON strings. Newlines,
carriage returns, terminal controls, bidirectional text and field delimiters
cannot create additional log structure. Colons and number signs inside quoted
tokens are escaped too, so embedded `::` and `##[` runner-command syntax remains
data even without a newline. Decode a quoted token with a JSON string parser;
do not execute it or interpolate its decoded value into shell code.

Encoding is presentation only. Original identities determine ordering and
deduplication; fingerprints, finding dispositions, count limits and validator
exit codes are unchanged. Evidence members/digests remain omitted. This is not
redaction, a source-truth check, or a repair of underlying topology findings.
The 20/50 limit bounds the number of identities, not a new per-token byte budget.

Regression coverage lives in the existing
`tests/validators/directory_governance/test_validate_output_security_topology.py`
module, which matches the topology test command below. Synthetic report and
mocked orchestration tests prove the display boundary, not a full repository
scan or execution on the hosted GitHub runner.

### Interpreting a failed run

Retain the raw validator exit and distinguish it from a diagnostic/upload step
that deliberately continues. Match repository, run ID/attempt, event, head SHA,
actual checkout and validator/baseline bytes before attributing a failure. A
pull-request merge checkout is not necessarily the PR head. If the log's rule
identities disagree with the pinned implementation, classify attribution as
`UNRESOLVED/NON_COMPARABLE`; do not reset a baseline, invent an owner, or waive a
rule to reconcile contradictory evidence. Test code and tests at the exact
candidate, and re-pin before delivery.

External implementation references (checked 2026-09-11):
[GitHub workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands),
[GitHub workflow logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs),
[GitHub pull-request events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request),
and [OWASP logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#event-collection).
These explain transport and logging risks; they do not establish KFM run results.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Boundary

A green validator result is conformance evidence for a projection. It does not create or activate roots, authorize compatibility writes, amend Directory Rules, approve an ADR, migrate or delete paths, grant evidence or policy authority, or authorize release, deployment, promotion, or publication.

## Commands

```bash
python tools/validators/directory_governance/validate_root_registry.py --fixtures
python tools/validators/directory_governance/validate_root_registry.py
python tools/validators/directory_governance/validate_repository_topology.py --format text
python tools/validators/directory_governance/render_repository_topology_diagnostics.py
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_*topology.py' \
  --verbose
```
