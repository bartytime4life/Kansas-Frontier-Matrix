import { readBoundedJson } from "../../../bounded-json";
import { PREVIEW_SOURCES, isPublicPreviewKind, parsePublicPreview, publicPreviewQuery, validPreviewBounds } from "../../../public-map-preview-model";
export async function GET(request: Request) {
  const params=new URL(request.url).searchParams, kind=params.get("kind"), bounds=(params.get("bounds")??"").split(",").map(Number);
  if (!isPublicPreviewKind(kind) || !validPreviewBounds(bounds)) return Response.json({error:"Choose a Kansas area smaller than 0.6 degrees across."},{status:400});
  const signal=AbortSignal.any([request.signal,AbortSignal.timeout(20_000)]);
  try {
    const response=await fetch(publicPreviewQuery(kind,bounds),{signal,redirect:"manual"});
    if (!response.ok) throw new Error("Provider unavailable");
    const data=parsePublicPreview(await readBoundedJson(response,4_000_000,signal),kind,bounds);
    return Response.json({...data,bounds,kind,source:PREVIEW_SOURCES[kind],retrievedAt:new Date().toISOString()},{headers:{"Cache-Control":"no-store"}});
  } catch { return Response.json({error:"The provider could not return a verified bounded response. No coverage or absence is inferred."},{status:502}); }
}
