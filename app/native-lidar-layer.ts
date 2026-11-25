import type {CustomLayerInterface,CustomRenderMethodInput,Map as MapLibreMap} from './maplibre-seam';
import {nativeAttributeDomain,nativePointColor,nativePointEligible,nativePointPosition,type NativeColorMode,type NativeDataset} from './native-lidar';
export const NATIVE_LIDAR_LAYER='external-native-lidar-points';
export const NATIVE_FRAME_PIXEL_LIMIT=4_194_304;
export type NativeLayerOptions={scale:number;size:number;color:NativeColorMode;selected:number|null;opacity?:number;gridColor?:'height'|'slope'|'local-relief';framePixelLimit?:number};
export type NativeGeometryBounds=readonly [readonly number[],readonly number[]];
export function nativeTranslatedMatrix(matrix:ArrayLike<number>,origin:readonly number[],bounds?:NativeGeometryBounds|null):Float32Array{
  // Retain double precision through translation and the depth-range remap.
  // XY/W are the original map projection. Only our independent depth buffer
  // uses a tighter range, avoiding coplanar quantization of small height steps.
  const out=Float64Array.from(matrix);for(let row=0;row<4;row++)out[12+row]=matrix[row]*origin[0]+matrix[4+row]*origin[1]+matrix[8+row]*origin[2]+matrix[12+row];
  if(bounds){
    let low=Infinity,high=-Infinity,front=true;
    for(let corner=0;corner<8;corner++){
      const p=[bounds[corner&1][0],bounds[(corner>>1)&1][1],bounds[(corner>>2)&1][2]];
      const w=out[3]*p[0]+out[7]*p[1]+out[11]*p[2]+out[15];
      const z=out[2]*p[0]+out[6]*p[1]+out[10]*p[2]+out[14];
      if(!Number.isFinite(w)||!Number.isFinite(z)||w<=1e-12){front=false;break;}
      low=Math.min(low,z/w);high=Math.max(high,z/w);
    }
    const pad=(high-low)*.01;
    low=Math.max(-1,low-pad);high=Math.min(1,high+pad);
    if(front&&Number.isFinite(low)&&Number.isFinite(high)&&high-low>1e-12){
      const midpoint=(high+low)/2,factor=2/(high-low);
      for(let col=0;col<4;col++)out[col*4+2]=(out[col*4+2]-midpoint*out[col*4+3])*factor;
    }
  }
  return Float32Array.from(out);
}
export function nativePickPixel(point:{x:number;y:number},cssWidth:number,cssHeight:number,width:number,height:number):[number,number]|null{
  if(![point.x,point.y,cssWidth,cssHeight,width,height].every(Number.isFinite)||cssWidth<=0||cssHeight<=0||width<1||height<1||point.x<0||point.y<0||point.x>=cssWidth||point.y>=cssHeight)return null;
  return [Math.floor(point.x/cssWidth*width),height-1-Math.floor(point.y/cssHeight*height)];
}
export const nativeDecodePick=(pixel:ArrayLike<number>,count:number):number|null=>{const id=pixel[0]+pixel[1]*256+pixel[2]*65536-1;return Number.isInteger(id)&&id>=0&&id<count?id:null;};
const VERTEX=`#version 300 es
layout(location=0) in vec3 position;layout(location=1) in vec3 color;layout(location=2) in float pointId;
uniform mat4 matrix;uniform float size;uniform float selected;out vec3 vColor;flat out uint vId;flat out float vSelected;
void main(){gl_Position=matrix*vec4(position,1.);vId=uint(pointId);vSelected=pointId==selected?1.:0.;gl_PointSize=size+(vSelected>.5?4.:0.);vColor=color;}`;
const FRAGMENT=`#version 300 es
precision highp float;precision highp int;in vec3 vColor;flat in uint vId;flat in float vSelected;
uniform bool circles;layout(location=0) out vec4 color;layout(location=1) out vec4 pickId;
void main(){float radius=length(gl_PointCoord-.5);if(circles&&radius>.5)discard;color=vec4(vSelected>.5&&(!circles||radius>.28)?vec3(1.,.83,.28):vColor,1.);pickId=vec4(float(vId&255u),float((vId>>8u)&255u),float((vId>>16u)&255u),255.)/255.;}`;
const QUAD_VERTEX=`#version 300 es
out vec2 uv;void main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);uv=p;gl_Position=vec4(p*2.-1.,0.,1.);}`;
const QUAD_FRAGMENT=`#version 300 es
precision highp float;in vec2 uv;uniform sampler2D cloud;uniform float opacity;out vec4 color;void main(){color=texture(cloud,uv)*opacity;}`;
export type NativePointLayer=CustomLayerInterface&{update(options:NativeLayerOptions):void;pick(point:{x:number;y:number}):number|null;invalidate():void;readonly eligible:number;readonly failed:boolean};
/** Native point cloud has its own depth buffer. Its color and ID attachments are
 * produced by the SAME rasterization, then composed above map context. Terrain
 * is intentionally not an occluder: registration is unverified, not corrected. */
