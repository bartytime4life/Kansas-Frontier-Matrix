# Byte-preserving Flight preload normalization in the Site mirror

PR #5817 already aligned the mirror React family on 19.2.9. This follow-up
ports only #5810's separate transport-compatibility repair to the existing
Cloudflare composition. It does not duplicate the dependency update.

The pinned Vinext kfm.1 helper decodes the complete Flight stream as UTF-8.
Binary bytes and hint-like text inside length-framed payloads can consequently
change. The replacement preserves every declared binary/long-text payload,
streams ordinary rows without whole-row buffering, and normalizes only valid
stylesheet preload hints. Header and hint buffering are bounded. Invalid or
truncated framing passes through for the codec to handle; errors and cancellation
retain their existing stream semantics.

An exact resolved-module Vite alias selects worker/rsc-stream-hints.mjs for
this composition's runtime. The helper is byte-identical to #5810's reviewed
implementation. The merged raw-codec regressions retain their legitimate
controls and aligned React-family assertions, and now cover the selected
wrapper. Emitted RSC and SSR checks verify direct codec selection; the RSC
artifact must select the replacement helper and exclude the original normalizer.

The 33 focused checks and production build/type/lint evidence are recorded in
the PR. Synthetic transport fixtures are not RCE payloads or proof of application
exploitability. Node versions, full-suite results and exact-head CI remain
separately attributable; no live provider, private store or model is exercised.

The append-only successor receipt binds the five application changes against
main's merged React-security receipt. Predecessor receipts, original Site identity,
canonical mappings, 262 withheld carriers and pending-review/false hosted-equivalence
declarations remain. This is CONTENT_PARITY_ONLY, not acceptance or publication.

Implementation/test/docs remain under apps/site/source; receipt evidence stays
under data/receipts/generated, selector implementation under tools/qa, and its
regression under tests/qa, following ADR-0029 and ADR-0048. No new authority root.

Revert the helper, alias, regressions, documentation and successor selector as
one unit while retaining patched React 19.2.9 and immutable receipt history.
No Site binding, Worker entry, audience, data-admission rule, model configuration,
installed service, public GoDaddy composition or publication changes are included.
