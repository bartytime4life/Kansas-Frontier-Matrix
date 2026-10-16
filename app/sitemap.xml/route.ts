import { SITEMAP_XML } from "../crawler-discovery";

const headers = {
  "Content-Type": "application/xml; charset=utf-8",
  "Cache-Control": "public, max-age=3600",
  "X-Content-Type-Options": "nosniff",
};

export function GET() {
  return new Response(SITEMAP_XML, { headers });
}

export function HEAD() {
  return new Response(null, { headers });
}
