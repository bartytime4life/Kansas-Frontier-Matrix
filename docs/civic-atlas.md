# Kansas civic atlas

Status: implemented source-discovery and offline-intake foundation; dataset qualification and publication remain separate. Research checked 2026-10-24. This document distinguishes current code from the proposed expansion.

## What this change delivers

`/civic` gives visitors a searchable, grouped directory of 48 civic/economic source notes, an explicit county-context loader using the existing Census endpoint, a link back to the map, neutral research-question drafting, and a private values-reflection worksheet. It is reachable from Topics and the People & communities map guide. Page checks are visibly different from dataset availability. Candidate, disclosure, budget and happiness records are not fabricated to fill empty views.

The offline `scripts/pc-pipeline/civic-intake.mjs` adapter validates local research packets into an in-memory SQLite workspace. Source observations, county reference points and county-directory candidates stay `research_only`/held. This is an executable intake contract and reproducible local experiment, not a migration of the hosting database, an importer into released knowledge, or an installed pipeline schedule.

The first UI uses existing application conventions. It does not create a new map engine, political-profile store, source-of-truth registry, public write endpoint or inferred candidate ranking. The values worksheet stays in component memory and clears on reload; the civic feature does not send its contents to AI, telemetry, storage or a server.

## Evidence and placement basis

The original hosted implementation base was `a0-hosted-ai-web-20261017@291cbf394209520b38af72fcad91d7dfc5da1aee`, tree `851789a7d23991fc9b117d2f343a927d43adc85b`. All 1,537 blob paths and hashes were compared with the isolated local validation snapshot before editing. Before opening the draft, PR #5454 advanced the hosted branch to `63fb2ac9795251d16837f6a817b3c7b0b73d0d82`, tree `b34e1eabecdfe0833a868e6f26f89308337dbd65`. Its 14 changed files do not overlap this patch; exact remote blobs were integrated for repeat validation. This is the separate GoDaddy composition identified by its current `AGENTS.md`; it does not replace the preserved Sites composition or the main monorepo.

