// Shared discussion budgets and output checks used by home inference.
// The former embedded GoDaddy model loader is retired; this module performs no inference.
export const PUBLIC_AI_JOB_MS=270000;
export const PUBLIC_AI_MAX_LIFETIME_MS=3*PUBLIC_AI_JOB_MS;
export {CONTINUE_REPLY} from './hosted-ai-prompt.mjs';

export function hasRepeatedPhrase(value){
 const words=value.toLowerCase().match(/[a-z0-9]+/g)??[],counts=new Map();
 for(let i=0;i+3<words.length;i++){const phrase=words.slice(i,i+4).join(' '),n=(counts.get(phrase)??0)+1;if(n>=3)return true;counts.set(phrase,n);}
 return false;
}

// A continuation that mostly copies its preceding reply is not new progress.
// Compare phrases, not shared subject words; short answers are excluded.
export function repeatsPriorReply(value,prior){
 const words=text=>(text??'').toLowerCase().match(/[\p{L}\p{N}]+/gu)??[];
 const current=words(value),previous=words(prior);
 if(current.length<24||previous.length<24)return false;
 // A complete leading replay is still repetition when appended text dilutes
 // the phrase-overlap percentage. Partial shared introductions remain allowed.
 if(previous.every((word,index)=>current[index]===word))return true;
 const phrases=new Set();for(let i=0;i+3<previous.length;i++)phrases.add(previous.slice(i,i+4).join(' '));
 let matches=0;for(let i=0;i+3<current.length;i++)if(phrases.has(current.slice(i,i+4).join(' ')))matches++;
 return matches/(current.length-3)>=0.75;
}

