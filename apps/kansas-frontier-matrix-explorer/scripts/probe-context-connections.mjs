/** Explicit-run Node CLI; browser-safe transport lives in the app-local module. */
import { pathToFileURL } from 'node:url';
import { probeContextConnections } from '../app/context-connection-probe.mjs';
export { CONNECTIONS, REFERENCE_MIRROR, validateOrigin, probeContextConnections } from '../app/context-connection-probe.mjs';

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  if (process.argv.length !== 4 || process.argv[2] !== '--origin') {
    console.error('Usage: node scripts/probe-context-connections.mjs --origin <existing-Site-or-loopback-origin>');
    process.exitCode = 2;
  } else {
    try { console.log(JSON.stringify(await probeContextConnections({ origin: process.argv[3] }), null, 2)); }
    catch { console.error('Probe refused: use an allowed origin without credentials, path, query, or fragment.'); process.exitCode = 2; }
  }
}
