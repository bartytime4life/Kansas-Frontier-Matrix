const FAVICON = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="13" fill="#061416"/><path d="M14 15h8v14l12-14h10L31 30l15 19H36L25 35l-3 3v11h-8z" fill="#e0ba6d"/></svg>`;

export function GET() {
  return new Response(FAVICON, {
    headers: {
      "content-type": "image/svg+xml; charset=utf-8",
      "cache-control": "public, max-age=604800, immutable",
    },
  });
}
