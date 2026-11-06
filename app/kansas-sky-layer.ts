import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";
import { TRAFFIC_ALTITUDE_COLORS, type Aircraft } from "./aviation-traffic";
import { bankHeightOffset, type SkyPoint } from "./kansas-sky";

type SkyPickPoint = Readonly<{ x: number; y: number }>;
const aircraftPickers = new WeakMap<MapLibreMap, (point: SkyPickPoint) => boolean>();
/** Called by the map's click owner after measuring/point-picking priority guards. */
export function pickKansasSkyAircraft(map: MapLibreMap, point: SkyPickPoint): boolean {
  return aircraftPickers.get(map)?.(point) ?? false;
}

const ID = "kfm-kansas-sky";
const LIMIT = 3000, TRAIL_VERTICES = 60000;
const RAD = Math.PI / 180;
const xy = (lon: number, lat: number) => [(lon + 180) / 360, (180 - Math.log(Math.tan(Math.PI / 4 + lat * RAD / 2)) / RAD) / 360];
const origin = xy(-98.35, 38.5);
const uniforms = ["u_matrix", "u_world", "u_origin", "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"];
type Bundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; u: Record<string, WebGLUniformLocation | null> };
export type SkyTrail = Readonly<{ hex: string; points: readonly SkyPoint[] }>;
type Position = Pick<Aircraft,"onGround"|"altGeomFt"|"altBaroFt"|"emergency">;
const displayAltitude=(a:Position)=>a.onGround?0:a.altGeomFt??a.altBaroFt;
const altitude = (a: Position) => Math.max(0, displayAltitude(a) ?? 0) * .3048;
function color(a: Position, selected: boolean): readonly number[] {
  if (selected) return [1, .84, .42];
  if (a.emergency) return [224/255,48/255,30/255];
  const feet = displayAltitude(a);
  const hex=feet===null?TRAFFIC_ALTITUDE_COLORS[0][1]:[...TRAFFIC_ALTITUDE_COLORS].reverse().find(([floor])=>feet>=floor)?.[1]??TRAFFIC_ALTITUDE_COLORS[0][1];
  return [1,3,5].map(offset=>parseInt(hex.slice(offset,offset+2),16)/255);
}
/** One persistent buffer; bounded trail detail degrades before aircraft are removed.
 * Altitude is explicitly approximate, never an airspace-membership calculation. */
