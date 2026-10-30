// Shared by the root installer and its isolated installed-tree smoke test.
import { mkdir, copyFile, chmod } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export async function copyKit(destination) {
  const root = fileURLToPath(new URL('../..', import.meta.url));
  const files = ['server/ingestion-sources.mjs','server/pipeline-contract.mjs','server/pipeline-normalize.mjs','server/pipeline-files.mjs','server/pipeline-auth.mjs','server/county-history-candidate.mjs','server/county-history-release.mjs',
    'app/pipeline-catalog.mjs','scripts/pc-pipeline/config.mjs','scripts/pc-pipeline/capture.mjs','scripts/pc-pipeline/health.mjs','scripts/pc-pipeline/revalidate.mjs',
    'scripts/pc-pipeline/journal.mjs','scripts/pc-pipeline/publisher.mjs','scripts/pc-pipeline/worker.mjs','scripts/pc-pipeline/cli.mjs','scripts/pc-pipeline/connection.mjs',
    'scripts/pc-pipeline/copy.mjs','scripts/pc-pipeline/ftps.mjs','scripts/pc-pipeline/storage-policy.mjs'];
  for (const name of files) {
    const target = resolve(destination, name);
    await mkdir(dirname(target), { recursive: true });
    await copyFile(resolve(root, name), target);
    await chmod(target, 0o644);
  }
}
