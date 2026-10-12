import { openSync, closeSync, fstatSync, constants, readFileSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";

/** Explicit private local configuration, shared by launcher and daily runner.
 * Generate each token from 32 random bytes; never put them in source or argv. */
export function readArchiveAccess(file = path.join(homedir(), ".config/kfm/daily-archive-access")) {
  let fd;
  try { fd = openSync(file, constants.O_RDONLY | constants.O_NOFOLLOW); }
  catch (error) { if (error.code === "ENOENT") return null; throw new Error("ARCHIVE_ACCESS_FILE_UNSAFE"); }
  try {
    const info = fstatSync(fd);
    if (!info.isFile() || info.uid !== process.getuid() || (info.mode & 0o077) || info.size > 4096) throw new Error("ARCHIVE_ACCESS_FILE_UNSAFE");
    let access;
    try { access = JSON.parse(readFileSync(fd, "utf8")); } catch { throw new Error("ARCHIVE_ACCESS_FILE_INVALID"); }
    if (!access || ![access.ownerToken, access.workerToken].every(value => typeof value === "string" && /^[A-Za-z0-9_-]{43,128}$/.test(value)) || access.ownerToken === access.workerToken) throw new Error("ARCHIVE_ACCESS_FILE_INVALID");
    return access;
  } finally { closeSync(fd); }
}
