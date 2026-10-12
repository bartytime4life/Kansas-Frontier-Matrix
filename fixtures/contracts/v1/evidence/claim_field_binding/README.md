# ClaimFieldBinding fixture profile

This directory contains one reusable base plus isolated mutations for the
inactive `kfm.evidence.claim-field-binding.v1` profile.

The matrix proves four coherent candidates:

- exact field support;
- deterministic normalized support;
- context-only qualified support;
- unresolved conflict support.

It also proves fail-closed handling for malformed field pointers, missing
EvidenceRef support, incomplete or nondeterministic transforms, confidence
overclaim, incomplete conflict closure, release/public/effect overclaim, and
identity corruption.

Fixtures contain synthetic references and digests only. They perform no network
access, EvidenceRef resolution, source activation, policy decision, lifecycle
write, release, publication, or public delivery.
