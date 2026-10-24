import { tfrResponse } from "../../../aviation-drone-server";

export const dynamic = "force-dynamic";

export async function GET() {
  return tfrResponse();
}
