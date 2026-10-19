/** Sites identity + a bounded adapter to the existing Node Qwen service.
 * No model, Node accounts, private records or credentials are copied here.
 */
type Settings = { KFM_STAGING_QWEN_ORIGIN?: string; KFM_STAGING_QWEN_TOKEN?: string };
const SITE = "appgprj_6acd1aafe0d88191a4306ea2ab44ed91";
const ORIGINS = new Set(["https://kansasfrontiermatrix.com", "https://q9r9beo47t.preview.c38.airoapp.ai"]);
const HEADERS = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie", "Cross-Origin-Resource-Policy": "same-origin" };
const response = (body: unknown, status = 200) => Response.json(body, {status, headers: HEADERS});
const failure = (reasonCode: string, status = 503) => response({reasonCode}, status);
const object = (x: unknown): x is Record<string, unknown> => Boolean(x && typeof x === "object" && !Array.isArray(x));
const text = (x: unknown, max: number) => typeof x === "string" && new TextEncoder().encode(x).length <= max && !/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(x);
const correlation = /^evidence_[a-f0-9]{32}$/;
const jobId = /^[A-Za-z0-9_-]{43}$/;
async function json(request: Request | Response, limit = 32768) {
  if (!request.body) throw new Error("INVALID_REQUEST");
  const reader = request.body.getReader(), chunks: Uint8Array[] = []; let count = 0;
  let timer: ReturnType<typeof setTimeout>;
  const timeout = new Promise<never>((_, reject)=>{timer=setTimeout(()=>reject(new Error("BODY_TIMEOUT")),8000);});
  try { while (true) { const next = await Promise.race([reader.read(),timeout]); if (next.done) break; count += next.value.length; if (count > limit) throw new Error("REQUEST_TOO_LARGE"); chunks.push(next.value); } }
  catch (error) { await reader.cancel().catch(()=>{}); throw error; }
  finally { clearTimeout(timer!); }
  const all = new Uint8Array(count); let offset = 0; for (const chunk of chunks) { all.set(chunk, offset); offset += chunk.length; }
  return JSON.parse(new TextDecoder("utf-8", {fatal:true}).decode(all));
}
export function createStagingAssistant({settings, catalog, fetcher = fetch, clock = Date.now}: {
  settings: Settings; catalog: (request: Request) => Promise<Response>; fetcher?: typeof fetch; clock?: () => number;
}) {
  const connected = ORIGINS.has(settings.KFM_STAGING_QWEN_ORIGIN ?? "") && /^[A-Za-z0-9_-]{43,128}$/.test(settings.KFM_STAGING_QWEN_TOKEN ?? "");
  return async (request: Request): Promise<Response> => {
    const url = new URL(request.url), path = url.pathname.replace(/^\/api\/ai\//, "");
    const id = request.headers.get("oai-authenticated-user-id"), email = request.headers.get("oai-authenticated-user-email");
    const signedIn = Boolean(id && email);
    if (url.search) return failure("INVALID_QUERY", 400);
    if (url.pathname === "/api/staging/account" && request.method === "GET") {
      return response({configured:true,online:true,ready:signedIn,account:signedIn ? email : null,role:null,
        signIn:"/signin-with-chatgpt?return_to=%2F%3Fkfm-chat%3D1",signOut:"/signout-with-chatgpt?return_to=%2F"});
    }
    const reading = request.method === "GET" && (path === "status" || /^jobs\/[A-Za-z0-9_-]{1,128}$/.test(path));
    const writing = request.method === "POST" && (path === "jobs" || /^jobs\/[A-Za-z0-9_-]{1,128}\/cancel$/.test(path));
    if (!reading && !writing) return failure("ROUTE_NOT_FOUND", 404);
    if (writing && (request.headers.get("origin") !== url.origin || request.headers.get("sec-fetch-site") === "cross-site" || !/^application\/json(?:;|$)/i.test(request.headers.get("content-type") ?? ""))) return failure("ORIGIN_DENIED", 403);
    if (!signedIn) return path === "status" ? response({configured:true,online:false,ready:false,evidenceSearchAvailable:false,requiresLogin:true,reasonCode:"SITE_SIGN_IN_REQUIRED"}) : failure("SITE_SIGN_IN_REQUIRED", 401);
    const remote = async (suffix: string, value?: unknown) => {
      const actor = [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(SITE+"\0"+id)))].map(x=>x.toString(16).padStart(2,"0")).join("");
      const result = await fetcher(settings.KFM_STAGING_QWEN_ORIGIN+"/api/sites-qwen/v1/"+suffix, {method:value === undefined ? "GET" : "POST", redirect:"error", signal:AbortSignal.timeout(10000),
        headers:{Authorization:"Bearer "+settings.KFM_STAGING_QWEN_TOKEN,"X-KFM-Site":SITE,"X-KFM-Site-Actor":actor,...(value === undefined ? {} : {"Content-Type":"application/json"})}, body:value === undefined ? undefined : JSON.stringify(value)});
      if (!result.ok) throw new Error("QWEN_CONNECTION_UNAVAILABLE");
      return json(result, 65536);
    };
    const evidence = async (key: string) => {
      const check = await catalog(new Request(url.origin+"/api/governed/public/catalog",{headers:request.headers}));
      const result = await json(check);
      const reasonCode = result?.envelope?.outcome === "ANSWER" ? "EVIDENCE_INDEX_UNAVAILABLE" : result?.envelope?.reason_code === "NO_APPROVED_PUBLIC_RELEASE" ? "NO_RELEASED_EVIDENCE" : "EVIDENCE_WITHHELD";
      return response({id:key,state:"completed",deadline:clock()+900000,checkedAt:new Date(clock()).toISOString(),sourceRevision:null,releaseId:null,context:null,
        result:{outcome:"ABSTAIN",reasonCode,answer:null,interpretation:null,citations:[]}});
    };
    try {
      if (path === "status") {
        let ready = false, online = false, code = "QWEN_CONNECTION_NOT_CONFIGURED";
        if (connected) { const s = await remote("status"); ready = s.ready === true && s.provider === "hosted-qwen3" && s.model === "onnx-community/Qwen3-0.6B-ONNX"; online = s.online === true; code = ready ? "QWEN_READY" : "QWEN_CONNECTION_UNAVAILABLE"; }
        return response({configured:true,online,ready,evidenceSearchAvailable:true,requiresLogin:false,model:"onnx-community/Qwen3-0.6B-ONNX",reasonCode:code});
      }
      let value;
      if (writing) value = await json(request);
      if (path === "jobs") {
        if (!object(value) || Object.keys(value).some(k=>!["question","term","place","start","end","mode","style","depth","context","investigationId"].includes(k)) || !text(value.question,4096) || String(value.question).trim().length < 2 || !text(value.term,120) || !["explore","evidence"].includes(String(value.mode))) return failure("INVALID_REQUEST",400);
        if (value.mode === "evidence") return response({id:"evidence_"+crypto.randomUUID().replaceAll("-",""),deadline:clock()+900000},202);
        if (!connected) return failure("QWEN_CONNECTION_NOT_CONFIGURED");
        // Reconstruct the only allowed display context. No record IDs, attributes,
        // camera, filters, source references, uploads or account fields leave Sites.
        const c = value.context;
        if (c !== undefined && (!object(c) || c.selection !== null || !Array.isArray(c.layers) || c.layers.length || !Number.isInteger(c.frame) || Number(c.frame)<-5e9 || Number(c.frame)>2200 || !["2D","Terrain 3D","Globe","Page"].includes(String(c.view)))) return failure("CONTEXT_WITHHELD",403);
        const payload = {...value, place:"", start:"", end:"", ...(object(c) ? {context:{version:1,frame:c.frame,view:c.view,surface:"map",layers:[],selection:null}} : {})};
        const created = await remote("jobs",payload);
        if (!jobId.test(created.id) || !Number.isFinite(created.deadline) || created.deadline > clock()+960000) throw new Error("INVALID_QWEN_RESPONSE");
        return response({id:created.id,deadline:created.deadline},202);
      }
      const [, key, cancel] = path.split("/");
      if (correlation.test(key)) return cancel ? response({cancelled:false}) : evidence(key);
      if (!connected || !jobId.test(key)) return failure("JOB_NOT_FOUND",404);
      if (cancel) { if (!object(value) || Object.keys(value).length) return failure("INVALID_REQUEST",400); const r = await remote(path,{}); return response({cancelled:r.cancelled === true}); }
      const r = await remote(path);
      if (r.id !== key || !Number.isFinite(r.deadline) || r.deadline > clock()+960000 || !["preparing","queued","running","completed","expired","cancelled"].includes(r.state)) throw new Error("INVALID_QWEN_RESPONSE");
      const result = r.result;
      if (result && (!object(result) || !["ABSTAIN","DENY","ERROR"].includes(String(result.outcome)) || !/^[A-Z][A-Z0-9_]{1,100}$/.test(String(result.reasonCode)) || result.reasonCode === "UNVERIFIED_AI_DISCUSSION" && !text(result.interpretation,20000))) throw new Error("INVALID_QWEN_RESPONSE");
      return response({id:key,state:r.state,deadline:r.deadline,checkedAt:new Date(clock()).toISOString(),sourceRevision:null,releaseId:null,context:null,
        result:result ? {outcome:result.outcome,reasonCode:result.reasonCode,answer:null,interpretation:result.reasonCode === "UNVERIFIED_AI_DISCUSSION" ? result.interpretation : null,citations:[],followUpQuestion:text(result.followUpQuestion,1000)?result.followUpQuestion:null,outputLimited:result.outputLimited === true,contextLimited:result.contextLimited === true} : null});
    } catch { return path === "status" ? response({configured:true,online:false,ready:false,evidenceSearchAvailable:true,requiresLogin:false,reasonCode:"QWEN_CONNECTION_UNAVAILABLE"}) : failure("QWEN_CONNECTION_UNAVAILABLE"); }
  };
}
