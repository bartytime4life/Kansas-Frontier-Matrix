#!/usr/bin/python3
"""Offline, bounded extraction worker. Launched inside a network-isolated sandbox."""

import json, os, re, subprocess, warnings
from pathlib import Path
from PIL import Image, ImageOps

Image.MAX_IMAGE_PIXELS = 32_000_000
warnings.simplefilter("error", Image.DecompressionBombWarning)
ROOT = Path("/work")
source = ROOT / "original"
result = {
    "status": "Complete",
    "method": "",
    "pages": None,
    "text": "",
    "textTruncated": False,
    "metadata": {},
    "warnings": [],
    "suggestions": [],
    "flags": [],
}


def run(args, timeout=20, env=None):
    p = subprocess.run(
        args,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        env=env,
    )
    if p.returncode:
        raise ValueError(
            "The local extraction tool could not read this file. It may be encrypted or damaged."
        )
    return p.stdout.decode("utf-8", "replace")


def ocr(path):
    env = {
        **os.environ,
        "LD_LIBRARY_PATH": "/ocr/usr/lib/x86_64-linux-gnu",
        "TESSDATA_PREFIX": "/ocr/usr/share/tesseract-ocr/5/tessdata",
        "OMP_THREAD_LIMIT": "2",
    }
    return run(
        ["/ocr/usr/bin/tesseract", str(path), "stdout", "-l", "eng", "--psm", "3"],
        25,
        env,
    )


def main():
    raw = source.open("rb").read(16)
    if raw.startswith(b"%PDF-"):
        result["method"] = "Local PDF text extraction (Poppler)"
        info = run(["/usr/bin/pdfinfo", str(source)])
        m = re.search(r"^Pages:\s*(\d+)", info, re.M)
        result["pages"] = int(m.group(1)) if m else None
        if re.search(r"^Encrypted:\s+yes", info, re.M):
            raise ValueError(
                "Encrypted PDFs require an unlocked copy. Original retained privately."
            )
        run(
            [
                "/usr/bin/pdftoppm",
                "-f",
                "1",
                "-singlefile",
                "-scale-to",
                "1400",
                "-png",
                str(source),
                str(ROOT / "preview"),
            ]
        )
        text = run(
            ["/usr/bin/pdftotext", "-f", "1", "-l", "30", "-layout", str(source), "-"]
        )
        pages = text.split("\f")
        result["text"] = "\n\n".join(
            f"[Page {n+1}]\n{t.strip()}" for n, t in enumerate(pages) if t.strip()
        )
        if (result["pages"] or 0) > 30:
            result["warnings"].append("Text extraction covers the first 30 pages only.")
            result["status"] = "Partial"
        if len(text.strip()) < 40:
            result["method"] = "Local scanned-PDF OCR (English, first 3 pages)"
            parts = []
            for n in range(1, min(result["pages"] or 1, 3) + 1):
                dest = ROOT / f"ocr-{n}"
                run(
                    [
                        "/usr/bin/pdftoppm",
                        "-f",
                        str(n),
                        "-l",
                        str(n),
                        "-singlefile",
                        "-scale-to",
                        "2200",
                        "-png",
                        str(source),
                        str(dest),
                    ]
                )
                parts.append(f"[Page {n} · OCR]\n" + ocr(str(dest) + ".png"))
                Path(str(dest) + ".png").unlink(missing_ok=True)
            result["text"] = "\n\n".join(parts)
            result["warnings"].append(
                "OCR can misread words and numbers. Verify against the original."
            )
            result["status"] = "Partial"
            if (result["pages"] or 1) > 3:
                result["warnings"].append(
                    "Scanned-PDF OCR is limited to the first 3 pages; later pages are not analyzed."
                )
        elif any(len(t.strip()) < 25 for t in pages[: result["pages"] or len(pages)]):
            result["warnings"].append(
                "Some pages contain little or no extractable text. Images, tables and scanned regions may be missing."
            )
            result["status"] = "Partial"
        result["warnings"].append(
            "Text order and table structure may differ from the page. Preview shows the first page only."
        )
    else:
        with Image.open(source) as im:
            if im.format not in ("JPEG", "PNG", "WEBP", "TIFF"):
                raise ValueError(
                    "Unsupported image format. Use JPEG, PNG, WebP or TIFF."
                )
            result["metadata"] = {
                "width": im.width,
                "height": im.height,
                "format": im.format,
                "frames": getattr(im, "n_frames", 1),
                "hasExif": bool(im.getexif()),
            }
            if im.getexif():
                result["flags"].append(
                    "Photo metadata may contain identifying or precise-location details. Original is private; preview strips metadata."
                )
            im.load()
            frame = ImageOps.exif_transpose(im).convert("RGB")
            frame.thumbnail((2200, 2200))
            frame.save(ROOT / "ocr-image.png")
            frame.thumbnail((1400, 1400))
            frame.save(ROOT / "preview.png")
        result["method"] = "Local photo OCR (English, first frame)"
        result["text"] = ocr(ROOT / "ocr-image.png")
        (ROOT / "ocr-image.png").unlink(missing_ok=True)
        result["status"] = "Partial"
        result["warnings"].append(
            "Photo analysis extracts visible text only; it does not recognize objects, people or places. Describe the image to improve suggestions."
        )
        if result["metadata"]["frames"] > 1:
            result["warnings"].append(
                "Only the first frame of this image was analyzed."
            )
    if not result["text"].strip():
        result["warnings"].append(
            "No readable text found. Add a description and choose a destination manually."
        )
        result["status"] = "Partial"
    if len(result["text"]) > 250000:
        result["text"] = result["text"][:250000]
        result["textTruncated"] = True
        result["status"] = "Partial"
        result["warnings"].append("Extracted text is capped at 250,000 characters.")


try:
    main()
except Exception as e:
    result["status"] = "Failed"
    result["warnings"].append(
        str(e)
        if isinstance(e, ValueError)
        else "Extraction failed or exceeded resource limits. Original retained; review manually."
    )
(ROOT / "analysis.json").write_text(json.dumps(result, ensure_ascii=False))
