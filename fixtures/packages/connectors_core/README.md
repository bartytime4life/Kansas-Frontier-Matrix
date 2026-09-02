# connectors_core synthetic fixture lane

This lane is reserved for small, public-safe, source-agnostic connector primitive fixtures.
The first implementation keeps values inline in focused unit tests because no source bytes,
source endpoint, source identity, or connector runtime is needed to prove the pure behavior.

Any later fixture added here must be synthetic, no-network, secret-free, and incapable of
being mistaken for admitted source data. A fixture cannot authorize source admission,
lifecycle promotion, evidence closure, release, or publication.
