/** Public administrative data is not sensitive merely because it concerns a
 * contract or payment. This narrow WIHA projection is not a universal public-
 * data admission gate, identity resolver or complete personal-data detector. */
// A probable personal identity beside a tract still needs review. A given name
// that is also an ordinary word, or ownership/payment wording alone, is not enough.
const GIVEN_NAMES = new Set((
  "Aaron Adam Alan Albert Alex Alice Allen Amanda Amy Andrew Andy Angela Ann Anna Anne Anthony Arthur Barbara "+
  "Barry Ben Benjamin Betty Beverly Bill Billy Bob Bobby Bonnie Brad Bradley Brandon Brenda Brent Brian Bruce "+
  "Bryan Carl Carol Carolyn Catherine Charles Charlie Cheryl Chris Christine Christopher Chuck Cindy Clarence "+
  "Clark Clint Cody Conrad Craig Curtis Cynthia Dale Dan Daniel Danny Darrell David Dean Deb Debbie Deborah Debra "+
  "Dennis Derek Diana Diane Don Donald Donna Doris Dorothy Doug Douglas Duane Dustin Dwight Earl Ed Eddie Edward "+
  "Elaine Elizabeth Ellen Emily Eric Ernest Eugene Evelyn Floyd Frances Frank Fred Gail Gary Gene George Gerald "+
  "Glen Glenn Gloria Gordon Greg Gregory Harold Harry Heather Helen Henry Herb Howard Jack Jacob James Jane Janet "+
  "Janice Jason Jay Jean Jeff Jeffrey Jennifer Jerry Jessica Jim Jimmy Joan Joe Joel John Johnny Jon Jonathan "+
  "Joseph Joshua Joyce Juanita Judith Judy Julie Justin Karen Kathleen Kathy Keith Kelly Ken Kenneth Kent Kevin "+
  "Kim Kirk Kristi Kurt Kyle Larry Laura Lawrence Lee Leon Leonard Leroy Linda Lisa Lloyd Lois Lori Louis Lyle "+
  "Lynn Marc Margaret Maria Marie Marilyn Mark Marlin Marsha Martha Martin Marvin Mary Matt Matthew Melvin "+
  "Michael Michelle Mike Mildred Nancy Nathan Neil Nicholas Norma Norman Pam Pamela Pat Patricia Patrick Paul "+
  "Paula Peggy Perry Pete Peter Phil Phillip Phyllis Ralph Randy Ray Raymond Rebecca Rex Richard Rick Rita Rob "+
  "Robert Rodney Roger Ron Ronald Rose Ross Roy Russell Ruth Ryan Sally Sam Samuel Sandra Sandy Sara Sarah Scott "+
  "Sharon Shawn Sheila Sherry Shirley Stan Stanley Stephen Steve Steven Sue Susan Ted Teresa Terry Theresa Thomas "+
  "Tim Timothy Todd Tom Tony Tracy Travis Troy Tyler Vernon Vicki Victor Virginia Walter Warren Wayne Wendy "+
  "Wesley William Willie Zach"
).split(" "));
const GIVEN_NAMES_LOWER = new Set([...GIVEN_NAMES].map(name => name.toLowerCase()));
const PLACE_WORD = /^(?:County|Creek|Lake|River|Road|Rd|Township|Twp|Street|St|Avenue|Ave|Draw|Pond|Reservoir|Ranch|Park)\b/i;
const FAMILY = /\b(?:son|daughter|wife|husband|brother|sister|mother|father|family|grand(?:son|daughter)|widow(?:er)?|nephew|niece|heirs?)\b/i;
const LEGAL_DESCRIPTION = /\b(?:sec(?:tion)?\s*:?\s*\d+|T\d+[NS]|R\d+[EW]|[NESW]\s*\/\s*[24])\b/i;
const namesPerson = (text: string) => {
  const words = text.split(/\s+/);
  for (const [index, word] of words.entries()) {
    const name = /^[^A-Za-z]*([A-Za-z]+)(?:['’]s)?[^A-Za-z]*$/.exec(word)?.[1]?.toLowerCase();
    const next = words[index + 1] ?? "";
    if (!name || !GIVEN_NAMES_LOWER.has(name)) continue;
    if (PLACE_WORD.test(next) && !/\b(?:owns?|resides?|lives?)\b/i.test(words.slice(index + 2).join(" "))) continue;
    if (name === "bill" && /^(?:paid|payment|amount|due|expires?|for|received|approved)\b/i.test(next)
      || name === "mark" && /^(?:public|access|boundaries|boundary|the|all|each|signs?|trails?|corners?|gates?|entrances?|exits?)\b/i.test(next)) continue;
    const historicalReference = /^(?:historic(?:al)? (?:interpretation|site|marker|reference)|memorial|museum|monument)\b/i.test(words.slice(index + 2, index + 5).join(" "));
    if (!historicalReference && (/['’]s\b/i.test(word) || LEGAL_DESCRIPTION.test(text)
      || /^[A-Za-z][A-Za-z'’-]+[.,;:]?$/.test(next))) return true;
  }
  return FAMILY.test(text) && /\b(?:house|home|residence|address)\b/i.test(text);
};

const screeningText = (text: string) => {
  const normalized = text.normalize("NFKC").replace(/[\u200b-\u200d\ufeff]/g, "")
    .replace(/[\u2010-\u2015\u2212]/g, "-")
    .replace(/\s*(?:\[\s*at\s*\]|\(\s*at\s*\))\s*/gi, "@")
    .replace(/\s*(?:\[\s*dot\s*\]|\(\s*dot\s*\))\s*/gi, ".");
  return /\b(?:e-?mail|contact|write|send)\b/i.test(normalized)
    ? normalized.replace(/\b([A-Z0-9._%+-]+)\s+at\s+([A-Z0-9.-]+(?:\s+dot\s+[A-Z]{2,})+)\b/gi, (_, user: string, domain: string) => `${user}@${domain.replace(/\s+dot\s+/gi, ".")}`)
    : normalized;
};
const personalPhones = (raw: string) => [...raw.matchAll(/(?<!\d)(?:\+?1[ .-]?)?(?:\(\d{3}\)[ .-]?|\d{3}[ .-]?)\d{3}[ .-]?\d{4}(?!\d)/g)]
  .filter(match => /[+(). -]/.test(match[0]) || /\b(?:phone|call|text|mobile|cell|tel(?:ephone)?|contact)\b/i.test(raw.slice(Math.max(0, match.index - 80), match.index))
    || /^\s*(?:[(-]\s*)?(?:(?:owner|personal|private)\s+)?(?:phone|mobile|cell|tel(?:ephone)?|contact)\b/i.test(raw.slice(match.index + match[0].length, match.index + match[0].length + 50)));
const STREET_ADDRESS = /\b\d{1,6}\s+(?:[A-Za-z0-9.'-]+\s+){1,5}(?:street|st|road|rd|lane|ln|avenue|ave|drive|dr|court|ct|boulevard|blvd|way)\b/i;
const hasPersonalDetail = (text: string, note = true) => {
  const raw = screeningText(text);
  const ssnPattern = /\b\d{3}-\d{2}-\d{4}\b/;
  const contact = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(raw)
    || personalPhones(raw).length > 0;
  const personalId = ssnPattern.test(raw)
    || /\b(?:SSN|social security|passport|driver'?s? licen[cs]e)\s*(?:(?:number|no\.?|#|:)\s*)?[A-Z]*\d{4,}\b/i.test(raw);
  const address = [...raw.matchAll(/\b(?:home|residential|mailing) address\s*(?::|is\b|=)/gi)]
    .some(match => !/\bno\s+$/i.test(raw.slice(0, match.index)))
    || STREET_ADDRESS.test(raw)
      && /\b(?:owner|tenant|resident|home|resides|lives)\b/i.test(raw)
    || /\b[A-Z][a-z]+\s+[A-Z][a-z]+,\s*\d+\s/.test(raw);
  const seen = [...raw.matchAll(/\b(?:last seen at|last known location)\b/gi)].some(match => {
    const subject = raw.slice(0, match.index).split(/[.!?;]/).at(-1) ?? "";
    return !/\b(?:wildlife|pheasants?|quails?|deer|turkeys?|birds?|waterfowl)(?:\s+(?:was|were))?\s*$/i.test(subject);
  });
  const scheduledPerson = /\b[A-Z][a-z]+\s+[A-Z][a-z]+\s+at\b.{0,100}\b(?:\d{1,2}:\d{2}|daily|every weekday)\b/.test(raw);
  const residence = /\b(?:family|owner|tenant|resident)\b.{0,60}\b(?:lives?|resides?)\s+(?:at|by|near|in|on)\b/i.test(raw)
    || /\b(?:owner|landowner|tenant|resident)(?:['’]s)?\s+(?:home|house|residence|address)\b/i.test(raw);
  const targeting = address || seen || scheduledPerson || residence || /\b(?:lives at|resides at|(?:personal|private) (?:phone|email)\s*:|current whereabouts\s*:|(?:live|real-time) location\b|leaves? home|commutes?\b|(?:track|follow)\s+\w+\s+\w+\s+(?:from|home)|is (?:currently|now) at\s+[-+]?\d)/i.test(raw);
  // Species vernacular can look like names (Ross's goose, Virginia rail).
  // In that typed field require additional person/tract context for name guesses.
  const person = (note || /\b(?:owner|tenant|resident|family|personal|private|owns?)\b/i.test(raw) || LEGAL_DESCRIPTION.test(raw)) && namesPerson(raw);
  return contact || personalId || targeting ? "detail" : person ? "person" : null;
};

// Same 105 canonical county names as public/data/subsurface/manifest.json.
// This is a local field validator, not a new provider lookup or dataset admission.
const COUNTIES = new Map((
  "Allen|Anderson|Atchison|Barber|Barton|Bourbon|Brown|Butler|Chase|Chautauqua|Cherokee|Cheyenne|Clark|Clay|Cloud|Coffey|Comanche|Cowley|Crawford|Decatur|Dickinson|Doniphan|Douglas|Edwards|Elk|Ellis|Ellsworth|Finney|Ford|Franklin|Geary|Gove|Graham|Grant|Gray|Greeley|Greenwood|Hamilton|Harper|Harvey|Haskell|Hodgeman|Jackson|Jefferson|Jewell|Johnson|Kearny|Kingman|Kiowa|Labette|Lane|Leavenworth|Lincoln|Linn|Logan|Lyon|Marion|Marshall|McPherson|Meade|Miami|Mitchell|Montgomery|Morris|Morton|Nemaha|Neosho|Ness|Norton|Osage|Osborne|Ottawa|Pawnee|Phillips|Pottawatomie|Pratt|Rawlins|Reno|Republic|Rice|Riley|Rooks|Rush|Russell|Saline|Scott|Sedgwick|Seward|Shawnee|Sheridan|Sherman|Smith|Stafford|Stanton|Stevens|Sumner|Thomas|Trego|Wabaunsee|Wallace|Washington|Wichita|Wilson|Woodson|Wyandotte"
).split("|").map(name => [name.toLowerCase(), name]));
const boundedText = (value: unknown) => typeof value === "string" && value.length <= 4096 ? value.replace(/\s+/g, " ").trim() : "";

export const wihaPublicRecord = (record: Record<string, unknown>) => {
  const input = typeof record.NOTES === "string" ? record.NOTES : "";
  const oversized = input.length > 4096;
  const raw = boundedText(input);
  // Every allowed string is screened in full before shortening or deriving
  // names/summaries. No raw field bypasses this projection in the route.
  const held = hasPersonalDetail(raw);
  const county = COUNTIES.get(boundedText(record.COUNTY).replace(/\s+County$/i, "").toLowerCase()) ?? null;
  const fields: string[] = [];
  if (record.COUNTY && !county) fields.push("county");
  const species = [1, 2, 3, 4, 5].flatMap(index => {
    const value = record[`SPECIES${index}`], text = boundedText(value);
    if (value && (!text || !/\p{L}/u.test(text) || STREET_ADDRESS.test(screeningText(text)) || hasPersonalDetail(text, false))) { fields.push(`species ${index}`); return []; }
    return text ? [text.slice(0, 40)] : [];
  });
  const contract = typeof record.CONTRACTID === "number" && Number.isSafeInteger(record.CONTRACTID)
    ? String(record.CONTRACTID) : typeof record.CONTRACTID === "string" ? record.CONTRACTID.trim() : "";
  // A public administrative reference, not an owner identity or account number.
  // Digit-only public IDs remain eligible without a personal phone label.
  const phoneDigits = (value: string) => value.replace(/\D/g, "").replace(/^1(?=\d{10}$)/, "");
  const copiesHeldPhone = /^\d{10,11}$/.test(contract) && [input, record.COUNTY, ...[1, 2, 3, 4, 5].map(index => record[`SPECIES${index}`])]
    .some(value => personalPhones(screeningText(boundedText(value))).some(match => phoneDigits(match[0]) === phoneDigits(contract)));
  const contractReference = /^[A-Za-z0-9][A-Za-z0-9._/-]{0,39}$/.test(contract) && !hasPersonalDetail(contract) && !copiesHeldPhone ? contract : null;
  if (contract && !contractReference) fields.push("contract reference");
  return {
    county, species: species.length ? species.join(", ") : null,
    fieldsStatus: fields.length ? `Provider fields withheld: ${fields.join(", ")}; review required` : null,
    contractReference,
    notes: raw && !held ? raw.slice(0, 240) : null,
    notesStatus: oversized ? "Note exceeds 4096-character screening limit; review required" : !raw ? "Not supplied by provider" : held ? (held === "person" ? "Withheld for a possible personal name or family detail; review required" : "Withheld for possible personal contact, identity or location detail; review required")
      : raw.length > 240 ? "Public provider note · shortened to 240 characters" : "Public provider note",
  };
};
