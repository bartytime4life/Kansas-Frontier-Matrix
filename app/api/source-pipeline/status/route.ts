import { ingestionStatus } from "../../../../server/ingestion-runner.mjs";
import { json } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function GET() { return json(await ingestionStatus()); }