export type LidarGeometry={id:string;eligibleCount:number;sourceCount:number;triangles?:boolean;vertexLimit?:number;origin:(scale:number)=>[number,number,number];pack:(options:NativeLayerOptions)=>Float32Array;isEligible:(index:number)=>boolean};
export function createNativePointLayer(dataset:NativeDataset,initial:NativeLayerOptions,report:(message:string)=>void):NativePointLayer{
  const eligible=dataset.points.reduce((n,p)=>n+Number(nativePointEligible(p)),0);
  return createLidarGeometryLayer({id:NATIVE_LIDAR_LAYER,eligibleCount:eligible,sourceCount:dataset.points.length,origin:scale=>nativePointPosition(dataset.points[0],scale).mercator,isEligible:index=>nativePointEligible(dataset.points[index]),pack:options=>{
    const origin=nativePointPosition(dataset.points[0],options.scale).mercator,packed=new Float32Array(eligible*7),domain=nativeAttributeDomain(dataset,options.color)??[0,0];let count=0;
    dataset.points.forEach((p,id)=>{if(!nativePointEligible(p))return;const pos=nativePointPosition(p,options.scale).mercator,color=nativePointColor(p,options.color,domain),offset=count++*7;packed.set([pos[0]-origin[0],pos[1]-origin[1],pos[2]-origin[2],...color,id+1],offset);});return packed;
  }},initial,report);
}
export function createLidarGeometryLayer(geometry:LidarGeometry,initial:NativeLayerOptions,report:(message:string)=>void):NativePointLayer{
  let map:MapLibreMap|null=null,gl:WebGL2RenderingContext|null=null;
  let program:WebGLProgram|null=null,quad:WebGLProgram|null=null;
  let vao:WebGLVertexArrayObject|null=null,quadVao:WebGLVertexArrayObject|null=null,buffer:WebGLBuffer|null=null;
  let fbo:WebGLFramebuffer|null=null,depth:WebGLRenderbuffer|null=null,textures:WebGLTexture[]=[];
  let bounds:NativeGeometryBounds|null=null;
  let width=0,height=0,ready=false,failed=false,dirty=true,options={...initial},count=0;
  const eligible=geometry.eligibleCount,origin=geometry.origin(initial.scale);
  let uniforms:{matrix:WebGLUniformLocation|null;size:WebGLUniformLocation|null;selected:WebGLUniformLocation|null;circles:WebGLUniformLocation|null}|null=null;
  let compositeUniforms:{cloud:WebGLUniformLocation|null;opacity:WebGLUniformLocation|null}|null=null,maxPointSize=1;

  // A map repaint does not necessarily change this layer. Keep its color and
  // exact ID attachments together until camera, geometry or appearance changes.
  // Composition still runs every map frame; only the expensive raster is reused.
  let frameValid=false,frameMatrix:Float64Array|null=null,frameCssWidth=0,frameCssHeight=0;
  const invalidateFrame=()=>{ready=false;frameValid=false;};
  const sameMatrix=(matrix:ArrayLike<number>)=>frameMatrix!==null&&matrix.length===16&&frameMatrix.every((v,i)=>v===matrix[i]);
  const fail=()=>{
    if(failed)return;
    failed=true;invalidateFrame();
    report(geometry.triangles?'Terrain cell rendering is unavailable. Continuous elevation context and source data remain available; refresh this view.':'Native point rendering is unavailable. Continuous terrain and the source data remain available; retry the point view.');
  };
  const compile=(kind:number,source:string)=>{
    const shader=gl!.createShader(kind);if(!shader)throw Error('Shader allocation');
    gl!.shaderSource(shader,source);gl!.compileShader(shader);
    if(!gl!.getShaderParameter(shader,gl!.COMPILE_STATUS)){gl!.deleteShader(shader);throw Error('Point shader');}
    return shader;
  };
  const link=(vertex:string,fragment:string)=>{
    const v=compile(gl!.VERTEX_SHADER,vertex);let f:WebGLShader|null=null,p:WebGLProgram|null=null;
    try{
      f=compile(gl!.FRAGMENT_SHADER,fragment);p=gl!.createProgram();if(!p)throw Error('Program allocation');
      gl!.attachShader(p,v);gl!.attachShader(p,f);gl!.linkProgram(p);
      if(!gl!.getProgramParameter(p,gl!.LINK_STATUS))throw Error('Point program');
      return p;
    }catch(error){if(p)gl!.deleteProgram(p);throw error;}
    finally{gl!.deleteShader(v);if(f)gl!.deleteShader(f);}
  };
  const disposeFrame=()=>{
    invalidateFrame();frameMatrix=null;
    if(!gl)return;
    for(const texture of textures)gl.deleteTexture(texture);
    textures=[];
    if(depth)gl.deleteRenderbuffer(depth);if(fbo)gl.deleteFramebuffer(fbo);
    depth=null;fbo=null;width=0;height=0;
  };
  const allocate=(w:number,h:number)=>{
    if(w===width&&h===height&&fbo)return;
    disposeFrame();width=w;height=h;
    fbo=gl!.createFramebuffer();depth=gl!.createRenderbuffer();if(!fbo||!depth)throw Error('Framebuffer allocation');
    gl!.bindFramebuffer(gl!.FRAMEBUFFER,fbo);
    for(let index=0;index<2;index++){
      const texture=gl!.createTexture();if(!texture)throw Error('Texture allocation');textures.push(texture);
      gl!.bindTexture(gl!.TEXTURE_2D,texture);
      gl!.texParameteri(gl!.TEXTURE_2D,gl!.TEXTURE_MIN_FILTER,gl!.NEAREST);
      gl!.texParameteri(gl!.TEXTURE_2D,gl!.TEXTURE_MAG_FILTER,gl!.NEAREST);
      gl!.texParameteri(gl!.TEXTURE_2D,gl!.TEXTURE_WRAP_S,gl!.CLAMP_TO_EDGE);
      gl!.texParameteri(gl!.TEXTURE_2D,gl!.TEXTURE_WRAP_T,gl!.CLAMP_TO_EDGE);
      gl!.texImage2D(gl!.TEXTURE_2D,0,gl!.RGBA8,w,h,0,gl!.RGBA,gl!.UNSIGNED_BYTE,null);
      gl!.framebufferTexture2D(gl!.FRAMEBUFFER,gl!.COLOR_ATTACHMENT0+index,gl!.TEXTURE_2D,texture,0);
    }
    gl!.bindRenderbuffer(gl!.RENDERBUFFER,depth);gl!.renderbufferStorage(gl!.RENDERBUFFER,gl!.DEPTH_COMPONENT24,w,h);
    gl!.framebufferRenderbuffer(gl!.FRAMEBUFFER,gl!.DEPTH_ATTACHMENT,gl!.RENDERBUFFER,depth);
    gl!.drawBuffers([gl!.COLOR_ATTACHMENT0,gl!.COLOR_ATTACHMENT1]);
    if(gl!.checkFramebufferStatus(gl!.FRAMEBUFFER)!==gl!.FRAMEBUFFER_COMPLETE)throw Error('Incomplete point frame');
  };
  const upload=()=>{
    origin.splice(0,3,...geometry.origin(options.scale));
    const packed=geometry.pack(options),limit=geometry.triangles?geometry.vertexLimit??100_000:100_000;
    if(!Number.isSafeInteger(limit)||limit<1||limit>300_000||packed.length%7!==0||packed.length>limit*7)throw Error('Geometry budget');
    const low=[Infinity,Infinity,Infinity],high=[-Infinity,-Infinity,-Infinity];
    for(let i=0;i<packed.length;i+=7)for(let axis=0;axis<3;axis++){low[axis]=Math.min(low[axis],packed[i+axis]);high[axis]=Math.max(high[axis],packed[i+axis]);}
    bounds=packed.length?[low,high]:null;
    count=packed.length/7;gl!.bindBuffer(gl!.ARRAY_BUFFER,buffer);gl!.bufferData(gl!.ARRAY_BUFFER,packed,gl!.STATIC_DRAW);
    dirty=false;invalidateFrame();
  };
  const layer:NativePointLayer={
    id:geometry.id,type:'custom',renderingMode:'3d',
    get eligible(){return eligible;},get failed(){return failed;},
    update(next){
      if(next.framePixelLimit!==undefined&&(!Number.isSafeInteger(next.framePixelLimit)||next.framePixelLimit<65_536||next.framePixelLimit>NATIVE_FRAME_PIXEL_LIMIT))throw Error('Invalid terrain drawing budget');
      if(!Number.isFinite(next.scale)||next.scale<.1||next.scale>5||!Number.isFinite(next.size)||next.size<1||next.size>6||!['elevation','classification','intensity'].includes(next.color)||(next.gridColor!==undefined&&!['height','slope','local-relief'].includes(next.gridColor))||(next.opacity!==undefined&&(!Number.isFinite(next.opacity)||next.opacity<0||next.opacity>1)))throw Error('Invalid point display settings');
      const changedGeometry=next.scale!==options.scale||(geometry.triangles===true?(next.gridColor??'height')!==(options.gridColor??'height'):next.color!==options.color);
      if(changedGeometry||next.selected!==options.selected||(!geometry.triangles&&next.size!==options.size)||next.framePixelLimit!==options.framePixelLimit)invalidateFrame();
      dirty||=changedGeometry;options={...next};
      // Opacity belongs only to composition. A cached ID frame is still exact;
      // hidden layers cannot pick, and showing them needs no redundant raster.
      if(options.opacity===0)ready=false;
      map?.triggerRepaint();
    },
    invalidate:invalidateFrame,
    onAdd(nextMap,context){
      map=nextMap;gl=context;
      const priorVao=gl.getParameter(gl.VERTEX_ARRAY_BINDING),priorBuffer=gl.getParameter(gl.ARRAY_BUFFER_BINDING);
      try{
        if(typeof gl.drawBuffers!=='function')throw Error('WebGL2 required');
        program=link(VERTEX,FRAGMENT);quad=link(QUAD_VERTEX,QUAD_FRAGMENT);
        uniforms={matrix:gl.getUniformLocation(program,'matrix'),size:gl.getUniformLocation(program,'size'),selected:gl.getUniformLocation(program,'selected'),circles:gl.getUniformLocation(program,'circles')};
        compositeUniforms={cloud:gl.getUniformLocation(quad,'cloud'),opacity:gl.getUniformLocation(quad,'opacity')};
        maxPointSize=Number(gl.getParameter(gl.ALIASED_POINT_SIZE_RANGE)[1]);
        buffer=gl.createBuffer();vao=gl.createVertexArray();quadVao=gl.createVertexArray();
        if(!buffer||!vao||!quadVao)throw Error('Point buffers');
        gl.bindVertexArray(vao);gl.bindBuffer(gl.ARRAY_BUFFER,buffer);
        for(let a=0;a<3;a++){gl.enableVertexAttribArray(a);gl.vertexAttribPointer(a,a===2?1:3,gl.FLOAT,false,28,a===0?0:a===1?12:24);}
        dirty=true;invalidateFrame();
      }catch{fail();}
      finally{gl.bindVertexArray(priorVao);gl.bindBuffer(gl.ARRAY_BUFFER,priorBuffer);}
    },
    render(context,input:CustomRenderMethodInput){
      if(failed||!map||!gl||!program||!quad||!vao||!buffer||!uniforms||!compositeUniforms)return;
      if(map.getProjection()?.type!=='mercator'){invalidateFrame();return;}
      if(options.opacity===0){ready=false;return;}
      // MapLibre 6.9 marks its tracked GL state dirty after every custom layer
      // and restores it before the next draw (webgl/draw/draw_custom.ts).
      // Reading that state back here serializes the browser/GPU on every pan.
      // Preserve only the actual render targets/viewport, plus untracked flags.
      const prior={draw:gl.getParameter(gl.DRAW_FRAMEBUFFER_BINDING),read:gl.getParameter(gl.READ_FRAMEBUFFER_BINDING),viewport:gl.getParameter(gl.VIEWPORT),scissor:gl.isEnabled(gl.SCISSOR_TEST),dither:gl.isEnabled(gl.DITHER)};
      try{
        if(gl.isContextLost())throw Error('Context lost');
        gl.activeTexture(gl.TEXTURE0);
        const ratio=Math.min(1,Math.sqrt((options.framePixelLimit??NATIVE_FRAME_PIXEL_LIMIT)/(gl.drawingBufferWidth*gl.drawingBufferHeight)));
        const w=Math.max(1,Math.floor(gl.drawingBufferWidth*ratio)),h=Math.max(1,Math.floor(gl.drawingBufferHeight*ratio));
        allocate(w,h);if(dirty)upload();
        const canvas=map.getCanvas(),cssWidth=canvas.clientWidth||1,cssHeight=canvas.clientHeight||1,matrix=input.defaultProjectionData.mainMatrix;
        if(!frameValid||!sameMatrix(matrix)||frameCssWidth!==cssWidth||frameCssHeight!==cssHeight){
          gl.bindFramebuffer(gl.FRAMEBUFFER,fbo);gl.viewport(0,0,w,h);
          gl.disable(gl.SCISSOR_TEST);gl.disable(gl.STENCIL_TEST);gl.disable(gl.BLEND);gl.disable(gl.DITHER);gl.disable(gl.CULL_FACE);
          gl.enable(gl.DEPTH_TEST);gl.depthRange(0,1);gl.depthFunc(gl.LESS);gl.depthMask(true);gl.colorMask(true,true,true,true);
          gl.clearColor(0,0,0,0);gl.clearDepth(1);gl.clear(gl.COLOR_BUFFER_BIT|gl.DEPTH_BUFFER_BIT);
          gl.useProgram(program);gl.bindVertexArray(vao);
          gl.uniformMatrix4fv(uniforms.matrix,false,nativeTranslatedMatrix(matrix,origin,bounds));
          gl.uniform1f(uniforms.size,Math.min(maxPointSize,options.size*w/cssWidth));
          gl.uniform1f(uniforms.selected,options.selected===null?-1:options.selected+1);
          gl.uniform1i(uniforms.circles,geometry.triangles?0:1);
          gl.drawArrays(geometry.triangles?gl.TRIANGLES:gl.POINTS,0,count);
          // Copy the matrix. MapLibre can mutate and reuse its own array.
          frameMatrix=Float64Array.from(matrix);frameCssWidth=cssWidth;frameCssHeight=cssHeight;frameValid=true;
        }
        // Composite into the actual map target every time. Context layers may
        // have changed beneath this independent, registration-unverified depth.
        gl.bindFramebuffer(gl.DRAW_FRAMEBUFFER,prior.draw);gl.viewport(...Array.from(prior.viewport) as [number,number,number,number]);
        gl.disable(gl.SCISSOR_TEST);gl.disable(gl.STENCIL_TEST);gl.disable(gl.CULL_FACE);gl.disable(gl.DITHER);gl.colorMask(true,true,true,true);
        gl.disable(gl.DEPTH_TEST);gl.depthMask(false);gl.enable(gl.BLEND);gl.blendEquationSeparate(gl.FUNC_ADD,gl.FUNC_ADD);
        gl.blendFuncSeparate(gl.ONE,gl.ONE_MINUS_SRC_ALPHA,gl.ONE,gl.ONE_MINUS_SRC_ALPHA);
        gl.useProgram(quad);gl.bindVertexArray(quadVao);gl.bindTexture(gl.TEXTURE_2D,textures[0]);
        gl.uniform1i(compositeUniforms.cloud,0);gl.uniform1f(compositeUniforms.opacity,options.opacity??1);gl.drawArrays(gl.TRIANGLES,0,3);ready=true;
      }catch{fail();}
      finally{
        gl.bindFramebuffer(gl.DRAW_FRAMEBUFFER,prior.draw);gl.bindFramebuffer(gl.READ_FRAMEBUFFER,prior.read);
        gl.viewport(...Array.from(prior.viewport) as [number,number,number,number]);
        gl.bindVertexArray(null);
        if(prior.scissor)gl.enable(gl.SCISSOR_TEST);else gl.disable(gl.SCISSOR_TEST);
        if(prior.dither)gl.enable(gl.DITHER);else gl.disable(gl.DITHER);
      }
    },
    pick(point){
      if(!ready||failed||!gl||!map||!fbo)return null;
      const pixel=nativePickPixel(point,map.getCanvas().clientWidth,map.getCanvas().clientHeight,width,height);if(!pixel)return null;
      const previous=gl.getParameter(gl.READ_FRAMEBUFFER_BINDING);
      try{
        gl.bindFramebuffer(gl.READ_FRAMEBUFFER,fbo);gl.readBuffer(gl.COLOR_ATTACHMENT1);
        const color=new Uint8Array(4);gl.readPixels(pixel[0],pixel[1],1,1,gl.RGBA,gl.UNSIGNED_BYTE,color);
        const id=nativeDecodePick(color,geometry.sourceCount);return id!==null&&geometry.isEligible(id)?id:null;
      }catch{fail();return null;}
      finally{gl.bindFramebuffer(gl.READ_FRAMEBUFFER,previous);}
    },
    onRemove(){
      invalidateFrame();
      if(gl){disposeFrame();if(program)gl.deleteProgram(program);if(quad)gl.deleteProgram(quad);if(vao)gl.deleteVertexArray(vao);if(quadVao)gl.deleteVertexArray(quadVao);if(buffer)gl.deleteBuffer(buffer);}
      program=null;quad=null;uniforms=null;compositeUniforms=null;vao=null;quadVao=null;buffer=null;gl=null;map=null;
    }
  };
  return layer;
}

const nativePickers=new WeakMap<MapLibreMap,(point:{x:number;y:number})=>boolean>();
export function registerNativeLidarPicker(map:MapLibreMap,pick:((point:{x:number;y:number})=>boolean)|null){if(pick)nativePickers.set(map,pick);else nativePickers.delete(map);}
export const pickNativeLidarPoint=(map:MapLibreMap,point:{x:number;y:number})=>nativePickers.get(map)?.(point)??false;
