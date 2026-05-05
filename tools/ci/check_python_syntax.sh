#!/bin/sh
set -eu

manifest=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --manifest)
      manifest="$2"
      shift 2
      ;;
    *)
      echo "check_python_syntax: unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

targets_file="$(mktemp)"
trap 'rm -f "$targets_file"' EXIT

if [ -n "$manifest" ]; then
  if [ ! -f "$manifest" ]; then
    echo "check_python_syntax: manifest not found: $manifest" >&2
    exit 2
  fi

  missing=0
  while IFS= read -r rel || [ -n "$rel" ]; do
    case "$rel" in
      ""|\#*)
        continue
        ;;
    esac

    if [ ! -f "$rel" ]; then
      echo "check_python_syntax: missing file listed in manifest: $rel" >&2
      missing=1
      continue
    fi

    printf "%s\n" "$rel" >> "$targets_file"
  done < "$manifest"

  if [ "$missing" -ne 0 ]; then
    exit 1
  fi
else
  find . -type f -name '*.py' \
    -not -path './.git/*' \
    -not -path './.pytest_cache/*' \
    -not -path '*/__pycache__/*' \
    | sort > "$targets_file"
fi

if [ ! -s "$targets_file" ]; then
  echo "check_python_syntax: no Python files found to check" >&2
  exit 2
fi

while IFS= read -r path || [ -n "$path" ]; do
  python3 -m py_compile "$path"
done < "$targets_file"

if [ -n "$manifest" ]; then
  echo "check_python_syntax: ok (manifest)"
else
  echo "check_python_syntax: ok (all python files)"
fi
