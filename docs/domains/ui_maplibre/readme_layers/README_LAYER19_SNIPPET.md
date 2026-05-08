# Layer 19 — Selective Disclosure Trust Packet + Verifiable Auditor Exchange

This layer compiles Layer 18 assurance outputs into deterministic disclosure packets for scoped audiences. It is offline-testable and fail-closed.

## CLI usage
- plan-only: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-spec disclosure/disclosure_spec_example.json --assurance-pack-root assurance_packs/<id> --output-root disclosure_packets --mode plan-only`
- public-transparency: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-spec disclosure/disclosure_spec_example.json --assurance-pack-root assurance_packs/<id> --output-root disclosure_packets --mode public-transparency`
- auditor-full: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-spec disclosure/disclosure_spec_example.json --assurance-pack-root assurance_packs/<id> --output-root disclosure_packets --mode auditor-full`
- regulator: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-spec disclosure/disclosure_spec_example.json --assurance-pack-root assurance_packs/<id> --output-root disclosure_packets --mode regulator`
- internal-review: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-spec disclosure/disclosure_spec_example.json --assurance-pack-root assurance_packs/<id> --output-root disclosure_packets --mode internal-review`
- verification-only: `python tools/soilgrids/soilgrids_disclosure_packet.py --disclosure-packet-root disclosure_packets/<packet_id> --output-root disclosure_packets/verification --mode verification-only`

Warning: this layer prepares controlled disclosure packets only. It does **not** publish remotely, make legal certification claims, or mutate source evidence.
