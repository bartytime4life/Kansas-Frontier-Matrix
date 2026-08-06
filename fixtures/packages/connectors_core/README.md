# connectors_core synthetic fixture lane

This lane is reserved for small, public-safe, source-agnostic connector fixtures.

The current implementation keeps primitive values and fake transport exchanges inline in the focused tests because no source bytes, source endpoint, source identity, credential, or live connector runtime is required. The fake responses cover success, HEAD, not-modified, timeout, rate limit, cancellation, redirect, wrong media type, partial body, response-size, length, and digest-mismatch behavior.

Any later fixture added here must be synthetic, no-network, secret-free, deterministic, and incapable of being mistaken for admitted source data. A fixture cannot authorize source admission, lifecycle promotion, evidence closure, release, or publication.
