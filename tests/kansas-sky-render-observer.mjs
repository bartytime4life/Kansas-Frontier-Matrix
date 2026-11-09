// Test-only GPU observation. Serialize this function into the real built
// MapLibre fixture; production does not import it.
export function installSkyRenderObserver(MapClass) {
  const add = MapClass.prototype.addLayer;
  MapClass.prototype.addLayer = function (layer, ...rest) {
    if (layer.id === 'kfm-kansas-sky') {
      window.__skyMap = this;
      const stats = window.__skyRender = {frames:0,aircraftVertices:0,trailVertices:0,lineTrailVertices:0,pathTriangles:0,maxZ:0};
      const uploaded = new Map();
      const render = layer.render;
      layer.render = function (gl, ...args) {
        const draw = gl.drawArrays, upload = gl.bufferSubData;
        stats.aircraftVertices=0;stats.trailVertices=0;stats.lineTrailVertices=0;stats.pathTriangles=0;stats.maxZ=0;
        gl.drawArrays = function (mode, start, count) {
          const program = gl.getParameter(gl.CURRENT_PROGRAM);
          const stroke = gl.getAttribLocation(program, 'a_edge') >= 0;
          if (mode === gl.TRIANGLES && !stroke) {
            stats.aircraftVertices += count;
            const location=gl.getAttribLocation(program,'a_position');
            if(location>=0){
              const stride=gl.getVertexAttrib(location,gl.VERTEX_ATTRIB_ARRAY_STRIDE);
              const data=uploaded.get(gl.getVertexAttrib(location,gl.VERTEX_ATTRIB_ARRAY_BUFFER_BINDING));
              if(stride===24&&data)for(let i=start*6+2;i<Math.min(data.length,(start+count)*6);i+=6)stats.maxZ=Math.max(stats.maxZ,Math.abs(data[i]));
            }
          }
          if (mode === gl.LINES) {stats.lineTrailVertices+=count;stats.trailVertices+=count;}
          // The actual stroked route is drawn from vertex zero; later ranges
          // are terrain guides. Both halo and core are real GPU route draws.
          if (mode === gl.TRIANGLES && stroke && start === 0) {stats.pathTriangles+=count;stats.trailVertices+=count;}
          return draw.call(this,mode,start,count);
        };
        gl.bufferSubData = function (target, offset, data, ...more) {
          if(data instanceof Float32Array&&offset===0)uploaded.set(gl.getParameter(gl.ARRAY_BUFFER_BINDING),new Float32Array(data));
          return upload.call(this,target,offset,data,...more);
        };
        try {const result=render.call(this,gl,...args);stats.frames++;return result;}
        finally {gl.drawArrays=draw;gl.bufferSubData=upload;}
      };
    }
    return add.call(this,layer,...rest);
  };
}
