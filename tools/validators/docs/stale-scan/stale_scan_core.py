from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


PROFILE_ID = "kfm.docs.stale-scan.v1"
OUTCOME_PASS = "DOC_STALE_SCAN_PASS"
OUTCOME_WARN = "DOC_STALE_SCAN_WARN"
OUTCOME_FAIL = "DOC_STALE_SCAN_FAIL"
OUTCOME_ERROR = "ERROR"

SEVERITY_ORDER = {"info": 0, "warn": 1, "fail": 2}


class StaleScanError(RuntimeError):
    """Raised when the bounded scan cannot complete safely."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    severity: str
    path: str
    message: str
    current: bool = True
    historical: bool = False

    def __post_init__(self) -> None:
        if self.severity not in SEVERITY_ORDER:
            raise ValueError(f"unsupported severity: {self.severity}")

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "severity": self.severity,
            "path": self.path,
            "message": self.message,
            "current": self.current,
            "historical": self.historical,
        }


@dataclass(frozen=True)
class StaleScanResult:
    profile: str
    as_of: str
    review_window_days: int
    placeholder_grace_days: int
    counts: Mapping[str, int]
    documents: tuple[Mapping[str, Any], ...]
    findings: tuple[Finding, ...]
    report_digest: str
    outcome: str
    exit_code: int
    limitations: tuple[str, ...]

    def payload(self, *, include_digest: bool = True) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "profile": PROFILE_ID,
            "scan_profile": self.profile,
            "as_of": self.as_of,
            "review_window_days": self.review_window_days,
            "placeholder_grace_days": self.placeholder_grace_days,
            "outcome": self.outcome,
            "exit_code": self.exit_code,
            "counts": dict(sorted(self.counts.items())),
            "documents": [dict(item) for item in self.documents],
            "findings": [item.to_dict() for item in self.findings],
            "limitations": list(self.limitations),
        }
        if include_digest:
            payload["report_digest"] = self.report_digest
        return payload

    def to_json(self) -> str:
        return canonical_json(self.payload())

    def to_text(self) -> str:
        lines = [
            f"{self.outcome} ({self.exit_code})",
            f"profile={self.profile}",
            f"as_of={self.as_of}",
            f"documents={self.counts.get('documents', 0)}",
            f"findings={self.counts.get('findings', 0)}",
            f"report_digest={self.report_digest}",
        ]
        for finding in self.findings:
            scope = "current" if finding.current else "historical"
            lines.append(
                f"{finding.severity.upper()} {finding.code} {finding.path} "
                f"[{scope}] {finding.message}"
            )
        return "\n".join(lines)

    def to_markdown(self) -> str:
        lines = [
            "# KFM Documentation Freshness Workbench",
            "",
            "> This report is a deterministic QA projection. It is not doctrine,",
            "> evidence, source admission, policy approval, human review, release,",
            "> publication, correction, or proof that a document is materially current.",
            "",
            "## Summary",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| Outcome | `{self.outcome}` |",
            f"| Exit code | `{self.exit_code}` |",
            f"| Scan profile | `{self.profile}` |",
            f"| As of | `{self.as_of}` |",
            f"| Review window | `{self.review_window_days}` days |",
            f"| Placeholder grace | `{self.placeholder_grace_days}` days |",
            f"| Documents | `{self.counts.get('documents', 0)}` |",
            f"| Documents with metadata | `{self.counts.get('documents_with_metadata', 0)}` |",
            f"| Current findings | `{self.counts.get('current_findings', 0)}` |",
            f"| Historical findings | `{self.counts.get('historical_findings', 0)}` |",
            f"| Report digest | `{self.report_digest}` |",
            "",
            "## Findings",
            "",
        ]
        if not self.findings:
            lines.append("No configured freshness finding was emitted.")
        else:
            lines.extend(
                [
                    "| Severity | Code | Path | Scope | Message |",
                    "|---|---|---|---|---|",
                ]
            )
            for finding in self.findings:
                scope = "current" if finding.current else "historical"
                message = finding.message.replace("|", "\\|")
                lines.append(
                    f"| `{finding.severity}` | `{finding.code}` | "
                    f"`{finding.path}` | `{scope}` | {message} |"
                )
        lines.extend(["", "## Document review index", ""])
        if not self.documents:
            lines.append("No document entered the bounded scan.")
        else:
            lines.extend(
                [
                    "| Path | Review date | Age | Window | Owner placeholder | Current |",
                    "|---|---|---:|---:|---|---|",
                ]
            )
            for item in self.documents:
                review_date = item.get("review_date") or "—"
                age = item.get("age_days")
                age_text = "—" if age is None else str(age)
                window = item.get("review_window_days")
                lines.append(
                    f"| `{item['path']}` | `{review_date}` | {age_text} | "
                    f"{window} | `{str(item.get('owner_placeholder', False)).lower()}` | "
                    f"`{str(item.get('current', True)).lower()}` |"
                )
        lines.extend(["", "## Limits", ""])
        for limitation in self.limitations:
            lines.append(f"- {limitation}")
        return "\n".join(lines)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def result_from_parts(
    *,
    profile: str,
    as_of: str,
    review_window_days: int,
    placeholder_grace_days: int,
    documents: Iterable[Mapping[str, Any]],
    findings: Iterable[Finding],
    warnings_as_errors: bool,
    limitations: Sequence[str],
) -> StaleScanResult:
    ordered_documents = tuple(sorted((dict(item) for item in documents), key=lambda x: x["path"]))
    ordered_findings = tuple(
        sorted(
            findings,
            key=lambda item: (
                -SEVERITY_ORDER[item.severity],
                item.path,
                item.code,
                item.message,
            ),
        )
    )
    fail_count = sum(item.severity == "fail" for item in ordered_findings)
    warn_count = sum(item.severity == "warn" for item in ordered_findings)
    if fail_count:
        outcome, exit_code = OUTCOME_FAIL, 1
    elif warn_count:
        outcome, exit_code = OUTCOME_WARN, 0
    else:
        outcome, exit_code = OUTCOME_PASS, 0
    counts = {
        "documents": len(ordered_documents),
        "documents_with_metadata": sum(bool(item.get("has_metadata")) for item in ordered_documents),
        "documents_without_metadata": sum(not bool(item.get("has_metadata")) for item in ordered_documents),
        "findings": len(ordered_findings),
        "current_findings": sum(item.current for item in ordered_findings),
        "historical_findings": sum(item.historical for item in ordered_findings),
        "fail_findings": fail_count,
        "warn_findings": warn_count,
        "info_findings": sum(item.severity == "info" for item in ordered_findings),
        "warnings_as_errors": int(warnings_as_errors),
    }
    digest_material = {
        "profile": PROFILE_ID,
        "scan_profile": profile,
        "as_of": as_of,
        "review_window_days": review_window_days,
        "placeholder_grace_days": placeholder_grace_days,
        "counts": counts,
        "documents": ordered_documents,
        "findings": [item.to_dict() for item in ordered_findings],
        "limitations": list(limitations),
    }
    return StaleScanResult(
        profile=profile,
        as_of=as_of,
        review_window_days=review_window_days,
        placeholder_grace_days=placeholder_grace_days,
        counts=counts,
        documents=ordered_documents,
        findings=ordered_findings,
        report_digest=sha256_digest(digest_material),
        outcome=outcome,
        exit_code=exit_code,
        limitations=tuple(limitations),
    )


def error_result(*, as_of: str, profile: str, message: str) -> StaleScanResult:
    limitation = "The scan stopped before a complete bounded result could be produced."
    finding = Finding("SCAN_ERROR", "fail", "<scan>", message)
    result = result_from_parts(
        profile=profile,
        as_of=as_of,
        review_window_days=0,
        placeholder_grace_days=0,
        documents=(),
        findings=(finding,),
        warnings_as_errors=False,
        limitations=(limitation,),
    )
    return replace(result, outcome=OUTCOME_ERROR, exit_code=2)


def changed_paths_from_git(repo_root: Path, range_spec: str) -> set[str]:
    try:
        completed = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACMR", range_spec],
            cwd=repo_root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError, UnicodeError) as exc:
        raise StaleScanError("git changed-path scope could not be resolved") from exc
    return {
        line.strip().replace("\\", "/")
        for line in completed.stdout.splitlines()
        if line.strip()
    }


def ratchet_findings(
    findings: Iterable[Finding],
    *,
    changed_paths: set[str] | None,
    warnings_as_errors: bool,
) -> tuple[Finding, ...]:
    if changed_paths is None:
        ratcheted = [
            replace(item, severity="fail")
            if warnings_as_errors and item.severity == "warn"
            else item
            for item in findings
        ]
    else:
        ratcheted = []
        for finding in findings:
            current = finding.path in changed_paths or finding.path == "<scan>"
            if current:
                severity = finding.severity
                if warnings_as_errors and severity == "warn":
                    severity = "fail"
                ratcheted.append(
                    replace(
                        finding,
                        severity=severity,
                        current=True,
                        historical=False,
                    )
                )
                continue
            if finding.severity == "fail":
                ratcheted.append(
                    replace(
                        finding,
                        severity="warn",
                        current=False,
                        historical=True,
                        message="Historical finding: " + finding.message,
                    )
                )
            # Unchanged warnings and informational findings are intentionally omitted
            # from changed-file gates. Whole-repository scans retain them.
    return tuple(ratcheted)
