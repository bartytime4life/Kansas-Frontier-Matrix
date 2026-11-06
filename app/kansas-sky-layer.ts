import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";
import { TRAFFIC_ALTITUDE_COLORS, type Aircraft } from "./aviation-traffic";
import { bankHeightOffset, heightProfile, SKY_MAX_HEIGHT_GUIDES, type SkyPoint } from "./kansas-sky";

type SkyPickPoint = Readonly<{ x: number; y: number }>;
const aircraftPickers = new WeakMap<MapLibreMap, (point: SkyPickPoint) => boolean>();
/** Called by the map's click owner after measuring/point-picking priority guards. */
export function pickKansasSkyAircraft(map: MapLibreMap, point: SkyPickPoint): boolean {
  return aircraftPickers.get(map)?.(point) ?? false;
}

/** Explicit presentation-only focus. Restores owned paint values and leaves TFRs and source state intact. */
export function attachKansasSkyFocus(map:MapLibreMap){
  type PaintName=Parameters<MapLibreMap["getPaintProperty"]>[1];
  type PaintValue=Parameters<MapLibreMap["setPaintProperty"]>[2];
  const owned=new Map<string,{layer:unknown;property:PaintName;original:PaintValue;applied:PaintValue}>();let active=true,changing=false;
  const same=(a:unknown,b:unknown)=>JSON.stringify(a)===JSON.stringify(b);
  const apply=()=>{
    if(!active||changing)return;changing=true;
    try{for(const layer of map.getStyle()?.layers??[]){
      if(!/^kfm-aviation-(?:airspace|drone|uas|airways|runways|airports|metar|ceilings|pireps)(?:-|$)/.test(layer.id))continue;
      const properties:readonly PaintName[]=layer.type==="fill"?["fill-opacity"]:layer.type==="fill-extrusion"?["fill-extrusion-opacity"]:layer.type==="line"?["line-opacity"]:layer.type==="circle"?["circle-opacity","circle-stroke-opacity"]:layer.type==="symbol"?["text-opacity","icon-opacity"]:[];
      for(const property of properties){const key=`${layer.id}:${property}`,identity=map.getLayer(layer.id),current=map.getPaintProperty(layer.id,property),existing=owned.get(key);
        if(existing&&existing.layer===identity&&same(current,existing.applied))continue;
        const original=current as PaintValue,applied=(typeof original==="number"?original*.12:["*",original??1,.12]) as PaintValue;
        owned.set(key,{layer:identity,property,original,applied});map.setPaintProperty(layer.id,property,applied);
      }
    }}finally{changing=false;}
  };
  map.on("styledata",apply);apply();
  return ()=>{active=false;map.off("styledata",apply);for(const [key,record]of owned){const id=key.slice(0,key.lastIndexOf(":"));if(map.getLayer(id)===record.layer&&same(map.getPaintProperty(id,record.property),record.applied))map.setPaintProperty(id,record.property,record.original);}owned.clear();};
}

