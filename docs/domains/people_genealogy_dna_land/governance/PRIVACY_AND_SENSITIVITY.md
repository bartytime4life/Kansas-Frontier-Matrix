# Privacy and Sensitivity Posture

## Default posture
- **Living-person output:** deny by default.
- **DNA output:** restricted/deny by default for public surfaces.
- **Exact residential linkage:** deny unless explicitly allowed.

## Decision factors
A claim may be released only when all are satisfied:
1. Source terms permit the intended surface.
2. Sensitivity label allows the visibility level.
3. EvidenceRef resolves to a reviewable EvidenceBundle.
4. Policy decision returns finite allowable outcome for that surface.
5. Review state is sufficient for publication.

## Field-level guidance
- Do not expose raw DNA kit or vendor identifiers.
- Avoid precise location fields for living persons unless policy explicitly permits.
- Use role-qualified wording for assessor facts.
- Display uncertainty and correction state when evidence is partial.

## Redaction checklist
- Remove direct identifiers not required for claim interpretation.
- Replace exact residential coordinates with coarse place when required.
- Remove segment-level DNA details from public payloads.
- Preserve auditability through references, not sensitive raw content.