export function attachKansasSky(map: MapLibreMap, select: (hex: string) => void, report: (message: string) => void) {
  let gl: WebGL2RenderingContext | null = null, buffer: WebGLBuffer | null = null, active = true, dirty = true;
  let planes: readonly Aircraft[] = [], trails: readonly SkyTrail[] = [], selected: string | null = null;
  let planeVertices = 0, trailVertices = 0, flat = false;
  const data = new Float32Array((LIMIT * 12 + TRAIL_VERTICES) * 6);
  const bundles = new Map<string, Bundle>();
  const failed = new Set<string>();
  let hits: { hex: string; x: number; y: number }[] = [];
  const groundMarkers = new Map<string, {lon:number;lat:number;height:number}>();
  const markerAltitude=(a:Aircraft)=>{
    if(flat)return 0;
    if(!a.onGround&&(a.altGeomFt!==null||a.altBaroFt!==null))return altitude(a);
    const cached=groundMarkers.get(a.hex);if(cached&&cached.lon===a.lon&&cached.lat===a.lat)return cached.height;
    let height=0;try{const ground=map.queryTerrainElevation([a.lon,a.lat]);if(ground!==null&&Number.isFinite(ground))height=ground;}catch{/* Missing DEM remains an explicitly approximate ground locator. */}
    if(groundMarkers.size>=LIMIT)groundMarkers.clear();groundMarkers.set(a.hex,{lon:a.lon,lat:a.lat,height});return height;
  };
  const compile = (kind: number, source: string) => {
    const shader = gl!.createShader(kind)!; gl!.shaderSource(shader, source); gl!.compileShader(shader);
    if (!gl!.getShaderParameter(shader, gl!.COMPILE_STATUS)) { gl!.deleteShader(shader); throw new Error("Aircraft shader unavailable"); }
    return shader;
  };
  const build = (input: CustomRenderMethodInput, globe: boolean) => {
    const vertex = compile(gl!.VERTEX_SHADER, `#version 300 es\n${globe ? `${input.shaderData.vertexShaderPrelude}\n${input.shaderData.define}` : "uniform mat4 u_matrix; uniform float u_world;"}
      uniform vec2 u_origin; in vec3 a_position; in vec3 a_color; out vec3 v_color;
      void main(){v_color=a_color; gl_Position=${globe ? "projectTileWithElevation(u_origin+a_position.xy,a_position.z)" : "u_matrix*vec4((u_origin+a_position.xy)*u_world,a_position.z,1.)"};}`);
    const fragment = compile(gl!.FRAGMENT_SHADER, "#version 300 es\nprecision highp float; in vec3 v_color; out vec4 fragColor; void main(){fragColor=vec4(v_color,1.);}");
    const program = gl!.createProgram()!; gl!.attachShader(program, vertex); gl!.attachShader(program, fragment); gl!.linkProgram(program);
    gl!.deleteShader(vertex); gl!.deleteShader(fragment);
    if (!gl!.getProgramParameter(program, gl!.LINK_STATUS)) { gl!.deleteProgram(program); throw new Error("Aircraft shader unavailable"); }
    const vao = gl!.createVertexArray()!; gl!.bindVertexArray(vao); gl!.bindBuffer(gl!.ARRAY_BUFFER, buffer);
    for (const [name, offset] of [["a_position", 0], ["a_color", 12]] as const) { const at = gl!.getAttribLocation(program, name); gl!.enableVertexAttribArray(at); gl!.vertexAttribPointer(at, 3, gl!.FLOAT, false, 24, offset); }
    gl!.bindVertexArray(null);
    return { program, vao, u: Object.fromEntries(uniforms.map(name => [name, gl!.getUniformLocation(program, name)])) };
  };
  const upload = () => {
    let count = 0;
    const put = (x: number, y: number, z: number, c: readonly number[]) => { data.set([x - origin[0], y - origin[1], z, ...c], count * 6); count++; };
    const size = Math.max(35, Math.min(1600, 180000 / 2 ** (map.getZoom() - 1)));
    for (const a of planes.slice(0, LIMIT)) {
      const [x,y] = xy(a.lon,a.lat), unit = 1 / (40075016.686 * Math.cos(a.lat * RAD));
      const heading = (a.trackDeg ?? 0) * RAD, bank = (flat?0:a.rollDeg ?? 0) * RAD, c = color(a,a.hex===selected);
      // Four simple triangles: fuselage, wings and tail, visibly schematic.
      const outline=a.trackDeg===null
        ? [[0,0],[0,.6],[.6,0],[0,0],[.6,0],[0,-.6],[0,0],[0,-.6],[-.6,0],[0,0],[-.6,0],[0,.6]]
        : [[0,1],[.13,-.8],[-.13,-.8],[-.9,-.1],[0,.25],[.9,-.1],[-.45,-.75],[0,-.5],[.45,-.75],[0,1],[.13,-.8],[-.13,-.8]];
      for (const [east,north] of outline) {
        const e=east*size*Math.cos(bank), n=north*size;
        // readsb positive roll is right-wing down; local east is the aircraft's right side.
        put(x+(e*Math.cos(heading)+n*Math.sin(heading))*unit,y+(e*Math.sin(heading)-n*Math.cos(heading))*unit,markerAltitude(a)+bankHeightOffset(east*size,flat?0:a.rollDeg),c);
      }
    }
    planeVertices=count;
    const segments=trails.reduce((n,t)=>n+Math.max(0,t.points.length-1),0);
    const stride=Math.max(1,Math.ceil(segments/(TRAIL_VERTICES/2)));
    for (const trail of trails) for(let i=1;i<trail.points.length;i+=stride) {
      if(count-planeVertices+2>TRAIL_VERTICES) break;
      const end=Math.min(i+stride-1,trail.points.length-1);
      for(const p of [trail.points[i-1],trail.points[end]]) { const [x,y]=xy(p.lon,p.lat); put(x,y,flat?0:altitude(p),color(p,trail.hex===selected)); }
    }
    trailVertices=count-planeVertices;
    gl!.bindBuffer(gl!.ARRAY_BUFFER,buffer); gl!.bufferSubData(gl!.ARRAY_BUFFER,0,data.subarray(0,count*6)); dirty=false;
  };
  const layer: CustomLayerInterface = { id:ID,type:"custom",renderingMode:"3d",onAdd(_map,context) {
    gl=context as WebGL2RenderingContext; buffer=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buffer); gl.bufferData(gl.ARRAY_BUFFER,data.byteLength,gl.DYNAMIC_DRAW); dirty=true;
  },render(_context,input) {
    if(!active||!gl||!buffer||document.hidden) return;
    const globe=map.getProjection().type==="globe", key=globe?input.shaderData.variantName:"mercator";
    if(failed.has(key))return;
    let bundle=bundles.get(key);
    try { if(!bundle) {bundle=build(input,globe);bundles.set(key,bundle);} } catch {failed.add(key);report("Aircraft renderer unavailable; use the aircraft list.");return;}
    if(dirty) upload();
    gl.useProgram(bundle.program); gl.bindVertexArray(bundle.vao); const u=bundle.u, world=512*2**map.getZoom();
    gl.uniform2f(u.u_origin,...origin as [number,number]);
    if(globe) {const p=input.defaultProjectionData;gl.uniformMatrix4fv(u.u_projection_matrix,false,p.mainMatrix as Float32Array);gl.uniformMatrix4fv(u.u_projection_fallback_matrix,false,p.fallbackMatrix as Float32Array);gl.uniform4f(u.u_projection_tile_mercator_coords,...p.tileMercatorCoords);gl.uniform4f(u.u_projection_clipping_plane,...p.clippingPlane);gl.uniform1f(u.u_projection_transition,p.projectionTransition);}
    else {gl.uniformMatrix4fv(u.u_matrix,false,Float32Array.from(input.modelViewProjectionMatrix));gl.uniform1f(u.u_world,world);}
    if(flat)gl.disable(gl.DEPTH_TEST);else gl.enable(gl.DEPTH_TEST);gl.depthMask(false);gl.disable(gl.CULL_FACE);gl.lineWidth(1);
    gl.drawArrays(gl.LINES,planeVertices,trailVertices);gl.drawArrays(gl.TRIANGLES,0,planeVertices);gl.bindVertexArray(null);
    // Mercator's exact elevated clip positions make aircraft clickable in 3D.
    hits=[];
    if(!globe) {const m=input.modelViewProjectionMatrix;for(const a of planes){const [xx,yy]=xy(a.lon,a.lat),x=xx*world,y=yy*world,z=markerAltitude(a),w=m[3]*x+m[7]*y+m[11]*z+m[15];if(w<=0)continue;hits.push({hex:a.hex,x:((m[0]*x+m[4]*y+m[8]*z+m[12])/w+1)*map.getCanvas().clientWidth/2,y:(1-(m[1]*x+m[5]*y+m[9]*z+m[13])/w)*map.getCanvas().clientHeight/2});}}
  },onRemove(){if(gl){for(const b of bundles.values()){gl.deleteProgram(b.program);gl.deleteVertexArray(b.vao);}if(buffer)gl.deleteBuffer(buffer);}bundles.clear();failed.clear();buffer=null;gl=null;hits=[];}};
  const pick=(point:SkyPickPoint)=>{if(!active)return false;const hit=hits.map(h=>({...h,d:Math.hypot(h.x-point.x,h.y-point.y)})).filter(h=>h.d<18).sort((a,b)=>a.d-b.d)[0];if(!hit)return false;select(hit.hex);return true;};
  aircraftPickers.set(map,pick);
  const install=()=>{
    if(!active||!map.isStyleLoaded())return;
    if(!map.getLayer(ID))map.addLayer(layer);
    map.off("render",install);
    map.off("error",install);
  };
  // Other style listeners can queue source work before this renderer mounts.
  // Recheck on ready frames, then release the listener after installation.
  const awaitStyle=()=>{if(!active)return;map.on("render",install);map.on("error",install);install();};
  const zoom=()=>{dirty=true;groundMarkers.clear();};
  map.on("style.load",awaitStyle);map.on("zoom",zoom);awaitStyle();
  return { update(next:readonly Aircraft[], nextTrails:readonly SkyTrail[], id:string|null, flatView=false){flat=flatView;planes=next;trails=nextTrails;selected=id;dirty=true;map.triggerRepaint();}, dispose(){active=false;map.off("style.load",awaitStyle);map.off("render",install);map.off("error",install);if(aircraftPickers.get(map)===pick)aircraftPickers.delete(map);map.off("zoom",zoom);if(map.getLayer(ID))map.removeLayer(ID);} };
}
