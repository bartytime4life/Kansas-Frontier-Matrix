from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping
from urllib.parse import urlencode

from urllib.request import urlopen

LOGGER = logging.getLogger("soilgrids_wcs_ingest")

COVERAGE_PART_RE = re.compile(r"^[a-z0-9]+$")
DEPTH_RE = re.compile(r"^\d+-\d+cm$")
STAT_RE = re.compile(r"^[a-z]+$")
BBOX_EPSILON = 0.0


@dataclass(frozen=True)
class RunReceipt:
    run_id: str
    spec_hash: str
    source: str
    coverage_id: str
    bbox: tuple[float, float, float, float]
    request_url: str
    output_path: str
    bytes_written: int
    status: str


def _setup_logging() -> None:
    if not LOGGER.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)


def _log(event: str, **fields: object) -> None:
    payload = {"event": event, **fields}
    LOGGER.info(json.dumps(payload, sort_keys=True))


def _validate_coverage_parts(property_name: str, depth: str, statistic: str) -> str:
    if not COVERAGE_PART_RE.fullmatch(property_name):
        raise ValueError("Invalid property format")
    if not DEPTH_RE.fullmatch(depth):
        raise ValueError("Invalid depth format")
    if not STAT_RE.fullmatch(statistic):
        raise ValueError("Invalid statistic format")
    return f"{property_name}_{depth}_{statistic}"


def _validate_bbox(bbox: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    xmin, ymin, xmax, ymax = bbox
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("Invalid bbox extents")
    if xmin < -180 or xmax > 180 or ymin < -90 or ymax > 90:
        raise ValueError("Bbox out of EPSG:4326 bounds")
    return bbox


def _build_request_url(property_name: str, coverage_id: str, bbox: tuple[float, float, float, float]) -> tuple[str, str]:
    endpoint = f"https://maps.isric.org/mapserv?map=/map/{property_name}.map"
    bbox_string = ",".join(f"{value:.8f}" for value in bbox)
    params = [
        ("SERVICE", "WCS"),
        ("REQUEST", "GetCoverage"),
        ("VERSION", "2.0.1"),
        ("COVERAGEID", coverage_id),
        ("SUBSET", f"Long({bbox[0]:.8f},{bbox[2]:.8f})"),
        ("SUBSET", f"Lat({bbox[1]:.8f},{bbox[3]:.8f})"),
        ("FORMAT", "image/tiff"),
    ]
    canonical_query = urlencode(params)
    spec_material = "\n".join([
        endpoint,
        f"coverage_id={coverage_id}",
        f"bbox={bbox_string}",
        "crs=EPSG:4326",
        "service=WCS",
        "request=GetCoverage",
        "version=2.0.1",
        "format=image/tiff",
    ])
    spec_hash = hashlib.sha256(spec_material.encode("utf-8")).hexdigest()
    return f"{endpoint}&{canonical_query}", spec_hash


def _validate_geotiff_bytes(content: bytes) -> None:
    if len(content) < 8:
        raise ValueError("Output file too small")
    if not (content[:2] in (b"II", b"MM") and content[2:4] in (b"*\x00", b"\x00*")):
        raise ValueError("Not a valid TIFF header")


def fetch_soilgrids_wcs(
    property_name: str,
    depth: str,
    statistic: str,
    bbox: tuple[float, float, float, float],
    output_path: str,
    http_get: Callable[[str], bytes] | None = None,
    fixture_bytes: bytes | None = None,
) -> RunReceipt:
    _setup_logging()
    coverage_id = _validate_coverage_parts(property_name, depth, statistic)
    clean_bbox = _validate_bbox(bbox)
    request_url, spec_hash = _build_request_url(property_name, coverage_id, clean_bbox)
    run_id = hashlib.sha256(f"{spec_hash}|{request_url}".encode("utf-8")).hexdigest()[:24]

    bbox_hash = hashlib.sha256(",".join(f"{value:.8f}" for value in clean_bbox).encode("utf-8")).hexdigest()[:12]
    expected_name = f"{property_name}_{depth}_{statistic}_{bbox_hash}.tif"
    output_file = Path(output_path)
    if output_file.name != expected_name:
        output_file = output_file.parent / expected_name

    receipt_base: Mapping[str, object] = {
        "run_id": run_id,
        "spec_hash": spec_hash,
        "source": "soilgrids_wcs",
        "coverage_id": coverage_id,
        "bbox": clean_bbox,
        "request_url": request_url,
        "output_path": str(output_file),
    }

    try:
        if fixture_bytes is not None:
            content = fixture_bytes
        else:
            if http_get is not None:
                content = http_get(request_url)
            else:
                with urlopen(request_url, timeout=120) as response:
                    status = getattr(response, "status", None)
                    if status != 200:
                        raise RuntimeError(f"HTTP status {status}")
                    content = response.read()

        _validate_geotiff_bytes(content)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_bytes(content)
        size = output_file.stat().st_size
        if size <= 0:
            raise ValueError("Empty output file")

        receipt = RunReceipt(
            **receipt_base,
            bytes_written=size,
            status="success",
        )
        _log("ingest_complete", **asdict(receipt), timestamp=datetime.now(timezone.utc).isoformat())
        return receipt
    except Exception as exc:
        receipt = RunReceipt(
            **receipt_base,
            bytes_written=0,
            status="error",
        )
        _log("ingest_error", **asdict(receipt), error=str(exc), timestamp=datetime.now(timezone.utc).isoformat())
        raise


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deterministic SoilGrids WCS ingestion")
    parser.add_argument("--property", dest="property_name", required=True)
    parser.add_argument("--depth", required=True)
    parser.add_argument("--stat", dest="statistic", required=True)
    parser.add_argument("--bbox", required=True, help="xmin,ymin,xmax,ymax")
    parser.add_argument("--output-path", required=True)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    bbox_parts = tuple(float(v) for v in args.bbox.split(","))
    if len(bbox_parts) != 4:
        raise ValueError("bbox must include exactly 4 values")
    receipt = fetch_soilgrids_wcs(
        property_name=args.property_name,
        depth=args.depth,
        statistic=args.statistic,
        bbox=bbox_parts,  # type: ignore[arg-type]
        output_path=args.output_path,
    )
    print(json.dumps(asdict(receipt), sort_keys=True))


if __name__ == "__main__":
    main()
