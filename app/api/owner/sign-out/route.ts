import { ownerLogout } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function POST(request: Request) { return ownerLogout(request); }
