import { defineConfig } from "vite";

// This opt-in transport exists only in the loopback development server.
// Production builds and the ordinary offline Explorer have no API proxy.
export default defineConfig(({ command }) => ({
  server: {
    host: "127.0.0.1",
    ...(command === "serve" && process.env.VITE_KFM_LOCAL_EVIDENCE === "1"
      ? {
          port: 4173,
          strictPort: true,
          proxy: {
            "/__local__/evidence": {
              target: "http://127.0.0.1:8765",
              changeOrigin: true,
              timeout: 5_000,
              proxyTimeout: 5_000,
            },
          },
        }
      : {}),
  },
}));
