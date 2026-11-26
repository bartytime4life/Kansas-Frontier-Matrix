// Public discovery metadata for this GoDaddy composition, not release authority.
import { COUNTY_PAGES } from "./county-pages";
import { LANDING_GUIDES } from "./landing-guides";
export const PUBLIC_SITE_ORIGIN = "https://kansasfrontiermatrix.com";

export const ROBOTS_TEXT = `# Guidance only. Authentication and release controls remain separate.
User-agent: *
Disallow: /api/
Disallow: /acquisition
Disallow: /earth-engine
Disallow: /knowledge/record
Disallow: /governed/
Disallow: /*?*

Sitemap: ${PUBLIC_SITE_ORIGIN}/sitemap.xml
`;

// Public reading pages that were reachable from the site but missing from the sitemap. Pages robots.txt
// disallows, sign-in and status pages, and the Knowledge search (whose store is not provisioned) are left out.
export const PUBLIC_PAGES = Object.freeze(["/records", "/topics", "/civic", "/curated", "/data-library", "/observatory", "/observatory/sources", "/research",
  "/labs", "/labs/observatory", "/labs/drought-replay", "/labs/ghost-towns", "/labs/newspaper-pulse", "/labs/water-chemistry",
  "/history/people-events", "/history/prentis-1909", "/science", "/labs/heat-and-rain", "/labs/county-drought", "/labs/soil-profile"]);

export const SITEMAP_XML = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${PUBLIC_SITE_ORIGIN}/</loc></url>
  <url><loc>${PUBLIC_SITE_ORIGIN}/about</loc></url>
  <url><loc>${PUBLIC_SITE_ORIGIN}/privacy</loc></url>
  <url><loc>${PUBLIC_SITE_ORIGIN}/explore</loc></url>
${LANDING_GUIDES.map(guide => `  <url><loc>${PUBLIC_SITE_ORIGIN}/explore/${guide.slug}</loc></url>
`).join("")}  <url><loc>${PUBLIC_SITE_ORIGIN}/counties</loc></url>
${COUNTY_PAGES.map(county => `  <url><loc>${PUBLIC_SITE_ORIGIN}/counties/${county.slug}</loc></url>
`).join("")}${PUBLIC_PAGES.map(path => `  <url><loc>${PUBLIC_SITE_ORIGIN}${path}</loc></url>
`).join("")}</urlset>
`;
