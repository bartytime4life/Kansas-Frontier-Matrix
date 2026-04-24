#!/bin/sh
set -eu

repo_root="."
manifest_path="tools/ci/readme_required_paths.txt"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --root)
      if [ "$#" -lt 2 ]; then
        echo "missing value for --root" >&2
        exit 2
      fi
      repo_root="$2"
      shift 2
      ;;
    --manifest)
      if [ "$#" -lt 2 ]; then
        echo "missing value for --manifest" >&2
        exit 2
      fi
      manifest_path="$2"
      shift 2
      ;;
    --help|-h)
      echo "usage: $0 [--root <repo_root>] [--manifest <path>]"
      exit 0
      ;;
    --*)
      echo "unknown option: $1" >&2
      exit 2
      ;;
    *)
      echo "unexpected argument: $1" >&2
      exit 2
      ;;
  esac
done

cd "$repo_root"

if [ ! -f "$manifest_path" ]; then
  echo "manifest not found: $manifest_path" >&2
  exit 2
fi

missing_count=0
checked_count=0

while IFS= read -r line || [ -n "$line" ]; do
  path="$(printf '%s' "$line" | sed 's/[[:space:]]*$//')"
  case "$path" in
    ''|\#*)
      continue
      ;;
  esac

  checked_count=$((checked_count + 1))
  if [ ! -f "$path" ]; then
    echo "missing: $path" >&2
    missing_count=$((missing_count + 1))
  fi
done < "$manifest_path"

if [ "$checked_count" -eq 0 ]; then
  echo "manifest has no paths: $manifest_path" >&2
  exit 2
fi

if [ "$missing_count" -ne 0 ]; then
  echo "check_readme_paths: failed ($missing_count missing path(s))" >&2
  exit 1
fi

echo "check_readme_paths: ok ($checked_count paths checked)"
