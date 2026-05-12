#!/usr/bin/env bash
set -euo pipefail

START_DATE="$(date -d '365 days ago' +%F)"
END_DATE="$(date +%F)"
MARKER_FILE=".painted"

if [[ -f "$MARKER_FILE" ]]; then
  recorded_range="$(<"$MARKER_FILE")"
  if [[ "$recorded_range" == "$START_DATE,$END_DATE" ]]; then
    echo "Already painted for date range $START_DATE through $END_DATE. Nothing to do."
    exit 0
  fi
fi

if [[ -z "${GIT_USER_NAME:-}" ]]; then
  echo "Error: GIT_USER_NAME is unset. Export it before running this script."
  exit 1
fi

if [[ -z "${GIT_USER_EMAIL:-}" ]]; then
  echo "Error: GIT_USER_EMAIL is unset. Export it before running this script."
  echo "This email must match a verified email on your GitHub account or commits will not count."
  exit 1
fi

MIN_COMMITS="${MIN_COMMITS:-1}"
MAX_COMMITS="${MAX_COMMITS:-4}"

if ! [[ "$MIN_COMMITS" =~ ^[0-9]+$ && "$MAX_COMMITS" =~ ^[0-9]+$ ]]; then
  echo "Error: MIN_COMMITS and MAX_COMMITS must be non-negative integers."
  exit 1
fi

if (( MIN_COMMITS < 0 || MAX_COMMITS < 0 )); then
  echo "Error: MIN_COMMITS and MAX_COMMITS must be non-negative integers."
  exit 1
fi

if (( MIN_COMMITS > MAX_COMMITS )); then
  echo "Error: MIN_COMMITS cannot be greater than MAX_COMMITS."
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init
fi

git config user.name "$GIT_USER_NAME"
git config user.email "$GIT_USER_EMAIL"

current_date="$START_DATE"
total_commits=0

while [[ "$current_date" < "$END_DATE" || "$current_date" == "$END_DATE" ]]; do
  range_size=$((MAX_COMMITS - MIN_COMMITS + 1))
  commits_today=$((MIN_COMMITS + RANDOM % range_size))

  for ((n = 1; n <= commits_today; n++)); do
    hour=$((9 + RANDOM % 13))

    commit_ts="$(date -d "$current_date ${hour}:00:00" '+%Y-%m-%dT%H:%M:%S%z')"

    GIT_AUTHOR_DATE="$commit_ts" \
    GIT_COMMITTER_DATE="$commit_ts" \
      git commit --allow-empty -m "daily: $current_date #$n" >/dev/null

    total_commits=$((total_commits + 1))
  done

  current_date="$(date -d "$current_date + 1 day" +%F)"
done

echo "$START_DATE,$END_DATE" > "$MARKER_FILE"

repo_name="contrib-paint-$(date +%Y%m%d)"

echo "Created $total_commits commits for $START_DATE through $END_DATE."
echo ""
echo "Next commands (not executed):"
echo "  gh repo create \"$repo_name\" --public"
echo "  git remote add origin \"git@github.com:<YOUR_GITHUB_USERNAME>/$repo_name.git\""
echo "  git branch -M main"
echo "  git push -u origin main"
