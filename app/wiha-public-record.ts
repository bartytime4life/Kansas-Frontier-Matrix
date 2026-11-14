/** Public administrative data is not sensitive merely because it concerns a
 * contract or payment. This narrow WIHA projection is not a universal public-
 * data admission gate, identity resolver or complete personal-data detector. */
// Common given names. A capitalized given name, or a family/ownership relation, in a
// note beside a tract can tie that private land to a person; hold the note for review.
// Names followed by a place word (for example "Clark County") are geography, not people.
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
const PLACE_WORD = /^(?:County|Creek|Lake|River|Road|Rd|Township|Twp|Street|St|Avenue|Ave|Draw|Pond|Reservoir|Ranch|Park)\b/;
const RELATION = /\b(?:owner'?s?|landowners?'?|tenants?|renters?|son|daughter|wife|husband|brother|sister|mother|father|grand(?:son|daughter)|widow(?:er)?|nephew|niece|estate of|heirs?)\b/i;
const namesPerson = (text: string) => {
  const words = text.split(/\s+/);
  for (const [index, word] of words.entries()) {
    const name = /^[^A-Za-z]*([A-Z][a-z]+)(?:'s)?[^A-Za-z]*$/.exec(word)?.[1];
    if (name && GIVEN_NAMES.has(name) && !PLACE_WORD.test(words[index + 1] ?? "")) return true;
  }
  return RELATION.test(text);
};

export const wihaPublicRecord = (record: Record<string, unknown>) => {
  const input = typeof record.NOTES === "string" ? record.NOTES : "";
  const oversized = input.length > 4096;
  const raw = oversized ? "" : input.replace(/\s+/g, " ").trim();
  // Screen the complete value BEFORE truncating. Hold the whole note rather
  // than publishing a remaining fragment that could identify or locate someone.
  const phonePattern = /(?:\+?1[ .-]?)?(?:\(\d{3}\)[ .-]?|\d{3}[ .-])\d{3}[ .-]\d{4}\b/;
  const ssnPattern = /\b\d{3}-\d{2}-\d{4}\b/;
  const contact = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(raw)
    || phonePattern.test(raw);
  const personalId = ssnPattern.test(raw)
    || /\b(?:SSN|social security|passport|driver'?s? licen[cs]e)\s*(?:(?:number|no\.?|#|:)\s*)?[A-Z]*\d{4,}\b/i.test(raw);
  const targeting = /\b(?:(?:home|residential) address\s*:|lives at|(?:personal|private) (?:phone|email)\s*:|current whereabouts\s*:|last seen at|(?:live|real-time) location\s*:)/i.test(raw);
  const person = namesPerson(raw);
  const held = contact || personalId || targeting || person;
  const contract = typeof record.CONTRACTID === "number" && Number.isSafeInteger(record.CONTRACTID)
    ? String(record.CONTRACTID) : typeof record.CONTRACTID === "string" ? record.CONTRACTID.trim() : "";
  // A public administrative reference, not an owner identity or account number.
  const contractReference = /^[A-Za-z0-9][A-Za-z0-9._/-]{0,39}$/.test(contract) && !phonePattern.test(contract) && !ssnPattern.test(contract) ? contract : null;
  return {
    contractReference,
    notes: raw && !held ? raw.slice(0, 240) : null,
    notesStatus: oversized ? "Note exceeds 4096-character screening limit; review required" : !raw ? "Not supplied by provider" : held ? (person && !contact && !personalId && !targeting ? "Withheld for a possible personal name or family detail; review required" : "Withheld for possible personal contact, identity or location detail; review required")
      : raw.length > 240 ? "Public provider note · shortened to 240 characters" : "Public provider note",
  };
};
