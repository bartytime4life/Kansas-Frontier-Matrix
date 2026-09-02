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

Derived from the pinned bootstrap, the current ratchet records 127 exact
inherited finding groups after reviewed convergence. Those are warnings, not
conformance claims: any addition or changed fingerprint fails as new drift, any
removed finding requires the baseline to shrink in the same change, and
invariant rules cannot be baselined. In pull-request CI the proposed baseline is
also compared with the trusted base commit: waiver additions, waiver mutation,
metadata changes, and deadline extensions fail. Future ordinary changes may
only remove entries, strictly shrink one aggregate evidence set, or shorten the
deadline.

`repository_topology_reconciliation.json` is a separate, append-only proof
register for one narrower case: an exact README merge-conflict correction that
already exists unchanged on the trusted base but left the content-sensitive
`KFM-TOPO-004` baseline stale. A new record is accepted only when the trusted
base and tested tree have identical frozen-root evidence, the baseline changes
exactly one registered `README.md` blob at equal cardinality, the prior Git blob
contains a complete conflict-marker triplet, the current blob contains none,
and the record binds the trusted commit, old and new blobs, evidence digests,
fingerprints, governance issue, and retirement condition. At most one new
record may be added in a transition; records cannot be removed or mutated. This
mechanism does not authorize a frozen-root write or accept a same-change edit.

`render_repository_topology_diagnostics.py` is a bounded diagnostic projection
for failed ratchet runs. It preserves the ratchet exit code and reports only the
failure disposition, rule id, subject, and fingerprint for new drift, invariant
findings, baseline mismatches, and stale baseline entries. It intentionally does
not emit evidence members or evidence digests, does not mutate the baseline, and
does not create path authority. Output is deterministically sorted and bounded
to 20 identities by default (maximum 50).

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
