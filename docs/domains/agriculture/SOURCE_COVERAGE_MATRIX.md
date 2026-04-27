# Agriculture Source Coverage Matrix

Status legend: `PLANNED`, `FIXTURE-READY`, `READY-FOR-LIVE-INTAKE`, `ACTIVE`, `BLOCKED`.

| Source family | Role | Status | Public release default | Blocking condition |
|---|---|---|---|---|
| SSURGO / SDA | Authoritative soil survey context | PLANNED | Allowed after evidence + provenance validation | Schema home and source descriptor unresolved |
| gSSURGO | Gridded soil companion context | PLANNED | Allowed with explicit gridded label | Must not be promoted as independent authority |
| Kansas Mesonet | Station observation context | FIXTURE-READY | Allowed with station/depth/time caveats | Unit/QC normalization tests incomplete |
| NRCS SCAN / NOAA USCRN | Station corroboration | PLANNED | Allowed after source-role and QC mapping | Source mapping not finalized |
| NASA SMAP | Satellite grid soil moisture context | FIXTURE-READY | Allowed only as gridded remote-sensing context | Product/version + mask capture tests needed |
| NASA HLS / HLS-VI | Remote-sensing vegetation context | FIXTURE-READY | Allowed as derived/remote-sensing layer only | Mask and cloud quality constraints pending |
| USDA NASS QuickStats / Crop Progress | Aggregate agricultural context | PLANNED | Allowed at aggregate geography/time only | Field-level misuse guardrails must be tested |
| Private/proprietary farm data | Restricted future class | BLOCKED | Deny by default | No restricted-data lane approved |
