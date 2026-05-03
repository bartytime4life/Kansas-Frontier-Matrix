#!/usr/bin/env bash
set -euo pipefail
# Whole-run rollback
git reset --hard HEAD~1

# Remove sprint artifacts if needed
rm -rf docs/registers/reorg
