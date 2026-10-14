import { ownerSignIn } from "../../../../server/owner-auth.mjs";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return ownerSignIn(request); }
