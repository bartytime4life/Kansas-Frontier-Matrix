from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .base import NLPError, PipelineStage, TextRecord
from .tokenizer import Tokenizer
from .date_extractor import DateExtractor
from .entity_extractor import EntityExtractor
from .glossary import Glossary
from .linker import Linker

# STAC + provenance from ingest layer
from kansas_geo_timeline.ingest.provenance import Provenance
from kansas_geo_timeline.ingest.stac_writer import StacWriter


class NLPPipeline:
    """Composable NLP pipeline → JSONL + STAC Items."""

    def __init__(
        self,
        stages: List[PipelineStage] | None = None,
        stac_items_dir: str | Path = "stac/items/text",
    ) -> None:
        self.stages = stages or [
            _TokenizerStage(),
            _DateStage(),
            _EntityStage(),
            _GlossaryStage(),
            _LinkerStage(),
        ]
        self.items_dir = Path(stac_items_dir)

    def process_record(self, rec: TextRecord) -> Dict[str, Any]:
        data: Dict[str, Any] = {"id": rec.id, "text": rec.text, "meta": rec.meta}
        # Pass a shallow object through the stages; each stage enriches `data`
        for stage in self.stages:
            out = stage.run(TextRecord(rec.id, rec.text, data))
            data = out.meta  # stages should merge into meta
        # ensure basic fields
        data.setdefault("id", rec.id)
        data.setdefault("text", rec.text)
        return data

    def run_file(self, input_path: Path, output_path: Path, collection: str | None = None) -> Tuple[int, List[Path]]:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        count = 0
        stac_paths: List[Path] = []

        with input_path.open("r", encoding="utf-8") as fin, output_path.open("w", encoding="utf-8") as fout:
            for line in fin:
                if not line.strip():
                    continue
                obj = json.loads(line)
                rec = TextRecord(id=str(obj.get("id") or f"rec-{count+1}"), text=obj.get("text", ""), meta=obj)
                data = self.process_record(rec)

                # Write processed JSONL line
                fout.write(json.dumps(data, ensure_ascii=False) + "\n")
                count += 1

                # STAC per record (minimal, text asset)
                text_file = self._write_text_blob(output_path.parent, rec.id, rec.text)
                digest = Provenance.digest_and_sidecar(text_file)
                props = {
                    "kfm:ingest": "text",
                    "kfm:sha256": digest,
                    "kfm:src": obj.get("source") or input_path.as_posix(),
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
                stac_path = StacWriter.write_item(item, self.items_dir)
                stac_paths.append(stac_path)

        return count, stac_paths

    def _write_text_blob(self, out_dir: Path, rec_id: str, text: str) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"{rec_id}.txt"
        path.write_text(text, encoding="utf-8")
        return path


# ------------------- thin adapters (stages) -------------------

class _TokenizerStage(PipelineStage):
    def __init__(self) -> None:
        self.tk = Tokenizer()

    def run(self, rec: TextRecord) -> TextRecord:
        out = self.tk.run(rec.text)
        rec.meta.update(out)
        return rec


class _DateStage(PipelineStage):
    def __init__(self) -> None:
        self.de = DateExtractor()

    def run(self, rec: TextRecord) -> TextRecord:
        out = self.de.run(rec.text)
        rec.meta.update(out)
        return rec


class _EntityStage(PipelineStage):
    def __init__(self) -> None:
        self.ee = EntityExtractor()

    def run(self, rec: TextRecord) -> TextRecord:
        out = self.ee.run(rec.text)
        rec.meta.update(out)
        return rec


class _GlossaryStage(PipelineStage):
    def __init__(self) -> None:
        self.gl = Glossary()

    def run(self, rec: TextRecord) -> TextRecord:
        out = self.gl.run(rec.text)
        rec.meta.update(out)
        return rec


class _LinkerStage(PipelineStage):
    def __init__(self) -> None:
        self.lk = Linker()

    def run(self, rec: TextRecord) -> TextRecord:
        ents = rec.meta.get("entities", [])
        out = self.lk.run(ents)
        rec.meta.update(out)
        return rec


# ------------------------- CLI -------------------------

def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="KFM NLP pipeline")
    p.add_argument("--input", required=True, type=Path, help="JSONL with {'id','text',...} per line")
    p.add_argument("--output", required=True, type=Path, help="Output JSONL (processed)")
    p.add_argument("--stac-dir", default="stac/items/text", type=Path, help="Where to write STAC items")
    p.add_argument("--collection", default=None, help="Optional STAC collection id")
    return p

def main(argv: list[str] | None = None) -> int:
    args = _build_argparser().parse_args(argv)
    pipe = NLPPipeline(stac_items_dir=args.stac_dir)
    n, items = pipe.run_file(args.input, args.output, collection=args.collection)
    print(f"[nlp] processed={n} → {args.output}  stac_items={len(items)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
