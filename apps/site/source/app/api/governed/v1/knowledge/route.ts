import { kansasKnowledgeRead } from "../../../../kansas-knowledge-server";
export const dynamic = "force-dynamic";
export async function GET(request: Request) { return kansasKnowledgeRead(request); }
