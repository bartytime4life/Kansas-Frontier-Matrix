import { createHash } from "node:crypto";
import { QWEN_KNOWLEDGE_PACK } from "./qwen-knowledge-pack.mjs";
import { QWEN_LOCAL_KNOWLEDGE_VERSION } from "./qwen-local-contract.mjs";

/**
 * Bridge-side knowledge selection. The pack is source metadata (what each
 * source is, how often it updates, what it is NOT) plus KFM vocabulary and
 * exploration ideas. It ships with the companion, so a browser cannot alter
 * it, and its digest is recorded in every interpretation receipt.
 */
if (QWEN_KNOWLEDGE_PACK.version !== QWEN_LOCAL_KNOWLEDGE_VERSION) {
  throw new Error("The local Qwen knowledge pack does not match the bridge contract.");
}

export const QWEN_KNOWLEDGE_VERSION = QWEN_KNOWLEDGE_PACK.version;
export const QWEN_KNOWLEDGE_DIGEST = `sha256:${createHash("sha256").update(JSON.stringify(QWEN_KNOWLEDGE_PACK)).digest("hex")}`;
export const QWEN_KNOWLEDGE_MAX_DETAILED_SOURCES = 8;
const MAX_IDEA_DOMAINS = 3;
const MAX_CROSS_DOMAIN_IDEAS = 3;
const DOMAIN_BY_SOURCE_ID = new Map(QWEN_KNOWLEDGE_PACK.officialSources.map((source) => [source.id, source.domain]));

/** Domains of the sources the map is actually displaying; question words do not count. */
const displayedDomains = (context) => new Set((Array.isArray(context?.officialSources) ? context.officialSources : [])
  .filter((source) => source?.displayed === true)
  .map((source) => DOMAIN_BY_SOURCE_ID.get(source.id))
  .filter(Boolean));

const STOP_WORDS = new Set([
  "about", "and", "are", "can", "does", "for", "from", "has", "have", "how", "into", "its", "kansas",
  "map", "show", "shows", "should", "that", "the", "this", "view", "visible", "what", "when", "where",
  "which", "who", "why", "with", "would", "you", "your", "there", "these", "those", "data", "layer", "layers",
]);

const normalize = (value) => typeof value === "string"
  ? value.normalize("NFKD").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim()
  : "";
const tokensOf = (value) => [...new Set(normalize(value).split(" ")
  .filter((token) => token.length >= 3 && !STOP_WORDS.has(token)))];

const SOURCE_SEARCH_TEXT = new Map(QWEN_KNOWLEDGE_PACK.officialSources.map((source) => [source.id, {
  heading: ` ${normalize([source.id, source.title, source.shortTitle, source.domain, source.organization].join(" "))} `,
  body: ` ${normalize([source.cadence, source.freshness, source.boundary].join(" "))} `,
}]));

const DISPLAY_SOURCE_TOPICS = /\b(?:basemap|imagery|satellite|aerial|street|streets|topo|topographic|terrain|elevation|3d|building|buildings|attribution)\b/;

/** Rank official sources by what the user is looking at and what they asked. */
export function rankQwenKnowledgeSources(question, context) {
  const questionTokens = tokensOf(question);
  const normalizedQuestion = ` ${normalize(question)} `;
  const contextSources = new Map((Array.isArray(context?.officialSources) ? context.officialSources : [])
    .map((source) => [source?.id, source]));
  const selectionTokens = tokensOf([context?.selection?.domain, context?.selection?.layerTitle].join(" "));
  return QWEN_KNOWLEDGE_PACK.officialSources
    .map((source, index) => {
      const text = SOURCE_SEARCH_TEXT.get(source.id);
      const active = contextSources.get(source.id);
      let score = 0;
      if (active?.displayed) score += 100;
      else if (active?.selected) score += 60;
      if (normalizedQuestion.includes(` ${normalize(source.domain)} `)) score += 20;
      for (const token of questionTokens) {
        if (text.heading.includes(` ${token} `)) score += 8;
        else if (text.body.includes(` ${token} `)) score += 3;
      }
      for (const token of selectionTokens) if (text.heading.includes(` ${token} `)) score += 4;
      return { source, index, score };
    })
    .filter((entry) => entry.score > 0)
    .sort((left, right) => right.score - left.score || left.index - right.index)
    .map((entry) => entry.source);
}

const byteLength = (value) => Buffer.byteLength(JSON.stringify(value));

