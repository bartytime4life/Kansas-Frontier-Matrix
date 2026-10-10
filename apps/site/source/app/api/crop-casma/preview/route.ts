import { cropCasmaPreview } from "../../../crop-casma-preview-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return cropCasmaPreview(request); }
