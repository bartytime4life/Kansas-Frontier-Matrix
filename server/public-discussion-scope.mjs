// Topic names alone do not make a general definition a sensitive-site request.
// This is a closed vocabulary and whole-question grammar, not a permission
// phrase such as "educational" that can override a request for real records.
const concepts = new Map([
 ['archaeological site','an archaeological site'],
 ['archaeological sites','archaeological sites'],
 ['archaeology','archaeology'],
 ['rare species','rare species'],
 ['critical infrastructure','critical infrastructure'],
 ['dna','DNA'],
 ['gps','GPS'],
 ['coordinates','geographic coordinates'],
 ['geographic coordinates','geographic coordinates'],
 ['latitude','latitude'],
 ['longitude','longitude'],
]);
const suffixes = new Set([
 '', 'in general', 'in general terms', 'in simple terms', 'for beginners',
 'explain the general concept only, without identifying or locating any real sites',
]);

export function generalDiscussionQuestion(input){
 if(typeof input!=='string'||input.length>240)return null;
 const value=input.normalize('NFKC').toLowerCase().trim().replace(/\s+/g,' ');
 const match=/^(?:please )?(?:what (?:is|are)|what['’]s|define|explain) (?:(?:a|an|the) )?(.+)$/.exec(value);
 if(!match)return null;
 for(const [name,topic] of concepts){
  if(!match[1].startsWith(name))continue;
  const rest=match[1].slice(name.length);
  // Require a word boundary; names, places, actions, extra instructions and
  // appended questions are not part of this exception.
  if(rest&&!/^[\s.!?]/.test(rest))continue;
  const suffix=rest.replace(/^[\s.!?]+|[\s.!?]+$/g,'');
  if(!suffixes.has(suffix))continue;
  return `Explain the general concept of ${topic}. Use hypothetical examples only. Do not identify real people, sites, species locations or infrastructure assets. Do not give precise locations, operational instructions or personalized safety, medical or legal advice. This is general education, not a claim about the current map or released KFM evidence.`;
 }
 return null;
}
