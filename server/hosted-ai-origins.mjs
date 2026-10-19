// Exact controlled hosting origins only; no wildcard preview hosts.
const ORIGINS = new Set([
  'https://kansasfrontiermatrix.com',
  'https://q9r9beo47t.preview.c38.airoapp.ai',
  'https://urdng3v1vk.preview.c38.airoapp.ai',
]);
export const hostedAiOriginAllowed = value => ORIGINS.has(value);
