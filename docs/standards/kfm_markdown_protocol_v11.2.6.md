# .github/actions/schema-validate/action.yml
name: "KFM Schema Validate"
description: "Validate JSON / YAML / JSON-LD files against a KFM profile (JSON Schema; optional SHACL) and emit a machine-readable report."

inputs:
  paths:
    description: "Newline-separated glob patterns of files to validate (relative to working_directory)."
    required: true

  profile:
    description: "Validation profile identifier (e.g., kfm-config, kfm-stac-item, kfm-telemetry-ci-v11). Used to resolve schema + optional shape bundles."
    required: true

  mode:
    description: "Validation mode: all|changed. 'changed' best-effort (requires sufficient git history / base ref availability)."
    required: false
    default: "all"

  fail_level:
    description: "Minimum severity that causes failure: error|warning."
    required: false
    default: "error"

  working_directory:
    description: "Base directory for resolving globs and schema roots. Relative to $GITHUB_WORKSPACE."
    required: false
    default: "."

  schema_root:
    description: "Base directory for JSON Schemas. Relative to working_directory."
    required: false
    default: "schemas/json"

  shape_root:
    description: "Base directory for SHACL shapes. Relative to working_directory."
    required: false
    default: "schemas/shacl"

  use_shapes:
    description: "If 'true', run SHACL validation when a matching shape bundle exists and the input can be parsed as RDF/JSON-LD."
    required: false
    default: "false"

  report_path:
    description: "Output path for the full validation report JSON (relative to working_directory)."
    required: false
    default: "artifacts/schema/schema-validation.json"

  telemetry_path:
    description: "Output path for summary telemetry JSON (relative to working_directory)."
    required: false
    default: "artifacts/schema/schema-validation-telemetry.json"

  extra_args:
    description: "Reserved for advanced use (future passthrough flags). Currently ignored."
    required: false
    default: ""

outputs:
  status:
    description: "\"passed\" or \"failed\" based on fail_level and findings."
    value: ${{ steps.schema_validate.outputs.status }}
  error_count:
    description: "Total number of validation errors across all files."
    value: ${{ steps.schema_validate.outputs.error_count }}
  warning_count:
    description: "Total number of validation warnings across all files."
    value: ${{ steps.schema_validate.outputs.warning_count }}
  files_scanned:
    description: "Count of files processed."
    value: ${{ steps.schema_validate.outputs.files_scanned }}
  report_path:
    description: "Final resolved path to the JSON validation report."
    value: ${{ steps.schema_validate.outputs.report_path }}
  telemetry:
    description: "Final resolved path to telemetry JSON report."
    value: ${{ steps.schema_validate.outputs.telemetry }}

