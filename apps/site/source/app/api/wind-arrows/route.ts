import { serveWindArrows } from "../../wind-arrow-data";

export const runtime = "edge";
export async function GET(request: Request) { return serveWindArrows(request); }
