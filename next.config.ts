import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Vinext applies its multipart guard before API-route dispatch. Allow room
  // for a 10 MB file plus form fields; the route enforces the lower byte cap.
  experimental: { serverActions: { bodySizeLimit: "11mb" } },
  // Baseline headers for worker-rendered pages and routes. Vinext only adds a config
  // header when the route has not set it, so API routes keep their own values.
  // No framing rule here: the hosting platform may preview the Site in a frame.
  // Geolocation stays allowed for this origin (the map's locate control).
  async headers() {
    const headers = [
      { key: "Content-Security-Policy", value: "default-src 'self'; base-uri 'self'; object-src 'none'; script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src 'self' blob:; connect-src 'self' https://tiles.openfreemap.org https://s3.amazonaws.com; img-src 'self' data: blob: https://tiles.openfreemap.org https://s3.amazonaws.com; font-src 'self' data: https://tiles.openfreemap.org; form-action 'self'" },
      { key: "X-Content-Type-Options", value: "nosniff" },
      { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
      { key: "Permissions-Policy", value: "camera=(), microphone=(), payment=(), usb=(), geolocation=(self)" },
    ];
    // Vinext's "/:path*" does not match the root path, so "/" is listed too.
    return [{ source: "/", headers }, { source: "/:path*", headers }];
  },
};

export default nextConfig;
