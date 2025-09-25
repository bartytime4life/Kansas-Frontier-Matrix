// scripts/sync-roadmap.js
// Roadmap sync: Labels, Milestones, Issues (idempotent).
// DRY_RUN=true → parse + diff logging only (no writes).
// Optional pruning: PRUNE_LABELS=true, PRUNE_MILESTONES=true (skips "protected" items).

import fs from 'node:fs';
import path from 'node:path';
import * as core from '@actions/core';
import * as github from '@actions/github';
import yaml from 'js-yaml';

const {
  GITHUB_TOKEN,
  GITHUB_REPOSITORY,
  GITHUB_WORKSPACE = process.cwd(),
  ROADMAP_FILE = '.github/roadmap/roadmap.yaml',
  DRY_RUN = 'false',
  PRUNE_LABELS = 'false',
  PRUNE_MILESTONES = 'false'
} = process.env;

if (!GITHUB_REPOSITORY) {
  core.setFailed('GITHUB_REPOSITORY env is missing (expected "owner/repo")');
  process.exit(1);
}
if (!GITHUB_TOKEN) {
  core.setFailed('GITHUB_TOKEN env is missing');
  process.exit(1);
}

const [owner, repo] = GITHUB_REPOSITORY.split('/');
const octokit = github.getOctokit(GITHUB_TOKEN);
const isDry = String(DRY_RUN).toLowerCase() === 'true';
const doPruneLabels = String(PRUNE_LABELS).toLowerCase() === 'true';
const doPruneMilestones = String(PRUNE_MILESTONES).toLowerCase() === 'true';

// ---------------- util ----------------
const resolvePath = (p) => {
  const abs1 = path.isAbsolute(p) ? p : path.join(GITHUB_WORKSPACE, p);
  return fs.existsSync(abs1) ? abs1 : path.resolve(p);
};
const readYaml = (p) => yaml.load(fs.readFileSync(resolvePath(p), 'utf8'));
const log = (msg) => core.info(msg);
const warn = (msg) => core.warning(msg);
const would = (action, target) => core.info(`[DRY_RUN] would ${action}: ${target}`);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function normalizeLabelColor(hex) {
  if (!hex) return 'ededed';
  const c = hex.replace('#', '').trim();
  return /^[0-9a-fA-F]{6}$/.test(c) ? c.toLowerCase() : 'ededed';
}

// Simple retry/backoff for REST calls
async function withRetry(fn, desc, { retries = 3, baseMs = 500 } = {}) {
  let err;
  for (let i = 0; i <= retries; i++) {
    try {
      return await fn();
    } catch (e) {
      err = e;
      const wait = baseMs * Math.pow(2, i);
      warn(`[retry ${i + 1}/${retries + 1}] ${desc}: ${e?.message || e}. waiting ${wait}ms`);
      await sleep(wait);
    }
  }
  throw err;
}

// ---------------- labels ----------------
async function listAllLabels() {
  return await withRetry(
    () => octokit.paginate(octokit.rest.issues.listLabelsForRepo, { owner, repo, per_page: 100 }),
    'list labels'
  );
}

async function upsertLabel(def, existingByName) {
  const name = def.name;
  const color = normalizeLabelColor(def.color);
  const description = def.description || '';

  const existing = existingByName.get(name.toLowerCase());
  if (!existing) {
    if (isDry) return would('create label', name);
    await withRetry(
      () => octokit.rest.issues.createLabel({ owner, repo, name, color, description }),
      `create label ${name}`
    );
    log(`Created label: ${name}`);
    return;
  }

  const curColor = normalizeLabelColor(existing.color);
  const curDesc = existing.description || '';
  if (curColor !== color || curDesc !== description) {
    if (isDry) return would('update label', name);
    await withRetry(
      () => octokit.rest.issues.updateLabel({ owner, repo, name, color, description, new_name: name }),
      `update label ${name}`
    );
    log(`Updated label: ${name} (color ${curColor}→${color}${curDesc !== description ? ', desc changed' : ''})`);
  } else {
    log(`Label OK: ${name}`);
  }
}

async function ensureLabelsFromRoadmap(labels, createMissing = true) {
  if (!Array.isArray(labels)) labels = [];
  const existing = await listAllLabels();
  const existingByName = new Map(existing.map((l) => [l.name.toLowerCase(), l]));

  for (const l of labels) {
    await upsertLabel(l, existingByName);
    existingByName.set(l.name.toLowerCase(), { ...existingByName.get(l.name.toLowerCase()), ...l });
  }
  return { existingByName };
}

