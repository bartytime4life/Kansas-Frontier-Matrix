import type { MetadataRoute } from "next";
import { LANDING_GUIDES } from "./landing-guides";
import { PUBLIC_SITE_ORIGIN } from "./site-identity";

/** Public entry pages only. Owner tools, APIs and signed-in workspaces are never listed. */
export const SITEMAP_PATHS: readonly string[] = Object.freeze([
  "/", "/explore", ...LANDING_GUIDES.map(guide => `/explore/${guide.slug}`), "/topics", "/about", "/observatory", "/observatory/sources", "/labs/heat-and-rain", "/almanacs",
]);

export default function sitemap(): MetadataRoute.Sitemap {
  return SITEMAP_PATHS.map(path => ({ url: `${PUBLIC_SITE_ORIGIN}${path === "/" ? "" : path}`, changeFrequency: path.startsWith("/explore") ? "monthly" : "weekly" }));
}
