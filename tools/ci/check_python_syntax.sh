#!/bin/sh
set -eu

manifest="./tools/ci/python_syntax_targets.txt"

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

if [ ! -f "$manifest" ]; then
  echo "check_python_syntax: manifest not found: $manifest" >&2
  exit 2
fi

missing=0
targets=""

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

  targets="$targets $rel"
done < "$manifest"

if [ "$missing" -ne 0 ]; then
  exit 1
fi

if [ -z "${targets# }" ]; then
  echo "check_python_syntax: no targets listed in manifest" >&2
  exit 2
fi

# shellcheck disable=SC2086
python3 -m py_compile $targets

echo "check_python_syntax: ok"
