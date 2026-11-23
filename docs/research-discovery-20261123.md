# Research Discovery — hosted source, 2026-11-23

## Purpose and source

`/research` gives visitors a searchable entry into existing Kansas map sources, a three-source comparison and four guided investigations. It uses this hosted composition's `OFFICIAL_CONTEXT_SOURCES`, `SOURCE_DOWNLOADS` and `SCIENCE_EVENTS`; the observed scope is 59 registered map sources, 13 domains and 18 methods/phenomena. Counts describe catalog metadata, not live provider availability or admitted KFM evidence.

The implementation starts at `a0-hosted-ai-web-20261017@90d4c737f8e8bd7c462e9048241d2b2069956c7c` in `bartytime4life/Kansas-Frontier-Matrix`. The initial monorepo mirror prototype was reconciled with that newer source rather than replacing it. Navigation joins Explorer's More menu and welcome options, Labs, About, the source guide and the existing sitemap. The footer uses the current `/data-library` and `/labs` destinations.

## Visitor workflow

1. Open `/research` and choose a question about surface water, groundwater, fire/smoke or historical infrastructure.
2. Search source names, provider acronyms, dates and limitations, then filter by subject or representation. Show more reveals further results without hiding the total.
3. Select up to three sources. The comparison preserves provider, representation, freshness, cadence, limitations and missing-data wording.
4. Inspect original providers/downloads and open the selected sources in Explorer's Layers display. The map URL contains only selected catalog IDs and explicit workspace controls.

Search, subject, representation and comparison IDs are reflected in a shareable URL. Unknown domains, representations and comparison IDs are discarded; query length and source selection are bounded. Search text is rendered as text. Provider/download URLs accept HTTPS without embedded credentials or safe same-origin paths. The conceptual hero graphic is explicitly labelled as an illustration, not measured data.

## Scientific boundary

Sources retain `EXTERNAL_CONTEXT_ONLY` and their existing dates, reference periods, attribution, fallback and scientific limits. Search and map co-display do not establish compatible units, shared sampling design, spatial or temporal joins, causation, a reviewed analysis or current service health. Science methods retain their existing support labels.

The prairie research section links to the NEON KONZ site, BioStudies accessions E-GEOD-16418 and E-GEOD-35492, and PubMed records 41943985 and 21328008. These public references were checked on 2026-11-23. They are discovery leads only. No study files, sequence data, specimen locations or new dataset records are imported, and existing held Konza candidates remain held.

## Validation at authoring

- Production build: PASS, including staged browser assets.
- Full Node suite using CI's exact Node 22.23.3: **3,337 passed, 25 skipped, zero failed** (3,362 total). The older local Node 22.13.1 lacked SQLite FTS5/RTree; no application or test changes were made to suppress those environment failures.
- TypeScript (`tsc --noEmit --incremental false`): PASS.
- Focused source, science, aquifer, navigation and Konza tests: 104 passed, zero failed.
- New production HTTP tests: two passed as part of the full suite. They check `/research`, canonical identity, advertised assets, entry links, sitemap, valid groundwater comparison and inert/unknown URL input.
- ESLint on the new feature and adjacent edited navigation modules: zero errors; one existing hook-dependency warning at `app/living-welcome/welcome.jsx:213`. Whole-tree lint is not claimed. The root Explorer change is a single navigation anchor.
- Git whitespace and preservation of the original checkout's 23 pre-existing dirty files: PASS.

Exact-head hosted CI, rendered acceptance of this reconciled 59-source version and independent human review remain separate, pending checks at authoring. The initial 48-source mirror prototype's browser screenshots are not evidence of this hosted revision.

## Live delivery boundary and rollback

Public HTTP observation on 2026-11-23 found `/research` returning 404. `/api/build` reported source digest `sha256:db2a82e8ee4e82f34705574f59765c39860694cca1a878363d5b4c667aa002ad`, 1,401 inputs, null source commit and `WORKTREE_MODIFIED`. The clean hosted base has digest `sha256:4d281f02737167c4befdb976bfc1a880c50510cab5f0c39f7385ac1100477e3b`; neither proves this candidate is published.

Chrome lists the signed-in dashboard for GoDaddy app `urdng3v1vk`, but page reads fail with `Cannot read properties of undefined (reading 'timeoutMs')`, including after the user reconnected Chrome. No dashboard settings, Preview pull or Publish was performed. Verify the connected branch, exact Preview revision and build identity before publishing; read back `/research`, its assets and `/api/build` afterward. Preserve environment settings, models, relay, storage and DNS. The original private Sites project remains separate.

The application, tests, guide and receipt stay in their established roots under the standalone composition's existing placement/ADR-0029 boundary. No authority, source admission or publication semantics change. Rollback is a focused revert of this feature and redeployment of a verified prior application revision; no data migration is required.
