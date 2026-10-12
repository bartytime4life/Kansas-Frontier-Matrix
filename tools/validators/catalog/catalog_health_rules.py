"""STAC Item and asset rules for the proposed KFM catalog-health profile."""
from __future__ import annotations

import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from tools.validators.catalog.catalog_health_core import (
    HEAD_TIMEOUT_SECONDS,
    MAX_ASSET_BYTES,
    MAX_ASSETS,
    MAX_LINKS,
    REQUIRED_RELS,
    SHA256_RE,
    Finding,
    HeadResult,
    ValidationResult,
    array,
    bbox_valid,
    has_time,
    local_path,
    make_report,
    mapping,
    read_object,
    safe_href,
    sha256,
    string_list,
    text,
)

HeadProbe = Callable[[str, float], HeadResult]


def _head_default(url: str, timeout: float) -> HeadResult:
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *_args: Any, **_kwargs: Any) -> None:
            return None

    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "kfm-catalog-health/1"},
    )
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=timeout) as response:
            return HeadResult(
                int(response.status),
                {key.lower(): value for key, value in response.headers.items()},
            )
    except urllib.error.HTTPError as error:
        return HeadResult(
            int(error.code),
            {key.lower(): value for key, value in error.headers.items()},
        )


def _record_findings(record: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    links = array(record.get("links"))
    assets = mapping(record.get("assets"))
    properties = mapping(record.get("properties"))

    def block(code: str, field: str) -> None:
        findings.append(Finding(code, field, "blocking"))

    if record.get("type") != "Feature":
        block("CAT_STAC_TYPE_INVALID", "/type")
    if not text(record.get("stac_version")):
        block("CAT_STAC_VERSION_MISSING", "/stac_version")
    if not text(record.get("id")):
        block("CAT_STAC_ID_MISSING", "/id")
    if not isinstance(record.get("geometry"), dict) or not bbox_valid(record.get("bbox")):
        block("CAT_STAC_SPATIAL_INVALID", "/geometry")
    if not has_time(properties):
        block("CAT_STAC_TIME_MISSING", "/properties")
    if not (text(properties.get("created")) and text(properties.get("updated"))):
        block("CAT_STAC_TIMESTAMP_MISSING", "/properties")
    if not text(record.get("license")):
        block("CAT_STAC_LICENSE_MISSING", "/license")
    providers = array(record.get("providers"))
    if not providers or any(
        not isinstance(item, dict)
        or not text(item.get("name"))
        or not string_list(item.get("roles"))
        for item in providers
    ):
        block("CAT_STAC_PROVIDERS_MISSING", "/providers")
    if not links or len(links) > MAX_LINKS:
        block("CAT_STAC_LINKS_INVALID", "/links")
    rels: set[str] = set()
    for index, item in enumerate(links):
        if (
            not isinstance(item, dict)
            or not text(item.get("rel"))
            or not safe_href(item.get("href"))
        ):
            block("CAT_STAC_LINK_INVALID", f"/links/{index}")
        else:
            rels.add(str(item["rel"]))
    if not REQUIRED_RELS <= rels:
        block("CAT_STAC_PROVENANCE_REL_MISSING", "/links")
    if not assets or len(assets) > MAX_ASSETS:
        block("CAT_STAC_ASSETS_INVALID", "/assets")
    return findings


def _asset_findings(
    record: Mapping[str, Any],
    *,
    asset_root: Path,
    network_mode: str,
    allowed_hosts: frozenset[str],
    head_probe: HeadProbe,
) -> tuple[list[Finding], dict[str, int], dict[str, int]]:
    findings: list[Finding] = []
    summary = {
        "assets_total": 0,
        "assets_local_verified": 0,
        "assets_remote_reachable": 0,
        "assets_embargoed": 0,
        "assets_held": 0,
    }
    network = {"attempted": 0, "succeeded": 0}
    links = array(record.get("links"))
    has_via = any(
        isinstance(item, dict)
        and item.get("rel") == "via"
        and safe_href(item.get("href"))
        for item in links
    )

    for key, raw in sorted(mapping(record.get("assets")).items()):
        summary["assets_total"] += 1
        field = f"/assets/{key}"
        if not isinstance(raw, dict):
            findings.append(Finding("CAT_ASSET_DESCRIPTOR_INVALID", field, "blocking"))
            continue
        href = raw.get("href")
        roles = raw.get("roles")
        checksum = raw.get("file:checksum")
        declared_size = raw.get("file:size")
        descriptor_ok = (
            safe_href(href)
            and text(raw.get("type"))
            and string_list(roles)
            and text(raw.get("title"))
            and isinstance(checksum, str)
            and SHA256_RE.fullmatch(checksum)
            and isinstance(declared_size, int)
            and 0 <= declared_size <= MAX_ASSET_BYTES
        )
        if not descriptor_ok:
            findings.append(Finding("CAT_ASSET_DESCRIPTOR_INVALID", field, "blocking"))
            continue

        parsed = urllib.parse.urlsplit(str(href))
        if parsed.scheme.lower() == "https":
            if "embargoed" in roles:
                summary["assets_embargoed"] += 1
                if not has_via:
                    findings.append(
                        Finding("CAT_ASSET_EMBARGO_VIA_MISSING", field, "blocking")
                    )
                continue
            host = (parsed.hostname or "").rstrip(".").lower()
            if network_mode != "HEAD":
                summary["assets_held"] += 1
                findings.append(
                    Finding("CAT_ASSET_REMOTE_UNVERIFIED", field, "hold")
                )
                continue
            if host not in allowed_hosts:
                summary["assets_held"] += 1
                findings.append(
                    Finding("CAT_ASSET_HOST_NOT_ALLOWLISTED", field, "hold")
                )
                continue
            network["attempted"] += 1
            result = head_probe(str(href), HEAD_TIMEOUT_SECONDS)
            if not 200 <= result.status < 300:
                findings.append(
                    Finding("CAT_ASSET_REMOTE_UNREACHABLE", field, "blocking")
                )
                continue
            network["succeeded"] += 1
            summary["assets_remote_reachable"] += 1
            length = result.headers.get("content-length")
            if length is None or not length.isdigit() or int(length) != declared_size:
                findings.append(
                    Finding("CAT_ASSET_SIZE_MISMATCH", field, "blocking")
                )
            continue

        local, code = local_path(asset_root, str(href))
        if code:
            findings.append(Finding(code, field, "blocking"))
            continue
        assert local is not None
        try:
            if not local.is_file() or local.stat().st_size > MAX_ASSET_BYTES:
                raise OSError
            actual_size = local.stat().st_size
            actual_digest = sha256(local)
        except OSError:
            findings.append(Finding("CAT_ASSET_READ_ERROR", field, "blocking"))
            continue
        if actual_size != declared_size:
            findings.append(Finding("CAT_ASSET_SIZE_MISMATCH", field, "blocking"))
        elif actual_digest != checksum:
            findings.append(Finding("CAT_ASSET_DIGEST_MISMATCH", field, "blocking"))
        else:
            summary["assets_local_verified"] += 1
    return findings, summary, network


def validate_record(
    path: Path,
    *,
    asset_root: Path | None = None,
    network_mode: str = "DENY",
    allowed_hosts: Sequence[str] = (),
    head_probe: HeadProbe | None = None,
) -> ValidationResult:
    """Validate one STAC Item with local evidence and optional bounded HEAD probes."""
    mode = network_mode.upper()
    if mode not in {"DENY", "HEAD"}:
        return make_report(
            path,
            None,
            [Finding("CAT_NETWORK_MODE_INVALID", "/network", "blocking")],
            network_mode="DENY",
        )
    if mode == "HEAD" and os.environ.get("KFM_NO_NETWORK") == "1":
        return make_report(
            path,
            None,
            [Finding("CAT_NETWORK_KILL_SWITCH", "/network", "blocking")],
            network_mode="HEAD",
        )
    record, findings = read_object(path)
    if record is None:
        return make_report(path, None, findings, network_mode=mode)
    findings.extend(_record_findings(record))
    asset_findings, summary, network = _asset_findings(
        record,
        asset_root=asset_root or path.parent,
        network_mode=mode,
        allowed_hosts=frozenset(host.rstrip(".").lower() for host in allowed_hosts),
        head_probe=head_probe or _head_default,
    )
    findings.extend(asset_findings)
    return make_report(
        path,
        record,
        findings,
        network_mode=mode,
        network=network,
        summary=summary,
    )
