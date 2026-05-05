#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path as _P
sys.path.insert(0,str(_P(__file__).resolve().parents[2]))
from pathlib import Path
from kfm.air_quality.airnow.qa.run_qa import run_qa
from kfm.air_quality.airnow.qa.ids import sha256_text, canonical_json, make_id

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    m=json.loads(Path(a.manifest).read_text())
    out,errs=run_qa(m,a.created_at)
    if errs:
        print(json.dumps({"validation_outcome":"FAIL","errors":errs},indent=2))
        return 2
    od=Path(a.out_dir); od.mkdir(parents=True,exist_ok=True)
    names=["coverage_summary","freshness_summary","source_completeness_summary","parameter_coverage_summary","geography_coverage_summary","relationship_graph_summary","conflict_summary","orphan_summary","quarantine_summary","governance_summary"]
    for n in names: (od/f"{n}.json").write_text(json.dumps(out[n],indent=2,sort_keys=True)+"\n")
    (od/'qa_findings.jsonl').write_text(''.join(canonical_json(r)+"\n" for r in out['qa_findings']))
    (od/'qa_report.md').write_text(out['qa_report'])
    rec={"object_type":"AirNowQAReceipt","schema_version":"v1","source_id":"airnow","manifest_id":m['manifest_id'],"qa_runner":"airnow_layer5_qa","qa_runner_version":"v1","input_counts":out['coverage_summary']['record_counts'],"output_counts":{"qa_findings":len(out['qa_findings']),"summary_documents":10,"markdown_reports":1},"validation_outcome":"PASS","finite_outcome":"ANSWER","input_hashes":{"manifest_hash":sha256_text(Path(a.manifest).read_text())},"output_hashes":{},"outputs":{},"warnings":[],"errors":[],"created_at":a.created_at}
    for n in names:
        fn=f"{n}.json"; rec['output_hashes'][f"{n}_hash"]=sha256_text((od/fn).read_text()); rec['outputs'][f"{n}_json"]=fn
    rec['output_hashes']['qa_findings_hash']=sha256_text((od/'qa_findings.jsonl').read_text()); rec['output_hashes']['qa_report_hash']=sha256_text((od/'qa_report.md').read_text())
    rec['outputs']['qa_findings_jsonl']='qa_findings.jsonl'; rec['outputs']['qa_report_md']='qa_report.md'
    rec['receipt_id']=make_id('kfm:air_quality:airnow:qa_receipt:v1',[rec['input_counts'],rec['output_hashes'],a.created_at])
    (od/'qa_receipt.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n")
    print(json.dumps(rec,indent=2,sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
