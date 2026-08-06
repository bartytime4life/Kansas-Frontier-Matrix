# Source ingestion-plan fixtures

**Status:** PROPOSED · synthetic · fixture-only · no-network.

This fixture family exercises three source-ingestion planning modes derived from *New Ideas 3-19-26*:

- conditional HTTP polling for remote sources KFM does not control;
- event-driven CDC for authoritative transactional systems KFM controls; and
- scheduled ETL for bulk or slow-changing corpora.

Valid fixtures prove only local shape and consistency. Invalid fixtures are exact-negative cases with reviewed finding codes. No fixture contains credentials, live source locators, source bytes, rights clearance, sensitivity clearance, activation authority, lifecycle mutations, release state, or public-use permission.