/**
 * Trim the least specific sections first until the payload fits the byte
 * budget the bridge has left after the map context: the source index, then
 * basemap details, then project, cross-domain and domain ideas, then domain
 * terms, then detailed sources from the least relevant.
 */
function fitToBudget(payload, maxBytes) {
  if (!Number.isFinite(maxBytes) || byteLength(payload) <= maxBytes) return payload;
  const fitted = { ...payload, otherSources: [] };
  const steps = [
    () => { fitted.displaySources = []; },
    () => { fitted.projectIdeas = []; },
    () => { fitted.crossDomainIdeas = []; },
    () => { fitted.domainIdeas = []; },
    () => { fitted.domainTerms = []; },
  ];
  for (const step of steps) {
    if (byteLength(fitted) <= maxBytes) return fitted;
    step();
  }
  while (fitted.relevantSources.length > 0 && byteLength(fitted) > maxBytes) {
    fitted.relevantSources = fitted.relevantSources.slice(0, -1);
  }
  return fitted;
}

/**
 * Select a bounded, relevance-ordered slice of the pack. Detailed metadata is
 * capped; every other source still appears in a one-line index so the model
 * can name what exists without guessing. Principles and the glossary are never
 * trimmed: they are what keeps an interpretation inside KFM's rules.
 */
export function selectQwenKnowledge(question, context, { maxBytes = Infinity } = {}) {
  const detailed = rankQwenKnowledgeSources(question, context).slice(0, QWEN_KNOWLEDGE_MAX_DETAILED_SOURCES);
  const detailedIds = new Set(detailed.map((source) => source.id));
  const ideaDomains = [...new Set(detailed.map((source) => source.domain))].slice(0, MAX_IDEA_DOMAINS);
  const wantsDisplaySources = DISPLAY_SOURCE_TOPICS.test(normalize(question));
  const inView = displayedDomains(context);
  const payload = fitToBudget({
    knowledgeVersion: QWEN_KNOWLEDGE_VERSION,
    authority: "METADATA_NOT_EVIDENCE",
    principles: QWEN_KNOWLEDGE_PACK.principles,
    glossary: QWEN_KNOWLEDGE_PACK.glossary,
    relevantSources: detailed.map(({ id, title, organization, domain, kind, cadence, freshness, boundary, fallback, attribution, evidenceRole }) => ({
      id, title, organization, domain, kind, cadence, freshness, boundary, fallback, attribution, evidenceRole,
    })),
    otherSources: QWEN_KNOWLEDGE_PACK.officialSources
      .filter((source) => !detailedIds.has(source.id))
      .map((source) => `${source.id} · ${source.shortTitle} · ${source.domain}`),
    displaySources: wantsDisplaySources
      ? QWEN_KNOWLEDGE_PACK.displaySources.map(({ id, title, organization, kind, boundary }) => ({ id, title, organization, kind, boundary }))
      : QWEN_KNOWLEDGE_PACK.displaySources.map((source) => `${source.title} · ${source.kind}`),
    domainIdeas: (ideaDomains.length ? ideaDomains : QWEN_KNOWLEDGE_PACK.domains.map((domain) => domain.name).slice(0, MAX_IDEA_DOMAINS))
      .map((name) => ({ domain: name, ideas: QWEN_KNOWLEDGE_PACK.domains.find((domain) => domain.name === name)?.ideas ?? [] })),
    domainTerms: ideaDomains
      .map((name) => ({ domain: name, terms: QWEN_KNOWLEDGE_PACK.domains.find((domain) => domain.name === name)?.terms ?? {} }))
      .filter((entry) => Object.keys(entry.terms).length > 0),
    // Eligibility comes from what is displayed; order prefers pairs that touch
    // the question's relevant domains, so the cap keeps the most useful ideas.
    crossDomainIdeas: QWEN_KNOWLEDGE_PACK.crossDomainIdeas
      .filter((entry) => entry.domains.every((domain) => inView.has(domain)))
      .map((entry, index) => ({ entry, index, relevance: entry.domains.filter((domain) => ideaDomains.includes(domain)).length }))
      .sort((left, right) => right.relevance - left.relevance || left.index - right.index)
      .slice(0, MAX_CROSS_DOMAIN_IDEAS)
      .map(({ entry }) => entry.idea),
    projectIdeas: QWEN_KNOWLEDGE_PACK.projectIdeas,
  }, maxBytes);
  return Object.freeze({
    version: QWEN_KNOWLEDGE_VERSION,
    digest: QWEN_KNOWLEDGE_DIGEST,
    sourceIds: Object.freeze(payload.relevantSources.map((source) => source.id)),
    payload,
  });
}
