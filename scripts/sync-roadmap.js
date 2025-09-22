// scripts/sync-roadmap.js
// Roadmap sync: Labels, Milestones, Issues (idempotent).
// DRY_RUN=true → parse + diff logging only (no writes).

import fs from 'node:fs';
import path from 'node:path';
import * as core from '@actions/core';
import * as github from '@actions/github';
import yaml from 'js-yaml';

const {
  GITHUB_TOKEN,
  GITHUB_REPOSITORY,
  ROADMAP_FILE = '.github/roadmap/roadmap.yaml',
  DRY_RUN = 'false'
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

const readYaml = (p) => yaml.load(fs.readFileSync(path.resolve(p), 'utf8'));

const log = (msg) => core.info(msg);
const would = (action, target) => core.info(`[DRY_RUN] would ${action}: ${target}`);

function normalizeLabelColor(hex) {
  if (!hex) return 'ededed';
  const c = hex.replace('#', '').trim();
  return /^[0-9a-fA-F]{6}$/.test(c) ? c.toLowerCase() : 'ededed';
}

// ---------- Labels ----------
async function listAllLabels() {
  return await octokit.paginate(octokit.rest.issues.listLabelsForRepo, { owner, repo, per_page: 100 });
}

async function upsertLabel(def, existingByName) {
  const name = def.name;
  const color = normalizeLabelColor(def.color);
  const description = def.description || '';

  const existing = existingByName.get(name.toLowerCase());
  if (!existing) {
    if (isDry) return would('create label', name);
    await octokit.rest.issues.createLabel({ owner, repo, name, color, description });
    return log(`Created label: ${name}`);
  }

  // Update if changed (color or description)
  const curColor = normalizeLabelColor(existing.color);
  const curDesc = existing.description || '';
  if (curColor !== color || curDesc !== description) {
    if (isDry) return would('update label', name);
    await octokit.rest.issues.updateLabel({ owner, repo, name, color, description, new_name: name });
    return log(`Updated label: ${name}`);
  }
  return log(`Label OK: ${name}`);
}

async function ensureLabelsFromRoadmap(labels, createMissing = true) {
  if (!Array.isArray(labels)) return;
  const existing = await listAllLabels();
  const existingByName = new Map(existing.map(l => [l.name.toLowerCase(), l]));

  for (const l of labels) {
    await upsertLabel(l, existingByName);
    // refresh cache
    existingByName.set(l.name.toLowerCase(), { ...existingByName.get(l.name.toLowerCase()), ...l });
  }

  return { existingByName, createMissing };
}

async function ensureReferencedLabels(labelNames, existingByName, createMissing = true) {
  for (const name of labelNames || []) {
    const key = (name || '').toLowerCase();
    if (!key) continue;
    if (!existingByName.has(key)) {
      if (!createMissing) {
        core.warning(`Label referenced but not defined and create_missing_labels=false: ${name}`);
        continue;
      }
      const def = { name, color: 'ededed', description: '' };
      if (isDry) {
        would('create missing referenced label', name);
      } else {
        await octokit.rest.issues.createLabel({ owner, repo, name, color: 'ededed', description: '' });
      }
      existingByName.set(key, def);
    }
  }
}

// ---------- Milestones ----------
async function listAllMilestones() {
  return await octokit.paginate(octokit.rest.issues.listMilestones, { owner, repo, state: 'all', per_page: 100 });
}

function equalOrUndefined(a, b) {
  return (a || '') === (b || '');
}

async function upsertMilestone(ms, existing) {
  const found = existing.find(m => m.title === ms.title);
  const body = {
    title: ms.title,
    description: ms.description || '',
    state: ms.state || 'open'
  };
  if (ms.due_on) body.due_on = ms.due_on;

  if (found) {
    // diff
    const needsDesc = !equalOrUndefined(found.description, body.description);
    const needsState = (body.state !== found.state);
    const needsDue = (body.due_on || null) !== (found.due_on || null);

    if (needsDesc || needsState || needsDue) {
      if (isDry) {
        would('update milestone', `${ms.title} (#${found.number})`);
      } else {
        await octokit.rest.issues.updateMilestone({
          owner, repo, milestone_number: found.number,
          description: body.description,
          state: body.state,
          due_on: body.due_on
        });
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
  const created = await octokit.rest.issues.createMilestone(body);
  log(`Created milestone: ${ms.title} (#${created.data.number})`);
  return created.data.number;
}

// ---------- Issues ----------
async function findIssueByExactTitle(title) {
  const q = `repo:${owner}/${repo} is:issue in:title "${title.replace(/"/g, '\\"')}"`;
  const res = await octokit.rest.search.issuesAndPullRequests({ q, per_page: 20 });
  return res.data.items.find(i => i.title === title && !i.pull_request) || null;
}

function mergeDefaultsIntoIssue(issue, defaults) {
  const mergedLabels = Array.from(new Set([...(issue.labels || []), ... (defaults.labels || [])]));
  const assignees = (issue.assignees && issue.assignees.length) ? issue.assignees : (defaults.assignees || []);
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
    owner, repo,
    title: merged.title,
    body: merged.body || '',
    labels,
    assignees: merged.assignees || [],
    milestone: milestoneNumber || null,
    state: merged.state
  };

  if (!existing) {
    if (isDry) return would('create issue', merged.title);
    const created = await octokit.rest.issues.create(body);
    log(`Created issue #${created.data.number}: ${merged.title}`);
    return;
  }

  // Update patch
  if (isDry) return would('update issue', `${merged.title} (#${existing.number})`);
  await octokit.rest.issues.update({ ...body, issue_number: existing.number });
  log(`Updated issue #${existing.number}: ${merged.title}`);
}

// ---------- Main ----------
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

    log(`Repo: ${owner}/${repo} | DRY_RUN=${isDry} | Roadmap: ${ROADMAP_FILE}`);

    // Labels: upsert (create/update color/desc)
    const { existingByName: labelByName } =
      await ensureLabelsFromRoadmap(conf.labels || [], defaults.create_missing_labels);

    // Milestones & Issues
    const existingMilestones = await listAllMilestones();

    for (const ms of conf.milestones || []) {
      let number = null;
      const found = existingMilestones.find(x => x.title === ms.title);
      if (found) {
        number = await upsertMilestone(ms, existingMilestones);
      } else if (defaults.create_missing_milestones) {
        number = await upsertMilestone(ms, existingMilestones);
      } else {
        core.warning(`Milestone missing and create_missing_milestones=false: ${ms.title}`);
      }

      // Issues under this milestone
      for (const issue of ms.issues || []) {
        await upsertIssue(number, issue, labelByName, defaults.create_missing_labels, defaults.issue);
      }
    }

    log('Roadmap sync complete.');
  } catch (err) {
    core.setFailed(err?.message || String(err));
  }
})();
