#!/usr/bin/env python3
"""Derive review inventories from one immutable Git commit, never the worktree.

This is a repository-tooling report generator under Directory Rules/ADR-0029,
not a new registry, validator, deletion decision, or publication surface. Every
path remains HOLD pending authority, consumer, rights, and unique-content review.
Root metadata is an explicitly inherited projection, not per-file conformance.

Only fixed, read-only Git commands run. Git objects are hashed in full; symlink
blobs are inventoried without following their targets. No network, submodule,
filter, import, template, or repository-provided executable is invoked. Text
analysis is bounded and heuristic; commands are represented by line/digest,
URLs lose credentials/query strings, and no source payload bodies are emitted.

An absent --output prints summary JSON (dry run). --output must be a new
directory outside the checkout and Git metadata; existing paths are refused.
The output directory is private, and failed writes may leave a partial report
without manifest.json. Existing files are never overwritten. The manifest is
written last and binds every other report file. No concurrent hostile ancestor
replacement protection is claimed for the caller-selected output parent.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import posixpath
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit


VERSION = "1"
REGISTRY = "control_plane/root_registry.yaml"
FAMILIES = (
    "SourceDescriptor", "EvidenceRef", "EvidenceBundle", "LayerManifest",
    "LayerFrame", "PolicyDecision", "RunReceipt", "ProofPack", "ReleaseManifest",
    "CorrectionNotice", "RollbackCard", "MapRuntimePort",
)
FAMILY_RE = re.compile(r"\b(" + "|".join(FAMILIES) + r")\b")
LOCKS = {"pnpm-lock.yaml", "package-lock.json", "yarn.lock", "uv.lock", "poetry.lock"}
ROOT_SHAPED = {
    "apps", "packages", "contracts", "schemas", "policy", "docs", "data",
    "fixtures", "scripts", "runtime", "infra", "configs", "tests", "release",
}
HASH_RE = re.compile(r"(?<![a-zA-Z0-9])[0-9a-f]{7,40}(?![a-zA-Z0-9])")
HEAD_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
META_RE = re.compile(r"^(doc_id|title|status|owning_root|responsibility):[ \t]*(.+)$", re.M)
URL_RE = re.compile(r"https?://[^\s<>\"'`\]\[{}]+")
LINK_RE = re.compile(r"\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:[^\n)]*)\)")
REF_RE = re.compile(r"^\s*\[[^\]\n]+\]:\s*(<[^>]+>|\S+)", re.M)
HTML_LINK_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']")
ANCHOR_RE = re.compile(r"\b(?:id|name)=[\"']([^\"']+)[\"']")
IMPORT_RE = re.compile(r"(?:\bfrom\s+|\bimport\s*\(?|\brequire\s*\()\s*['\"]([^'\"]+)['\"]")


class InventoryError(ValueError):
    """Bounded inspection or safe report creation was not possible."""


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def normalized(value: str) -> str:
    """Normalize only CRLF/trailing whitespace and final blank lines."""
    return "\n".join(line.rstrip() for line in value.splitlines()).strip("\n") + "\n"


def git_env() -> dict[str, str]:
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_NO_LAZY_FETCH="1", GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    return env


def git_argv(repo: Path, *args: str) -> list[str]:
    return ["git", "--no-replace-objects", "--no-lazy-fetch", "-c", "protocol.allow=never", "-C", str(repo), *args]


def git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(git_argv(repo, *args), env=git_env(), capture_output=True, timeout=180)
    if result.returncode:
        raise InventoryError(f"read-only git {args[0]} failed (exit {result.returncode})")
    return result.stdout


def read_tree(repo: Path, commit: str) -> list[dict]:
    rows = []
    for record in git(repo, "ls-tree", "-r", "-z", "-l", "--full-tree", commit, "--").split(b"\0"):
        if not record:
            continue
        metadata, path = record.split(b"\t", 1)
        mode, kind, oid, size = metadata.split()
        rows.append({"path": path.decode("utf-8", "surrogateescape"), "git_mode": mode.decode(),
                     "git_kind": kind.decode(), "git_oid": oid.decode(),
                     "byte_size": None if size == b"-" else int(size)})
    return rows


def read_blobs(repo: Path, rows: list[dict], text_limit: int) -> dict[str, dict]:
    unique = {row["git_oid"]: row for row in rows if row["git_kind"] == "blob"}
    if len(rows) > 100_000 or sum(row["byte_size"] for row in unique.values()) > 2_000_000_000:
        raise InventoryError("tree exceeds 100,000 paths or 2 GB of unique blob bytes")
    result = {}
    with subprocess.Popen(git_argv(repo, "cat-file", "--batch"), env=git_env(),
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as proc:
        assert proc.stdin and proc.stdout
        for oid, row in sorted(unique.items()):
            proc.stdin.write((oid + "\n").encode("ascii"))
            proc.stdin.flush()
            header = proc.stdout.readline().split()
            if header != [oid.encode(), b"blob", str(row["byte_size"]).encode()]:
                raise InventoryError("Git blob header differs from pinned tree")
            hasher = hashlib.sha256()
            git_hasher = hashlib.new("sha1" if len(oid) == 40 else "sha256")
            git_hasher.update(f"blob {row['byte_size']}\0".encode())
            remaining = row["byte_size"]
            captured = bytearray()
            while remaining:
                chunk = proc.stdout.read(min(remaining, 1024 * 1024))
                if not chunk:
                    raise InventoryError("Git blob ended before declared size")
                hasher.update(chunk)
                git_hasher.update(chunk)
                if row["byte_size"] <= text_limit:
                    captured.extend(chunk)
                remaining -= len(chunk)
            if proc.stdout.read(1) != b"\n":
                raise InventoryError("Git blob terminator missing")
            if git_hasher.hexdigest() != oid:
                raise InventoryError("Git object bytes do not match pinned blob identity")
            text = None
            state = "size_limit" if row["byte_size"] > text_limit else "binary_or_non_utf8"
            if row["byte_size"] <= text_limit and b"\0" not in captured:
                try:
                    text = captured.decode("utf-8")
                    state = "complete_utf8"
                except UnicodeDecodeError:
                    pass
            result[oid] = {"sha256": hasher.hexdigest(), "text": text, "text_analysis": state}
        proc.stdin.close()
        if proc.wait(timeout=30):
            raise InventoryError("Git cat-file failed")
    return result


def last_touches(repo: Path, commit: str, limit: int) -> tuple[dict[str, str], int]:
    observed, current, count, expect_path = {}, None, 0, False
    data = git(repo, "log", "--first-parent", "-m", f"--max-count={limit}",
               "--format=%x00COMMIT:%H%x00", "--raw", "--no-renames", "-z", commit, "--")
    for token in data.split(b"\0"):
        if expect_path:
            observed.setdefault(token.decode("utf-8", "surrogateescape"), current)
            expect_path = False
            continue
        token = token.lstrip(b"\n")
        if token.startswith(b"COMMIT:"):
            current = token[7:].decode("ascii")
            count += 1
        elif token.startswith(b":") and current:
            expect_path = True
    return observed, count


def safe_url(value: str) -> str:
    try:
        parsed = urlsplit(value)
        host = parsed.hostname or ""
        port = f":{parsed.port}" if parsed.port else ""
        return urlunsplit((parsed.scheme, host + port, parsed.path, "", ""))
    except ValueError:
        return "INVALID_URL_REDACTED"


def anchor_slug(value: str) -> str:
    value = re.sub(r"<[^>]*>", "", value).lower()
    return re.sub(r"[^\w\- ]", "", value).replace(" ", "-")


def markdown(path: str, value: str) -> dict:
    block = re.search(r"\[KFM_META_BLOCK_V2\](.*?)\[/KFM_META_BLOCK_V2\]", value[:32000], re.S)
    if block:
        metadata_text = block[1]
    else:
        frontmatter = re.match(r"\A---\s*\n(.*?)\n---", value[:32000], re.S)
        metadata_text = frontmatter[1] if frontmatter else ""
    declarations = dict(META_RE.findall(metadata_text))
    # Mask fenced examples while preserving source offsets and line numbers.
    structural = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$",
                        lambda match: re.sub(r"[^\n]", " ", match[0]), value, flags=re.M | re.S)
    headings, anchors, seen = [], [], Counter()
    for found in HEAD_RE.finditer(structural):
        slug = anchor_slug(found[2])
        anchor = f"{slug}-{seen[slug]}" if seen[slug] else slug
        seen[slug] += 1
        anchors.append(anchor)
        headings.append({"level": len(found[1]), "title": found[2], "anchor_candidate": anchor,
                         "line": value.count("\n", 0, found.start()) + 1, "offset": found.start()})
    anchors.extend(ANCHOR_RE.findall(structural))
    sections = []
    boundaries = [0] + [heading["offset"] for heading in headings if heading["offset"] > 0] + [len(value)]
    for start, end in zip(boundaries, boundaries[1:]):
        section = normalized(value[start:end])
        if section.strip():
            sections.append({"start_line": value.count("\n", 0, start) + 1,
                             "sha256_normalized": digest(section.encode()), "characters": len(section)})
    commands = []
    for block in re.finditer(r"^```(?:bash|sh|shell|console|powershell)\s*\n(.*?)^```", value, re.M | re.S):
        commands.append({"start_line": value.count("\n", 0, block.start()) + 1,
                         "sha256": digest(block[1].encode()), "line_count": len(block[1].splitlines())})
    return {"path": path, "title": declarations.get("title", headings[0]["title"] if headings else None),
            "declared": declarations, "headings": [{k: v for k, v in row.items() if k != "offset"} for row in headings],
            "anchors_heuristic": sorted(set(anchors)), "sections": sections, "command_blocks": commands,
            "heading_signature": digest("\n".join(h["title"].lower() for h in headings).encode()) if headings else None}


def resolve_link(source: str, value: str, paths: set[str]) -> tuple[str | None, str]:
    decoded = unquote(value.strip("<>"))
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", decoded) or decoded.startswith("//"):
        return None, "external_or_scheme"
    target, _, anchor = decoded.partition("#")
    target = target.split("?", 1)[0]
    target = posixpath.normpath(posixpath.join(posixpath.dirname(source), target)) if target else source
    if target in paths:
        return target, anchor
    # Root-relative project links and directory README targets are candidates.
    rooted = decoded.split("#", 1)[0].lstrip("/").rstrip("/")
    for candidate in (rooted, f"{target}/README.md", f"{rooted}/README.md"):
        if candidate in paths:
            return candidate, anchor
    return None, "unresolved"


def clusters(rows: list[dict], field: str) -> list[dict]:
    groups = defaultdict(list)
    for row in rows:
        if row.get(field):
            groups[row[field]].append(row["path"])
    return [{"digest": key, "paths": sorted(paths), "deletion_authorized": False}
            for key, paths in sorted(groups.items()) if len(paths) > 1]


def strict_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InventoryError("root registry contains a duplicate JSON key")
        result[key] = value
    return result


def build_inventory(repo: Path, commit: str, *, history_limit: int = 5000,
                    text_limit: int = 2_000_000) -> dict:
    repo = repo.resolve()
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise InventoryError("--commit requires a full immutable lowercase Git commit ID")
    if not 1 <= history_limit <= 50_000 or not 1 <= text_limit <= 16_000_000:
        raise InventoryError("history/text analysis limits outside supported bounds")
    if git(repo, "cat-file", "-t", commit).strip() != b"commit":
        raise InventoryError("input must identify a commit, not a tree or mutable ref")
    tree = git(repo, "rev-parse", f"{commit}^{{tree}}").decode().strip()
    rows = read_tree(repo, commit)
    blobs = read_blobs(repo, rows, text_limit)
    path_rows = {row["path"]: row for row in rows}
    paths = set(path_rows)
    reg_row = path_rows.get(REGISTRY)
    if reg_row is None or reg_row["git_mode"] not in {"100644", "100755"}:
        raise InventoryError("root registry missing or not a regular Git blob")
    try:
        registry = json.loads(blobs[reg_row["git_oid"]]["text"], object_pairs_hook=strict_object)
        roots = {root["path"]: {**registry.get("entry_defaults", {}),
                               **registry.get("class_defaults", {}).get(root["class"], {}), **root} for root in registry["roots"]}
        if len(roots) != len(registry["roots"]):
            raise InventoryError("root registry contains duplicate root paths")
    except (ValueError, TypeError, KeyError) as exc:
        raise InventoryError("root registry requires current JSON-compatible YAML projection") from exc
    touches, history_count = last_touches(repo, commit, history_limit)
    documents, references, families, anomalies, packages, pins = [], [], [], [], [], []
    literal_re = re.compile(r"(?<![\w/-])(?:" + "|".join(re.escape(root) for root in roots) + r")[^\s`'\"<>\[\](){},;:]+")
    text_paths = {}
    for row in rows:
        path = row["path"]
        root = path.split("/", 1)[0] + "/" if "/" in path else "(root file)"
        authority = roots.get(root, {})
        blob = blobs.get(row["git_oid"], {})
        regular = row["git_mode"] in {"100644", "100755"}
        value = blob.get("text") if regular else None
        row.update(root=root, root_class=authority.get("class", "UNKNOWN"),
                   root_id=authority.get("root_id"), owner=authority.get("owner", "UNKNOWN"),
                   exposure_inherited=authority.get("exposure", "UNKNOWN"),
                   mutability_inherited=authority.get("mutation", "UNKNOWN"),
                   retention_inherited=authority.get("retention", "UNKNOWN"),
                   responsibility_inherited=authority.get("responsibility", "UNKNOWN"),
                   root_metadata_evidence=f"{commit}:{REGISTRY}#{root}" if authority else None,
                   per_file_authority_review="NEEDS_VERIFICATION", classification="HOLD",
                   classification_reason="PER_FILE_AUTHORITY_CONSUMER_AND_NO_LOSS_REVIEW_REQUIRED",
                   proposed_target=None, unique_content_disposition="PRESERVE_ALL_SOURCE_BYTES",
                   validation="IMMUTABLE_BLOB_IDENTITY_AND_SHA256_ONLY" if row["git_kind"] == "blob" else "GITLINK_IDENTITY_ONLY",
                   rollback=f"recover original object from {commit}:{path}",
                   authority_required="PER_FILE_OWNER_REVIEW_AND_APPLICABLE_MIGRATION_AUTHORITY",
                   sha256=blob.get("sha256"), type=PurePosixPath(path).suffix.lower() or "extensionless",
                   generation_status="UNKNOWN", text_analysis=blob.get("text_analysis", "gitlink_not_read") if regular else "nonregular_not_analyzed",
                   sha256_normalized=digest(normalized(value).encode()) if value is not None else None,
                   last_touch_first_parent=touches.get(path), last_meaningful_change="UNKNOWN")
        flags = []
        if not authority:
            flags.append("ROOT_FILE_REVIEW" if root == "(root file)" else "UNREGISTERED_ROOT")
        if authority.get("class") in {"deprecated", "compatibility", "conditional", "retired"}:
            flags.append("AUTHORITY_TRANSITION_HOLD")
        if not regular:
            flags.append("SYMLINK_NOT_FOLLOWED" if row["git_mode"] == "120000" else "GITLINK_NOT_FETCHED")
        parts = PurePosixPath(path).parts
        if any(part in ROOT_SHAPED for part in parts[1:-1]):
            flags.append("NESTED_RESPONSIBILITY_NAME_REVIEW")
        if any(part in {"node_modules", "__pycache__", ".cache", ".venv", "dist", "build", ".next"} for part in parts[:-1]):
            flags.append("CACHE_OR_BUILD_NAME_REVIEW")
        if any(part.lower() in {"vendor", "vendored", "third_party"} for part in parts):
            flags.append("VENDORED_NAME_REVIEW")
        if parts[-1] in {".gitkeep", ".keep", ".gitignore"} and row["byte_size"] == 0:
            flags.append("EMPTY_DIRECTORY_SURROGATE_CANDIDATE")
        if row["byte_size"] == 0:
            flags.append("EMPTY_BLOB")
        if parts[-1] in LOCKS:
            flags.append("LOCKFILE_SCOPE_REVIEW")
        if value is not None:
            text_paths[path] = value
            intro = value[:12000]
            if re.search(r"(?i)(?:do not edit|automatically generated|@generated)", intro):
                row["generation_status"] = "GENERATED_MARKER_REQUIRES_PRODUCER_REVIEW"
                flags.append("GENERATED_MARKER")
            if re.search(r"(?i)\b(?:tombstone|redirect|compatibility)\b", intro):
                flags.append("COMPATIBILITY_TEXT_REVIEW")
            if re.search(r"(?i)\b(?:placeholder|TODO|stub)\b", intro):
                flags.append("PLACEHOLDER_TEXT_REVIEW")
            if path.lower().endswith((".md", ".markdown", ".mdx")):
                documents.append(markdown(path, value))
                for match in HASH_RE.finditer(value):
                    token = match[0]
                    pins.append({"path": path, "line": value.count("\n", 0, match.start()) + 1,
                                 "token": token, "state": "MATCHES_BASE_PREFIX" if commit.startswith(token) else "NON_BASE_HEX_CANDIDATE_NOT_PROVEN_STALE"})
            for family, count in sorted(Counter(FAMILY_RE.findall(value)).items()):
                families.append({"path": path, "family": family, "literal_occurrences": count, "root": root})
            if parts[-1] == "package.json":
                try:
                    package = json.loads(value)
                    packages.append({"path": path, "name": package.get("name"), "version": package.get("version"),
                                     "dependencies": {kind: sorted(package.get(kind, {})) for kind in ("dependencies", "devDependencies", "peerDependencies")},
                                     "scripts": {name: digest(command.encode()) for name, command in package.get("scripts", {}).items() if isinstance(command, str)}})
                except (ValueError, AttributeError):
                    flags.append("PACKAGE_JSON_PARSE_ERROR")
        row["review_flags"] = sorted(flags)
        anomalies.extend({"path": path, "finding": flag, "classification": "HOLD"} for flag in sorted(flags))
    docs_by_path = {doc["path"]: doc for doc in documents}
    for source, value in sorted(text_paths.items()):
        occurrences = []
        for found in literal_re.finditer(value):
            target = found[0].rstrip(".#/")
            target = target.split("#", 1)[0]
            if target in paths and target != source:
                occurrences.append((found.start(), "literal_tracked_path", target, ""))
        if source in docs_by_path:
            for pattern in (LINK_RE, REF_RE, HTML_LINK_RE):
                for found in pattern.finditer(value):
                    target, anchor = resolve_link(source, found[1], paths)
                    kind = "markdown_link_candidate"
                    if target:
                        anchor_state = "not_requested" if not anchor else "NEEDS_VERIFICATION"
                        if anchor and target in docs_by_path:
                            anchor_state = "heuristic_match" if anchor in docs_by_path[target]["anchors_heuristic"] else "heuristic_missing"
                        occurrences.append((found.start(), kind, target, anchor_state))
                    elif anchor == "unresolved":
                        # Hash unresolved text instead of exposing arbitrary embedded values.
                        occurrences.append((found.start(), "unresolved_markdown_link_digest", digest(found[1].encode()), "NEEDS_VERIFICATION"))
        for found in IMPORT_RE.finditer(value):
            specifier = found[1]
            if specifier.startswith("."):
                stem = posixpath.normpath(posixpath.join(posixpath.dirname(source), specifier))
                for suffix in ("", ".ts", ".tsx", ".js", ".jsx", ".py", "/index.ts", "/index.tsx", "/__init__.py"):
                    if stem + suffix in paths:
                        occurrences.append((found.start(), "relative_import_candidate", stem + suffix, "NEEDS_VERIFICATION"))
            else:
                occurrences.append((found.start(), "module_specifier", specifier, "external_or_alias_unresolved"))
        for found in URL_RE.finditer(value):
            occurrences.append((found.start(), "external_url_redacted", safe_url(found[0]), "not_fetched"))
        for offset, kind, target, status in sorted(set(occurrences)):
            references.append({"source": source, "line": value.count("\n", 0, offset) + 1,
                               "kind": kind, "target": target, "status": status})
    incoming = Counter(ref["target"] for ref in references if ref["target"] in paths)
    outgoing = Counter(ref["source"] for ref in references)
    section_owners = defaultdict(set)
    for doc in documents:
        for section in doc["sections"]:
            section_owners[section["sha256_normalized"]].add(doc["path"])
    ledger = []
    for doc in documents:
        for section in doc["sections"]:
            section["document_count_with_exact_normalized_section"] = len(section_owners[section["sha256_normalized"]])
        doc["inbound_reference_occurrences"] = incoming[doc["path"]]
        doc["outbound_reference_occurrences"] = outgoing[doc["path"]]
        unique = sum(section["document_count_with_exact_normalized_section"] == 1 for section in doc["sections"])
        doc["byte_distinct_section_count"] = unique
        ledger.append({"path": doc["path"], "classification": "HOLD", "canonical_target": None,
                       "byte_distinct_section_count": unique, "unique_knowledge_review": "NOT_PERFORMED",
                       "affected_reference_occurrences": incoming[doc["path"]], "consumer_closure": "UNKNOWN",
                       "unique_content_disposition": "PRESERVE_ALL_SOURCE_BYTES", "validation": "IMMUTABLE_BLOB_HASH_ONLY",
                       "rollback": f"recover original bytes from {commit}:{doc['path']}",
                       "authority_required": "PER_FILE_OWNER_REVIEW_AND_APPLICABLE_MIGRATION_AUTHORITY",
                       "deletion_authorized": False})
    for row in rows:
        row["observed_reference_occurrences"] = incoming[row["path"]]
        row["consumer_closure"] = "UNKNOWN"
    root_counts = Counter(row["root"] for row in rows)
    root_summary = [{"path": root, "tracked_files": count, "registered": root in roots,
                     "kind": "directory", "projection": roots.get(root), "classification": "HOLD"}
                    for root, count in sorted(root_counts.items()) if root != "(root file)"]
    root_summary.extend({"path": row["path"], "tracked_files": 1, "registered": False,
                         "kind": "root_file", "projection": None, "classification": "HOLD"}
                        for row in rows if row["root"] == "(root file)")
    root_summary.sort(key=lambda row: row["path"])
    duplicates = {"exact_bytes": clusters(rows, "sha256"), "normalized_text": clusters(rows, "sha256_normalized"),
                  "heading_structure_review_aid": clusters(documents, "heading_signature")}
    duplicate_ids = defaultdict(list)
    for doc in documents:
        if doc["declared"].get("doc_id"):
            duplicate_ids[doc["declared"]["doc_id"]].append(doc["path"])
    duplicates["declared_document_ids"] = [{"doc_id": key, "paths": sorted(value)} for key, value in sorted(duplicate_ids.items()) if len(value) > 1]
    duplicate_packages = defaultdict(list)
    for package in packages:
        if package["name"]:
            duplicate_packages[package["name"]].append(package["path"])
    duplicates["package_names"] = [{"name": name, "paths": sorted(value)} for name, value in sorted(duplicate_packages.items()) if len(value) > 1]
    codeowners_rules = []
    for line, value in enumerate(text_paths.get(".github/CODEOWNERS", "").splitlines(), 1):
        tokens = value.split()
        if tokens and not tokens[0].startswith("#"):
            codeowners_rules.append({"source": ".github/CODEOWNERS", "line": line, "pattern": tokens[0],
                                     "declared_review_routes": tokens[1:], "glob_resolution": "NOT_PERFORMED",
                                     "independent_stewardship": "NOT_PROVEN"})
    summary = {"report_version": VERSION, "authority": "NON_AUTHORITATIVE_REVIEW_INVENTORY", "commit": commit,
               "tree": tree, "root_registry_blob": reg_row["git_oid"], "root_registry_sha256": blobs[reg_row["git_oid"]]["sha256"],
               "counts": {"tracked_paths": len(rows), "markdown_documents": len(documents), "reference_occurrences": len(references),
                          "object_family_path_pairs": len(families), "HOLD": len(rows), "deletion_authorized": 0,
                          "exact_duplicate_clusters": len(duplicates["exact_bytes"]), "normalized_duplicate_clusters": len(duplicates["normalized_text"]),
                          "heading_structure_clusters": len(duplicates["heading_structure_review_aid"]), "anomalies_for_review": len(anomalies)},
               "history": {"method": "first_parent_last_touch_no_rename_following", "limit": history_limit,
                           "commits_examined": history_count, "paths_with_touch": len([r for r in rows if r["last_touch_first_parent"]]),
                           "shallow": git(repo, "rev-parse", "--is-shallow-repository").strip() == b"true"},
               "text_analysis_max_bytes": text_limit, "text_analysis_states": dict(sorted(Counter(r["text_analysis"] for r in rows).items())),
               "limitations": ["Root ownership/exposure/mutation/retention are inherited metadata, not per-file conformance or rights decisions.",
                               "All paths remain HOLD. No files moved, merged, deleted, admitted, deployed or published.",
                               "Markdown parsing, anchors, local imports, literal consumers and hex pins are heuristic review aids; no zero-consumer proof.",
                               "Section uniqueness measures normalized bytes, not unique knowledge; structural similarity never authorizes deletion.",
                               "Last-touch traversal is bounded first-parent history, not last meaningful change, review acceptance or source authorship.",
                               "Binary, non-UTF8, symlink, submodule and oversized text content is not interpreted; hashes cover full blob bytes.",
                               "External consumers, generated dynamic imports, CODEOWNERS glob resolution, Python module graphs, semantic similarity, source rights and secret scanning remain unverified.",
                               "Tracked metadata may be sensitive; report is private review material and contains no source payload bodies."]}
    return {"summary": summary, "paths": rows, "roots": root_summary, "markdown": documents, "references": references,
            "duplicates": duplicates, "no_loss_ledger": ledger, "object_families": families, "anomalies": anomalies,
            "packages": packages, "pin_candidates": pins, "codeowners_rules": codeowners_rules}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")) + "\n").encode()


def write_reports(report: dict, output: Path, repo: Path) -> dict:
    output = output.absolute()
    resolved = output.resolve()
    worktree_root = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    git_dir = Path(git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip()).resolve()
    if resolved.is_relative_to(worktree_root) or resolved.is_relative_to(git_dir):
        raise InventoryError("report output must be outside repository and Git metadata")
    if output.exists() or output.is_symlink():
        raise InventoryError("output path already exists; overwrite denied")
    if not output.parent.is_dir() or output.parent.is_symlink() or output.parent.resolve() != output.parent:
        raise InventoryError("output requires an existing parent without symlink ancestors")
    output.mkdir(mode=0o700)
    manifest = {"authority": "NON_AUTHORITATIVE_REVIEW_INVENTORY", "commit": report["summary"]["commit"], "files": {}}

    def put(name: str, payload: bytes) -> None:
        with (output / name).open("xb") as handle:
            handle.write(payload)
        manifest["files"][name] = {"sha256": digest(payload), "byte_size": len(payload)}

    for key, value in report.items():
        put(f"{key}.json", json_bytes(value))
    csv_buffer = io.StringIO(newline="")
    columns = list(report["paths"][0]) if report["paths"] else ["path"]
    writer = csv.DictWriter(csv_buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in report["paths"]:
        # Neutralize spreadsheet formulas without changing the authoritative JSON.
        safe = {key: json.dumps(value, ensure_ascii=True) if isinstance(value, (list, dict)) else value for key, value in row.items()}
        safe = {key: "'" + value if isinstance(value, str) and value[:1] in ("=", "+", "-", "@", "\t", "\r") else value for key, value in safe.items()}
        writer.writerow(safe)
    put("paths.csv", csv_buffer.getvalue().encode("utf-8", "backslashreplace"))
    summary = report["summary"]
    lines = ["# Repository convergence review inventory", "", "HOLD: generated inspection report; no mutation or deletion authority.", "",
             f"Commit: `{summary['commit']}`", f"Tree: `{summary['tree']}`", "", "| Observation | Count |", "|---|---:|"]
    lines.extend(f"| {key} | {value} |" for key, value in summary["counts"].items())
    lines.extend(["", "Every tracked path is classified HOLD. Registry metadata remains separate from per-file acceptance.", "",
                  "Machine reports include paths, roots, Markdown graph and section hashes, hash clusters, object-family occurrences,",
                  "package metadata, no-loss ledger, anomaly candidates and non-base hex candidates. Commands are line/digest references.", ""])
    lines.extend("- " + item for item in summary["limitations"])
    put("summary.md", ("\n".join(lines) + "\n").encode())
    # Completion marker is intentionally last and does not contain its own hash.
    with (output / "manifest.json").open("xb") as handle:
        handle.write(json_bytes(manifest))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--history-limit", type=int, default=5000)
    parser.add_argument("--text-limit", type=int, default=2_000_000)
    args = parser.parse_args()
    try:
        report = build_inventory(args.repo, args.commit, history_limit=args.history_limit, text_limit=args.text_limit)
        if args.output:
            write_reports(report, args.output, args.repo)
        print(json.dumps(report["summary"], sort_keys=True))
        return 0
    except (InventoryError, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
