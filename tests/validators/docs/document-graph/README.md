# Documentation graph validator tests

This directory proves the bounded, deterministic behavior of
`tools/validators/docs/document-graph/check_document_graph.py` and
`select_changed_receipts.py` with public-safe, no-network fixture repositories.

The graph suite covers:

- Markdown navigation and bounded reference-style links;
- metadata-declared path and stable-document-identity relationships;
- generated Maps of Content and backlinks;
- entrypoint reachability, orphan, and unreachable-document findings;
- duplicate document identity;
- optional machine document-registry parity;
- path-escape and symbolic-link denial;
- changed-file ratchet behavior;
- warning promotion; and
- stable JSON/Markdown/CLI results.

The changed-receipt suite covers:

- no selection for artifact-only edits;
- selection of added, modified, and renamed matching receipts;
- exclusion of deleted and unrelated receipt families;
- direct and merge-base range semantics;
- NUL-delimited CLI output;
- invalid-ref failure; and
- repository-prefix escape denial.

Run the focused suite:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/document-graph \
  --pattern 'test_*.py' \
  --verbose
```

A passing test run establishes only the documented QA behavior over synthetic
local Git fixtures. It does not prove documentation truth, evidence closure,
source admissibility, policy, review, release, publication, historical
authorship beyond a validated receipt, or whole-repository connectivity.
