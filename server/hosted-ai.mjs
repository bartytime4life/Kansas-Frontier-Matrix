// Shared discussion budgets and output checks used by home inference.
// The former embedded GoDaddy model loader is retired; this module performs no inference.
import {INFERENCE_BUDGETS} from '../scripts/home-inference/budgets.mjs';
export const PUBLIC_AI_JOB_MS=INFERENCE_BUDGETS.jobMs;
export const PUBLIC_AI_MAX_LIFETIME_MS=INFERENCE_BUDGETS.publicSlots*PUBLIC_AI_JOB_MS;
export {CONTINUE_REPLY} from './hosted-ai-prompt.mjs';

// A degenerate loop repeats the same wording. A proper name ("the Santa Fe
// Trail") or the subject the visitor asked about naturally recurs in a correct
// answer, so those phrases need more repeats before the reply counts as a loop.
const NAME_GLUE=new Set(['the','of','and','de','la','del','du','des','le','los','las']);
const fourWordPhrases=tokens=>{const out=[];for(let i=0;i+3<tokens.length;i++)out.push(tokens.slice(i,i+4));return out;};
export function hasRepeatedPhrase(value,question=''){
 const tokens=value.match(/[A-Za-z0-9]+/g)??[],counts=new Map();
 const asked=new Set(fourWordPhrases((typeof question==='string'?question:'').toLowerCase().match(/[a-z0-9]+/g)??[]).map(words=>words.join(' ')));
 for(const words of fourWordPhrases(tokens)){
  const phrase=words.join(' ').toLowerCase();
  const named=words.every(word=>NAME_GLUE.has(word.toLowerCase())||/^[A-Z0-9]/.test(word))&&words.filter(word=>/^[A-Z]/.test(word)).length>=2;
  const n=(counts.get(phrase)??0)+1;
  if(n>=(named||asked.has(phrase)?5:3))return true;
  counts.set(phrase,n);
 }
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

