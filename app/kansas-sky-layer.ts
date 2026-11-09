import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";
import { TRAFFIC_ALTITUDE_COLORS, type Aircraft } from "./aviation-traffic";
import { bankHeightOffset, skyDrawableTrails, limitSkyTrailPoints, SKY_MAX_HEIGHT_GUIDES, type SkyPoint, type SkyTrail } from "./kansas-sky";

type SkyPickPoint = Readonly<{ x: number; y: number }>;
const aircraftPickers = new WeakMap<MapLibreMap, (point: SkyPickPoint) => boolean>();
/** Called by the map's click owner after measuring/point-picking priority guards. */
export function pickKansasSkyAircraft(map: MapLibreMap, point: SkyPickPoint): boolean {
  return aircraftPickers.get(map)?.(point) ?? false;
}

type SkyTerrain=NonNullable<ReturnType<MapLibreMap["getTerrain"]>>;
const terrainFocusLeases=new WeakMap<MapLibreMap,{owners:number;release:()=>void}>();
/** Display terrain at 1× during focus; preserve the latest requested source/scale. */
export function leaseKansasSkyTerrain(map:MapLibreMap):()=>void{
  let lease=terrainFocusLeases.get(map);
  if(!lease){
    let requested:SkyTerrain|null=null,changing=false;
    const reconcile=()=>{
      if(changing)return;
      const current=map.getTerrain?.();requested=current?{...current}:null;
      if(current&&(current.exaggeration??1)!==1){changing=true;try{map.setTerrain({...current,exaggeration:1});}finally{changing=false;}}
    };
    const styleChanged=()=>{const current=map.getTerrain?.();if(!current||current.source!==requested?.source||(current.exaggeration??1)!==1)reconcile();};
    map.on("terrain",reconcile);map.on("style.load",styleChanged);reconcile();
    lease={owners:0,release:()=>{map.off("terrain",reconcile);map.off("style.load",styleChanged);const current=map.getTerrain?.();if(current&&requested&&current.source===requested.source&&(current.exaggeration??1)===1)map.setTerrain(requested);}};
    terrainFocusLeases.set(map,lease);
  }
  lease.owners++;let active=true;
  return()=>{if(!active)return;active=false;if(--lease!.owners===0){terrainFocusLeases.delete(map);lease!.release();}};
}

/** Explicit presentation-only focus. Restores owned paint values and leaves TFRs and source state intact. */
export function attachKansasSkyFocus(map:MapLibreMap){
  const restoreTerrain=leaseKansasSkyTerrain(map);
  type PaintName=Parameters<MapLibreMap["getPaintProperty"]>[1];
  type PaintValue=Parameters<MapLibreMap["setPaintProperty"]>[2];
  const owned=new Map<string,{layer:unknown;property:PaintName;original:PaintValue;applied:PaintValue}>();let active=true,changing=false;
  const same=(a:unknown,b:unknown)=>JSON.stringify(a)===JSON.stringify(b);
  const apply=()=>{
    if(!active||changing)return;changing=true;
    try{const style=map.getStyle();for(const layer of style?.layers??[]){
      const chart=layer.id.startsWith("chart-"),background=layer.id==="kfm-background"&&style?.name==="KFM Aviation Chart";
      const context=/^kfm-aviation-(?:airspace|drone|uas|airways|runways|airports|metar|ceilings|pireps)(?:-|$)/.test(layer.id);
      const paints:Record<string,unknown>={};
      if(background)paints["background-color"]="#0a202c";
      if(chart){
        if(layer.type==="color-relief"){paints["color-relief-color"]=["interpolate",["linear"],["elevation"],0,"#0d2935",500,"#163843",1500,"#224550",3500,"#30505a"];paints["color-relief-opacity"]=.8;}
        if(layer.type==="fill"){paints["fill-color"]=layer.id.includes("water")?"#092b3d":"#26434e";paints["fill-opacity"]=.65;}
        // Provider land-use outlines are basemap context, not airspace restrictions.
        if(layer.id==="chart-urban")paints["fill-outline-color"]="#3f5c63";
        if(layer.type==="line"){paints["line-color"]="#60818b";paints["line-opacity"]=layer.id.includes("boundary")||layer.id.includes("outline")?.65:.3;}
        if(layer.type==="symbol"){paints["text-color"]="#b5cbd0";paints["text-halo-color"]="#0c2531";paints["text-halo-width"]=1;paints["text-opacity"]=.8;}
        if(layer.type==="circle"){paints["circle-opacity"]=.2;paints["circle-stroke-opacity"]=.5;}
      }
      if(layer.type==="hillshade"&&style?.name==="KFM Aviation Chart"){paints["hillshade-exaggeration"]=.14;paints["hillshade-shadow-color"]="#061b27";paints["hillshade-highlight-color"]="#345660";paints["hillshade-accent-color"]="#24434d";}
      if(layer.type==="raster"&&!/^kfm-/.test(layer.id)){paints["raster-brightness-max"]=.32;paints["raster-saturation"]=-.65;paints["raster-contrast"]=-.15;}
      const properties:readonly PaintName[]=context?(layer.type==="fill"?["fill-opacity"]:layer.type==="fill-extrusion"?["fill-extrusion-opacity"]:layer.type==="line"?["line-opacity"]:layer.type==="circle"?["circle-opacity","circle-stroke-opacity"]:layer.type==="symbol"?["text-opacity","icon-opacity"]:[]):Object.keys(paints) as PaintName[];
      for(const property of properties){const key=`${layer.id}:${property}`,identity=map.getLayer(layer.id),current=map.getPaintProperty(layer.id,property),existing=owned.get(key);
        if(existing&&existing.layer===identity&&same(current,existing.applied))continue;
        const original=current as PaintValue,applied=(context?(typeof original==="number"?original*.12:["*",original??1,.12]):paints[property]) as PaintValue;
        owned.set(key,{layer:identity,property,original,applied});map.setPaintProperty(layer.id,property,applied);
      }
    }}finally{changing=false;}
  };
  map.on("styledata",apply);apply();
  return ()=>{active=false;map.off("styledata",apply);for(const [key,record]of owned){const id=key.slice(0,key.lastIndexOf(":"));if(map.getLayer(id)===record.layer&&same(map.getPaintProperty(id,record.property),record.applied))map.setPaintProperty(id,record.property,record.original);}owned.clear();restoreTerrain();};
}

