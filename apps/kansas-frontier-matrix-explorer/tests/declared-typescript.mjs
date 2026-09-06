import { readFileSync, realpathSync, statSync } from 'node:fs';
import { join, resolve, relative, isAbsolute } from 'node:path';

/** Resolve the app's declared CLI, never the classic API alias or an ambient tsc.
 * Frozen package installation supplies byte integrity; this checks identities,
 * lock agreement and entrypoint confinement, not package-tarball integrity.
 */
export function resolveDeclaredTypeScript(appRoot) {
  const read = path => JSON.parse(readFileSync(path, 'utf8'));
  const manifest = read(join(appRoot, 'package.json'));
  const lock = read(join(appRoot, 'package-lock.json'));
  const dependencies = manifest.devDependencies ?? {};
  const key = Object.hasOwn(dependencies, '@typescript/native') ? '@typescript/native' : 'typescript';
  const declaration = dependencies[key];
  const match = typeof declaration === 'string' && declaration.match(key === '@typescript/native'
    ? /^npm:typescript@(\d+\.\d+\.\d+)$/ : /^(\d+\.\d+\.\d+)$/);
  if (!match) throw new Error('Declared TypeScript CLI must be an exact version or npm:typescript alias');
  const version = match[1];
  const entry = lock.packages?.[`node_modules/${key}`];
  if (lock.packages?.['']?.devDependencies?.[key] !== declaration
      || entry?.version !== version || (entry.name ?? 'typescript') !== 'typescript'
      || typeof entry.integrity !== 'string' || !entry.integrity.startsWith('sha512-')) {
    throw new Error('TypeScript CLI declaration and app lock do not agree');
  }
  const directory = realpathSync(join(appRoot, 'node_modules', key));
  const installed = read(join(directory, 'package.json'));
  if (installed.name !== 'typescript' || installed.version !== version) {
    throw new Error('Installed TypeScript CLI identity does not match the app lock');
  }
  const bin = installed.bin?.tsc;
  if (typeof bin !== 'string' || bin !== entry.bin?.tsc || isAbsolute(bin)) {
    throw new Error('TypeScript CLI entrypoint does not match the app lock');
  }
  const compiler = realpathSync(resolve(directory, bin));
  const path = relative(directory, compiler);
  if (!path || path === '..' || path.startsWith('../') || path.startsWith('..\\')
      || isAbsolute(path) || !statSync(compiler).isFile()) {
    throw new Error('TypeScript CLI entrypoint escapes the declared package');
  }
  return Object.freeze({ compiler, compilerVersion: version,
    compilerMode: 'DECLARED_CLI_VERSION_MATCH', installedByteIntegrity: 'FROZEN_INSTALL_REQUIRED_NOT_REHASHED' });
}
