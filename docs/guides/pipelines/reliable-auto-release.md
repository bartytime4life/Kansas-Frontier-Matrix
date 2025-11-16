# ======================================================================
#  🔁 reliable-auto-release.yml
#  Kansas Frontier Matrix — Reliable Auto-Release Runner
#  Schedule + Webhook → Watch → Fetch → Validate → Transform → Diff → SemVer → Publish
#  Idempotent · FAIR+CARE Safe · Deterministic · Fully Auditable
# ======================================================================

name: reliable-auto-release

on:
  schedule:
    - cron: "*/15 * * * *"              # Every 15 minutes
  workflow_dispatch: {}                 # Manual trigger
  repository_dispatch:
    types: [upstream_changed]           # Webhook → GHA fan-in event

concurrency:
  group: reliable-auto-release-${{ github.ref }}   # Per-branch isolation
  cancel-in-progress: false                        # Never cancel mid-run

permissions:
  contents: write
  pull-requests: write

jobs:
  run:
    name: Reliable Auto-Release Pipeline
    runs-on: ubuntu-latest

    steps:

      # ---------------------------------------------------------------
      # Checkout repo (full history for SemVer, changelogs, diffing)
      # ---------------------------------------------------------------
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # ---------------------------------------------------------------
      # Python runtime
      # ---------------------------------------------------------------
      - name: Setup Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      # ---------------------------------------------------------------
      # Install pipeline dependencies
      # ---------------------------------------------------------------
      - name: Install pipeline dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      # ---------------------------------------------------------------
      # Watch → Fetch
      # If the source ETag has not changed, no further steps should run.
      # ---------------------------------------------------------------
      - name: Watch & Fetch (conditional)
        id: fetch
        env:
          SOURCE_URL: ${{ vars.SOURCE_URL }}
        run: |
          set -euo pipefail

          python -m src.pipelines.reliable_auto_release.watcher \
            --emit-dispatch=false

          python -m src.pipelines.reliable_auto_release.fetch \
            --url "$SOURCE_URL" \
            --etag-cache data/work/reliable_auto_release/cache/etag.json \
            --out data/work/reliable_auto_release/input.dat \
            --log data/work/reliable_auto_release/fetch.log

      # ---------------------------------------------------------------
      # Validation
      # ---------------------------------------------------------------
      - name: Validate dataset
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.validate \
            --in data/work/reliable_auto_release/input.dat \
            --schemas schemas/ \
            --log data/work/reliable_auto_release/validate.log

      # ---------------------------------------------------------------
      # Transform (deterministic)
      # ---------------------------------------------------------------
      - name: Transform (deterministic)
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.transform \
            --in data/work/reliable_auto_release/input.dat \
            --out data/work/reliable_auto_release/output.parquet \
            --log data/work/reliable_auto_release/transform.log

      # ---------------------------------------------------------------
      # Diff + SemVer classification
      # ---------------------------------------------------------------
      - name: Diff & Version
        if: steps.fetch.outputs.changed == 'true'
        id: version
        run: |
          # Diff old vs new to classify column / row deltas
          python -m src.pipelines.reliable_auto_release.diff_classify \
            --new data/work/reliable_auto_release/output.parquet \
            --old releases/latest/output.parquet || true

          # Deterministic SemVer bump (major/minor/patch)
          python -m src.pipelines.reliable_auto_release.versioner \
            --strategy deterministic \
            --out .version

      # ---------------------------------------------------------------
      # Prepare artifacts (CHANGELOG, manifest, SBOM)
      # ---------------------------------------------------------------
      - name: Prepare Release Artifacts (CHANGELOG, manifest, SBOM)
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.publish \
            --version-file .version \
            --changelog releases/${{ steps.version.outputs.version }}/CHANGELOG.md \
            --manifest releases/${{ steps.version.outputs.version }}/manifest.zip \
            --sbom releases/${{ steps.version.outputs.version }}/sbom.spdx.json \
            --stage-only

      # ---------------------------------------------------------------
      # Publish PR or Release
      # ---------------------------------------------------------------
      - name: Publish PR or Release
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.publish --do-publish

      # ---------------------------------------------------------------
      # Telemetry + Notification
      # ---------------------------------------------------------------
      - name: Emit Telemetry & Notify
        if: steps.fetch.outputs.changed == 'true'
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        run: |
          python -m src.pipelines.reliable_auto_release.telemetry --emit
          python -m src.pipelines.reliable_auto_release.notify \
            --slack-webhook "$SLACK_WEBHOOK_URL"


