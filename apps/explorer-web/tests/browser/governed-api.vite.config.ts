import { defineConfig, mergeConfig } from "vite";
import explorer from "../../vite.config";

// Test runner only. Production Vite/Sites configuration has no API proxy.
export default mergeConfig(explorer, defineConfig({
  server: {
    proxy: {
      "^/evidence$": {
        target: "http://127.0.0.1:4174",
        changeOrigin: false,
        followRedirects: false,
      },
    },
  },
}));