const ID = "kfm-kansas-sky";
const LIMIT = 3000, PLANE_CAPACITY = LIMIT * 12 + 48, TRAIL_VERTICES = 60000, GUIDE_VERTICES = SKY_MAX_HEIGHT_GUIDES * 4;
const STROKE_SEGMENTS=4096+SKY_MAX_HEIGHT_GUIDES;
const RAD = Math.PI / 180;
const DIAMOND=[[0,0],[0,.6],[.6,0],[0,0],[.6,0],[0,-.6],[0,0],[0,-.6],[-.6,0],[0,0],[-.6,0],[0,.6]];
const PLANE=[[0,1],[.13,-.8],[-.13,-.8],[-.9,-.1],[0,.25],[.9,-.1],[-.45,-.75],[0,-.5],[.45,-.75],[0,1],[.13,-.8],[-.13,-.8]];
const SELECTED_PLANE=[[0,1,0,1.1],[.11,-.7,0,.75],[0,-.6,.13,1.1],[0,1,0,1.1],[0,-.6,.13,1.1],[-.11,-.7,0,.9],[0,1,0,.65],[0,-.7,-.1,.5],[.11,-.7,0,.75],[0,1,0,.65],[-.11,-.7,0,.9],[0,-.7,-.1,.5],[-1,-.22,0,.75],[-.1,.28,.02,1],[0,-.35,.04,1.1],[0,-.35,.04,1.1],[.1,.28,.02,1],[1,-.22,0,.7],[-.46,-.82,0,.75],[0,-.54,.04,1.1],[.46,-.82,0,.85],[0,-.92,0,.7],[0,-.48,.04,1],[0,-.77,.38,1.2]];
const xy = (lon: number, lat: number) => [(lon + 180) / 360, (180 - Math.log(Math.tan(Math.PI / 4 + lat * RAD / 2)) / RAD) / 360];
const origin = xy(-98.35, 38.5);
const uniforms = ["u_marker_max_size", "u_marker_size", "u_pixel_ratio", "u_matrix", "u_world", "u_origin", "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition", "u_viewport", "u_width", "u_halo", "u_opacity", "u_point"];
type Bundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; u: Record<string, WebGLUniformLocation | null> };
export type { SkyTrail } from "./kansas-sky";
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
export function attachKansasSky(map: MapLibreMap, select: (hex: string) => void, report: (message: string) => void, projectionChanged?:(phase:number|null)=>void) {
  let gl: WebGL2RenderingContext | null = null, buffer: WebGLBuffer | null = null, active = true, dirty = true;
  let projectionPhase:number|null=null,projectionNoticePending=false;
  const notifyProjection=(phase:number|null)=>{if(phase===projectionPhase)return;projectionPhase=phase;if(projectionChanged&&!projectionNoticePending){projectionNoticePending=true;queueMicrotask(()=>{projectionNoticePending=false;if(active)projectionChanged(projectionPhase);});}};
  let strokeBuffer:WebGLBuffer|null=null,markerBuffer:WebGLBuffer|null=null,strokeVertices=0,routeVertices=0,markerPointLimit=256;
  const markerData=new Float32Array(LIMIT*11),markerBundles=new Map<string,Bundle>();
  const strokeData=new Float32Array(STROKE_SEGMENTS*6*11),strokeBundles=new Map<string,Bundle>();
  let planes: readonly Aircraft[] = [], trails: readonly SkyTrail[] = [], selected: string | null = null;
  let planeVertices = 0, trailVertices = 0, fallbackVertices=0, focalVertex=-1, flat = false, trailDirty = true, showPaths = true, showGuides = true;
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
  let hits: { hex: string; x: number; y: number; radius:number; depth:number }[] = [];
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
  const build = (input: CustomRenderMethodInput, stroke=false) => {
    const vertex = compile(gl!.VERTEX_SHADER, `#version 300 es\n${input.shaderData.vertexShaderPrelude}\n${input.shaderData.define}
      uniform vec2 u_origin; in vec3 a_position; in vec3 a_color; out vec3 v_color; out float v_visibility; uniform float u_point;
      ${stroke?"in vec3 a_other; in float a_side; in float a_edge; out float v_edge; uniform vec2 u_viewport; uniform float u_width;":""}
      void main(){v_color=a_color; gl_PointSize=36.; gl_Position=projectTileFor3D((u_origin+a_position.xy)*8192.,a_position.z);
        v_visibility=1.;
        #ifdef GLOBE
        // Keep true depth and clip the hidden hemisphere independently.
        vec3 elevated=projectToSphere((u_origin+a_position.xy)*8192.)*(1.+a_position.z/6371008.8);
        v_visibility=1.-globeComputeClippingZ(elevated)*clamp((u_projection_transition-.2)/.8,0.,1.);
        #endif
        ${stroke?`vec4 other=projectTileFor3D((u_origin+a_other.xy)*8192.,a_other.z);
          v_edge=a_edge;
          if(gl_Position.w<=.00001||other.w<=.00001){gl_Position=vec4(2.,2.,2.,1.);return;}
          vec2 direction=(other.xy/max(.00001,other.w)-gl_Position.xy/max(.00001,gl_Position.w))*u_viewport;
          vec2 normal=vec2(-direction.y,direction.x)/max(.00001,length(direction));
          gl_Position.xy+=normal*a_side*u_width/u_viewport*gl_Position.w;`:""}
      }`);
    const fragment = compile(gl!.FRAGMENT_SHADER, `#version 300 es\nprecision highp float; in vec3 v_color; in float v_visibility; uniform float u_opacity; uniform float u_point; ${stroke?"uniform float u_halo; in float v_edge;":""} out vec4 fragColor; void main(){
      if(v_visibility<0.)discard;
      float alpha=u_opacity;
      ${stroke?"alpha*=u_halo>.5?pow(max(0.,1.-abs(v_edge)),2.):1.-smoothstep(.55,1.,abs(v_edge));":"if(u_point>.5){float d=length(gl_PointCoord-vec2(.5))*2.;alpha=(1.-smoothstep(.15,1.,d))*.22+(1.-smoothstep(.035,.085,abs(d-.64)))*.45;}"}
      fragColor=vec4(v_color,alpha);}`);
    const program = gl!.createProgram()!; gl!.attachShader(program, vertex); gl!.attachShader(program, fragment); gl!.linkProgram(program);
    gl!.deleteShader(vertex); gl!.deleteShader(fragment);
    if (!gl!.getProgramParameter(program, gl!.LINK_STATUS)) { gl!.deleteProgram(program); throw new Error("Aircraft shader unavailable"); }
    const vao = gl!.createVertexArray()!; gl!.bindVertexArray(vao); gl!.bindBuffer(gl!.ARRAY_BUFFER, stroke?strokeBuffer:buffer);
    const attributes=stroke?[["a_position",0,3],["a_other",12,3],["a_side",24,1],["a_color",28,3],["a_edge",40,1]] as const:[["a_position",0,3],["a_color",12,3]] as const;
    for (const [name, offset, size] of attributes) { const at = gl!.getAttribLocation(program, name); gl!.enableVertexAttribArray(at); gl!.vertexAttribPointer(at, size, gl!.FLOAT, false, stroke?44:24, offset); }
    gl!.bindVertexArray(null);
    return { program, vao, u: Object.fromEntries(uniforms.map(name => [name, gl!.getUniformLocation(program, name)])) };
  };
  // One point per observation, independent of world-size mesh detail. The
  // backing/outline are schematic CSS pixels; position and 3D depth stay exact.
  const buildMarkers = (input:CustomRenderMethodInput):Bundle => {
    const vertex=compile(gl!.VERTEX_SHADER,`#version 300 es\n${input.shaderData.vertexShaderPrelude}\n${input.shaderData.define}
      uniform vec2 u_origin; uniform vec2 u_viewport; uniform float u_marker_size; uniform float u_marker_max_size; uniform float u_pixel_ratio;
      in vec3 a_position; in vec3 a_other; in vec3 a_color; in float a_selected; in float a_known;
      out vec3 v_color; out vec2 v_marker_direction; out float v_selected; out float v_known; out float v_visibility;
      void main(){
        gl_Position=projectTileFor3D((u_origin+a_position.xy)*8192.,a_position.z);
        vec4 nose=projectTileFor3D((u_origin+a_other.xy)*8192.,a_other.z);
        vec2 direction=(nose.xy/max(.00001,nose.w)-gl_Position.xy/max(.00001,gl_Position.w))*u_viewport;
        v_marker_direction=length(direction)>.00001?normalize(direction):vec2(0.,1.);
        gl_PointSize=min((a_selected>.5?40.:u_marker_size)*u_pixel_ratio,u_marker_max_size);
        v_color=a_color;v_selected=a_selected;v_known=a_known;v_visibility=1.;
        #ifdef GLOBE
        vec3 elevated=projectToSphere((u_origin+a_position.xy)*8192.)*(1.+a_position.z/6371008.8);
        v_visibility=1.-globeComputeClippingZ(elevated)*clamp((u_projection_transition-.2)/.8,0.,1.);
        #endif
      }`);
    const fragment=compile(gl!.FRAGMENT_SHADER,`#version 300 es\nprecision highp float;
      in vec3 v_color;in vec2 v_marker_direction;in float v_selected;in float v_known;in float v_visibility;out vec4 fragColor;
      float triangle(vec2 p,vec2 a,vec2 b,vec2 c){
        float ab=(b.x-a.x)*(p.y-a.y)-(b.y-a.y)*(p.x-a.x),bc=(c.x-b.x)*(p.y-b.y)-(c.y-b.y)*(p.x-b.x),ca=(a.x-c.x)*(p.y-c.y)-(a.y-c.y)*(p.x-c.x);
        return (ab>=0.&&bc>=0.&&ca>=0.)||(ab<=0.&&bc<=0.&&ca<=0.)?1.:0.;
      }
      float glyph(vec2 p){return max(triangle(p,vec2(0.,.82),vec2(.13,-.65),vec2(-.13,-.65)),max(triangle(p,vec2(-.8,-.1),vec2(0.,.25),vec2(.8,-.1)),triangle(p,vec2(-.4,-.62),vec2(0.,-.4),vec2(.4,-.62))));}
      void main(){
        if(v_visibility<0.)discard;
        vec2 p=(gl_PointCoord-vec2(.5))*2.;p.y=-p.y;float d=length(p);
        if(d>.98)discard;
        vec2 nose=v_marker_direction,right=vec2(nose.y,-nose.x),q=vec2(dot(p,right),dot(p,nose));
        float shape=v_known>.5?glyph(q*1.3):1.-step(.53,abs(q.x)+abs(q.y));
        // Crisp ivory and dark backing work on both chart and light terrain.
        vec3 ink=vec3(.02,.08,.12),bright=mix(v_color,vec3(1.,.98,.88),.7);
        float ring=(1.-smoothstep(.04,.09,abs(d-.81)))*(v_selected>.5?1.:.5);
        float backing=(1.-smoothstep(.65,.76,d))*(v_selected>.5?.78:.93);
        float alpha=max(backing,ring);if(alpha<.01)discard;
        fragColor=vec4(mix(ink,bright,max(shape,ring)),alpha);
      }`);
    const program=gl!.createProgram()!;gl!.attachShader(program,vertex);gl!.attachShader(program,fragment);gl!.linkProgram(program);gl!.deleteShader(vertex);gl!.deleteShader(fragment);
    if(!gl!.getProgramParameter(program,gl!.LINK_STATUS)){gl!.deleteProgram(program);throw new Error("Aircraft locators unavailable");}
    const vao=gl!.createVertexArray()!;gl!.bindVertexArray(vao);gl!.bindBuffer(gl!.ARRAY_BUFFER,markerBuffer);
    for(const [name,offset,size]of [["a_position",0,3],["a_other",12,3],["a_color",24,3],["a_selected",36,1],["a_known",40,1]] as const){const at=gl!.getAttribLocation(program,name);gl!.enableVertexAttribArray(at);gl!.vertexAttribPointer(at,size,gl!.FLOAT,false,44,offset);}
    gl!.bindVertexArray(null);return{program,vao,u:Object.fromEntries(uniforms.map(name=>[name,gl!.getUniformLocation(program,name)]))};
  };
  // CPU counterpart of the installed public projectTileFor3D contract. It is
  // used only for hit centers; GPU output remains the rendering authority.
  const multiply=(m:ArrayLike<number>,x:number,y:number,z:number)=>[m[0]*x+m[4]*y+m[8]*z+m[12],m[1]*x+m[5]*y+m[9]*z+m[13],m[2]*x+m[6]*y+m[10]*z+m[14],m[3]*x+m[7]*y+m[11]*z+m[15]];
  const clipPosition=(lon:number,lat:number,height:number,p:ReturnType<CustomRenderMethodInput["getProjectionData"]>,globe:boolean)=>{
    const [x,y]=xy(lon,lat);
    if(!globe)return {clip:multiply(p.mainMatrix,x*8192,y*8192,height),visibility:1};
    const radius=1+height/6371008.8,cos=Math.cos(lat*RAD),sphere=[Math.sin(lon*RAD)*cos*radius,Math.sin(lat*RAD)*radius,Math.cos(lon*RAD)*cos*radius];
    const actual=multiply(p.mainMatrix,sphere[0],sphere[1],sphere[2]),fallback=multiply(p.fallbackMatrix,x*8192,y*8192,height),phase=p.projectionTransition;
    const plane=p.clippingPlane,visibility=1-(1-(sphere[0]*plane[0]+sphere[1]*plane[1]+sphere[2]*plane[2]+plane[3]))*Math.max(0,Math.min(1,(phase-.2)/.8));
    return {clip:phase>.999?actual:actual.map((value,index)=>fallback[index]*(1-phase)+value*phase),visibility};
  };
  const upload = () => {
    let count = 0;
    const put = (x: number, y: number, z: number, c: readonly number[],shade=1) => {const offset=count++*6;data[offset]=x-origin[0];data[offset+1]=y-origin[1];data[offset+2]=z;data[offset+3]=Math.min(1,c[0]*shade);data[offset+4]=Math.min(1,c[1]*shade);data[offset+5]=Math.min(1,c[2]*shade);};
    const size = Math.min(1600, 180000 / 2 ** (map.getZoom() - 1));
    for (const a of planes.slice(0, LIMIT)) {
      const [x,y] = xy(a.lon,a.lat), unit = 1 / (40075016.686 * Math.cos(a.lat * RAD));
      const direction=a.trueHeadingDeg??a.renderedTrackDeg??a.trackDeg;
      const heading = (direction ?? 0) * RAD, bank = (flat?0:a.rollDeg ?? 0) * RAD, c = color(a,a.hex===selected);
      // The selected aircraft is a larger faceted symbol; it is not a scale model.
      // Other aircraft retain the small, bounded four-triangle silhouette.
      const detailed=a.hex===selected&&direction!==null&&!flat;
      const symbolSize=size*(detailed?4.5:1),outline=direction===null?DIAMOND:detailed?SELECTED_PLANE:PLANE;
      const height=markerAltitude(a);
      for (const [east,north,up=0,shade=1] of outline) {
        const e=(east*Math.cos(bank)+up*Math.sin(bank))*symbolSize,n=north*symbolSize;
        // readsb positive roll is right-wing down; local east is the aircraft's right side.
        const z=height+bankHeightOffset(east*symbolSize,flat?0:a.rollDeg)+up*symbolSize*Math.cos(bank);
        put(x+(e*Math.cos(heading)+n*Math.sin(heading))*unit,y+(e*Math.sin(heading)-n*Math.cos(heading))*unit,z,detailed?[1,.94,.76]:c,shade);
      }
    }
    planeVertices=count;
    let marker=0;
    for(const a of planes.slice(0,LIMIT)){
      const [x,y]=xy(a.lon,a.lat),height=markerAltitude(a),unit=1000/(40075016.686*Math.cos(a.lat*RAD)),direction=a.trueHeadingDeg??a.renderedTrackDeg??a.trackDeg,heading=(direction??0)*RAD,c=color(a,a.hex===selected);
      markerData.set([x-origin[0],y-origin[1],height,x+Math.sin(heading)*unit-origin[0],y-Math.cos(heading)*unit-origin[1],height,c[0],c[1],c[2],a.hex===selected?1:0,direction==null?0:1],marker++*11);
    }
    gl!.bindBuffer(gl!.ARRAY_BUFFER,markerBuffer);gl!.bufferSubData(gl!.ARRAY_BUFFER,0,markerData.subarray(0,marker*11));
    focalVertex=-1;const focal=planes.find(plane=>plane.hex===selected);if(focal){focalVertex=count;const [x,y]=xy(focal.lon,focal.lat);put(x,y,markerAltitude(focal),[1,.83,.46]);}
    gl!.bindBuffer(gl!.ARRAY_BUFFER,buffer); gl!.bufferSubData(gl!.ARRAY_BUFFER,0,data.subarray(0,count*6));
    dirty=false;
    if(!trailDirty)return;
    count=PLANE_CAPACITY;
    strokeVertices=0;routeVertices=0;
    const stroke=(a:readonly number[],b:readonly number[],c:readonly number[])=>{
      if(strokeVertices+6>STROKE_SEGMENTS*6)return;
      for(const [from,to,side,edge]of [[a,b,-1,-1],[a,b,1,1],[b,a,1,-1],[a,b,1,1],[b,a,-1,1],[b,a,1,-1]] as const){const offset=strokeVertices++*11;strokeData[offset]=from[0]-origin[0];strokeData[offset+1]=from[1]-origin[1];strokeData[offset+2]=from[2];strokeData[offset+3]=to[0]-origin[0];strokeData[offset+4]=to[1]-origin[1];strokeData[offset+5]=to[2];strokeData[offset+6]=side;strokeData[offset+7]=c[0];strokeData[offset+8]=c[1];strokeData[offset+9]=c[2];strokeData[offset+10]=edge;}
    };
    const drawable=skyDrawableTrails(trails,flat);
    const segments=drawable.reduce((n,t)=>n+Math.max(0,t.points.length-1),0);
    const stride=Math.max(1,Math.ceil(segments/(TRAIL_VERTICES/2)));
    // Keep the selected route in the basic buffer as a bounded shader fallback.
    // It is drawn only if the optional feathered stroke program is unavailable.
    fallbackVertices=0;
    if(showPaths)for(const selectedPass of [true,false]){
      for(const trail of drawable)if((trail.hex===selected)===selectedPass)for(let i=1;i<trail.points.length;i+=stride){
        if(count-PLANE_CAPACITY+2>TRAIL_VERTICES)break;
        const end=Math.min(i+stride-1,trail.points.length-1);
        for(const p of [trail.points[i-1],trail.points[end]]){const [x,y]=xy(p.lon,p.lat);put(x,y,flat?0:altitude(p),trail.future?[.40,.88,1]:color(p,selectedPass));}
      }
      if(selectedPass)fallbackVertices=count-PLANE_CAPACITY;
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
      for(const {points:part} of limitSkyTrailPoints(selectedPaths,SKY_MAX_HEIGHT_GUIDES)){
        let previous: {point:SkyPoint;height:number}|null=null;
        for(const point of part){
          const ground=terrainAt(point);if(ground===null){previous=null;continue;}
          const [x,y]=xy(point.lon,point.lat);
          guideCount++;
          stroke([x,y,ground],[x,y,altitude(point)],[.36,.65,.71]);
          if(previous){const [px,py]=xy(previous.point.lon,previous.point.lat);put(px,py,previous.height,[.15,.43,.49]);put(x,y,ground,[.15,.43,.49]);}
          previous={point,height:ground};
        }
      }
    }
    trailVertices=count-PLANE_CAPACITY;
    if(trailVertices)gl!.bufferSubData(gl!.ARRAY_BUFFER,PLANE_CAPACITY*24,data.subarray(PLANE_CAPACITY*6,count*6));
    if(strokeVertices){gl!.bindBuffer(gl!.ARRAY_BUFFER,strokeBuffer);gl!.bufferSubData(gl!.ARRAY_BUFFER,0,strokeData.subarray(0,strokeVertices*11));}trailDirty=false;
  };
  const layer: CustomLayerInterface = { id:ID,type:"custom",renderingMode:"3d",onAdd(_map,context) {
    gl=context as WebGL2RenderingContext;
    const pointRange=gl.getParameter(gl.ALIASED_POINT_SIZE_RANGE);if(pointRange&&Number.isFinite(pointRange[1]))markerPointLimit=Math.max(1,pointRange[1]);
    buffer=gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,buffer); gl.bufferData(gl.ARRAY_BUFFER,data.byteLength,gl.DYNAMIC_DRAW);
    markerBuffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,markerBuffer);gl.bufferData(gl.ARRAY_BUFFER,markerData.byteLength,gl.DYNAMIC_DRAW);
    strokeBuffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,strokeBuffer);gl.bufferData(gl.ARRAY_BUFFER,strokeData.byteLength,gl.DYNAMIC_DRAW);dirty=true;trailDirty=true;
  },render(_context,input) {
    if(!active||!gl||!buffer||document.hidden) return;
    // Requested globe can render the Mercator variant at close zoom.
    const key=input.shaderData.variantName,globe=key!=="mercator";
    // World-tile coordinates use meter Z in both projection variants. The
    // default custom-layer Mercator matrix instead expects conformal Z.
    const projection=input.getProjectionData({tileID:{canonical:{z:0,x:0,y:0}},applyGlobeMatrix:true});
    const phase=globe?Math.max(0,Math.min(1,projection.projectionTransition)):0;
    notifyProjection(phase);
    if(failed.has(key))return;
    let bundle=bundles.get(key);
    try { if(!bundle) {bundle=build(input);bundles.set(key,bundle);} } catch {failed.add(key);report("Aircraft renderer unavailable; use the aircraft list.");return;}
    if(showGuides&&performance.now()-terrainRetry>5000){terrainRetry=performance.now();for(const [key,value]of terrainCache)if(value===null)terrainCache.delete(key);trailDirty=true;}
    if(dirty||trailDirty) upload();
    const project=(target:Bundle)=>{gl!.useProgram(target.program);gl!.bindVertexArray(target.vao);const u=target.u,p=projection;
      gl!.uniform2f(u.u_origin,...origin as [number,number]);
      gl!.uniformMatrix4fv(u.u_projection_matrix,false,Float32Array.from(p.mainMatrix));gl!.uniformMatrix4fv(u.u_projection_fallback_matrix,false,Float32Array.from(p.fallbackMatrix));gl!.uniform4f(u.u_projection_tile_mercator_coords,...p.tileMercatorCoords);gl!.uniform4f(u.u_projection_clipping_plane,...p.clippingPlane);gl!.uniform1f(u.u_projection_transition,p.projectionTransition);};
    project(bundle);
    if(flat)gl.disable(gl.DEPTH_TEST);else gl.enable(gl.DEPTH_TEST);gl.depthMask(false);gl.disable(gl.CULL_FACE);gl.lineWidth(1);
    gl.enable(gl.BLEND);gl.blendFuncSeparate(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA,gl.ONE,gl.ONE_MINUS_SRC_ALPHA);gl.uniform1f(bundle.u.u_point,0);gl.uniform1f(bundle.u.u_opacity,1);
    // Opaque aircraft establish depth before transparent paths and focal glow.
    gl.depthMask(!flat);gl.drawArrays(gl.TRIANGLES,0,planeVertices);gl.depthMask(false);gl.uniform1f(bundle.u.u_opacity,.48);
    gl.drawArrays(gl.LINES,PLANE_CAPACITY+fallbackVertices,trailVertices-fallbackVertices);
    if(strokeVertices&&!failed.has(`stroke:${key}`)){let pathBundle=strokeBundles.get(key);try{if(!pathBundle){pathBundle=build(input,true);strokeBundles.set(key,pathBundle);}project(pathBundle);
      gl.uniform2f(pathBundle.u.u_viewport,map.getCanvas().clientWidth,map.getCanvas().clientHeight);
      // Pixel-width strips remain legible at regional zoom; their centerline is still the observed route.
      gl.uniform1f(pathBundle.u.u_halo,1);gl.uniform1f(pathBundle.u.u_opacity,.34);gl.uniform1f(pathBundle.u.u_width,8);gl.drawArrays(gl.TRIANGLES,0,routeVertices);
      gl.uniform1f(pathBundle.u.u_halo,0);gl.uniform1f(pathBundle.u.u_opacity,.96);gl.uniform1f(pathBundle.u.u_width,2.5);gl.drawArrays(gl.TRIANGLES,0,routeVertices);
      gl.uniform1f(pathBundle.u.u_opacity,.32);gl.uniform1f(pathBundle.u.u_width,1.2);gl.drawArrays(gl.TRIANGLES,routeVertices,strokeVertices-routeVertices);
    }catch{failed.add(`stroke:${key}`);report("Flight path emphasis unavailable; aircraft and source details remain available.");}}
    project(bundle);if(fallbackVertices&&failed.has(`stroke:${key}`)){gl.uniform1f(bundle.u.u_opacity,.8);gl.drawArrays(gl.LINES,PLANE_CAPACITY,fallbackVertices);}gl.uniform1f(bundle.u.u_opacity,1);if(focalVertex>=0){gl.uniform1f(bundle.u.u_point,1);gl.drawArrays(gl.POINTS,focalVertex,1);}gl.uniform1f(bundle.u.u_point,0);gl.bindVertexArray(null);
    const canvas=map.getCanvas(),markerSize=planes.length>1000?18:22,pixelRatio=canvas.width>0?canvas.width/canvas.clientWidth:1;
    if(!failed.has(`marker:${key}`))try{
      let markers=markerBundles.get(key);if(!markers){markers=buildMarkers(input);markerBundles.set(key,markers);}project(markers);
      gl.uniform2f(markers.u.u_viewport,canvas.clientWidth,canvas.clientHeight);gl.uniform1f(markers.u.u_marker_size,markerSize);
      gl.uniform1f(markers.u.u_pixel_ratio,pixelRatio);gl.uniform1f(markers.u.u_marker_max_size,markerPointLimit);
      gl.drawArrays(gl.POINTS,0,Math.min(planes.length,LIMIT));gl.bindVertexArray(null);
    }catch{failed.add(`marker:${key}`);report("Aircraft locators unavailable; silhouettes and aircraft list remain available.");}
    hits=[];
    for(const a of planes.slice(0,LIMIT)){
      const {clip,visibility}=clipPosition(a.lon,a.lat,markerAltitude(a),projection,globe),[x,y,z,w]=clip,radius=Math.min(a.hex===selected?40:markerSize,markerPointLimit/pixelRatio)/2;
      if(visibility<0||w<=0||!clip.every(Number.isFinite)||z < -w||z>w)continue;
      const px=(x/w+1)*canvas.clientWidth/2,py=(1-y/w)*canvas.clientHeight/2;
      if(px<0||px>canvas.clientWidth||py<0||py>canvas.clientHeight)continue;
      hits.push({hex:a.hex,x:px,y:py,radius,depth:z/w});
    }
  },onRemove(){if(gl){for(const b of [...bundles.values(),...strokeBundles.values(),...markerBundles.values()]){gl.deleteProgram(b.program);gl.deleteVertexArray(b.vao);}if(buffer)gl.deleteBuffer(buffer);if(strokeBuffer)gl.deleteBuffer(strokeBuffer);if(markerBuffer)gl.deleteBuffer(markerBuffer);}bundles.clear();strokeBundles.clear();markerBundles.clear();failed.clear();buffer=null;strokeBuffer=null;markerBuffer=null;gl=null;hits=[];}};
  const pick=(point:SkyPickPoint)=>{if(!active)return false;const hit=hits.map(h=>({...h,d:Math.hypot(h.x-point.x,h.y-point.y)})).filter(h=>h.d<h.radius).sort((a,b)=>a.d-b.d||a.depth-b.depth)[0];if(!hit)return false;select(hit.hex);return true;};
  aircraftPickers.set(map,pick);
  const install=()=>{
    if(!active||!map.isStyleLoaded())return;
    if(!map.getLayer(ID))map.addLayer(layer);
    map.off("render",install);
    map.off("error",install);
  };
  // Other style listeners can queue source work before this renderer mounts.
  // Recheck on ready frames, then release the listener after installation.
  const awaitStyle=()=>{if(!active)return;notifyProjection(null);terrainCache.clear();groundMarkers.clear();trailDirty=true;map.on("render",install);map.on("error",install);install();};
  const zoom=()=>{dirty=true;groundMarkers.clear();};
  // Completed DEM tiles can have no sourceDataType, even while other tiles load.
  // Invalidate only the active terrain source, then coalesce queries at next draw.
  const invalidateTerrain=()=>{terrainCache.clear();groundMarkers.clear();dirty=true;trailDirty=true;map.triggerRepaint();};
  const terrainChanged=(event:{sourceId?:string})=>{const source=map.getTerrain?.()?.source;if(source&&event.sourceId===source)invalidateTerrain();};
  map.on("style.load",awaitStyle);map.on("zoom",zoom);map.on("sourcedata",terrainChanged);map.on("terrain",invalidateTerrain);awaitStyle();
  return { update(next:readonly Aircraft[], nextTrails:readonly SkyTrail[], id:string|null, flatView=false, paths=true, guides=true){
    if(trails!==nextTrails||selected!==id||flat!==flatView||showPaths!==paths||showGuides!==guides)trailDirty=true;
    flat=flatView;planes=next;trails=nextTrails;selected=id;showPaths=paths;showGuides=guides;dirty=true;map.triggerRepaint();
  }, updateAircraft(next:readonly Aircraft[]){planes=next;dirty=true;map.triggerRepaint();}, projection(){return projectionPhase;}, metrics(){return {aircraft:Math.min(planes.length,LIMIT),trailVertices,heightGuides:guideCount,terrainQueries};}, dispose(){active=false;map.off("style.load",awaitStyle);map.off("render",install);map.off("error",install);if(aircraftPickers.get(map)===pick)aircraftPickers.delete(map);map.off("zoom",zoom);map.off("sourcedata",terrainChanged);map.off("terrain",invalidateTerrain);terrainCache.clear();groundMarkers.clear();if(map.getLayer(ID))map.removeLayer(ID);} };
}
