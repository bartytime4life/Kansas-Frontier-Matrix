# StoryNode fixture matrix

Synthetic fixtures for the proposed
`kfm.ui.story-node.public-safe.v1` projection.

## Valid lane

The valid lane covers every finite node state:

- released `READY`;
- corrected `READY`;
- stale `PARTIAL`;
- evidence-missing `ABSTAINED`;
- rights-blocked `BLOCKED`;
- bounded `ERROR`; and
- correction-bound `SUPERSEDED`.

A valid negative state is not public claim authority. It proves only that the
projection can represent a fail-closed status without exposing prohibited
support.

## Semantic-invalid lane

The invalid lane exercises:

- ready content without release;
- ready content without evidence;
- blocked support leakage;
- error support leakage;
- supersession without correction;
- unresolved rights presented as an answer;
- self-referential supersession;
- state/outcome mismatch; and
- corrected state without correction references.

`expected_findings_manifest.json` records the exact value-free reason-code set
for each fixture.

All fixtures are synthetic, no-network, non-published, and contain no real
person, source credential, sensitive site, or precise restricted location.
