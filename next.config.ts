import type { NextConfig } from "next";
import { browserHeaders } from "./server/browser-headers.mjs";

const nextConfig: NextConfig = {
  // Vinext applies its multipart guard before API-route dispatch. Allow room
  // for a 10 MB file plus form fields; the route enforces the lower byte cap.
  experimental: { serverActions: { bodySizeLimit: "11mb" } },
  // Baseline headers for worker-rendered pages and routes. Vinext only adds a config
  // header when the route has not set it, so API routes keep their own values.
  // Allow the verified GoDaddy preview parent explicitly, rather than all sites.
  // Geolocation stays allowed for this origin (the map's locate control).
  async headers() {
    const headers = Object.entries(browserHeaders).map(([key, value]) => ({ key, value }));
    // Vinext's "/:path*" does not match the root path, so "/" is listed too.
    return [
      // HTTP Link canonicals apply to this client-rendered map page only. Child
      // information pages retain their own literal metadata canonicals.
      { source: "/", headers: [...headers, { key: "Link", value: '<https://kansasfrontiermatrix.com/>; rel="canonical"' }] },
      { source: "/:path*", headers },
    ];
  },
};

export default nextConfig;
