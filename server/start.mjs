import { startProdServer } from "vinext/server/prod-server";
import { resolve } from "node:path";
import { installPublicDelivery } from "./browser-headers.mjs";
import { reportNodeStartup } from "./startup-probe.mjs";

const rawPort = process.env.PORT ?? "3000";
if (!/^[0-9]+$/.test(rawPort)) throw new Error("PORT must be an integer");
const port = Number(rawPort);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("PORT is out of range");
const { server } = await startProdServer({ port, host: "0.0.0.0", outDir: resolve("dist") });
// Outlive the hosting proxy's pooled idle sockets; Node's 5 s default lets it reuse a closed one and answer 503.
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000;
// Include static assets and framework-level errors that bypass route headers.
// Later route responses can still replace these defaults with stricter policy.
installPublicDelivery(server);
// Binding a socket does not prove that the built application can answer HTTP.
// A failed probe is diagnostic; it does not change authorization or hide errors.
void reportNodeStartup(server);

// Inference runs only on the paired home PC. Retired embedded-model probe and
// acceptance flags deliberately have no effect on this web-server process.

// Owner-only opt-in memory observation. No model is loaded by this check.
if (process.env.KFM_HOSTED_AI_RESOURCE_PROBE === "1") {
  const { reportHostedResources } = await import("./hosted-ai-resources.mjs");
  reportHostedResources();
}
