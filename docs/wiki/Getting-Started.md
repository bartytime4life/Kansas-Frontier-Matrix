<!--
KFM_WIKI_SOURCE
page_id: Getting-Started
title: Getting Started
status: source-grounded documentation candidate; independent review pending
updated: 2026-10-27
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Getting-Started.md
evidence_checkpoint: main@17f106d558674ec92a11809bcf3a06c82453777e; hosted@bbcec824fe57e6be0409ba1e35d737fa99581560
publication_effect: none until reviewed source is separately synchronized
-->

# Getting Started

**Choose the experience or source you want to evaluate.**

## Explore in the browser

Open [Kansas Frontier Matrix](https://kansasfrontiermatrix.com/). Start with a category
or place, then inspect its source/time/limitation context. The [Visual Tour](visual-tour.md)
shows dated renderer excerpts before you open a workspace.

The public welcome was reachable in Chrome on October 27. Full route, provider,
accessibility and device acceptance are separate from that observation.

## Run the public application source

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

The [preserved Sites mirror](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/apps/site/README.md) has a separate
local workflow. Do not substitute it for the public Node application or overwrite its
source, audience or persisted data.

## Contribute one useful slice

Inspect [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/docs/doctrine/directory-rules.md),
then choose a bounded task, state the exact base/head and overlap, run changed-area
checks and prepare a draft with limitations and rollback.

[Development and Validation](Development-and-Validation.md) · [Contributing](Contributing.md) · [Project Status](Project-Status.md)
