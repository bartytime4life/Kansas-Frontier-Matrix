import { randomBytes } from "node:crypto";
import { openSync, closeSync, fstatSync, constants, readSync, mkdirSync, lstatSync, realpathSync, writeFileSync, fsyncSync, linkSync, unlinkSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";

const accessPath = () => path.join(homedir(), ".config/kfm/daily-archive-access");
const maxFileBytes = 4096;

/** Explicit private local configuration, shared by launcher and daily runner.
 * Generate each token from 32 random bytes; never put them in source or argv. */
export function readArchiveAccess(file = accessPath()) {
  let fd;
  try { fd = openSync(file, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK); }
  catch (error) { if (error.code === "ENOENT") return null; throw new Error("ARCHIVE_ACCESS_FILE_UNSAFE"); }
  try {
    const info = fstatSync(fd);
    if (!info.isFile() || info.uid !== process.getuid() || (info.mode & 0o077) || info.size > maxFileBytes) throw new Error("ARCHIVE_ACCESS_FILE_UNSAFE");
    const bytes = Buffer.alloc(maxFileBytes + 1);
    let size = 0;
    while (size < bytes.length) {
      const read = readSync(fd, bytes, size, bytes.length - size, null);
      if (read === 0) break;
      size += read;
    }
    if (size > maxFileBytes) throw new Error("ARCHIVE_ACCESS_FILE_UNSAFE");
    let access;
    try { access = JSON.parse(bytes.toString("utf8", 0, size)); } catch { throw new Error("ARCHIVE_ACCESS_FILE_INVALID"); }
    if (!access || ![access.ownerToken, access.workerToken].every(value => typeof value === "string" && /^[A-Za-z0-9_-]{43,128}$/.test(value)) || access.ownerToken === access.workerToken) throw new Error("ARCHIVE_ACCESS_FILE_INVALID");
    return access;
  } finally { closeSync(fd); }
}

function ensureOwnedDirectory(directory) {
  try { mkdirSync(directory, { mode: 0o700 }); }
  catch (error) { if (error.code !== "EEXIST") throw error; }
  const info = lstatSync(directory);
  if (!info.isDirectory() || info.uid !== process.getuid() || (info.mode & 0o022) || realpathSync(directory) !== directory) {
    throw new Error("ARCHIVE_ACCESS_DIRECTORY_UNSAFE");
  }
}

/** Provision a new local capability pair only. A valid existing pair is reused. */
export function initializeArchiveAccess(file = accessPath()) {
  const target = path.resolve(file);
  const directory = path.dirname(target);
  ensureOwnedDirectory(path.dirname(directory));
  ensureOwnedDirectory(directory);
  if (readArchiveAccess(target)) return "already-configured";

  const ownerToken = randomBytes(32).toString("base64url");
  let workerToken;
  do { workerToken = randomBytes(32).toString("base64url"); } while (workerToken === ownerToken);
  const temporary = path.join(directory, `.daily-archive-access-${randomBytes(12).toString("hex")}`);
  const fd = openSync(temporary, "wx", 0o600);
  try {
    writeFileSync(fd, JSON.stringify({ ownerToken, workerToken }) + "\n");
    fsyncSync(fd);
    // An exclusive link publishes only a complete file and never replaces a pair.
    try { linkSync(temporary, target); }
    catch (error) {
      if (error.code !== "EEXIST") throw error;
      if (!readArchiveAccess(target)) throw new Error("ARCHIVE_ACCESS_FILE_CHANGED");
      return "already-configured";
    }
    return "initialized";
  } finally {
    closeSync(fd);
    unlinkSync(temporary);
  }
}
