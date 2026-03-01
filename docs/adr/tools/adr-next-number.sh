#!/usr/bin/env bash
set -euo pipefail

max=$(find "$(dirname "$0")/.." -maxdepth 1 -type f -name "[0-9][0-9][0-9][0-9]-*.md" \
  | sed -E "s#.*/([0-9]{4})-.*#\1#" \
  | sort -n \
  | tail -n1)

if [[ -z "${max:-}" ]]; then
  printf "0001\n"
else
  printf "%04d\n" "$((10#$max + 1))"
fi