async function ensureReferencedLabels(labelNames, existingByName, createMissing = true) {
  for (const name of labelNames || []) {
    const key = (name || '').toLowerCase();
    if (!key) continue;
    if (!existingByName.has(key)) {
      if (!createMissing) {
        warn(`Label referenced but not defined and create_missing_labels=false: ${name}`);
        continue;
      }
      const def = { name, color: 'ededed', description: '' };
      if (isDry) {
        would('create missing referenced label', name);
      } else {
        await withRetry(
          () => octokit.rest.issues.createLabel({ owner, repo, name, color: 'ededed', description: '' }),
          `create referenced label ${name}`
        );
      }
      existingByName.set(key, def);
    }
  }
}

async function pruneLabels(roadmapNames) {
  if (!doPruneLabels) return;
  const protectedSet = new Set(
    (Array.isArray(roadmapNames) ? roadmapNames : []).map((n) => (n || '').toLowerCase())
  );
  const existing = await listAllLabels();
  for (const l of existing) {
    const name = l.name;
    const key = name.toLowerCase();
    // skip GitHub default labels and roadmap-protected labels
    const defaultProtected = new Set([
      'bug', 'documentation', 'duplicate', 'enhancement', 'good first issue',
      'help wanted', 'invalid', 'question', 'wontfix'
    ]);
    if (defaultProtected.has(key) || protectedSet.has(key)) continue;

    if (isDry) {
      would('delete label', name);
    } else {
      try {
        await withRetry(
          () => octokit.rest.issues.deleteLabel({ owner, repo, name }),
          `delete label ${name}`
        );
        log(`Deleted label: ${name}`);
      } catch (e) {
        warn(`Could not delete label "${name}": ${e?.message || e}`);
      }
    }
  }
}

// ---------------- milestones ----------------
async function listAllMilestones() {
  return await withRetry(
    () =>
      octokit.paginate(octokit.rest.issues.listMilestones, {
        owner,
        repo,
        state: 'all',
        per_page: 100
      }),
    'list milestones'
  );
}

function equalOrUndefined(a, b) {
  return (a || '') === (b || '');
}

async function upsertMilestone(ms, existing) {
  const found = existing.find((m) => m.title === ms.title);
  const body = {
    title: ms.title,
    description: ms.description || '',
    state: ms.state || 'open'
  };
  if (ms.due_on) body.due_on = ms.due_on;

  if (found) {
    const needsDesc = !equalOrUndefined(found.description, body.description);
    const needsState = body.state !== found.state;
    const needsDue = (body.due_on || null) !== (found.due_on || null);

    if (needsDesc || needsState || needsDue) {
      if (isDry) {
        would('update milestone', `${ms.title} (#${found.number})`);
      } else {
        await withRetry(
          () =>
            octokit.rest.issues.updateMilestone({
              owner,
              repo,
              milestone_number: found.number,
              description: body.description,
              state: body.state,
              due_on: body.due_on
            }),
          `update milestone ${ms.title}`
        );
        log(`Updated milestone: ${ms.title} (#${found.number})`);
      }
    } else {
      log(`Milestone OK: ${ms.title} (#${found.number})`);
    }
    return found.number;
  }

  if (isDry) {
    would('create milestone', ms.title);
    return null;
  }
  // ✅ FIX: include owner/repo for create
  const created = await withRetry(
    () =>
      octokit.rest.issues.createMilestone({
        owner,
        repo,
        title: body.title,
        state: body.state,
        description: body.description,
        due_on: body.due_on
      }),
    `create milestone ${ms.title}`
  );
  log(`Created milestone: ${ms.title} (#${created.data.number})`);
  return created.data.number;
}

async function pruneMilestones(roadmapTitles) {
  if (!doPruneMilestones) return;
  const protectedSet = new Set((roadmapTitles || []).map((t) => (t || '').toLowerCase()));
  const existing = await listAllMilestones();
  for (const m of existing) {
    const key = (m.title || '').toLowerCase();
    if (protectedSet.has(key)) continue;
    if (m.open_issues > 0 || m.closed_issues > 0) {
      warn(`Skip deleting milestone with issues: ${m.title} (#${m.number})`);
      continue;
    }
    if (isDry) {
      would('delete milestone', `${m.title} (#${m.number})`);
    } else {
      try {
        await withRetry(
          () => octokit.rest.issues.deleteMilestone({ owner, repo, milestone_number: m.number }),
          `delete milestone ${m.title}`
        );
        log(`Deleted milestone: ${m.title} (#${m.number})`);
      } catch (e) {
        warn(`Could not delete milestone "${m.title}": ${e?.message || e}`);
      }
    }
  }
}

