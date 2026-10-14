import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { getIngestionStore } from "../server/ingestion-store.mjs";
const sql = await readFile(new URL("../server/ingestion-schema.sql", import.meta.url), "utf8");
const sha256 = createHash("sha256").update(sql).digest("hex");
const statements = sql.replace(/--[^\n]*/g, "").split(";").map(statement => statement.trim()).filter(Boolean);
if (!process.argv.includes("--apply")) {
  console.log(JSON.stringify({ mode: "review-only", sha256, tables: ["kfm_ingest_control", "kfm_ingest_jobs", "kfm_ingest_captures", "kfm_ingest_chunks", "kfm_ingest_owner_session"], statements: statements.length, sharedDatabase: true, initialState: "paused", destructiveStatements: false }));
} else {
  if (process.env.KFM_MIGRATION_SHA256 !== sha256) throw new Error("Exact migration digest must be confirmed before --apply.");
  const store = await getIngestionStore();
  try { for (const statement of statements) await store.database.query(statement); await store.control(); console.log("Hosted capture schema verified; capture remains paused."); }
  catch { throw new Error("Migration was not verified. Preserve all tables, inspect the shared database, and retry the additive migration after repair."); }
  finally { await store.database.end(); }
}
