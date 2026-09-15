import { execFileSync } from "node:child_process";
import { pathToFileURL } from "node:url";

export const CURRENT_SITE_PROJECT = "appgprj_6aa0b1c41bc08191bfd86003920f1631";
const git = (root, ...args) => execFileSync("git", ["-C", root, ...args], {
  encoding: "utf8", maxBuffer: 8 * 1024 * 1024, stdio: ["ignore", "pipe", "pipe"],
}).trimEnd();

function inspect(root, revision) {
  if (typeof root !== "string" || !root || !/^[0-9a-f]{40}$/.test(revision ?? "")) {
    throw new Error("A checkout and an immutable full commit SHA are required.");
  }
  const commit = git(root, "rev-parse", "--verify", `${revision}^{commit}`);
  const tree = git(root, "rev-parse", `${commit}^{tree}`);
  const hosting = JSON.parse(git(root, "show", `${commit}:.openai/hosting.json`));
  const paths = git(root, "ls-tree", "-rz", "--name-only", commit).split("\0").filter(Boolean);
  return { commit, tree, projectId: hosting.project_id, files: paths.length };
}

/** Compare committed source bytes only. This does not inspect or deploy a host. */
export function verifySourceAlignment({ siteRoot, siteRevision, mirrorRoot, mirrorRevision }) {
  try {
    const site = inspect(siteRoot, siteRevision);
    const mirror = inspect(mirrorRoot, mirrorRevision);
    const reasons = [];
    if (site.projectId !== CURRENT_SITE_PROJECT || mirror.projectId !== CURRENT_SITE_PROJECT) {
      reasons.push("SITE_IDENTITY_MISMATCH");
    }
    if (site.tree !== mirror.tree) reasons.push("SOURCE_TREE_MISMATCH");
    return {
      outcome: reasons.length ? "HOLD" : "PASS", scope: "COMMITTED_SITE_MIRROR_BYTES",
      site, mirror, reasons, deploymentAuthorized: false, monorepoRuntimeParity: "NOT_ESTABLISHED",
    };
  } catch {
    return {
      outcome: "ERROR", scope: "COMMITTED_SITE_MIRROR_BYTES", reasons: ["SOURCE_INPUT_UNVERIFIED"],
      deploymentAuthorized: false, monorepoRuntimeParity: "NOT_ESTABLISHED",
    };
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const [siteRoot, siteRevision, mirrorRoot, mirrorRevision, ...extra] = process.argv.slice(2);
  const result = extra.length ? { outcome: "ERROR", reasons: ["UNEXPECTED_ARGUMENTS"] }
    : verifySourceAlignment({ siteRoot, siteRevision, mirrorRoot, mirrorRevision });
  console.log(JSON.stringify(result, null, 2));
  if (result.outcome !== "PASS") process.exitCode = 1;
}
