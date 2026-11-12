<!--
KFM_WIKI_SOURCE
page_id: Getting-Started
title: Getting Started
status: source-grounded documentation candidate; independent review pending
updated: 2026-11-11
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Getting-Started.md
evidence_checkpoint: main@d4d84171653a2f2582b48ece511dc010857fde15; historical-hosted@bbcec824fe57e6be0409ba1e35d737fa99581560
publication_effect: none until reviewed source is separately synchronized
-->

# Getting Started

## Repository update — November 11, 2026

Main `d4d84171653a2f2582b48ece511dc010857fde15` includes merged Explorer
recovery, replay-inspection and Flight/Zod corrections. The
[repository review](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/reports/documentation-currentness-review-20261111.md)
separates current source and recorded validation from the historical public
website and media qualification below. Use the
[Explorer guide index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/site/source/docs/README.md)
for current usage. This source update does not synchronize the native wiki or
establish a new deployed version.


**Choose the experience or source you want to evaluate.**

## Explore in the browser

Open [Kansas Frontier Matrix](https://kansasfrontiermatrix.com/). Start with a category
or place, then inspect its source/time/limitation context. The [Visual Tour](visual-tour.md)
shows dated renderer excerpts before you open a workspace.

The public welcome was reachable in Chrome on October 27. Full route, provider,
accessibility and device acceptance are separate from that observation.

## Reproduce the historical public application source

The public Node composition has its own source tree and npm lockfile. Use Node.js
`>=22.13.0`. This is the exact application revision built and tested in this edition:

```bash
git clone --single-branch --branch a0-hosted-ai-web-20261017 https://github.com/bartytime4life/Kansas-Frontier-Matrix.git kfm-public-review
cd kfm-public-review
git checkout --detach bbcec824fe57e6be0409ba1e35d737fa99581560
npm ci
npm run build
PORT=5187 npm start
```

Provider data needs network access. Chat needs separately configured server-side
inference. Never copy private host settings into a public issue or repository.
[Source and hosting runbook](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/docs/runbooks/godaddy-node-hosting.md).
Startup instructions are source-derived; this documentation run verified the build
and tests, not a fresh local interactive server.

## Work on the monorepo

Use `main` for contracts, schemas, validators, capture/admission and release support.
The root npm build/test/lint commands intentionally report `WORKFLOW_HOLD`; they do
not run the public app. [Repository Map](Repository-Map.md) explains ownership.

The [current repository Explorer](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/site/README.md) has a separate
[local installation and verification workflow](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/installation.md#explorer-site-mirror). Do not substitute it for the public Node application or overwrite its
source, audience or persisted data.

## Contribute one useful slice

Inspect [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/docs/doctrine/directory-rules.md),
then choose a bounded task, state the exact base/head and overlap, run changed-area
checks and prepare a draft with limitations and rollback.

[Development and Validation](Development-and-Validation.md) · [Contributing](Contributing.md) · [Project Status](Project-Status.md)
