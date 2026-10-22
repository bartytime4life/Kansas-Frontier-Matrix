// Optional mirror of an already committed public artifact. Never transfers originals.
import { spawn } from 'node:child_process';
import { mkdtemp, unlink } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { hashFile, immutable } from '../../server/pipeline-files.mjs';
import { sha, fail, ORIGIN } from '../../server/pipeline-contract.mjs';

const configQuote = value => {
  if (typeof value !== 'string' || /[\r\n\0]/.test(value)) fail('FTPS_CONFIG_INVALID');
  return '"' + value.replaceAll('\\', '\\\\').replaceAll('"', '\\"') + '"';
};
export function validateFtps(config) {
  if (config?.format !== 'kfm-qualified-ftps-v1' || config.qualified !== true || !/^[a-z0-9](?:[a-z0-9.-]{0,251}[a-z0-9])?$/.test(config.host ?? '')
    || !config.host.includes('.') || config.privateDirectory === config.publicDirectory
    || !['privateDirectory','publicDirectory'].every(key => /^\/[A-Za-z0-9_/-]+$/.test(config[key] ?? '') && !config[key].split('/').includes('..'))
    || !/^https:\/\/[a-z0-9.-]+(?:\/[A-Za-z0-9_/-]*)?$/.test(config.httpsBase ?? '') || config.username?.includes(':')) fail('FTPS_CONFIG_INVALID');
  configQuote(config.username); configQuote(config.password);
  return config;
}
export function curlRun(args, input) {
  return new Promise((accept, reject) => {
    const child = spawn('curl', args, { shell: false, stdio: ['pipe','ignore','pipe'] });
    child.stderr.on('data', () => {}); // curl errors can include endpoint/account text; fixed failure only.
    child.on('error', () => reject(new Error('FTPS_UNAVAILABLE')));
    child.on('exit', code => code === 0 ? accept() : reject(new Error('FTPS_TRANSFER_FAILED')));
    child.stdin.on('error', () => {}); child.stdin.end(input);
  });
}
export async function mirrorFtps(config, manifest, payload, receipt, { run = curlRun, fetcher = fetch } = {}) {
  validateFtps(config);
  if (receipt?.state !== 'COMMITTED' || receipt.payloadSha256 !== sha(payload) || manifest.payloadSha256 !== sha(payload)
    || !/^[a-f0-9]{64}$/.test(receipt.releaseId ?? '') || payload.length !== manifest.byteLength) fail('COMMITTED_PUBLIC_RELEASE_REQUIRED');
  const work = await mkdtemp(resolve(tmpdir(), 'kfm-ftps-'));
  const input = resolve(work, 'public.json'), readback = resolve(work, 'readback');
  await immutable(input, payload);
  const filename = receipt.releaseId + '.json';
  const staged = config.privateDirectory.replace(/\/$/, '') + '/' + filename + '.part';
  const target = config.publicDirectory.replace(/\/$/, '') + '/' + filename;
  const credential = 'user = ' + configQuote(config.username + ':' + config.password) + '\n';
  const base = ['--silent','--show-error','--fail','--max-time','120','--retry','0','--proto','=ftp','--ssl-reqd','--tlsv1.2','--ftp-pasv','--config','-'];
  try {
    await run([...base, '--upload-file', input, 'ftp://' + config.host + staged], credential);
    await run([...base, '--output', readback, 'ftp://' + config.host + staged], credential);
    const observed = await hashFile(readback);
    if (observed.sha256 !== manifest.payloadSha256 || observed.bytes !== payload.length) fail('FTPS_READBACK_FAILED');
    // A qualified account must enforce private staging. Public paths receive complete bytes only.
    await run([...base, '--quote', 'RNFR ' + staged, '--quote', 'RNTO ' + target, '--list-only', 'ftp://' + config.host + config.publicDirectory + '/'], credential);
    const url = config.httpsBase.replace(/\/$/, '') + '/' + filename;
    const response = await fetcher(url, { redirect: 'manual', signal: AbortSignal.timeout(30000) });
    if (!response.ok) fail('FTPS_HTTPS_UNVERIFIED');
    // Reuse the stream bound instead of trusting remote content-length.
    const { boundedBody } = await import('../../server/pipeline-contract.mjs');
    const body = await boundedBody(response, payload.length);
    if (sha(body) !== manifest.payloadSha256) fail('FTPS_HTTPS_UNVERIFIED');
    return { releaseId: receipt.releaseId, httpsUrl: url, sha256: manifest.payloadSha256, sourceOrigin: ORIGIN, state: 'mirror-verified' };
  } finally {
    await unlink(input).catch(() => {}); await unlink(readback).catch(() => {});
  }
}
