# Documentation graph validator tests

This directory proves the bounded, deterministic behavior of
`tools/validators/docs/document-graph/check_document_graph.py` with public-safe,
no-network fixtures.

The suite covers:

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

Run the focused suite:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/document-graph \
  --pattern 'test_*.py' \
  --verbose
```

A passing test run establishes only the documented QA behavior over the
synthetic fixture profile. It does not prove documentation truth, evidence
closure, source admissibility, policy, review, release, publication, or whole
repository connectivity.
