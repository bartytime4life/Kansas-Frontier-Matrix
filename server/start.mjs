import { startProdServer } from "vinext/server/prod-server";
import { resolve } from "node:path";
import { applyBrowserHeaders } from "./browser-headers.mjs";

const rawPort = process.env.PORT ?? "3000";
if (!/^[0-9]+$/.test(rawPort)) throw new Error("PORT must be an integer");
const port = Number(rawPort);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("PORT is out of range");
const { server } = await startProdServer({ port, host: "0.0.0.0", outDir: resolve("dist") });
// Include static assets and framework-level errors that bypass route headers.
// Later route responses can still replace these defaults with stricter policy.
server.prependListener("request", applyBrowserHeaders);
