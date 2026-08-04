#!/usr/bin/env python3
"""Validate KFM MaterialChangeAssessment records without network access.

A passing result proves bounded shape and local consistency only. It does not
resolve evidence, evaluate policy, authorize promotion, release, or publish.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/data/material_change_assessment.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/material_change_assessment"
MAX_FILE_BYTES = 1_048_576
SCOPE = "material-change-assessment-shape-and-local-consistency-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    if not path.is_file():
        return None, [Finding("FILE_NOT_FOUND", "/")]
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: dict[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in validator.iter_errors(candidate)
    ]


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _is_zero_digest(value: Any) -> bool:
    return isinstance(value, str) and value == "sha256:" + ("0" * 64)


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def _semantic_findings(candidate: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    assessment_id = candidate.get("assessment_id")
    profile = _mapping(candidate.get("profile"))
    comparison = _mapping(candidate.get("comparison"))
    classification = _mapping(candidate.get("classification"))
    evidence = _mapping(candidate.get("evidence"))
    timing = _mapping(candidate.get("timing"))
    lineage = _mapping(candidate.get("lineage"))
    governance = _mapping(candidate.get("governance"))
    criteria = _array(candidate.get("criteria"))

    for field, value in (
        ("/profile/spec_hash", profile.get("spec_hash")),
        ("/comparison/baseline_digest", comparison.get("baseline_digest")),
        ("/comparison/candidate_digest", comparison.get("candidate_digest")),
        ("/governance/spec_hash", governance.get("spec_hash")),
    ):
        if _is_zero_digest(value):
            findings.append(Finding("DIGEST_PLACEHOLDER", field))

    baseline_digest = comparison.get("baseline_digest")
    candidate_digest = comparison.get("candidate_digest")
    byte_changed = comparison.get("byte_changed")
    semantic_changed = comparison.get("semantic_changed")
    if isinstance(baseline_digest, str) and isinstance(candidate_digest, str) and isinstance(byte_changed, bool):
        if byte_changed != (baseline_digest != candidate_digest):
            findings.append(Finding("BYTE_CHANGE_DIGEST_MISMATCH", "/comparison/byte_changed"))

    criterion_ids = [item.get("criterion_id") for item in criteria if isinstance(item, dict)]
    if (
        len(criterion_ids) != len(criteria)
        or not all(isinstance(item, str) for item in criterion_ids)
        or criterion_ids != sorted(criterion_ids)
        or len(criterion_ids) != len(set(criterion_ids))
    ):
        findings.append(Finding("CRITERIA_NOT_CANONICAL", "/criteria"))
    for index, item in enumerate(criteria):
        if not isinstance(item, dict):
            continue
        refs = _array(item.get("evidence_refs"))
        if not _sorted_unique_strings(refs):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/criteria/{index}/evidence_refs"))

    for field in ("validation_report_refs", "source_refs"):
        refs = _array(evidence.get(field))
        if not _sorteYİ[š\]YWÜİš[™ÜÊ™YœÊN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘Q”×Ó“ÕĞĞS“Ó’PĞS‹ˆ‹Ù]šY[˜ÙKŞÙšY[HŠJBˆ™X\ÛÛœÈHØ\œ˜^JÛ\ÜÚYšXØ][Û‹™Ù]
œ™X\ÛÛ—ØÛÙ\ÈŠBˆYˆ›İÜÛÜYİ[š\]YWÜİš[™ÜÊ™X\ÛÛœÊN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ”×Ó“ÕĞĞS“Ó’PĞS‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJB‚ˆÚ[™ÙWØÛ\ÜÈHÛ\ÜÚYšXØ][Û‹™Ù]
˜Ú[™ÙWØÛ\ÜÈŠBˆX]\šX[HÛ\ÜÚYšXØ][Û‹™Ù]
›X]\šX[ŠBˆİ]ÛÛYHHÛ\ÜÚYšXØ][Û‹™Ù]
›İ]ÛÛYHŠBˆ™\]Z\™YÜ™\İ[ÈHÚ][K™Ù]
œ™\İ[ŠH›Üˆ][H[ˆÜš]\šXHYˆ\Ú[œİ[˜ÙJ][KXİ
H[™][K™Ù]
œ™\]Z\™YŠH\ÈYWBˆ[Ü™\İ[ÈHÚ][K™Ù]
œ™\İ[ŠH›Üˆ][H[ˆÜš]\šXHYˆ\Ú[œİ[˜ÙJ][KXİ
WB‚ˆ^XİYHÂˆ•SÒS‘ÑQˆ
˜[ÙK““Ó—ÑU‘S•‹˜[ÙJKˆ–UWÓÓ“Hˆ
˜[ÙK““Ó—ÑU‘S•‹˜[ÙJKˆ”ÑSPS•P×Ó“Ó—ÓPUT’PSˆ
˜[ÙK““Ó—ÑU‘S•‹YJKˆ“PUT’PSˆ
YK”“ÓSÕSÓ—ĞĞS‘QUH‹YJKˆ•S‘UT“RS‘Qˆ
›Û™K’Ó‹›Û™JKˆ‘T”“Ôˆˆ
›Û™K‘T”“Ôˆ‹›Û™JKˆBˆYˆÚ[™ÙWØÛ\ÜÈ[ˆ^XİY‚ˆ^XİYÛX]\šX[^XİYÛİ]ÛÛYK^XİYÜÙ[X[XÈH^XİYØÚ[™ÙWØÛ\Ü×BˆYˆX]\šX[\È›İ^XİYÛX]\šX[‚ˆš[™[™ÜË˜\[™
š[™[™Ê“PUT’PSÔÕUWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹ÛX]\šX[ŠJBˆYˆİ]ÛÛYHOH^XİYÛİ]ÛÛYN‚ˆš[™[™ÜË˜\[™
š[™[™Ê“ÕUÓÓQWĞÓTÔ×ÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ûİ]ÛÛYHŠJBˆYˆ^XİYÜÙ[X[XÈ\È›İ›Û™H[™Ù[X[X×ØÚ[™ÙY\È›İ^XİYÜÙ[X[XÎ‚ˆš[™[™ÜË˜\[™
š[™[™Ê”ÑSPS•P×ÔÕUWÓRTÓPUÒ‹‹ØÛÛ\\š\ÛÛ‹ÜÙ[X[X×ØÚ[™ÙYŠJB‚ˆYˆÚ[™ÙWØÛ\ÜÈOH•SÒS‘ÑQ‚ˆYˆ]WØÚ[™ÙY\È›İ˜[ÙN‚ˆš[™[™ÜË˜\[™
š[™[™Ê•SÒS‘ÑQĞ–UT×ÓRTÓPUÒ‹‹ØÛÛ\\š\ÛÛ‹Ø]WØÚ[™ÙYŠJBˆYˆ““×Ğ–UWĞÒS‘ÑHˆ›İ[ˆ™X\ÛÛœÎ‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJBˆ[YˆÚ[™ÙWØÛ\ÜÈOH–UWÓÓ“H‚ˆYˆ]WØÚ[™ÙY\È›İYN‚ˆš[™[™ÜË˜\[™
š[™[™Ê–UWÓÓ“WĞ–UT×ÓRTÓPUÒ‹‹ØÛÛ\\š\ÛÛ‹Ø]WØÚ[™ÙYŠJBˆYˆ›İ
È–UWÓÓ“WĞÒS‘ÑH‹ĞS“Ó’PĞSÑTURUSS•ŸH	ˆÙ]
™X\ÛÛœÊJN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJBˆ[YˆÚ[™ÙWØÛ\ÜÈOH”ÑSPS•P×Ó“Ó—ÓPUT’PS‚ˆYˆ]WØÚ[™ÙY\È›İYHÜˆ‘RSˆ›İ[ˆ[Ü™\İ[Î‚ˆš[™[™ÜË˜\[™
š[™[™Ê““Ó—ÓPUT’PSĞÔ’UT’PWÓRTÓPUÒ‹‹ØÜš]\šXHŠJBˆYˆ‘SÕ×ÓPUT’PSUWÕ‘TÒÓˆ›İ[ˆ™X\ÛÛœÎ‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJBˆ[YˆÚ[™ÙWØÛ\ÜÈOH“PUT’PS‚ˆYˆ]WØÚ[™ÙY\È›İYHÜˆ›İÜš]\šXHÜˆ›İ™\]Z\™YÜ™\İ[ÈÜˆ[J™\İ[OH”TÔÈˆ›Üˆ™\İ[[ˆ™\]Z\™YÜ™\İ[ÊN‚ˆš[™[™ÜË˜\[™
š[™[™Ê“PUT’PSĞÔ’UT’PWÓ“ÕÔĞUTÑ’QQ‹‹ØÜš]\šXHŠJBˆYˆ›İ
È“PUT’PSUWÕ‘TÒÓÓQU‹‘ÓPRS—ÔÕUT×ĞÒS‘ÑHŸH	ˆÙ]
™X\ÛÛœÊJN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJBˆ[YˆÚ[™ÙWØÛ\ÜÈOH•S‘UT“RS‘Q‚ˆYˆ›İ
È“RTÔÒS‘×ĞTÑSS‘H‹”“Ñ’SWÕS”‘TÓÓ‘Q‹“QU’P×ÕSURSP“H‹’S”ÕQ‘’PÒQS•ÑU’QSÑHŸH	ˆÙ]
™X\ÛÛœÊJN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJBˆ[YˆÚ[™ÙWØÛ\ÜÈOH‘T”“Ôˆ‚ˆYˆ›İ
È’S”UÒS•SQ‹”“Ñ’SWÒS•SQ‹‘USPUSÓ—ÑT”“ÔˆŸH	ˆÙ]
™X\ÛÛœÊJN‚ˆš[™[™ÜË˜\[™
š[™[™Ê”‘PTÓÓ—ÑSRSWÓRTÓPUÒ‹‹ØÛ\ÜÚYšXØ][Û‹Ü™X\ÛÛ—ØÛÙ\ÈŠJB‚ˆ˜\Ù[[™Wİ[YHHÜ\œÙWİ[YJ[Z[™Ë™Ù]
˜˜\Ù[[™WØ\×ÛÙˆŠJBˆØ[™Y]Wİ[YHHÜ\œÙWİ[YJ[Z[™Ë™Ù]
˜Ø[™Y]WØ\×ÛÙˆŠJBˆ\ÜÙ\ÜÙYİ[YHHÜ\œÙWİ[YJ[Z[™Ë™Ù]
˜\ÜÙ\ÜÙYØ]ŠJBˆYˆ˜\Ù[[™Wİ[YH[™Ø[™Y]Wİ[YH[™˜\Ù[[™Wİ[YHˆØ[™Y]Wİ[YN‚ˆš[™[™ÜË˜\[™
š[™[™ÊTÑSS‘WĞQ•T—ĞĞS‘QUH‹‹İ[Z[™ËØ˜\Ù[[™WØ\×ÛÙˆŠJBˆYˆØ[™Y]Wİ[YH[™\ÜÙ\ÜÙYİ[YH[™Ø[™Y]Wİ[YHˆ\ÜÙ\ÜÙYİ[YN‚ˆš[™[™ÜË˜\[™
š[™[™ÊĞS‘QUWĞQ•T—ĞTÔÑTÔÓQS•‹‹İ[Z[™ËØØ[™Y]WØ\×ÛÙˆŠJB‚ˆYˆ\ÜÙ\ÜÛY[ÚY[™[™XYÙK™Ù]
œİ\\œÙY\ÈŠHOH\ÜÙ\ÜÛY[ÚY‚ˆš[™[™ÜË˜\[™
š[™[™Ê”ÑS—ÔÕTT”ÑTÔÒSÓˆ‹‹Û[™XYÙKÜİ\\œÙY\ÈŠJBˆYˆ\ÜÙ\ÜÛY[ÚY[™[™XYÙK™Ù]
œİ\\œÙYYØHŠHOH\ÜÙ\ÜÛY[ÚY‚ˆš[™[™ÜË˜\[™
š[™[™Ê”ÑS—ÔÕTT”ÑTÔÒSÓˆ‹‹Û[™XYÙKÜİ\\œÙYØHŠJB‚ˆYˆ[JÛİ™\›˜[˜ÙK™Ù]
šY[
H\È›İ˜[ÙH›ÜˆšY[[ˆ
ˆ˜]]Üš]WØÜ™X]Y‹œÛXŞWÙ]˜[X]Y‹œ›Û[İ[Û—Ø]]Üš^™Y‹œX›X×İ\ÙWØ[İÙY‚ˆ
JHÜˆÛİ™\›˜[˜ÙK™Ù]
œ™[X\ÙWÜ™YˆŠH\È›İ›Û™N‚ˆš[™[™ÜË˜\[™
š[™[™Ê‘ÓÕ‘T“SÑWĞ“ÕS‘T–WÕ’SÓUSÓˆ‹‹ÙÛİ™\›˜[˜ÙHŠJB‚ˆ™]\›ˆš[™[™ÜÂ‚‚™Yˆ˜[Y]WØ\ÜÙ\ÜÛY[
]ˆ]
HOˆ˜[Y][Û”™\İ[‚ˆØ[™Y]Kš[™[™ÜÈHÜ™XYÛØš™Xİ
]
BˆYˆØ[™Y]H\È›Û™N‚ˆ™]\›ˆ˜[Y][Û”™\İ[
\JÛÜY
Ù]
š[™[™ÜÊJJJBˆš[™[™ÜË™^[™
ÜØÚ[XWÙš[™[™ÜÊØ[™Y]JJBˆš[™[™ÜË™^[™
ÜÙ[X[X×Ùš[™[™ÜÊØ[™Y]JJBˆ™]\›ˆ˜[Y][Û”™\İ[
\JÛÜY
Ù]
š[™[™ÜÊJJJB‚‚™YˆÜÙ\šX[^™J]ˆ]™\İ[ˆ˜[Y][Û”™\İ[
HOˆİ‚ˆ™]\›ˆœÛÛ‹™[\ÊˆÂˆ™š[Hˆ]˜\×ÜÜÚ^

Kˆ™š[™[™ÜÈˆŞÈ˜ÛÙHˆ][K˜ÛÙK™šY[ˆ][K™šY[H›Üˆ][H[ˆ™\İ[™š[™[™Ü×Kˆ›İ]ÛÛYHˆ”TÔÈˆYˆ™\İ[›ÚÈ[ÙH‘RS‹ˆœØÛÜHˆĞÓÔKˆKˆÛÜÚÙ^\ÏUYKˆÙ\\˜]ÜœÏJ‹‹ˆŠKˆ
B‚‚™YˆÙš^\™WÙš[\Ê\™XİÜNˆ]™Yš^ˆİŠHOˆ\İÔ]N‚ˆ™]\›ˆÛÜY
\™XİÜK™ÛØŠˆÜ™Yš^J‹šœÛÛˆŠKÙ^O[[X™H]ˆ]˜\×ÜÜÚ^

JB‚‚™YˆÙ^XİYÛX[šY™\İ
\™XİÜNˆ]
HOˆXİÜİ‹\İÜİ—WN‚ˆN‚ˆ˜[YHHœÛÛ‹›ØYÊ
\™XİÜHÈ™^XİYÙš[™[™Ü×ÛX[šY™\İšœÛÛˆŠKœ™XYİ^
[˜ÛÙ[™ÏH]‹NŠJBˆ^Ù\
ÔÑ\œ›Ü‹[šXÛÙQ\œ›Ü‹œÛÛ‹’”ÓÓ‘XÛÙQ\œ›ÜŠN‚ˆ™]\›ˆßBˆ™]\›ˆ˜[YHYˆ\Ú[œİ[˜ÙJ˜[YKXİ
H[ÙHßB‚‚™Yˆ[—Ùš^\™WÜ›Ùš[J
HOˆ[‚ˆ˜[YÙš[\ÈHÙš^\™WÙš[\Ê’VT‘WÔ“ÓÕÈ˜[Y‹˜[YÈŠBˆ[˜[YÙš[\ÈHÙš^\™WÙš[\Ê’VT‘WÔ“ÓÕÈš[˜[Y‹š[˜[YÈŠBˆX[šY™\İHÙ^XİYÛX[šY™\İ
’VT‘WÔ“ÓÕÈš[˜[YŠBˆYˆ›İ˜[YÙš[\ÈÜˆ›İ[˜[YÙš[\Î‚ˆ™]\›ˆBˆ\ÜÙYHYBˆ›Üˆ][ˆ˜[YÙš[\Î‚ˆ™\İ[H˜[Y]WØ\ÜÙ\ÜÛY[
]
Bˆš[
ÜÙ\šX[^™J]™\İ[
JBˆ\ÜÙYH\ÜÙY[™™\İ[›ÚÂˆ›Üˆ][ˆ[˜[YÙš[\Î‚ˆ™\İ[H˜[Y]WØ\ÜÙ\ÜÛY[
]
Bˆš[
ÜÙ\šX[^™J]™\İ[
JBˆXİX[HÛÜY
Ùš[™[™Ë˜ÛÙH›Üˆš[™[™È[ˆ™\İ[™š[™[™ÜßJBˆ^XİYHÛÜY
X[šY™\İ™Ù]
]›˜[YK×JJBˆYˆ™\İ[›ÚÈÜˆ›İ^XİYÜˆXİX[OH^XİY‚ˆ\ÜÙYH˜[ÙBˆš[
œÛÛ‹™[\ÊÈ˜XİX[ˆXİX[™^XİYˆ^XİY™š[Hˆ]˜\×ÜÜÚ^

K›İ]ÛÛYHˆ‘’VT‘WÔÓT’UWÑT”“ÔˆŸKÛÜÚÙ^\ÏUYKÙ\\˜]ÜœÏJ‹‹ˆŠJBˆ™]\›ˆYˆ\ÜÙY[ÙHB‚‚™YˆXZ[Š\™İˆÙ\]Y[˜ÙVÜİ—H›Û™HH›Û™JHOˆ[‚ˆ\œÙ\ˆH\™Ü\œÙK\™İ[Y[\œÙ\Š\ØÜš\[ÛH•˜[Y]H›ÜÜÙYÑ“HX]\šX[Ú[™ÙP\ÜÙ\ÜÛY[™XÛÜ™ËˆŠBˆ\œÙ\‹˜YØ\™İ[Y[
™š[\È‹˜\™ÜÏHŠˆ‹\OT]
Bˆ\œÙ\‹˜YØ\™İ[Y[
‹KYš^\™\È‹Xİ[ÛHœİÜ™WİYHŠBˆ\™ÜÈH\œÙ\‹œ\œÙWØ\™ÜÊ\™İŠBˆYˆ\™ÜË™š^\™\Î‚ˆYˆ\™ÜË™š[\Î‚ˆ\œÙ\‹™\œ›ÜŠ‹KYš^\™\ÈØ[››İ™HÛÛXš[™YÚ]^XÚ]š[\ÈŠBˆ™]\›ˆ[—Ùš^\™WÜ›Ùš[J
BˆYˆ›İ\™ÜË™š[\Î‚ˆ\œÙ\‹™\œ›ÜŠœ›İšYHÛ™HÜˆ[Ü™Hš[\ÈÜˆ\ÙHKYš^\™\ÈŠBˆ˜Z[YH˜[ÙBˆ›Üˆ][ˆÛÜY
\™ÜË™š[\ËÙ^O[[X™H][Nˆ][K˜\×ÜÜÚ^

JN‚ˆ™\İ[H˜[Y]WØ\ÜÙ\ÜÛY[
]
Bˆš[
ÜÙ\šX[^™J]™\İ[
JBˆ˜Z[YH˜Z[YÜˆ›İ™\İ[›ÚÂˆ™]\›ˆHYˆ˜Z[Y[ÙH‚‚šYˆ×Û˜[YW×ÈOH—×ÛXZ[—×È‚ˆ˜Z\ÙHŞ\İ[Q^]
XZ[Š
JB