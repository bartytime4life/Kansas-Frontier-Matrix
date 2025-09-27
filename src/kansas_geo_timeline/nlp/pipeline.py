# src/kansas_geo_timeline/nlp/pipeline.py
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from .base import NLPError, PipelineStage, TextRecord
from .tokenizer import Tokenizer
from .date_extractor import DateExtractor
from .entity_extractor import EntityExtractor
from .glossary import Glossary
from .linker import Linker

# STAC + provenance from ingest layer
from kansas_geo_timeline.ingest.provenance import Provenance
from kansas_geo_timeline.ingest.stac_writer import StacWriter

import logging
_logger = logging.getLogger("kfm.nlp")
if not _logger.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    _logger.addHandler(_h)
    _logger.setLevel(logging.INFO)


class NLPPipeline:
    """Composable NLP pipeline → JSONL (+ optional STAC Items)."""

    def __init__(
        self,
        stages: Optional[List[PipelineStage]] = None,
        stac_items_dir: str | Path = "stac/items/text",
        emit_stac: bool = True,
    ) -> None:
        self.stages = stages or [
            _TokenizerStage(),
            _DateStage(),
            _EntityStage(),
            _GlossaryStage(),
            _LinkerStage(),  # consumes entities + glossary
        ]
        self.items_dir = Path(stac_items_dir)
        self.emit_stac = bool(emit_stac)

    # ----------------------- record-level -----------------------

    def process_record(self, rec: TextRecord) -> Dict[str, Any]:
        """Run all stages with safety wrappers; return enriched dict."""
        data: Dict[str, Any] = {"id": rec.id, "text": rec.text, "meta": dict(rec.meta)}
        cur = TextRecord(rec.id, rec.text, data)

        for stage in self.stages:
            cur = stage.safe_run(cur)
            # Stages write into cur.meta; nothing else to do.

        # Ensure canonical top-level
        cur.meta.setdefault("id", rec.id)
        cur.meta.setdefault("text", rec.text)
        return cur.meta

    # ----------------------- file-level -------------------------

    def run_file(
        self,
        input_path: Path,
        output_path: Path,
        collection: str | None = None,
    ) -> Tuple[int, List[Path]]:
        """Stream a JSONL file, write processed JSONL atomically, and produce STAC items."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.items_dir.mkdir(parents=True, exist_ok=True)

        n_ok = 0
        n_err = 0
        stac_paths: List[Path] = []

        # Atomic write to temp → replace
        with input_path.open("r", encoding="utf-8") as fin, \
             tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=output_path.parent) as tmp_out:

            tmp_out_path = Path(tmp_out.name)

            for line_no, line in enumerate(fin, start=1):
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                    rec = TextRecord.from_obj(obj)
                    data = self.process_record(rec)

                    # Stream the enriched line
                    tmp_out.write(json.dumps(data, ensure_ascii=False) + "\n")
                    n_ok += 1

                    if self.emit_stac:
                        stac_paths.append(self._emit_stac_for_record(input_path, output_path.parent, collection, rec, data))

                except Exception as e:
                    n_err += 1
                    _logger.warning("Skipping line %d (%s): %s", line_no, input_path.name, e)

        os.replace(tmp_out_path, output_path)
        if n_err:
            _logger.info("Processed %s: ok=%d, errors=%d", input_path, n_ok, n_err)
        else:
            _logger.info("Processed %s: ok=%d", input_path, n_ok)

        return n_ok, stac_paths

    # ----------------------- helpers ----------------------------

    def _emit_stac_for_record(
        self,
        input_path: Path,
        text_dir: Path,
        collection: Optional[str],
        rec: TextRecord,
        data: Dict[str, Any],
    ) -> Path:
        """Write a stable text blob for the record and a STAC Item."""
        text_file = self._write_text_blob(text_dir, rec.id, rec.text)
        digest = Provenance.digest_and_sidecar(text_file)
        props = {
            "datetime": Provenance.now_iso(),
            "kfm:ingest": "text",
            "kfm:sha256": digest,
            "kfm:src": data.get("source") or input_path.as_posix(),
            "file:meta": Provenance.file_stats(text_file),
            "nlp:dates": data.get("dates", []),
            "nlp:entities": data.get("entities", []),
            "nlp:glossary": data.get("glossary", []),
            "nlp:links": data.get("links", []),
        }
        item = StacWriter.mk_item(
            id_=rec.id,
            source_path=input_path,
            out_path=text_file,
            bbox=None,
            geometry=None,
            properties=props,
            asset_media_type="text/plain; charset=utf-8",
            collection=collection,
        )
        return StacWriter.write_item(item, self.items_dir)

    @staticmethod
    def _safe_id(s: str) -> str:
        # conservative id sanitizer for text filenames
        import re
        s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s.strip())
        return s.strip("-") or "doc"

    def _write_text_blob(self, out_dir: Path, rec_id: str, text: str) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"{self._safe_id(rec_id)}.txt"
        # Atomic write
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=out_dir) as tmp:
            tmp.write(text)
            tmp_path = Path(tmp.name)
        os.replace(tmp_path, path)
        return path


# ------------------- thin adapters (stages) -------------------

class _TokenizerStage(PipelineStage):
    name = "tokenizer"
    def __init__(self) -> None:
        self.tk = Tokenizer()
    def run(self, rec: TextRecord) -> TextRecord:
        rec.meta.update(self.tk.run(rec.text))
        return rec


class _DateStage(PipelineStage):
    name = "date-extractor"
    def __init__(self) -> None:
        self.de = DateExtractor()
    def run(self, rec: TextRecord) -> TextRecord:
        rec.meta.update(self.de.run(rec.text))
        return rec


class _EntityStage(PipelineStage):
    name = "entity-extractor"
    def __init__(self) -> None:
        self.ee = EntityExtractor()
    def run(self, rec: TextRecord) -> TextRecord:
        rec.meta.update(self.ee.run(rec.text))
        return rec


class _GlossaryStage(PipelineStage):
    name = "glossary"
    def __init__(self) -> None:
        self.gl = Glossary()
    def run(self, rec: TextRecord) -> TextRecord:
        out = self.gl.run(rec.text)
        rec.meta.update(out)
        return rec


class _LinkerStage(PipelineStage):
    name = "linker"
    def __init__(self) -> None:
        self.lk = Linker()
    def run(self, rec: TextRecord) -> TextRecord:
        ents = rec.meta.get("entities", [])
        gloss = rec.meta.get("glossary", [])
        out = self.lk.run(entities=ents, glossary=gloss)
        rec.meta.update(out)
        return rec


# ------------------------- CLI -------------------------

def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="KFM NLP pipeline")
    p.add_argument("--input", required=True, type=Path, help="JSONL with one object per line (requires 'text')")
    p.add_argument("--output", required=True, type=Path, help="Output JSONL (processed)")
    p.add_argument("--stac-dir", default="stac/items/text", type=Path, help="Directory to write STAC Items")
    p.add_argument("--collection", default=None, help="Optional STAC collection id")
    p.add_argument("--no-stac", action="store_true", help="Disable STAC Item emission")
    return p

def main(argv: List[str] | None = None) -> int:
    args = _build_argparser().parse_args(argv)
    pipe = NLPPipeline(stac_items_dir=args.stac_dir, emit_stac=(not args.no_stac))
    n, items = pipe.run_file(args.input, args.output, collection=args.collection)
    print(f"[nlp] processed={n} → {args.output}  stac_items={0 if args.no_stac else len(items)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
