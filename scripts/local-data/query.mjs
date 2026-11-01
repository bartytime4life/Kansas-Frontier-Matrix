// Shared, dependency-free validation for local-data questions. The website and the PC gateway both
// normalize every question with these, so only the fixed shapes below ever become SQL parameters.
export const fail=()=>Object.assign(new Error('QUERY_INVALID'),{code:'QUERY_INVALID'});
const empty=v=>v===undefined||v===null||v==='';

/** Throws unless input is a plain object whose keys are all in allowed. */
export function only(input,allowed){
 if(!input||typeof input!=='object'||Array.isArray(input))throw fail();
 const keys=new Set(allowed);
 if(Object.keys(input).some(k=>!keys.has(k)))throw fail();
 return input;
}

export function text(v,pattern,{upper=true,required=false}={}){
 if(empty(v)){if(required)throw fail();return null;}
 let s=String(v).trim();if(upper)s=s.toUpperCase();
 if(!pattern.test(s))throw fail();
 return s;
}

export function int(v,{min,max,fallback=null,required=false}){
 if(empty(v)){if(required)throw fail();return fallback;}
 const s=String(v);if(!/^-?\d{1,9}$/.test(s))throw fail();
 const n=+s;if(n<min||n>max)throw fail();
 return n;
}

export function oneOf(v,values,{fallback=null,required=false}={}){
 if(empty(v)){if(required)throw fail();return fallback;}
 const s=String(v).trim();
 const hit=values.find(x=>x.toLowerCase()===s.toLowerCase());
 if(hit===undefined)throw fail();
 return hit;
}

/** YYYY-MM-DD between 1700 and 2100. */
export function day(v,fallback,{required=false}={}){
 if(empty(v)){if(required)throw fail();return fallback;}
 const m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(String(v).trim());if(!m)throw fail();
 const [y,mo,d]=[+m[1],+m[2],+m[3]];
 if(y<1700||y>2100||mo<1||mo>12||d<1||d>31)throw fail();
 return m[0];
}

/** YYYY-MM-DDTHH:MM (or a space instead of T); a bare date becomes 00:00 or, as an end, 23:59. */
export function minute(v,fallback,{end=false}={}){
 if(empty(v))return fallback;
 const s=String(v).trim();
 if(/^\d{4}-\d{2}-\d{2}$/.test(s))return day(s)+(end?'T23:59':'T00:00');
 const m=/^(\d{4}-\d{2}-\d{2})[T ](\d{2}):(\d{2})$/.exec(s);if(!m)throw fail();
 if(+m[2]>23||+m[3]>59)throw fail();
 return day(m[1])+'T'+m[2]+':'+m[3];
}

export function ordered(from,to){if(from>to)throw fail();}

/** west,south,east,north in degrees, at most 2 degrees on a side. */
export function bbox(v){
 if(empty(v))return null;
 const parts=String(v).split(',');if(parts.length!==4)throw fail();
 const n=parts.map(p=>{if(!/^-?\d{1,3}(?:\.\d{1,7})?$/.test(p.trim()))throw fail();return +p;});
 const [w,s,e,no]=n;
 if(w<-180||e>180||s<-90||no>90||w>=e||s>=no||e-w>2||no-s>2)throw fail();
 return {west:w,south:s,east:e,north:no};
}

/** Comma-separated list of values matching pattern, at most max. */
export function list(v,pattern,max){
 if(empty(v))return null;
 const items=[...new Set(String(v).split(',').map(x=>x.trim().toUpperCase()).filter(Boolean))];
 if(!items.length||items.length>max||items.some(x=>!pattern.test(x)))throw fail();
 return items.sort();
}

export function flag(v){
 if(empty(v))return false;
 const s=String(v).trim().toLowerCase();
 if(s==='1'||s==='true')return true;
 if(s==='0'||s==='false')return false;
 throw fail();
}

export const page=(input,{max,fallback,maxOffset=100000})=>({
 limit:int(input.limit,{min:1,max,fallback}),
 offset:int(input.offset,{min:0,max:maxOffset,fallback:0}),
});

// Row helpers for the gateway side.
export const num=v=>v===null||v===undefined||v===''||!Number.isFinite(+v)?null:+v;
export const str=v=>v===null||v===undefined||v===''?null:String(v);
/** IEM and similar text exports: 'M', 'None', 'NaN' and blanks mean missing, not zero. */
const MISSING=/^(?:|M|None|NaN|nan|null)$/;
export const reading=v=>v===null||v===undefined||MISSING.test(String(v).trim())?null:num(v);
/** The same missing markers for text values such as times. */
export const note=v=>v===null||v===undefined||MISSING.test(String(v).trim())?null:String(v).trim();
