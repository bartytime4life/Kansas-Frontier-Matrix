# System map

```
Sources ──▶ connectors/ ──▶ data/raw ──▶ pipelines/ ──▶ data/work
                                                     └▶ data/quarantine
                                          └▶ data/processed ──▶ data/catalog
                                                             └▶ data/triplets
                                                             └▶ data/proofs
                                                             └▶ data/receipts
                                                                      │
                                                                      ▼
                                                                release/ (governed)
                                                                      │
                                                                      ▼
                                                              data/published
                                                                      │
                                                                      ▼
                                          apps/governed-api ──▶ apps/explorer-web
                                                          └─▶ apps/review-console
                                                          └─▶ apps/cli
                                                          └─▶ runtime/ (model adapters)
```

Each arrow is a governed transition. The trust membrane is `apps/governed-api`.
