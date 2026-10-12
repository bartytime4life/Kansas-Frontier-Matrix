<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/briefing-source-adapter-protocol-source-map
title: Briefing SourceAdapter Protocol Adaptation Source Map
type: exploratory-intake; source-map
version: v1.0.0
status: proposed adaptation; no source activation
created: 2026-08-09
updated: 2026-08-09
[/KFM_META_BLOCK_V2] -->

# Briefing SourceAdapter protocol adaptation

The supplied Briefing-to-System Integration Architecture identifies the Phase 2 source-verification slice as a source-agnostic adapter protocol, immutable SourceArtifact metadata, synthetic transport cases, content-addressed storage, and parser-version binding. It explicitly separates this foundation from source activation, live pull-request network access, public APIs, maps, release, and publication.

Current repository evidence already contains the SourceAdapter semantic contract, injected transport primitives, immutable captured-byte handling, SourceArtifact handoff, content-addressed storage support, validation, and package tests. The missing dependency-closed gap is the executable source-agnostic discover/fetch/parse/source-health protocol and its boundary value objects.

This adaptation therefore adds only that pure package surface and focused no-network tests. It does not implement an NWS, KDHE, Mesonet, NRCS, or other source-specific adapter; choose a connector home; activate a SourceDescriptor; retrieve source bytes; create evidence; clear an advisory; or authorize release/public use.
