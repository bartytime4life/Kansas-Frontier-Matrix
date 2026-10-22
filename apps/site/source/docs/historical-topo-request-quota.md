# Historical map request quota

The authenticated overlay POST reserves one of ten catalog acquisitions per
requester and UTC day before contacting USGS. R2 conditional creation and ETag
compare-and-swap updates on the existing requester/day object enforce the bound
across Worker instances. No new binding, migration or data reset is required.
The quota key still uses the authenticated user ID, with lowercase email as the
fallback for older dispatch deployments.

Successful acquisitions cache the small canonical request record in that same
bounded object. Same-day retries for a cached catalog ID reread ready/pending
status without another provider call or charge. A concurrent request for the
same unresolved ID receives HTTP 429 and can retry once the first completes.
Queue creation is conditional on absence, preserving the original request and
timestamp when catalog IDs resolve to the same scan or queue writers race.
Cached metadata also permits retrying failed or uncertain queue writes without
repeating the lookup.

Failed lookups, new catalog IDs that resolve to an existing scan, and uncertain
reservations retain their acquisition charges. Refunding these would permit
unbounded upstream work. Failed lookups can be retried while daily capacity
remains; interrupted reservations stay charged without an automatic expiry.
Malformed accounting or unavailable storage fails closed. CAS retries are
bounded, and contention returns HTTP 429 without authorizing a lookup.

Legacy count-only objects keep their consumed capacity. They cannot identify
free retries from before this change. Similarly, the cache does not recognize
previous-day acquisitions. An uncached ID therefore needs an available lookup
slot, even for a scan already queued or ready; status GET remains available by
scan ID without catalog access. The limit resets at UTC midnight, as before.
During rollout, retire old Worker code that can overwrite accounting without
conditions; rolling back to that code also restores its advisory quota.

`tests/historical-topo-quota.test.mjs` runs the actual route and quota against
disposable local R2 with synthetic identity and provider responses. It covers
concurrent reservations, legacy accounting, cached/ready retries, aliases,
immutable queue races, failures, malformed state, and uncertain writes. It
does not contact USGS or alter hosted storage.
