"""Prepare one queued Kansas historical sheet and stage it for owner review.

Requires KFM_HISTORICAL_WORKER_TOKEN in the environment. A private Site may
also require KFM_SITES_BYPASS_TOKEN for its dispatch boundary. This tool never
activates a package or changes the public release pointer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from connectors.usgs.topoview.fetch_sheet import stream_geotiff

TRANSFORM = ROOT / "pipelines/normalize/geography/historical_topo_tiles.py"
SITE_ORIGIN = "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


OPENER = build_opener(NoRedirect())


def headers(token: str) -> dict[str, str]:
    result = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    bypass = os.getenv("KFM_SITES_BYPASS_TOKEN")
    if bypass:
        result["OAI-Sites-Authorization"] = f"Bearer {bypass}"
    return result


def request_json(url: str, token: str) -> dict:
    with OPENER.open(Request(url, headers=headers(token)), timeout=30) as response:
        if response.status != 200 or "json" not in response.headers.get("Content-Type", ""):
            raise ValueError("Site preparation queue returned an unexpected response")
        body = response.read(500_001)
        if len(body) > 500_000:
            raise ValueError("Site preparation queue exceeded its byte limit")
        return json.loads(body)


def stage(url: str, token: str, scan: int, package: str, address: str, path: Path) -> None:
    body = path.read_bytes()
    digest = hashlib.sha256(body).hexdigest()
    query = urlencode({"scan": scan, "package": package, "address": address})
    metadata = {**headers(token), "Content-Type": "application/json" if address == "manifest" else "image/png", "X-KFM-SHA256": digest}
    request = Request(f"{url}/api/historical-topo/stage?{query}", data=body, headers=metadata, method="PUT")
    for attempt in range(3):
        try:
            with OPENER.open(request, timeout=45) as response:
                result = json.load(response)
                if response.status not in (200, 201) or not result.get("staged") or result.get("sha256") != digest:
                    raise ValueError(f"Site did not confirm staged {address}")
                return
        except (HTTPError, URLError, TimeoutError) as error:
            if attempt == 2 or isinstance(error, HTTPError) and error.code not in (408, 425, 429, 500, 502, 503, 504):
                raise ValueError(f"Site staging failed for tile {address}") from None
            time.sleep(2 ** attempt)


def capture_raw(item: dict, raw: Path, scan: int) -> Path:
    """Persist the original and its receipt without exposing a partial capture."""
    original = raw / f"{scan}.tif"
    receipt = raw / f"{scan}.capture.json"
    if receipt.exists():
        if not original.is_file():
            raise ValueError("RAW receipt exists without its original GeoTIFF")
        return receipt
    if original.exists():
        raise ValueError("RAW GeoTIFF exists without its capture receipt")
    partial = raw / f"{scan}.tif.part"
    receipt_partial = raw / f"{scan}.capture.json.part"
    try:
        with partial.open("xb") as output:
            record = stream_geotiff(item, output.write)
            output.flush()
            os.fsync(output.fileno())
        with receipt_partial.open("x", encoding="utf-8") as output:
            json.dump(record, output, sort_keys=True, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        partial.rename(original)
        receipt_partial.rename(receipt)
    finally:
        partial.unlink(missing_ok=True)
        receipt_partial.unlink(missing_ok=True)
    return receipt


def run(site: str, raw: Path, packages: Path, token: str, dry_run: bool, request_file_input: Path | None) -> None:
    if site != SITE_ORIGIN:
        raise ValueError("use the exact HTTPS owner-private Site origin")
    if not dry_run and len(token) < 32:
        raise ValueError("KFM_HISTORICAL_WORKER_TOKEN is not configured")
    queue = {"requests": [json.loads(request_file_input.read_text(encoding="utf-8"))]} if request_file_input else request_json(f"{site}/api/historical-topo/queue", token)
    items = queue.get("requests")
    if not isinstance(items, list):
        raise ValueError("Site preparation queue changed shape")
    if not items:
        print("No pending Kansas sheet requests")
        return
    item = items[0]
    if item.get("state") != "KS" or not isinstance(item.get("scanId"), int):
        raise ValueError("queue returned an invalid Kansas request")
    scan = item["scanId"]
    raw.mkdir(parents=True, exist_ok=True)
    request_file = raw / f"{scan}.request.json"
    if not request_file.exists():
        request_file.write_text(json.dumps(item, sort_keys=True) + "\n", encoding="utf-8")
    elif json.loads(request_file.read_text(encoding="utf-8")) != item:
        raise ValueError("queued sheet identity changed after capture")
    receipt = capture_raw(item, raw, scan)
    capture = json.loads(receipt.read_text(encoding="utf-8"))
    package = capture["geotiff"]["sha256"][:24]
    folder = packages / f"{scan}-{package}"
    if not folder.exists():
        subprocess.run([sys.executable, str(TRANSFORM), "--capture", str(receipt), "--output", str(packages)], check=True)
    manifest_file = folder / "manifest.json"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    if manifest.get("packageId") != package or manifest.get("sheet", {}).get("scanId") != scan:
        raise ValueError("prepared package does not match the queued sheet")
    if dry_run:
        print(f"Prepared {len(manifest['tiles'])} tiles for scan {scan}; no upload requested")
        return
    for address, expected in sorted(manifest["tiles"].items()):
        path = folder / "tiles" / f"{address}.png"
        if not path.is_file() or path.stat().st_size != expected["bytes"] or hashlib.sha256(path.read_bytes()).hexdigest() != expected["sha256"]:
            raise ValueError(f"local tile digest failed: {address}")
        stage(site, token, scan, package, address, path)
    stage(site, token, scan, package, "manifest", manifest_file)
    print(f"Staged {len(manifest['tiles'])} tiles for scan {scan}; owner review and activation are still required")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", required=True)
    parser.add_argument("--raw", type=Path, required=True, help="external immutable capture directory")
    parser.add_argument("--packages", type=Path, required=True, help="external candidate package directory")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--request", type=Path, help="local queue record for an offline preparation rehearsal")
    args = parser.parse_args()
    run(args.site.rstrip("/"), args.raw, args.packages, os.getenv("KFM_HISTORICAL_WORKER_TOKEN", ""), args.dry_run, args.request)


if __name__ == "__main__":
    main()
