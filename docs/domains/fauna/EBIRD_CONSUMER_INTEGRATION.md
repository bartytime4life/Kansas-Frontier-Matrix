# eBird Consumer Integration (Layer 26)

Layer 26 provides **local-only** downstream handoff artifacts for public aggregate eBird data.

## CLIs
- `kfm-ebird-mock-control-plane`
- `kfm-ebird-consumer-pack`

## Safety
- No network calls.
- No credentials.
- No exact coordinates in public contracts.
- No restricted observations/suppression receipts.
- Descriptive contracts only (no occupancy/abundance/population trend/causal claims).

## Deterministic IDs
- `mock_id`: sha256 over canonicalized aggregate targets, input hashes, and adapter version; first 16 hex chars.
- `consumer_pack_id`: sha256 over canonicalized aggregate targets, input hashes, language, and adapter version; first 16 hex chars.

## Outputs
- Mock route and response fixture artifacts.
- Consumer contract manifest, route descriptor, and OpenAPI-lite descriptor.
