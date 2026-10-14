import { authenticateOwner, json } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return json({ owner: await authenticateOwner(request) }); }
