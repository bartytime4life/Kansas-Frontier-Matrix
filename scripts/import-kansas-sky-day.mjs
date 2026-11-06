#!/usr/bin/env node
// Run on an authorized operator worker with access to the existing hosted archive.
// Daily preparation/scheduling and GoDaddy job/Python availability are separate.
import { importKansasSkyDay } from "../server/kansas-sky-archive.mjs";
import { getIngestionStore } from "../server/ingestion-store.mjs";

let store;
try {
  const args = process.argv.slice(2), apply = args.includes("--apply");
  const positionals = args.filter(arg => arg !== "--apply");
  if (positionals.length !== 1 || positionals[0].startsWith("-") || args.filter(arg => arg === "--apply").length > 1) throw new Error("USAGE: node scripts/import-kansas-sky-day.mjs CANDIDATE_DIRECTORY [--apply]");
  const result = await importKansasSkyDay(positionals[0], { apply, storeFactory: async () => { store = await getIngestionStore(); return store; } });
  console.log(JSON.stringify(result, null, 2));
  if (result.state === "held") process.exitCode = 1;
} catch (error) {
  const reason = /^(?:SKY_[A-Z_]+|STORAGE_NOT_CONFIGURED|USAGE:)/.test(error.message) ? error.message : "SKY_IMPORT_HELD";
  console.error(JSON.stringify({ state: "held", complete: false, collectionActive: false, reason })); process.exitCode = 1;
} finally { await store?.database?.end(); }
