import { ROBOTS_TEXT } from "../crawler-discovery";

const headers = {
  "Content-Type": "text/plain; charset=utf-8",
  "Cache-Control": "public, max-age=3600",
  "X-Content-Type-Options": "nosniff",
};

export function GET() {
  return new Response(ROBOTS_TEXT, { headers });
}

export function HEAD() {
  return new Response(null, { headers });
}