runs:
  using: "composite"
  steps:
    # NOTE: Per KFM governance, pin third-party actions by full commit SHA in your repo.
    - name: "Set up Python"
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: "Install validator dependencies (pinned)"
      shell: bash
      run: |
        set -euo pipefail
        python -m pip install --disable-pip-version-check --no-input \
          "jsonschema==4.23.0" \
          "PyYAML==6.0.2" \
          "rfc3987==1.3.8" \
          "rdflib==7.0.0" \
          "pyshacl==0.26.0"

    - name: "Run schema validation"
      id: schema_validate
      shell: bash
      env:
        INPUT_PATHS: ${{ inputs.paths }}
        INPUT_PROFILE: ${{ inputs.profile }}
        INPUT_MODE: ${{ inputs.mode }}
        INPUT_FAIL_LEVEL: ${{ inputs.fail_level }}
        INPUT_WORKING_DIRECTORY: ${{ inputs.working_directory }}
        INPUT_SCHEMA_ROOT: ${{ inputs.schema_root }}
        INPUT_SHAPE_ROOT: ${{ inputs.shape_root }}
        INPUT_USE_SHAPES: ${{ inputs.use_shapes }}
        INPUT_REPORT_PATH: ${{ inputs.report_path }}
        INPUT_TELEMETRY_PATH: ${{ inputs.telemetry_path }}
        GITHUB_WORKSPACE: ${{ github.workspace }}
        GITHUB_SHA: ${{ github.sha }}
        GITHUB_BASE_REF: ${{ github.base_ref }}
      run: |
        set -euo pipefail
        python - << 'PY'
        import datetime as _dt
        import glob
        import json
        import os
        import platform
        import subprocess
        import sys
        import time
        from pathlib import Path

        import yaml
        import jsonschema
        from jsonschema import FormatChecker
        from jsonschema.validators import validator_for

        # Optional SHACL stack (installed above)
        import rdflib
        from pyshacl import validate as shacl_validate


        def _utc_iso(ts: float | None = None) -> str:
            if ts is None:
                ts = time.time()
            return _dt.datetime.fromtimestamp(ts, tz=_dt.timezone.utc).isoformat().replace("+00:00", "Z")


        def _json_no_dupes(fp: Path):
            def hook(pairs):
                obj = {}
                for k, v in pairs:
                    if k in obj:
                        raise ValueError(f"Duplicate key '{k}'")
                    obj[k] = v
                return obj

            with fp.open("r", encoding="utf-8") as fh:
                return json.load(fh, object_pairs_hook=hook)


        class _UniqueKeyLoader(yaml.SafeLoader):
            pass


        def _construct_mapping(loader: yaml.SafeLoader, node: yaml.nodes.MappingNode, deep: bool = False):
            mapping = {}
            for key_node, value_node in node.value:
                key = loader.construct_object(key_node, deep=deep)
                if key in mapping:
                    raise ValueError(f"Duplicate key '{key}'")
                mapping[key] = loader.construct_object(value_node, deep=deep)
            return mapping


        _UniqueKeyLoader.add_constructor(  # type: ignore[attr-defined]
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            _construct_mapping,
        )


        def _yaml_no_dupes(fp: Path):
            with fp.open("r", encoding="utf-8") as fh:
                return yaml.load(fh, Loader=_UniqueKeyLoader)


        def _as_pointer(path_parts) -> str:
            # jsonpointer encoding: "~"->"~0", "/"->"~1"
            out = ""
            for p in path_parts:
                s = str(p).replace("~", "~0").replace("/", "~1")
                out += "/" + s
            return out if out else "/"


        def _git_changed_files(repo_dir: Path) -> set[str] | None:
            """
            Best-effort changed-file detection. Returns None if git/base ref is unavailable.
            Assumes repo is already checked out.
            """
            base_ref = os.environ.get("GITHUB_BASE_REF") or ""
            try:
                if base_ref:
                    base = f"origin/{base_ref}"
                    # If base isn't present (shallow checkout), try a minimal fetch.
                    try:
                        subprocess.run(["git", "rev-parse", "--verify", base], cwd=repo_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    except Exception:
                        try:
                            subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", base_ref], cwd=repo_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        except Exception:
                            # can't fetch or still missing
                            pass

                    # Use merge-base if possible
                    try:
                        mb = subprocess.check_output(["git", "merge-base", "HEAD", base], cwd=repo_dir, text=True).strip()
                        diff_range = f"{mb}..HEAD"
                    except Exception:
                        diff_range = f"{base}..HEAD"
                else:
                    # push/non-PR fallback
                    diff_range = "HEAD~1..HEAD"

                out = subprocess.check_output(
                    ["git", "diff", "--name-only", "--diff-filter=ACMRT", diff_range],
                    cwd=repo_dir,
                    text=True,
                )
                return {line.strip() for line in out.splitlines() if line.strip()}
            except Exception:
                return None


        def _resolve_schema(profile: str, schema_root: Path) -> Path | None:
            # If profile is an explicit path, honor it.
            p = Path(profile)
            if p.is_file():
                return p

            # Try common naming variants.
            variants = [
                profile,
                profile.replace("@", "-"),
                profile.split("@")[0],
                profile.split("@")[0].replace("@", "-"),
            ]
            candidates: list[Path] = []
            for v in variants:
                candidates.extend(
                    [
                        schema_root / f"{v}.schema.json",
                        schema_root / f"{v}.json",
                        schema_root / v / "schema.json",
                        schema_root / v / f"{v}.schema.json",
                    ]
                )

            for c in candidates:
                if c.is_file():
                    return c
            return None


        def _resolve_shape(profile: str, shape_root: Path) -> Path | None:
            p = Path(profile)
            if p.is_file():
                # explicit path could be a ttl shape too, but only use if it looks like ttl
                if p.suffix.lower() in {".ttl", ".nt", ".n3", ".trig"}:
                    return p
                return None

            variants = [
                profile,
                profile.replace("@", "-"),
                profile.split("@")[0],
                profile.split("@")[0].replace("@", "-"),
            ]
            candidates: list[Path] = []
            for v in variants:
                candidates.extend(
                    [
                        shape_root / f"{v}.ttl",
                        shape_root / f"{v}-shape.ttl",
                        shape_root / f"{v}.shape.ttl",
                        shape_root / v / f"{v}-shape.ttl",
                        shape_root / v / f"{v}.ttl",
                    ]
                )

            for c in candidates:
                if c.is_file():
                    return c
            return None


        # ---- Inputs ----
        workspace = Path(os.environ.get("GITHUB_WORKSPACE", ".")).resolve()
        wd_in = os.environ.get("INPUT_WORKING_DIRECTORY", ".").strip() or "."
        working_directory = (workspace / wd_in).resolve()

        patterns_raw = os.environ.get("INPUT_PATHS", "")
        profile = os.environ.get("INPUT_PROFILE", "").strip()
        mode = (os.environ.get("INPUT_MODE", "all") or "all").strip().lower()
        fail_level = (os.environ.get("INPUT_FAIL_LEVEL", "error") or "error").strip().lower()
        schema_root = (working_directory / (os.environ.get("INPUT_SCHEMA_ROOT", "schemas/json").strip() or "schemas/json")).resolve()
        shape_root = (working_directory / (os.environ.get("INPUT_SHAPE_ROOT", "schemas/shacl").strip() or "schemas/shacl")).resolve()
        use_shapes = (os.environ.get("INPUT_USE_SHAPES", "false").strip().lower() == "true")
        report_path = (working_directory / (os.environ.get("INPUT_REPORT_PATH", "artifacts/schema/schema-validation.json").strip() or "artifacts/schema/schema-validation.json")).resolve()
        telemetry_path = (working_directory / (os.environ.get("INPUT_TELEMETRY_PATH", "artifacts/schema/schema-validation-telemetry.json").strip() or "artifacts/schema/schema-validation-telemetry.json")).resolve()
        commit_sha = os.environ.get("GITHUB_SHA", "")

        if not profile:
            print("❌ 'profile' input is required.", file=sys.stderr)
            sys.exit(2)

        patterns = [p.strip() for p in patterns_raw.splitlines() if p.strip()]
        if not patterns:
            print("❌ 'paths' input is required and must contain at least one glob.", file=sys.stderr)
            sys.exit(2)

        started = time.time()

        # ---- Discover files ----
        discovered: set[Path] = set()
        for pat in patterns:
            full_pat = str((working_directory / pat) if not os.path.isabs(pat) else Path(pat))
            for m in glob.glob(full_pat, recursive=True):
                p = Path(m)
                if p.is_file():
                    discovered.add(p.resolve())

        if not discovered:
            print("❌ No files matched inputs.paths patterns.", file=sys.stderr)
            sys.exit(2)

        warnings_global: list[dict] = []
        if mode == "changed":
            changed = _git_changed_files(working_directory)
            if changed is None:
                warnings_global.append({
                    "code": "KFM-SCHEMA-W_CHG001",
                    "message": "mode=changed requested, but git diff/base ref unavailable; validating all matched files.",
                    "severity": "warning",
                })
            else:
                # Normalize changed paths to absolute under working_directory
                changed_abs = set()
                for rel in changed:
                    try:
                        changed_abs.add((working_directory / rel).resolve())
                    except Exception:
                        pass
                discovered = {p for p in discovered if p in changed_abs}
                if not discovered:
                    # If nothing intersected, treat as config error (per spec)
                    print("❌ mode=changed resulted in zero files to validate (paths did not intersect git diff).", file=sys.stderr)
                    sys.exit(2)

        # ---- Resolve schema & optional shape ----
        schema_path = _resolve_schema(profile, schema_root)
        if schema_path is None:
            print(f"❌ Could not resolve JSON Schema for profile='{profile}' under schema_root='{schema_root}'.", file=sys.stderr)
            sys.exit(2)

        schema_path = schema_path.resolve()
        try:
            schema = _json_no_dupes(schema_path)
        except Exception as e:
            print(f"❌ Failed to load schema '{schema_path}': {e}", file=sys.stderr)
            sys.exit(2)

        try:
            vcls = validator_for(schema)
            vcls.check_schema(schema)
        except Exception as e:
            print(f"❌ Schema is not valid JSON Schema: {schema_path} :: {e}", file=sys.stderr)
            sys.exit(2)

        resolver = jsonschema.RefResolver(base_uri=schema_path.as_uri(), referrer=schema)  # noqa: S301 (RefResolver deprecated but stable)
        validator = vcls(schema, resolver=resolver, format_checker=FormatChecker())

        shape_path = None
        shapes_graph = None
        if use_shapes:
            shape_path = _resolve_shape(profile, shape_root)
            if shape_path and shape_path.is_file():
                shapes_graph = rdflib.Graph()
                try:
                    shapes_graph.parse(str(shape_path), format="turtle")
                except Exception as e:
                    warnings_global.append({
                        "code": "KFM-SHACL-W_LOAD001",
                        "message": f"Failed to parse SHACL shapes at '{shape_path}'; skipping SHACL validation. Error: {e}",
                        "severity": "warning",
                    })
                    shapes_graph = None
            else:
                warnings_global.append({
                    "code": "KFM-SHACL-W_MISSING001",
                    "message": f"use_shapes=true but no SHACL bundle found for profile '{profile}' under '{shape_root}'; skipping SHACL validation.",
                    "severity": "warning",
                })

        # ---- Validate files ----
        per_file = []
        error_count = 0
        warning_count = 0

        for fp in sorted(discovered):
            rel = str(fp.relative_to(working_directory)) if fp.is_relative_to(working_directory) else str(fp)
            file_errors = []
            file_warnings = []

            suffix = fp.suffix.lower()
            try:
                if suffix in {".yaml", ".yml"}:
                    doc = _yaml_no_dupes(fp)
                elif suffix in {".json", ".jsonld"}:
                    doc = _json_no_dupes(fp)
                else:
                    file_warnings.append({
                        "code": "KFM-SCHEMA-W_TYPE001",
                        "message": f"Unsupported file extension '{suffix}' (skipped).",
                        "json_pointer": "/",
                        "severity": "warning",
                    })
                    per_file.append({"path": rel, "errors": [], "warnings": file_warnings})
                    warning_count += len(file_warnings)
                    continue
            except Exception as e:
                file_errors.append({
                    "code": "KFM-SCHEMA-E_PARSE",
                    "message": f"Parse error: {e}",
                    "json_pointer": "/",
                    "severity": "error",
                })
                per_file.append({"path": rel, "errors": file_errors, "warnings": file_warnings})
                error_count += len(file_errors)
                warning_count += len(file_warnings)
                continue

            # JSON Schema validation
            try:
                errs = sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))
                for e in errs:
                    file_errors.append({
                        "code": "KFM-SCHEMA-E_VALIDATION",
                        "message": e.message,
                        "json_pointer": _as_pointer(e.absolute_path),
                        "validator": str(e.validator),
                        "severity": "error",
                    })
            except Exception as e:
                file_errors.append({
                    "code": "KFM-SCHEMA-E_ENGINE",
                    "message": f"Validator engine error: {e}",
                    "json_pointer": "/",
                    "severity": "error",
                })

            # Optional SHACL validation (only when shapes available + file parseable as JSON-LD/RDF)
            if use_shapes and shapes_graph is not None:
                # Best-effort: only parse JSON-LD (file extension .jsonld OR has @context)
                is_jsonldish = (suffix == ".jsonld") or (isinstance(doc, dict) and ("@context" in doc or "@graph" in doc))
                if is_jsonldish:
                    data_graph = rdflib.Graph()
                    try:
                        data_graph.parse(str(fp), format="json-ld")
                        conforms, results_graph, results_text = shacl_validate(
                            data_graph=data_graph,
                            shacl_graph=shapes_graph,
                            inference="rdfs",
                            abort_on_first=False,
                            meta_shacl=False,
                            advanced=False,
                            debug=False,
                        )
                        if not conforms:
                            # Keep the message short to avoid dumping too much into logs/telemetry.
                            msg = (results_text or "SHACL validation failed.").strip()
                            if len(msg) > 800:
                                msg = msg[:800] + "…"
                            file_errors.append({
                                "code": "KFM-SHACL-E_VALIDATION",
                                "message": msg,
                                "json_pointer": "/",
                                "severity": "error",
                            })
                    except Exception as e:
                        file_warnings.append({
                            "code": "KFM-SHACL-W_PARSE001",
                            "message": f"SHACL skipped: could not parse JSON-LD to RDF for file '{rel}'. Error: {e}",
                            "json_pointer": "/",
                            "severity": "warning",
                        })
                else:
                    file_warnings.append({
                        "code": "KFM-SHACL-W_SKIP001",
                        "message": "SHACL skipped: input not JSON-LD/RDF.",
                        "json_pointer": "/",
                        "severity": "warning",
                    })

            per_file.append({"path": rel, "errors": file_errors, "warnings": file_warnings})
            error_count += len(file_errors)
            warning_count += len(file_warnings)

        # Add global warnings
        warning_count += len(warnings_global)

        finished = time.time()
        duration = round(finished - started, 3)

        report = {
            "schema_version": "kfm-schema-validation-report-v1",
            "profile": profile,
            "run": {
                "started_at": _utc_iso(started),
                "finished_at": _utc_iso(finished),
                "duration_seconds": duration,
                "mode": mode,
                "fail_level": fail_level,
                "commit_sha": commit_sha,
            },
            "environment": {
                "python": platform.python_version(),
                "platform": platform.platform(),
                "jsonschema": getattr(jsonschema, "__version__", "unknown"),
            },
            "schema": {
                "schema_path": str(schema_path.relative_to(working_directory)) if schema_path.is_relative_to(working_directory) else str(schema_path),
                "schema_id": schema.get("$id") or schema.get("$schema") or None,
                "draft": schema.get("$schema") or None,
            },
            "shacl": {
                "enabled": bool(use_shapes),
                "shape_path": (str(shape_path.relative_to(working_directory)) if shape_path and shape_path.is_relative_to(working_directory) else (str(shape_path) if shape_path else None)),
            },
            "summary": {
                "files_scanned": len(per_file),
                "errors": error_count,
                "warnings": warning_count,
            },
            "global_warnings": warnings_global,
            "files": per_file,
        }

        telemetry = {
            "schema_version": "kfm-schema-validation-telemetry-v1",
            "profile": profile,
            "run": report["run"],
            "summary": report["summary"],
        }

        report_path.parent.mkdir(parents=True, exist_ok=True)
        telemetry_path.parent.mkdir(parents=True, exist_ok=True)

        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        telemetry_path.write_text(json.dumps(telemetry, indent=2), encoding="utf-8")

        failed = (error_count > 0) or (fail_level == "warning" and warning_count > 0)
        status = "failed" if failed else "passed"

        # Step summary (best-effort)
        step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if step_summary:
            with open(step_summary, "a", encoding="utf-8") as fh:
                fh.write(f"## 📐 KFM Schema Validate — {status.upper()}\n")
                fh.write(f"- Profile: `{profile}`\n")
                fh.write(f"- Files scanned: **{len(per_file)}**\n")
                fh.write(f"- Errors: **{error_count}**\n")
                fh.write(f"- Warnings: **{warning_count}**\n")
                fh.write(f"- Report: `{report_path}`\n")
                fh.write(f"- Telemetry: `{telemetry_path}`\n")

        # Emit composite outputs
        gh_out = os.environ.get("GITHUB_OUTPUT")
        if gh_out:
            with open(gh_out, "a", encoding="utf-8") as fh:
                fh.write(f"status={status}\n")
                fh.write(f"error_count={error_count}\n")
                fh.write(f"warning_count={warning_count}\n")
                fh.write(f"files_scanned={len(per_file)}\n")
                fh.write(f"report_path={str(report_path)}\n")
                fh.write(f"telemetry={str(telemetry_path)}\n")

        # Console summary
        print(json.dumps(report["summary"], indent=2))
        if failed:
            sys.exit(1)
        PY
