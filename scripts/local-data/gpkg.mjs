// GeoPackage geometry blobs (GP header + WKB) to GeoJSON, without dependencies. Handles the 2D
// types the PC's GeoPackages hold: Point, LineString, Polygon and their Multi forms.
// Coordinates are rounded to 6 decimals (about 0.1 m). Throws GEOMETRY_INVALID on anything else.
const fail=()=>Object.assign(new Error('GEOMETRY_INVALID'),{code:'GEOMETRY_INVALID'});
const ENVELOPE_BYTES=[0,32,48,48,64];
const round=v=>Math.round(v*1e6)/1e6;

export function gpkgToGeoJSON(blob){
 if(blob===null||blob===undefined)return null;
 const buf=Buffer.isBuffer(blob)?blob:Buffer.from(blob);
 if(buf.length<8||buf[0]!==0x47||buf[1]!==0x50)throw fail();
 const flags=buf[3],envelope=(flags>>1)&7;
 if(envelope>4)throw fail();
 if(flags&0x10)return null;// empty geometry
 let offset=8+ENVELOPE_BYTES[envelope];
 const read=()=>{
  if(offset+5>buf.length)throw fail();
  const little=buf[offset]===1;offset+=1;
  const u32=()=>{if(offset+4>buf.length)throw fail();const v=little?buf.readUInt32LE(offset):buf.readUInt32BE(offset);offset+=4;return v;};
  const f64=()=>{if(offset+8>buf.length)throw fail();const v=little?buf.readDoubleLE(offset):buf.readDoubleBE(offset);offset+=8;return v;};
  const type=u32();
  // ISO (1000s) and EWKB-style Z/M flags are not expected here; refuse rather than misread.
  if(type>7)throw fail();
  const point=()=>[round(f64()),round(f64())];
  const points=()=>{const n=u32();if(n>5_000_000)throw fail();const out=new Array(n);for(let i=0;i<n;i++)out[i]=point();return out;};
  const rings=()=>{const n=u32();if(n>100000)throw fail();const out=new Array(n);for(let i=0;i<n;i++)out[i]=points();return out;};
  const parts=expected=>{const n=u32();if(n>100000)throw fail();const out=[];for(let i=0;i<n;i++){const g=read();if(g.type!==expected)throw fail();out.push(g.coordinates);}return out;};
  switch(type){
   case 1:return {type:'Point',coordinates:point()};
   case 2:return {type:'LineString',coordinates:points()};
   case 3:return {type:'Polygon',coordinates:rings()};
   case 4:return {type:'MultiPoint',coordinates:parts('Point')};
   case 5:return {type:'MultiLineString',coordinates:parts('LineString')};
   case 6:return {type:'MultiPolygon',coordinates:parts('Polygon')};
   default:throw fail();
  }
 };
 return read();
}
