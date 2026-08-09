# Supply-chain policy lane

This directory holds proposed repository supply-chain allow/deny configuration. It does not hold credentials, package bytes, installed environments, attestations, SBOMs, release decisions, or deployment state.

`dependency_origin_policy.v1.json` is consumed by the no-network static validator. The current profile checks repository declarations only. Registry authentication, package signing, vulnerability response, lifecycle-script admission, and release attestations remain separate controls.

A passing check is a repository hygiene signal, not evidence, policy review, release, deployment, publication, or public-use authority.
