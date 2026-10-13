// Linux-only local package read. Validate the opened descriptor, not a path
// checked before opening that another process could replace in between.
import { constants } from "node:fs";
import { open, realpath } from "node:fs/promises";
import path from "node:path";

export async function readPackageObject(root, key, maxBytes) {
  if (typeof key !== "string" || !key || !Number.isSafeInteger(maxBytes) || maxBytes < 0 || maxBytes > 4_000_000) {
    throw new Error("Invalid package object request");
  }
  const file = path.resolve(root, key);
  if (!file.startsWith(root + path.sep)) throw new Error("Package path escapes root");
  const handle = await open(file, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    // /proc/self/fd names the object actually opened, including when an
    // intermediate directory was switched to a symlink during the open.
    const openedPath = await realpath(`/proc/self/fd/${handle.fd}`);
    if (!openedPath.startsWith(root + path.sep)) throw new Error("Opened object escapes package root");
    const info = await handle.stat();
    if (!info.isFile() || info.size > maxBytes) throw new Error("Invalid package object type or size");
    const bytes = Buffer.allocUnsafe(maxBytes + 1);
    let length = 0;
    while (length <= maxBytes) {
      const { bytesRead } = await handle.read(bytes, length, maxBytes + 1 - length, length);
      if (!bytesRead) break;
      length += bytesRead;
    }
    if (length > maxBytes) throw new Error("Package object grew beyond byte limit");
    return bytes.subarray(0, length);
  } finally {
    await handle.close();
  }
}
