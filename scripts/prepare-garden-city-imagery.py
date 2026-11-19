#!/usr/bin/env python3
"""Prepare the fixed Garden City Labs display pair from the verified source packet."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PIL import Image


def digest(contents):
    return hashlib.sha256(contents).hexdigest()


def local_file(directory, name, expected):
    if Path(name).name != name:
        raise ValueError("Expected a local packet filename")
    path = directory / name
    if digest(path.read_bytes()) != expected:
        raise ValueError(f"Packet hash mismatch for {name}")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text())
    export_geometry = packet["verifiedExportGeometry"]
    extent = export_geometry["extent"]
    bounds = [extent[key] for key in ("xmin", "ymin", "xmax", "ymax")]
    if (extent["spatialReference"]["latestWkid"] != 3857
            or bounds != packet["bounds"]
            or (packet["width"], packet["height"]) != (768, 768)
            or (export_geometry["width"], export_geometry["height"]) != (768, 768)
            or [item["edition"] for item in packet["editions"]] != [2021, 2024]):
        raise ValueError("Unexpected source footprint or editions")

    images = args.root / "public/labs/then-now"
    images.mkdir(parents=True, exist_ok=True)
    editions = []
    for item in packet["editions"]:
        year = item["edition"]
        source = local_file(args.packet.parent, item["imageFile"], item["imageSha256"])
        metadata = local_file(args.packet.parent, item["metadataFile"], item["metadataSha256"])
        record = json.loads(metadata.read_text())
        export = urlparse(item["exportUrl"])
        query = parse_qs(export.query)
        if (item["reuse"] != "CC0 1.0" or "CC0 1.0" not in record["licenseInfo"]
                or record["owner"] != "KansasGIS" or item["title"] != record["title"]
                or urlparse(item["catalog"]).hostname != "www.arcgis.com"
                or export.scheme != "https"
                or not item["exportUrl"].startswith(record["url"] + "/exportImage?")
                or query.get("bbox") != [",".join(map(str, bounds))]
                or any(query.get(key) != [value] for key, value in {
                    "bboxSR": "3857", "imageSR": "3857", "size": "768,768",
                    "bandIds": "0,1,2", "format": "png24", "f": "image",
                }.items())):
            raise ValueError("Expected the DASC natural-color item and its declared CC0 terms")
        target = images / f"garden-city-{year}.webp"
        with Image.open(source) as image:
            if image.format != "PNG" or image.mode != "RGB" or image.size != (768, 768):
                raise ValueError("Expected a full 768 × 768 RGB provider export")
            image.save(target, "WEBP", quality=88, method=6)
        editions.append({
            "year": year, "catalog": item["catalog"], "export": item["exportUrl"],
            "window": item["catalogueCaptureWindow"], "sourceSha256": item["imageSha256"],
            "preview": f"/labs/then-now/{target.name}", "previewSha256": digest(target.read_bytes()),
        })
    if editions[0]["sourceSha256"] == editions[1]["sourceSha256"]:
        raise ValueError("Expected two distinct provider exports")

    manifest = {
        "site": "Arkansas River crossing in Garden City, Kansas",
        "source": "Kansas Data Access and Support Center · NG911 Natural Color",
        "license": "CC0 1.0", "retrievedAt": packet["retrievedAt"],
        "footprint": {"crs": "EPSG:3857", "bounds": bounds, "width": 768, "height": 768},
        "editions": editions,
        "project": packet["publicWorksContext"]["sources"][0]["url"],
    }
    output = args.root / "app/labs/then-now/pair.json"
    output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
