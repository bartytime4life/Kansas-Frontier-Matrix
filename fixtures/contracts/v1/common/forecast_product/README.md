# ForecastProduct fixture profile

This directory contains one reusable forecast base plus isolated mutations for
the inactive `kfm.common.forecast-product.v1` profile.

Positive fixtures cover model, expert, hybrid-corrected, superseded, and
conflicted forecasts. Negative fixtures prove source-role and support-type
separation, distinct cutoff/issue/valid times, explicit method context,
fail-closed uncertainty, and release/public/effect non-authority.

All products, sources, methods, geographies, evidence references, and digests
are synthetic. No network request, live forecast, advisory, EvidenceBundle,
policy decision, lifecycle write, release, publication, or public guidance is
created.