// ---------------- issues ----------------
async function findIssueByExactTitle(title) {
  const q = `repo:${owner}/${repo} is:issue in:title "${title.replace(/"/g, '\\"')}"`;
  const res = await withRetry(
    () => octokit.rest.search.issuesAndPullRequests({ q, per_page: 30 }),
    `search issue "${title}"`
  );
  return res.data.items.find((i) => i.title === title && !i.pull_request) || null;
}

function toArray(x) {
  if (!x) return [];
  return Array.isArray(x) ? x : [x];
}

function mergeDefaultsIntoIssue(issue, defaults) {
  const mergedLabels = Array.from(new Set([...(toArray(issue.labels)), ...(toArray(defaults.labels))]));
  const assignees =
    (issue.assignees && issue.assignees.length) ? issue.assignees : (defaults.assignees || []);
  const state = issue.state || defaults.state || 'open';
  return { ...issue, labels: mergedLabels, assignees, state };
}

async function upsertIssue(milestoneNumber, issue, labelByName, createMissingLabels, defaults) {
  const merged = mergeDefaultsIntoIssue(issue, defaults);
  const labels = merged.labels || [];

  // ensure referenced labels exist
  await ensureReferencedLabels(labels, labelByName, createMissingLabels);

  const existing = await findIssueByExactTitle(merged.title);
  const body = {
    owner,
    repo,
    title: merged.title,
    body: merged.body || '',
    labels,
    assignees: merged.assignees || [],
    milestone: milestoneNumber || null,
    state: merged.state
  };

  if (!existing) {
    if (isDry) return would('create issue', merged.title);
    const created = await withRetry(() => octokit.rest.issues.create(body), `create issue ${merged.title}`);
    log(`Created issue #${created.data.number}: ${merged.title}`);
    return;
  }

  // Patch update (idempotent)
  if (isDry) return would('update issue', `${merged.title} (#${existing.number})`);
  await withRetry(
    () => octokit.rest.issues.update({ ...body, issue_number: existing.number }),
    `update issue ${merged.title}`
  );
  log(`Updated issue #${existing.number}: ${merged.title}`);
}

// ---------------- main ----------------
(async function main() {
  try {
    const conf = readYaml(ROADMAP_FILE);

    // Defaults from roadmap
    const defaults = {
      issue: {
        state: conf?.defaults?.issue?.state || 'open',
        assignees: conf?.defaults?.issue?.assignees || [],
        labels: conf?.defaults?.issue?.labels || []
      },
      create_missing_labels: conf?.defaults?.create_missing_labels !== false, // default true
      create_missing_milestones: conf?.defaults?.create_missing_milestones !== false // default true
    };

    log(`Repo: ${owner}/${repo} | DRY_RUN=${isDry} | Roadmap: ${resolvePath(ROADMAP_FILE)}`);
    log(`Prune: labels=${doPruneLabels} milestones=${doPruneMilestones}`);

    // 1) Labels
    const { existingByName: labelByName } =
      await ensureLabelsFromRoadmap(conf.labels || [], defaults.create_missing_labels);

    // 2) Milestones
    const existingMilestones = await listAllMilestones();
    const roadmapMilestoneTitles = (conf.milestones || []).map((m) => m.title);

    for (const ms of conf.milestones || []) {
      let number = null;
      const found = existingMilestones.find((x) => x.title === ms.title);

      if (found) {
        number = await upsertMilestone(ms, existingMilestones);
      } else if (defaults.create_missing_milestones) {
        number = await upsertMilestone(ms, existingMilestones);
      } else {
        warn(`Milestone missing and create_missing_milestones=false: ${ms.title}`);
      }

      // 3) Issues under this milestone
      for (const issue of ms.issues || []) {
        await upsertIssue(number, issue, labelByName, defaults.create_missing_labels, defaults.issue);
      }
    }

    // 4) Optional pruning (only items not present in roadmap, with safeguards)
    if (doPruneLabels) {
      await pruneLabels((conf.labels || []).map((l) => l.name));
    }
    if (doPruneMilestones) {
      await pruneMilestones(roadmapMilestoneTitles);
    }

    log('Roadmap sync complete.');
  } catch (err) {
    core.setFailed(err?.message || String(err));
  }
})();
