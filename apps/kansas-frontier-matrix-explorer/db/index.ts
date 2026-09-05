import { env } from "cloudflare:workers";
import { drizzle } from "drizzle-orm/d1";
import * as schema from "./schema";

type D1Binding = Parameters<typeof drizzle>[0];

function isD1Binding(value: unknown): value is D1Binding {
  return (
    typeof value === "object"
    && value !== null
    && "prepare" in value
    && typeof (value as { prepare?: unknown }).prepare === "function"
  );
}

export function getDb() {
  const database = env.DB;
  if (!isD1Binding(database)) {
    throw new Error(
      "Cloudflare D1 binding `DB` is unavailable. Set the `d1` field in .openai/hosting.json to `DB` or let your control plane inject the real binding values before using the database."
    );
  }

  return drizzle(database, { schema });
}
