# Settlements & Infrastructure API Contracts

Public APIs must resolve released artifacts only.

## Public contract obligations

- No direct RAW/WORK/QUARANTINE reads.
- Each consequential claim resolves `EvidenceRef -> EvidenceBundle`.
- Responses include source role, confidence/uncertainty, and temporal scope.
- Focus outcomes are finite: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`.

## Candidate endpoints (naming TBD)

- Settlements search/list/detail.
- Settlement boundary versions and status timeline.
- Infrastructure assets/networks/nodes/segments.
- Layer metadata and Evidence Drawer payloads.
- Release and correction lineage lookup.

## Response safety

- Redact or generalize restricted geometry.
- Return policy reason codes for denied/abstained outcomes.
