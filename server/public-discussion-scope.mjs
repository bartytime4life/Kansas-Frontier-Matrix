// Recognize a few unequivocal standalone definitions so an unrelated selected
// record can be omitted. This list does not limit the topics allowed in chat.
// It is not a permission phrase that overrides a request for protected data.
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

// Admission aid for explicit protected-data requests, not the host-security
// boundary. General conversation has no topic allowlist. Server-owned source
// readers, no-tools inference, signed transport, output checks and resource
// admission enforce the actual boundaries independently of these expressions.
export function blockedDiscussionRequest(input){
 if(typeof input!=='string')return true;
 const value=input.normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}/_. -]+/gu,' ').replace(/\s+/g,' ').trim();
 const disclosure=/\b(?:give|show|read|reveal|print|dump|fetch|download|expose|extract|access|list|find|get|want|need|locat\w*)\b/;
 const protectedData=/\b(?:private|withheld|restricted|unreleased|confidential|secret)\b.{0,80}\b(?:records?|data|files?|locations?|coordinates?|keys?|tokens?|passwords?|credentials?)\b/;
 const personalData=/\b(?:living person|someone|person|people|owner|user|visitor)\b.{0,60}\b(?:records?|results?|address|dna|genome|password|credentials?)\b|\b(?:their|his|her|someone s) (?:private |medical |genetic )?(?:records?|results?|address|dna|genome)\b/;
 const protectedPlaces=/\b(?:archaeolog\w*|burial|rare species|nests?|critical infrastructure|substations?)\b/;
 const locating=/\b(?:locat\w*|where|near|names?|list|identify|show|plot|map|gps|coordinates?|latitude|longitude|exact)\b/;
 const hostAccess=/\b(?:read|reveal|print|dump|fetch|download|expose|show|give|extract)\b.{0,100}(?:\/(?:etc|proc|root|home|private)\/|\b(?:environment variables|api keys?|access tokens?|passwords?|credentials?|server files?|host files?)\b)|\b(?:run|execute|install|delete|modify|change|disable)\b.{0,70}\b(?:shell|commands?|code|scripts?|software|files?|configuration|firewall|security controls?)\b.{0,60}\b(?:server|host|hosting|computer|pc|website)\b/;
 const hostTarget=/\b(?:your|this|the) (?:website|server|host|hosting|computer|pc)\b|\bhosting computer\b|\bhost (?:files?|environment)\b|^(?:please )?(?:read|dump|reveal) \/(?:etc|proc|root|home|private)\//;
 const personalSafety=/\b(?:is it|is this|is that|are they)\b.{0,40}\b(?:safe|dangerous|drinkable|potable)\b|\b(?:evacuate|rescue me|diagnose me|legal advice for me)\b/;
 return (disclosure.test(value)&&(protectedData.test(value)||personalData.test(value)))||(protectedPlaces.test(value)&&locating.test(value))||(hostTarget.test(value)&&hostAccess.test(value))||personalSafety.test(value);
}
