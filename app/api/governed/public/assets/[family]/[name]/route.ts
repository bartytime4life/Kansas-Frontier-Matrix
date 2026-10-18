import { publicAssetRead } from "../../../../../../public-release-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request, context: { params: Promise<{ family: string; name: string }> }) {
  const { family, name } = await context.params;
  return publicAssetRead(request, family, name);
}
