import { startProdServer } from "vinext/server/prod-server";
import { resolve } from "node:path";

const rawPort = process.env.PORT ?? "3000";
if (!/^[0-9]+$/.test(rawPort)) throw new Error("PORT must be an integer");
const port = Number(rawPort);
if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("PORT is out of range");
await startProdServer({ port, host: "0.0.0.0", outDir: resolve("dist") });
