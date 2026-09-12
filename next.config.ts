import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Vinext applies its multipart guard before API-route dispatch. Allow room
  // for a 10 MB file plus form fields; the route enforces the lower byte cap.
  experimental: { serverActions: { bodySizeLimit: "11mb" } },
};

export default nextConfig;