The original Library `Directory Rules.pdf` identity was resolved, but text/page extraction returned no readable content and the current transfer helper failed. Its contents are **NEEDS VERIFICATION** in this session. The current canonical successor was read from main: `docs/doctrine/directory-rules.md`, blob `fd49a0b83e55cef52c1124281f093e263526898d`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`. Accepted ADR-0029, blob `8cd8f3835bc2583d6976e0ff7a2f9be2088d1f09`, adopts those exact bytes; the retained draft label inside the pinned document is not its current adoption state.

The attached Contributor Reliability System PDF was inspected, SHA-256 `3ef04b080219a8e93bb948b3c579e62ac75f25f77f4410294df1c1232756a5ee`. Its exact-base/head, overlap, proportional validation, review separation and rollback requirements govern the PR. Historical enforcement claims in that PDF are not treated as current ruleset evidence.

| Artifact | Owning responsibility and placement | Boundary |
| --- | --- | --- |
| `app/civic/*`, `app/civic-model.ts`, `app/civic-sources.ts` | Existing hosted `app/` presentation/runtime composition; source-note precedent `app/transport-history-sources.ts` | Discovery navigation, not canonical source registration or released evidence |
| Existing `app/topics/page.tsx`, `app/layer-workspaces.ts` | Application navigation | Adds a route to an existing topic; no new domain authority |
| Existing `app/assistant-surfaces.mjs` | Fixed public interface guidance | Civic methods only; no private form values or discovered records injected |
| `scripts/pc-pipeline/civic-intake.mjs` | Existing local pipeline runtime adapter | Inline SQLite DDL belongs to this bounded adapter, following the existing journal pattern; no parallel global schema home |
| `tests/civic-*.test.mjs` | Existing test responsibility | Synthetic negative cases plus contract invariants; never data authority |
| `docs/civic-atlas.md` | Human explanation/design and migration note | Documents implemented boundary and proposed qualification work |

Directory rules applied: `DIR-PLACE-001` (responsibility before topic), `DIR-PLACE-002` (no public reads of internal candidate data), `DIR-PLACE-003` (acquisition does not publish), `DIR-PLACE-005` (derivatives do not establish authority), and `DIR-DOCS-004` (human source descriptions do not replace the canonical source register). No new repository root is added. These are hosted composition placements, not declarations that the main monorepo should adopt `app/` or `scripts/` as new canonical contract/data homes. Future durable source registration and release must use the main repository's existing responsibility roots after an exact-tree placement check.

## Proposed product expansion

| View | User question | Data and interaction | Release condition |
| --- | --- | --- | --- |
| My government | Who has authority here, now or in the past? | County/city/township/school/special district polygons; offices, terms, public contacts, meetings, jurisdiction crosswalk | Official boundary vintage and office/term identity verified; territorial overlap explained |
| Public money | What was proposed, authorized and actually spent? | Budget stages, fund/program totals, payments, contracts, grants and project locations; nominal/real and per-capita switches | Reconciled totals, fiscal basis, denominator/deflator, amendment and geographic-allocation method |
| Laws and outcomes | What changed, when, and what can be attributed? | Bill versions, roll calls, enactment/effective/implementation dates, ordinances, service outputs and outcome trends | Each link has evidence; causal wording requires a separately reviewed evaluation |
| Candidate comparison | What does the same record show for each candidate? | Official roster for one election/office; identical fields for positions, votes, experience, disclosures and missing evidence | Complete or visibly partial roster, temporal identity, symmetric selection rules and independent editorial review |
| Disclosures | What financial interests and campaign activity were reported? | Filed reports, amendments, organization/committee identity and aggregate receipts/expenditures | Public-interest minimization, rights checks, reviewed extraction; no private donor-address map or wealth inference |
| Jobs and services | Where can I get help or apply? | Official job/service destinations, eligibility source, hours, last verification and expiry | Current destination and service-area verification; application remains an intentional outbound action |
| Community well-being | How are conditions changing? | Published ACS/BLS/BEA/KDHE aggregates with survey method, estimate type, margins and period | Compatible geography/period and uncertainty; no invented county happiness series |
| Moral compass | What principles and tradeoffs matter in this decision? | Private reflection on benefits, burdens, rights, evidence, alternatives and reversibility | No virtue score for people/parties, no political profiling or conversion into voting recommendations |
| Claim check | What does the cited record support? | Exact claim, speaker, date, context, corroboration/conflict, correction trail | Cite-or-abstain; separate fact, forecast, allegation and value judgment |

Map design: a civic lens should retain the existing map, timeline and compact evidence drawer. Use neutral sequential scales for amounts, text plus symbols for status, and a table alternative. A district outline is an authority geography, an expenditure area may be an allocation, and a project point may be an approximate location: never give them the same visual meaning. State/metro measurements cannot be painted as measured county values. No party color is the default performance scale. Historical views require boundary versions valid at the selected time.

## Curated source families and qualification order

The application source notes preserve the exact URL, checked date, organization, geography, page/link status and limitations. They do not imply that payloads were downloaded, rights cleared, parsers implemented, or feeds operating. The companion research packet records the fuller acquisition status.

| Priority | Primary sources | First useful product | Main qualification work |
| --- | --- | --- | --- |
| 1 | [Kansas.gov county directory](https://portal.kansas.gov/government/county-list/), [Census county reference table](https://tigerweb.geo.census.gov/tigerwebmain/Files/acs26/tigerweb_acs26_county_ks.html), [SOS election offices](https://sos.ks.gov/elections/county-election-offices.html) | County coverage inventory and official service routing | Independently verify all destinations; use current boundary and office-location records separately |
| 1 | [State jobs](https://admin.ks.gov/offices/personnel-services/jobs), [Kansas services](https://portal.kansas.gov/services/) | Outbound service/job finder | Job records were not acquired; application destination needs cookies/login; expire closed positions |
| 1 | [KDOR quarterly tax rates](https://www.ksrevenue.gov/salesratechanges.html), [local distributions](https://www.ksrevenue.gov/prsalesreports.html) | Dated jurisdiction rates and receipts | Parse workbook with row locators; special districts and effective dates; do not infer a household tax bill |
| 1 | [KanView downloads](https://kanview.ks.gov/DataDownload.aspx) | Agency/fund/program expenditure explorer | Unaudited accounting data, not approved budget; bounded monthly imports, reconciliation, amendment handling |
| 2 | [Budget reports](https://budget.kansas.gov/budget-report/), [comparison reports](https://budget.kansas.gov/comparison-reports/), [municipal budgets](https://admin.ks.gov/offices/accounts-reports/local-government/municipal-services/municipal-budgets) | Requested/enacted/actual budget timelines | FY2027 index contains a year-text discrepancy; verify source PDF and corrected tables before extracting |
| 2 | [Legislature](https://www.kslegislature.gov/b2025_26/), [votes](https://www.kslegislature.gov/b2025_26/votes/), [feeds](https://www.kslegislature.gov/b2025_26/feeds/rsshelp/), [archives](https://www.kslegislature.gov/b2025_26/archive/) | Bill-action timeline and exact roll calls | Preserve bill/version/motion; distinguish sponsor, procedural vote, passage, enactment and effective date; feed retrieval remains unverified |
| 2 | [KPDC reports](https://kpdc.kansas.gov/campaign-finance/view-submitted-forms-and-reports/), [SSI](https://sos.ks.gov/elections/substantial-interest-center.html), [FEC](https://www.fec.gov/data/browse-data/) | Report-index links, then reviewed disclosure summaries | No sample filings extracted; local filing authorities differ; amendments, entity resolution, contributor-use restrictions and PII minimization |
| 2 | [ACS](https://www.census.gov/data/developers/data-sets/acs-5year.html), [QCEW CSV](https://www.bls.gov/cew/additional-resources/open-data/csv-data-slices.htm), [LAUS](https://www.bls.gov/lau/), [BEA RPP](https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area) | Comparable area context | API key/cadence limits, ACS margins and five-year windows, suppressed cells, resident/workplace distinctions; RPP is state/metro |
| 3 | [KDOT IKE](https://www.ksdot.gov/programs/eisenhower-legacy-transportation-program-ike/ike-projects-map), [Commerce transparency](https://www.kansascommerce.gov/dataview/transparency-explorer-home/), [Infrastructure Hub](https://www.kshub.gov/resources/state-agency-resources) | Projects and commitments versus observed delivery | Direct retrieval blocked/too large in this review; no production project data acquired; verify exact project footprint and milestones |
| 3 | [KDHE BRFSS](https://www.kdhe.ks.gov/1738/Technical-Notes), [OECD methods](https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-subjective-well-being-2025-update_9203632a-en.html) | Well-being evidence with uncertainty | Exact variables, years, sample domains and access terms unverified; keep representative surveys separate from voluntary feedback |

Two directory errors were observed: Jackson linked to Jefferson's domain, and Wallace linked to Washington's. Independently checked alternatives are [Jackson County](https://www.jacksoncountyks.com/) and [Wallace County](https://wallacecountyks.gov/). The 105 candidate directory entries are research observations, not 105 verified websites. Reference points parsed from the Census table describe counties, not offices or polling places. The original HTTP response bytes were not captured; no raw-response hash is claimed.

The official candidate-list endpoint returned 403. No candidate roster, candidate positions, financial filing records, polling-place assignment, or local happiness measurements were acquired. [VoterView](https://kansasvoterinfo.gov/VoterView) is an outbound personal lookup; KFM must not ingest the visitor's name, date of birth, party registration or individual ballot status.

## Treatment of the owner's additional links

| Supplied family | Role in this design | Current status |
| --- | --- | --- |
| Kansas.gov, USA.gov Kansas | Official navigation and authority discovery | Kansas.gov reviewed; USA.gov remains a supplied discovery lead |
| Governor, Revenue, Administration, Commerce, Education, Regents, Courts, Wildlife & Parks, Highway Patrol | Primary authority for their own records and services | Individual datasets need field-level verification; a homepage is not data-release evidence |
| Employee portal, user login, payment portal, DOV, business portal | Visitor service destinations | No authenticated scraping, credentials, payments, or employee data collection |
| INK/about | Portal governance and service context | Supplied discovery lead; no assumed API or data rights |
| CONTENTdm, K-State library guide, archived State Department Kansas page | Historical discovery and dated context | CONTENTdm returned only its JavaScript shell; other items need source/item review; archived federal page is not current state authority |
| Wikipedia (Kansas, government, cabinet), Kiddle, Ballotpedia | Secondary discovery and explanatory context | Follow to original records; do not substitute for current official terms, rosters, law or election instructions |
| Kansas Policy Institute, KansasOpenGov, Watkins Public Strategies | Attributed third-party/advocacy/commercial perspectives | Identify publisher and methodology, corroborate underlying records; never label as Kansas government merely from name/domain |
| X, Facebook, Instagram, LinkedIn | Attributed announcements and leads | Verify account ownership and preserve date/context; no bulk social profiling, sentiment-as-happiness or assumed official archival completeness |
| All county and town sites | Local authority, minutes, ordinances, adopted budgets, services | County inventory prepared; each destination and municipal identity remains its own qualification task |

## Logical SQL model for later qualification

This is **PROPOSED**, not an executed database migration. Keep existing KFM EvidenceRef/EvidenceBundle and release contracts as the authority; do not introduce a parallel approval model.

| Entity | Essential keys and fields | Integrity rule |
| --- | --- | --- |
| Jurisdiction / boundary version | stable ID, type, parent relations, source geometry version, valid_from/to, observed_at | Many overlapping authorities; never identify a voting district from county alone |
| Office / person / term / candidacy | separate IDs, office jurisdiction, election ID, term interval, status, evidence | No birth date/home address as identity keys; resolve aliases with evidence |
| Bill / action / roll call / ordinance | session/body/number/version, motion, member, vote, action/effective dates | Procedural and substantive votes stay distinct; no inferred stance from absence |
| Budget / payment / contract / project | fund, program, fiscal basis, amount/currency, stage, period, amendment, geographic allocation | Budget authority, spending, contract commitment and donations are not summed together |
| Disclosure / reported interest | filer/committee ID, form type, reporting period, filing date, supersedes, source locator | Reported interests are not net worth; missing report is not proven non-filing |
| Indicator / survey observation | variable/version, geography vintage, period, estimate, unit, MOE/CI, suppression, sampling/mode/weights | Null, suppressed and zero differ; survey estimates are not opt-in poll results |
| Claim / evaluation | exact attributed claim, evidence links, verdict rationale, design/estimand/assumptions, review | Causation requires a qualified evaluation, not a coincident timeline |
| Evidence / release references | existing IDs, source item hash, page/row locator, rights, sensitivity, review, supersession | EvidenceRef resolves to existing EvidenceBundle; approval and publication are separately recorded |

Use valid time (when a fact or boundary applied) and observation/record time (when KFM learned it). Preserve revisions rather than overwriting history. Store monetary values as precise decimal/minor units and preserve original units. Query through bound parameters and fixed approved query templates; AI text must never become executable SQL.

## Hosting and pipeline plan

Reuse the existing PC acquisition/processing and hosted released-product split. Proposed adapters obtain original bytes into RAW with URL, retrieval time, media type, SHA-256 and bounded response receipts. Parsing writes WORK or QUARANTINE with source row/page identity and transformation version. Qualification checks schema, identity, dates, totals, rights, sensitivity and source health. Only reviewed, approved products advance through PROCESSED and CATALOG/TRIPLET into released carriers.

The development PC should retain source documents, filing scans, revision history and expensive joins. GoDaddy should receive compact released county/district summaries and indexes through the existing bounded publisher. Do not copy the entire research store or run large geospatial joins per public request. Reuse existing admission limits; measure payloads, query plans and concurrency before selecting concrete indexes or changing hosting budgets. No production SQL capacity or hosting readiness was measured by this change.

Proposed layers: authority boundaries; public offices/service locations; project footprints and status; approved spending allocations; dated economic context. Layer registration must declare geometry role, source vintage, active interval, uncertainty and released product ID. County reference points in the research packet cannot serve as office locations or district boundaries. A temporal layer must expose true availability, gaps and revisions, rather than interpolate missing politics or finances.

## AI and fact-checking behavior

The implemented civic question composer produces neutral prompts that the visitor can inspect and copy. The existing page assistant also recognizes `/civic` through `app/assistant-surfaces.mjs`, supplying only fixed interface guidance and suggested method questions. It does not read the source inventory or private reflection into AI context. It does not install a civic factual-answer backend. General chat remains subject to its own evidence and availability controls; no live factual-answer qualification is claimed here.

Future public requests resolve map jurisdiction, selected time, topic and released EvidenceBundle IDs on the server. The model receives bounded excerpts and source metadata as untrusted data, never source-provided instructions. The response contract separates factual observations, explanations, uncertain interpretation and unanswered questions, with citations for each material factual claim. If evidence is missing, expired, conflicted or held, abstain and offer the official destination. Date-sensitive voting instructions require current official verification and expiry; an old page check cannot answer today's deadline.

Candidate comparisons use the same columns and completeness rules for everyone, including uncontested and withdrawn-status handling. Issue filters control which evidence rows are shown, not which candidate is promoted. Do not infer political beliefs from residence, demographics, browsing, reflection text or past questions. No opaque match percentage or persuasive targeting is part of this feature.

Fact checks retain claim text, speaker, date and scope; outcomes may be supported, contradicted, mixed, outdated or insufficient evidence, with reasoning and correction. Donations and disclosed interests alone do not prove corruption. Service outcomes during a term do not establish an official caused them. A visitor poll is not a representative population survey.

Research basis: [Stockinger et al. 2024](https://link.springer.com/article/10.1007/s10676-024-09790-6) and [Berdoz et al. 2025](https://www.ijcai.org/proceedings/2025/1063) motivate explicit comparison assumptions and robustness checks; they do not certify KFM neutrality. [World Bank impact-evaluation guidance](https://documents1.worldbank.org/curated/en/698441474029568469/pdf/108270-PUB-Box396299B-PUBLIC-PUBDATE-9-13-16.pdf) and [Callaway/Sant'Anna](https://psantanna.com/files/Callaway_SantAnna_2020.pdf) support separating descriptive trends from causal estimates. No Kansas causal effect was estimated.

## Validation, review and rollback

Run the civic model/intake tests, existing topic/navigation tests, TypeScript and production build. Record exact command outcomes and head in the PR. Browser acceptance must cover narrow/mobile and desktop layouts, keyboard access, empty/search results, county-load failure and success, copy failure and success, values clearing, map framing and safe external links. Do not infer browser acceptance from a build or source-string test. No hosted deployment is implied by local checks.

Review should independently check URL authority/status, prompt boundaries, private reflection, SQL transactionality, no public access to held data, missingness and temporal semantics. Production ingestion, operational schedules, candidate completeness, record rights, full county destination verification, live AI responses and representative well-being data remain open until separately evidenced.

Rollback is a reviewed revert of this bounded commit: remove the civic route/source/model/intake/tests/document and the two navigation additions. No production database was altered; no data restoration or service migration is required by this change. Preserve any exported research receipts and the review trail. Re-run the affected navigation tests and confirm the prior Topics/map navigation remains intact. Trigger rollback or hide the route for misleading authority labels, leaked reflection, broken navigation or an uncontained retrieval path.
