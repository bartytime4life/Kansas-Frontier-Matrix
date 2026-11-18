import type { MetadataRoute } from "next";
import { PUBLIC_SITE_ORIGIN } from "./site-identity";

/** Crawlers may read public pages; API routes and owner/data workspaces stay out of indexes. */
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/api/", "/data/", "/acquisition", "/downloads", "/stewards", "/governed/"] }],
    sitemap: `${PUBLIC_SITE_ORIGIN}/sitemap.xml`,
  };
}
