import { sourceBindingsMatch, validateSourceBindings, validateWorkbenchState } from './notebook.mjs';
export function encodeWorkbenchView({ workspace, state, sourceBindings }) {
  if (!['county', 'signal'].includes(workspace)) throw new Error('Unknown workspace.');
  const doc = JSON.stringify({ version: 1, workspace, state: validateWorkbenchState(state), sourceBindings: validateSourceBindings(sourceBindings) });
  const bytes = new TextEncoder().encode(doc);
  const token = btoa(Array.from(bytes, byte => String.fromCharCode(byte)).join('')).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  if (token.length > 12000) throw new Error('These settings are too large for a share link. Download an analysis receipt instead.');
  return token;
}
export function decodeWorkbenchView(token, { workspace, sourceBindings }) {
  try {
    if (typeof token !== 'string' || token.length > 12000 || !/^[a-zA-Z0-9_-]+$/.test(token)) return null;
    const binary = atob(token.replace(/-/g, '+').replace(/_/g, '/'));
    const doc = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(Uint8Array.from(binary, char => char.charCodeAt(0))));
    if (doc.version !== 1 || doc.workspace !== workspace || !['county', 'signal'].includes(workspace) || !sourceBindingsMatch(doc.sourceBindings, sourceBindings) || Object.keys(doc).some(key => !['version', 'workspace', 'state', 'sourceBindings'].includes(key))) return null;
    return { state: validateWorkbenchState(doc.state) };
  } catch { return null; }
}
