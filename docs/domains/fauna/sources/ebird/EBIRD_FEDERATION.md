# eBird Federation (Layer 12)

Layer 12 adds **public-safe federation/discovery/export** for eBird aggregate outputs (HUC12/county), with no downloads, no keys, and no exact points.

## Workflows
- `kfm-ebird-federate --mode build|validate|diff|report|index`
- `kfm-ebird-export --mode stac|ro-crate|warehouse|search|all|validate`

## Contracts
- Public federation index: `public_federation_index.json`
- Discovery docs: `public_discovery_index.jsonl`
- Semantic graph: `public_federation_graph.jsonl`
- JSON-LD context: `public_semantic_context.json`

## Safety rules
Public artifacts never include exact coordinates, geometries, restricted rows, quarantine paths, or suppression receipts.
