/** Public administrative data is not sensitive merely because it concerns a
 * contract or payment. This narrow WIHA projection is not a universal public-
 * data admission gate, identity resolver or complete personal-data detector. */
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
  const held = contact || personalId || targeting;
  const contract = typeof record.CONTRACTID === "number" && Number.isSafeInteger(record.CONTRACTID)
    ? String(record.CONTRACTID) : typeof record.CONTRACTID === "string" ? record.CONTRACTID.trim() : "";
  // A public administrative reference, not an owner identity or account number.
  const contractReference = /^[A-Za-z0-9][A-Za-z0-9._/-]{0,39}$/.test(contract) && !phonePattern.test(contract) && !ssnPattern.test(contract) ? contract : null;
  return {
    contractReference,
    notes: raw && !held ? raw.slice(0, 240) : null,
    notesStatus: oversized ? "Note exceeds 4096-character screening limit; review required" : !raw ? "Not supplied by provider" : held ? "Withheld for possible personal contact, identity or location detail; review required"
      : raw.length > 240 ? "Public provider note · shortened to 240 characters" : "Public provider note",
  };
};
