import fs from 'fs';
import path from 'path';
import * as core from '@actions/core';
import * as github from '@actions/github';
import yaml from 'js-yaml';

const repoFull = process.env.GITHUB_REPOSITORY;
if (!repoFull) {
  core.setFailed('GITHUB_REPOSITORY env is missing');
  process.exit(1);
}
const [owner, repo] = repoFull.split('/');
const token = process.env.GITHUB_TOKEN;
if (!token) {
  core.setFailed('GITHUB_TOKEN not provided');
  process.exit(1);
}

const octokit = github.getOctokit(token);

const ROADMAP_FILE = path.join('.github', 'roadmap', 'roadmap.yaml');

function mdChecklist(tasks = []) {
  return tasks.map(t => (t.startsWith('- [') ? t : `- [ ] ${t}`)).join('\n');
}

async function ensureLabels(labels) {
  if (!labels || !labels.length) return;
  const existing = await octokit.paginate(octokit.rest.issues.listLabelsForRepo, { owner, repo, per_page: 100 });
  const have = new Map(existing.map(l => [l.name.toLowerCase(), l]));
  for (const l of labels) {
    const key = l.name.toLowerCase();
    if (have.has(key)) continue;
    await octokit.rest.issues.createLabel({
      owner, repo,
      name: l.name,
      color: l.color?.replace('#', '') || 'ededed',
      description: l.description || ''
    });
  }
}

async function upsertMilestone(title, description) {
  const milestones = await octokit.paginate(octokit.rest.issues.listMilestones, { owner, repo, state: 'open', per_page: 100 });
  const found = milestones.find(m => m.title === title);
  if (found) {
    // Update description if changed
    if ((found.description || '') !== (description || '')) {
      await octokit.rest.issues.updateMilestone({
        owner, repo, milestone_number: found.number, description
      });
    }
    return found.number;
  }
  const created = await octokit.rest.issues.createMilestone({ owner, repo, title, description });
  return created.data.number;
}

async function findIssueByTitle(title) {
  const q = `repo:${owner}/${repo} in:title "${title}" is:issue`;
  const res = await octokit.rest.search.issuesAndPullRequests({ q, per_page: 10 });
  const hit = res.data.items.find(i => i.title === title && !i.pull_request);
  return hit || null;
}

async function upsertIssue(milestoneNumber, issueDef) {
  const { title, labels = [], body = '' } = issueDef;
  const existing = await findIssueByTitle(title);

  const labelNames = labels;

  if (!existing) {
    const created = await octokit.rest.issues.create({
      owner, repo,
      title,
      body,
      labels: labelNames,
      milestone: milestoneNumber
    });
    core.info(`Created issue #${created.data.number}: ${title}`);
    return;
  }

  // patch if needed
  const toUpdate = {
    owner, repo,
    issue_number: existing.number,
    title,
    body,
    labels: labelNames,
    milestone: milestoneNumber
  };
  await octokit.rest.issues.update(toUpdate);
  core.info(`Updated issue #${existing.number}: ${title}`);
}

(async function main() {
  try {
    const raw = fs.readFileSync(ROADMAP_FILE, 'utf8');
    const conf = yaml.load(raw);

    await ensureLabels(conf.labels || []);

    for (const m of conf.milestones || []) {
      const milestoneNumber = await upsertMilestone(m.title, m.description || '');
      for (const issue of m.issues || []) {
        await upsertIssue(milestoneNumber, issue);
      }
    }

    core.info('Roadmap sync complete.');
  } catch (err) {
    core.setFailed(err.message || String(err));
  }
})();
