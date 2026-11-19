import vinext from "vinext";
import { defineConfig, normalizePath } from "vite";
import { readFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { welcomeDemoCapturePlugin } from "./scripts/welcome-demos/capture-sink.mjs";

// Replace this one pinned Vinext transport helper in dev and production. Its
// text-only normalizer corrupts length-framed Flight binary and long-text rows.
const vinextRscStreamHints = normalizePath(fileURLToPath(new URL("./server/rsc-stream-hints.js", import.meta.resolve("vinext"))));

// Dev server only, and only when KFM_STORY_PREVIEW_DIR is set: serves locally exported story bundles
// (python3 -m tools.local_data.sql_feed_stories export) where the website would ask the relay.
function storyPreviewPlugin(directory: string) {
  const root = resolve(directory);
  return {
    name: "kfm-story-preview",
    apply: "serve" as const,
    configureServer(server: { middlewares: { use: (handler: (req: { url?: string; method?: string }, res: { statusCode: number; setHeader: (name: string, value: string) => void; end: (body: string | Buffer) => void }, next: () => void) => void) => void } }) {
      server.middlewares.use((req, res, next) => {
        const url = new URL(req.url ?? "/", "http://localhost");
        if (req.method !== "GET" || url.pathname !== "/api/local-data/stories") return next();
        const send = (status: number, body: string | Buffer) => { res.statusCode = status; res.setHeader("Content-Type", "application/json"); res.setHeader("Cache-Control", "no-store"); res.end(body); };
        const story = url.searchParams.get("story") ?? "";
        if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(story) || story.length > 64) return send(400, JSON.stringify({ reasonCode: "QUERY_INVALID" }));
        readFile(join(root, `${story}.json`)).then(body => send(200, body), () => send(404, JSON.stringify({ state: "not-configured", reasonCode: "STORY_PREVIEW_MISSING" })));
      });
    },
  };
}

// Separate Node composition; the preserved Sites source and bindings are unchanged.
export default defineConfig(({ command }) => {
  const recorderEnabled = command === "serve" && process.env.KFM_WELCOME_DEMO_RECORDER === "1";
  const storyPreview = command === "serve" ? process.env.KFM_STORY_PREVIEW_DIR : undefined;
  return {
  define: {
    __KFM_WELCOME_RECORDER__: JSON.stringify(recorderEnabled),
    __KFM_BUILD_UTC_YEAR__: JSON.stringify(Math.max(2026, new Date().getUTCFullYear())),
  },
  resolve: {
    alias: {
      "cloudflare:workers": fileURLToPath(new URL("./server/godaddy-env.ts", import.meta.url)),
      [vinextRscStreamHints]: fileURLToPath(new URL("./server/rsc-stream-hints.mjs", import.meta.url)),
    },
  },
  server: { host: recorderEnabled ? "127.0.0.1" : "0.0.0.0" },
  plugins: [...(storyPreview ? [storyPreviewPlugin(storyPreview)] : []), vinext(), ...(recorderEnabled ? [welcomeDemoCapturePlugin()] : [])],
  };
});