const ID = "kfm-kansas-sky";
const LIMIT = 3000, PLANE_CAPACITY = LIMIT * 12 + 48, TRAIL_VERTICES = 60000, GUIDE_VERTICES = SKY_MAX_HEIGHT_GUIDES * 4;
const STROKE_SEGMENTS=4096+SKY_MAX_HEIGHT_GUIDES;
const RAD = Math.PI / 180;
const xy = (lon: number, lat: number) => [(lon + 180) / 360, (180 - Math.log(Math.tan(Math.PI / 4 + lat * RAD / 2)) / RAD) / 360];
const origin = xy(-98.35, 38.5);
const uniforms = ["u_matrix", "u_world", "u_origin", "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition", "u_viewport", "u_width", "u_halo"];
type Bundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; u: Record<string, WebGLUniformLocation | null> };
export type SkyTrail = Readonly<{ hex: string; points: readonly SkyPoint[]; future?: boolean }>;
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
  let strokeBuffer:WebGLBuffer|null=null,strokeVertices=0,routeVertices=0;
  const strokeData=new Float32Array(STROKE_SEGMENTS*6*10),strokeBundles=new Map<string,Bundle>();
  let planes: readonly Aircraft[] = [], trails: readonly SkyTrail[] = [], selected: string | null = null;
  let planeVertices = 0, trailVertices = 0, flat = false, trailDirty = true, showPaths = true, showGuides = true;
  const data = new Float32Array((PLANE_CAPACITY + TRAIL_VERTICES + GUIDE_VERTICES) * 6);
  const terrainCache = new Map<string, number | null>();
  let terrainRetry = 0, terrainQueries = 0, guideCount = 0;
  const terrainAt = (point: SkyPoint) => {
    const key = `${point.lon.toFixed(6)},${point.lat.toFixed(6)}`;
    if (terrainCache.has(key)) return terrainCache.get(key)!;
    let height: number | null = null;
    try { const value=map.queryTerrainElevation([point.lon,point.lat]); if(value!==null&&Number.isFinite(value))height=value; } catch { /* Missing terrain omits the guide, not the aircraft. */ }
    if(terrainCache.size>=SKY_MAX_HEIGHT_GUIDES*4)terrainCache.delete(terrainCache.keys().next().value!);
    terrainCache.set(key,height);terrainQueries++;return height;
  };
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
  const build = (input: CustomRenderMethodInput, globe: boolean, stroke=false) => {
    const vertex = compile(gl!.VERTEX_SHADER, `#version 300 es\n${globe ? `${input.shaderData.vertexShaderPrelude}\n${input.shaderData.define}` : "uniform mat4 u_matrix; uniform float u_world;"}
      uniform vec2 u_origin; in vec3 a_position; in vec3 a_color; out vec3 v_color;
      ${stroke?"in vec3 a_other; in float a_side; uniform vec2 u_viewport; uniform float u_width;":""}
      void main(){v_color=a_color; gl_Position=${globe ? "projectTileWithElevation(u_origin+a_position.xy,a_position.z)" : "u_matrix*vec4((u_origin+a_position.xy)*u_world,a_position.z,1.)"};
        ${stroke?`vec4 other=${globe?"projectTileWithElevation(u_origin+a_other.xy,a_other.z)":"u_matrix*vec4((u_origin+a_other.xy)*u_world,a_other.z,1.)"};
          vec2 direction=(other.xy/max(.00001,other.w)-gl_Position.xy/max(.00001,gl_Position.w))*u_viewport;
          vec2 normal=vec2(-direction.y,direction.x)/max(.00001,length(direction));
          gl_Position.xy+=normal*a_side*u_width/u_viewport*gl_Position.w;`:""}
      }`);
    const fragment = compile(gl!.FRAGMENT_SHADER, `#version 300 es\nprecision highp float; in vec3 v_color; ${stroke?"uniform float u_halo;":""} out vec4 fragColor; void main(){fragColor=vec4(${stroke?"mix(v_color,vec3(.025,.09,.12),u_halo)":"v_color"},1.);}`);
    const program = gl!.createProgram()!; gl!.attachShader(program, vertex); gl!.attachShader(program, fragment); gl!.linkProgram(program);
    gl!.deleteShader(vertex); gl!.deleteShader(fragment);
    if (!gl!.getProgramParameter(program, gl!.LINK_STATUS)) { gl!.deleteProgram(program); throw new Error("Aircraft shader unavailable"); }
    const vao = gl!.createVertexArray()!; gl!.bindVertexArray(vao); gl!.bindBuffer(gl!.ARRAY_BUFFER, stroke?strokeBuffer:buffer);
    const attributes=stroke?[["a_position",0,3],["a_other",12,3],["a_side",24,1],["a_color",28,3]] as const:[["a_position",0,3],["a_color",12,3]] as const;
    for (const [name, offset, size] of attributes) { const at = gl!.getAttribLocation(program, name); gl!.enableVertexAttribArray(at); gl!.vertexAttribPointer(at, size, gl!.FLOAT, false, stroke?40:24, offset); }
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
      // The selected aircraft is a larger faceted symbol; it is not a scale model.
      // Other aircraft retain the small, bounded four-triangle silhouette.
      const detailed=a.hex===selected&&a.trackDeg!==null&&!flat;
      const symbolSize=size*(detailed?6:1);
      const outline:readonly (readonly number[])[]=a.trackDeg===null
        ? [[0,0],[0,.6],[.6,0],[0,0],[.6,0],[0,-.6],[0,0],[0,-.6],[-.6,0],[0,0],[-.6,0],[0,.6]]
        : detailed ? [
          [0,1,0,1.1],[.11,-.7,0,.75],[0,-.6,.13,1.1],
          [0,1,0,1.1],[0,-.6,.13,1.1],[-.11,-.7,0,.9],
          [0,1,0,.65],[0,-.7,-.1,.5],[.11,-.7,0,.75],
          [0,1,0,.65],[-.11,-.7,0,.9],[0,-.7,-.1,.5],
          [-1,-.22,0,.75],[-.1,.28,.02,1],[0,-.35,.04,1.1],
          [0,-.35,.04,1.1],[.1,.28,.02,1],[1,-.22,0,.7],
          [-.46,-.82,0,.75],[0,-.54,.04,1.1],[.46,-.82,0,.85],
          [0,-.92,0,.7],[0,-.48,.04,1],[0,-.77,.38,1.2],
        ] : [[0,1],[.13,-.8],[-.13,-.8],[-.9,-.1],[0,.25],[.9,-.1],[-.45,-.75],[0,-.5],[.45,-.75],[0,1],[.13,-.8],[-.13,-.8]];
      for (const [east,north,up=0,shade=1] of outline) {
        const e=(east*Math.cos(bank)+up*Math.sin(bank))*symbolSize,n=north*symbolSize;
        // readsb positive roll is right-wing down; local east is the aircraft's right side.
        const z=markerAltitude(a)+bankHeightOffset(east*symbolSize,flat?0:a.rollDeg)+up*symbolSize*Math.cos(bank);
        put(x+(e*Math.cos(heading)+n*Math.sin(heading))*unit,y+(e*Math.sin(heading)-n*Math.cos(heading))*unit,z,c.map(value=>Math.min(1,value*shade)));
      }
    }
    planeVertices=count;
    gl!.bindBuffer(gl!.ARRAY_BUFFER,buffer); gl!.bufferSubData(gl!.ARRAY_BUFFER,0,data.subarray(0,count*6));
    dirty=false;
    if(!trailDirty)return;
    count=PLANE_CAPACITY;
    strokeVertices=0;routeVertices=0;
    const stroke=(a:readonly number[],b:readonly number[],c:readonly number[])=>{
      if(strokeVertices+6>STROKE_SEGMENTS*6)return;
      for(const [from,to,side]of [[a,b,-1],[a,b,-1],[a,b,1],[b,a,1],[b,a,-1],[b,a,-1]] as const){strokeData.set([from[0]-origin[0],from[1]-origin[1],from[2],to[0]-origin[0],to[1]-origin[1],to[2],side,...c],strokeVertices*10);strokeVertices++;}
    };
    const drawable=flat?trails:trails.flatMap(trail=>heightProfile(trail.points,TRAIL_VERTICES/2).map(points=>({...trail,points})));
    const segments=drawable.reduce((n,t)=>n+Math.max(0,t.points.length-1),0);
    const stride=Math.max(1,Math.ceil(segments/(TRAIL_VERTICES/2)));
    if(showPaths)for (const trail of drawable) for(let i=1;i<trail.points.length;i+=stride) {
      if(count-PLANE_CAPACITY+2>TRAIL_VERTICES) break;
      const end=Math.min(i+stride-1,trail.points.length-1);
      for(const p of [trail.points[i-1],trail.points[end]]) { const [x,y]=xy(p.lon,p.lat); put(x,y,flat?0:altitude(p),trail.future?[.40,.88,1]:color(p,trail.hex===selected)); }
    }
    const selectedPaths=drawable.filter(trail=>trail.hex===selected),selectedSegments=selectedPaths.reduce((sum,t)=>sum+Math.max(0,t.points.length-1),0),selectedStride=Math.max(1,Math.ceil(selectedSegments/4096));
    if(showPaths)for(const trail of selectedPaths)for(let i=1;i<trail.points.length;i+=selectedStride){
      if(strokeVertices>=4096*6)break;
      const a=trail.points[i-1],b=trail.points[Math.min(trail.points.length-1,i+selectedStride-1)];
      stroke([...xy(a.lon,a.lat),flat?0:altitude(a)],[...xy(b.lon,b.lat),flat?0:altitude(b)],trail.future?[.40,.88,1]:[1,.82,.30]);
    }
    routeVertices=strokeVertices;
    guideCount=0;
    if(showPaths&&showGuides&&!flat&&selected){
      const selectedPoints=trails.filter(t=>t.hex===selected).flatMap((trail,index)=>trail.points.map((point,i)=>i===0&&index>0?{...point,breakBefore:true}:point));
      for(const part of heightProfile(selectedPoints,SKY_MAX_HEIGHT_GUIDES)){
        let previous: {point:SkyPoint;height:number}|null=null;
        for(const point of part){
          const ground=terrainAt(point);if(ground===null){previous=null;continue;}
          const [x,y]=xy(point.lon,point.lat);
          put(x,y,ground,[.22,.62,.68]);put(x,y,altitude(point),[.75,.70,.40]);guideCount++;
          stroke([x,y,ground],[x,y,altitude(point)],[.45,.80,.83]);
          if(previous){const [px,py]=xy(previous.point.lon,previous.point.lat);put(px,py,previous.height,[.15,.43,.49]);put(x,y,ground,[.15,.43,.49]);}
          previous={point,height:ground};
        }
      }
    }
    trailVertices=count-PLANE_CAPACITY;
    if(trailVertices)gl!.bufferSubData(gl!.ARRAY_BUFFER,PLANE_CAPACITY*24,data.subarray(PLANE_CAPACITY*6,count*6));
    if(strokeVertices){gl!.bindBuffer(gl!.ARRAY_BUFFER,strokeBuffer);gl!.bufferSubData(gl!.ARRAY_BUFFER,0,strokeData.subarray(0,strokeVertices*10));}trailDirty=false;
  };
  const layer: CustomLayerInterface = { id:ID,type:"custom",renderingMode:"3d",onAdd(_map,context) {
    gl=context as WebGL2RenderingContext; buffer=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buffer); gl.bufferData(gl.ARRAY_BUFFER,data.byteLength,gl.DYNAMIC_DRAW);
    strokeBuffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,strokeBuffer);gl.bufferData(gl.ARRAY_BUFFER,strokeData.byteLength,gl.DYNAMIC_DRAW);dirty=true;trailDirty=true;
  },render(_context,input) {
    if(!active||!gl||!buffer||document.hidden) return;
    const globe=map.getProjection().type==="globe", key=globe?input.shaderData.variantName:"mercator";
    if(failed.has(key))return;
    let bundle=bundles.get(key);
    try { if(!bundle) {bundle=build(input,globe);bundles.set(key,bundle);} } catch {failed.add(key);report("Aircraft renderer unavailable; use the aircraft list.");return;}
    if(showGuides&&performance.now()-terrainRetry>5000){terrainRetry=performance.now();for(const [key,value]of terrainCache)if(value===null)terrainCache.delete(key);trailDirty=true;}
    if(dirty||trailDirty) upload();
    const project=(target:Bundle)=>{gl!.useProgram(target.program);gl!.bindVertexArray(target.vao);const u=target.u, world=512*2**map.getZoom();
    gl!.uniform2f(u.u_origin,...origin as [number,number]);
    if(globe) {const p=input.defaultProjectionData;gl!.uniformMatrix4fv(u.u_projection_matrix,false,p.mainMatrix as Float32Array);gl!.uniformMatrix4fv(u.u_projection_fallback_matrix,false,p.fallbackMatrix as Float32Array);gl!.uniform4f(u.u_projection_tile_mercator_coords,...p.tileMercatorCoords);gl!.uniform4f(u.u_projection_clipping_plane,...p.clippingPlane);gl!.uniform1f(u.u_projection_transition,p.projectionTransition);}
    else {gl!.uniformMatrix4fv(u.u_matrix,false,Float32Array.from(input.modelViewProjectionMatrix));gl!.uniform1f(u.u_world,world);}};
    project(bundle);
    if(flat)gl.disable(gl.DEPTH_TEST);else gl.enable(gl.DEPTH_TEST);gl.depthMask(false);gl.disable(gl.CULL_FACE);gl.lineWidth(1);
    gl.drawArrays(gl.LINES,PLANE_CAPACITY,trailVertices);
    if(strokeVertices&&!failed.has(`stroke:${key}`)){let pathBundle=strokeBundles.get(key);try{if(!pathBundle){pathBundle=build(input,globe,true);strokeBundles.set(key,pathBundle);}project(pathBundle);
      gl.uniform2f(pathBundle.u.u_viewport,map.getCanvas().clientWidth,map.getCanvas().clientHeight);
      // Pixel-width strips remain legible at regional zoom; their centerline is still the observed route.
      gl.uniform1f(pathBundle.u.u_halo,1);gl.uniform1f(pathBundle.u.u_width,7);gl.drawArrays(gl.TRIANGLE_STRIP,0,routeVertices);
      gl.uniform1f(pathBundle.u.u_width,3);gl.drawArrays(gl.TRIANGLE_STRIP,routeVertices,strokeVertices-routeVertices);
      gl.uniform1f(pathBundle.u.u_halo,0);gl.uniform1f(pathBundle.u.u_width,3.2);gl.drawArrays(gl.TRIANGLE_STRIP,0,routeVertices);
      gl.uniform1f(pathBundle.u.u_width,1.2);gl.drawArrays(gl.TRIANGLE_STRIP,routeVertices,strokeVertices-routeVertices);
    }catch{failed.add(`stroke:${key}`);report("Flight path emphasis unavailable; aircraft and source details remain available.");}}
    project(bundle);gl.drawArrays(gl.TRIANGLES,0,planeVertices);gl.bindVertexArray(null);
    // Mercator's exact elevated clip positions make aircraft clickable in 3D.
    hits=[];
    if(!globe) {const m=input.modelViewProjectionMatrix,world=512*2**map.getZoom();for(const a of planes.slice(0,LIMIT)){const [xx,yy]=xy(a.lon,a.lat),x=xx*world,y=yy*world,z=markerAltitude(a),w=m[3]*x+m[7]*y+m[11]*z+m[15];if(w<=0)continue;hits.push({hex:a.hex,x:((m[0]*x+m[4]*y+m[8]*z+m[12])/w+1)*map.getCanvas().clientWidth/2,y:(1-(m[1]*x+m[5]*y+m[9]*z+m[13])/w)*map.getCanvas().clientHeight/2});}}
  },onRemove(){if(gl){for(const b of [...bundles.values(),...strokeBundles.values()]){gl.deleteProgram(b.program);gl.deleteVertexArray(b.vao);}if(buffer)gl.deleteBuffer(buffer);if(strokeBuffer)gl.deleteBuffer(strokeBuffer);}bundles.clear();strokeBundles.clear();failed.clear();buffer=null;strokeBuffer=null;gl=null;hits=[];}};
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
  const awaitStyle=()=>{if(!active)return;terrainCache.clear();groundMarkers.clear();trailDirty=true;map.on("render",install);map.on("error",install);install();};
  const zoom=()=>{dirty=true;groundMarkers.clear();};
  const terrainChanged=(event:{sourceDataType?:string})=>{if(event.sourceDataType!=="idle")return;terrainCache.clear();trailDirty=true;};
  map.on("style.load",awaitStyle);map.on("zoom",zoom);map.on("sourcedata",terrainChanged);awaitStyle();
  return { update(next:readonly Aircraft[], nextTrails:readonly SkyTrail[], id:string|null, flatView=false, paths=true, guides=true){
    if(trails!==nextTrails||selected!==id||flat!==flatView||showPaths!==paths||showGuides!==guides)trailDirty=true;
    flat=flatView;planes=next;trails=nextTrails;selected=id;showPaths=paths;showGuides=guides;dirty=true;map.triggerRepaint();
  }, updateAircraft(next:readonly Aircraft[]){planes=next;dirty=true;map.triggerRepaint();}, metrics(){return {aircraft:Math.min(planes.length,LIMIT),trailVertices,heightGuides:guideCount,terrainQueries};}, dispose(){active=false;map.off("style.load",awaitStyle);map.off("render",install);map.off("error",install);if(aircraftPickers.get(map)===pick)aircraftPickers.delete(map);map.off("zoom",zoom);map.off("sourcedata",terrainChanged);terrainCache.clear();if(map.getLayer(ID))map.removeLayer(ID);} };
}
