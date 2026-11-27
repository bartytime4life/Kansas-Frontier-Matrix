# Connected science and custom-work inquiries

The science hub at `/science` opens five source-backed labs and the existing
Topeka comparison report. Its question and year controls open each tool's
native window. Locations, units, observation clocks and coverage remain
specific to that tool. A soil station is not substituted for a Topeka reading.

The shared science navigation identifies the active tool and offers a custom
work inquiry tied to its current normalized selectors. Thresholds retain their
native stored units; inspected dates travel only where the lab already supports
them in its URL. Navigation does not certify that a snapshot has loaded or that
a finding has passed scientific review.

## What a visitor can request

`/science/services` offers three separately scoped conversations:

- A **custom evidence brief**: one useful question with source-linked figures,
  explicit coverage and a reproducible data appendix.
- A **reusable data pack**: a documented table, units, quality flags, source
  lineage and preparation steps for an agreed use.
- A **guided team walkthrough**: a question-led session using the public tools,
  with a reading guide and next steps.

The existing `/science/compare` report is the free worked example. All public
science tools, self-service reports and downloads remain free. The inquiry page
quotes no prices or delivery dates and takes no payment. Availability, scope,
data suitability, deliverables and pricing must be agreed before work begins.

## Draft handling

The inquiry builder composes text on the visitor's device. It does not submit a
form, save the fields to browser storage, add analytics or send an email. The
visitor can copy or download a text brief, or explicitly open an email draft to
the existing public contact `Andy.barta.pro@gmail.com`. Their email application
controls the eventual send. A selectable text fallback remains available when
clipboard access fails. Form text and feedback follow the current selection.

Only exact public science routes and documented, bounded selectors can enter
the starting-analysis link. Arbitrary URLs, repeated keys, credentials,
coordinates, fragments and unknown selectors are rejected. The link contains
settings, not private data or an assertion of a verified result. Visitors should
describe a general area and omit sensitive records from an initial inquiry.

## First revenue experiment

Start with a small custom evidence brief because the existing comparison report
already demonstrates the deliverable. Offer one agreed question, place and
period using suitable available data. Discuss the effort, revision boundary and
quote directly; do not promise a county, field or time period the source cannot
support. Reusable data preparation and team walkthroughs are adjacent options
to qualify through actual inquiries.

This is a proposed business experiment, not evidence of buyer demand, booked
revenue or guaranteed earnings. Kansas organizations already offer related GIS,
cartography, data development and custom web mapping services; that establishes
an existing service category rather than demand for KFM specifically.
[K-State GISSAL services](https://www.k-state.edu/gissal/services/),
[Johnson County AIMS](https://www.jocogov.org/department/aims).

Use conversations to learn the buyer's question, current alternative and desired
output before expanding the service. This follows the SBA's guidance to assess
demand, competition and customer needs. Track qualified inquiries, agreed scopes,
completed paid work and actual delivery effort separately; a draft email or page
visit is not a sale.
[SBA market research guidance](https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis).

No checkout, paid data API, subscription, sponsorship promise or automatic
outreach is part of this implementation. Source terms, attribution, data quality
and scientific limitations remain attached to any proposed deliverable.

## Validation and delivery boundaries

`tests/science-handoff.test.mjs` checks native route windows, manifest coverage,
selection retention, URL rejection and inquiry text. Component tests cover
launcher/navigation and copy/download/email behavior. Source parity receipts,
CI, local browser review and public deployment each have their own evidence.
Scientific review and dataset admission remain pending; dataset release remains
unreleased. Reverting the connected-science change removes the inquiry surface
without a database migration or payment cleanup.
