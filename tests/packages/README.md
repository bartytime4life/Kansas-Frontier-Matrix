# Package tests

Executable conformance and boundary tests for reusable code under
[`packages/`](../../packages/README.md). Production code must not import this
tree.

```text
tests/packages/
├── README.md
└── evidence_resolver/   # bounded evidence candidate checks
```

These tests prove only the behavior they execute. They do not confer contract,
evidence, policy, review, release, or publication authority.
