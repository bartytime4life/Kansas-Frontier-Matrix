// Public discovery metadata for this GoDaddy composition, not release authority.
export const PUBLIC_SITE_ORIGIN = "https://kansasfrontiermatrix.com";

export const ROBOTS_TEXT = `# Guidance only. Authentication and release controls remain separate.
User-agent: *
Disallow: /api/
Disallow: /acquisition
Disallow: /source-operations
Disallow: /stewards
Disallow: /data
Disallow: /earth-engine
Disallow: /knowledge/record
Disallow: /governed/
Disallow: /*?*

Sitemap: ${PUBLIC_SITE_ORIGIN}/sitemap.xml
`;

export const SITEMAP_XML = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${PUBLIC_SITE_ORIGIN}/</loc></url>
  <url><loc>${PUBLIC_SITE_ORIGIN}/about</loc></url>
  <url><loc>${PUBLIC_SITE_ORIGIN}/privacy</loc></url>
</urlset>
`;
