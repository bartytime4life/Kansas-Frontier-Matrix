# Page titles and canonical addresses (2026-11-23)

A sweep of the public pages on 2026-11-22 found two things search engines and shared links
depend on missing from most of them.

- **No canonical address.** Only the home page, the guides and (later) the county and records
  pages named their own address. Pages such as the Event Observatory are opened with many
  different query strings (a replay link, a station, a time), and each one looked like a
  separate page.
- **The site-wide title.** `/data-lab` and `/data-library` showed "Kansas Frontier Matrix
  Explorer", because both are client components, which cannot declare a title.

## What changed

- Twelve public reading pages now declare `alternates.canonical` with their own address:
  `/topics`, `/civic`, `/curated`, `/observatory`, `/observatory/sources`, the County
  Observatory, four lab pages and the two history pages.
- `/data-lab` and `/data-library` each gain a small `layout.tsx` that carries a title, a
  description and the canonical address. Neither has child routes, so the address applies to
  that page alone.

## Left alone, on purpose

- **`/labs`.** It is a client page, and a layout there would also wrap every lab. A canonical
  address declared in it would be inherited by any lab that does not declare its own, pointing
  those labs at the index. A test holds this.
- **`/assistant`, `/downloads` and `/earth-engine-downloads/setup`** showed the site-wide title
  in the sweep because they are redirects, not pages.

## Checks

`tests/page-identity.test.mjs` reads the sitemap's list of public pages and requires each to
declare its own canonical address (and no other page's), requires the four layouts that carry
one to have no child routes, and checks the two new titles.
