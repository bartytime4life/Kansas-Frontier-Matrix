# Evidence resolver package tests

Tests for the internal
`kfm/evidence-ref-bundle-candidate/v1alpha1` implementation under
[`packages/evidence-resolver/`](../../../packages/evidence-resolver/README.md).

## Scope

- Owner: evidence/proof, package, and validation stewards — `OWNER_TBD`.
- Inputs: synthetic fixtures under
  [`fixtures/packages/evidence_resolver/v1alpha1/`](../../../fixtures/packages/evidence_resolver/v1alpha1/README.md).
- Outputs: unittest pass/fail state and bounded subprocess output.
- Exposure/retention: public-safe test material only; no production state.
- Prohibited: live registry/network access, real evidence, source activation,
  policy inference, review/release actions, public responses, or publication.

## Current tree

```text
tests/packages/evidence_resolver/
├── README.md
├── test_cli.py    # command, fixture polarity, and no-echo behavior
└── test_core.py   # finite outcomes, bounds, determinism, and no-network checks
```

Run:

```bash
make evidence-resolver
make evidence-resolver-deny
```

The suite checks exact fixture outcomes, deterministic serialization,
non-authority, safe diagnostics, duplicate/non-finite/size/depth rejection,
standard-library-only imports, history-shape pinning, bitemporal replay,
subject binding, finite-outcome precedence, and active denial of DNS/socket
access.
