from __future__ import annotations
from typing import Any
from tools.runtime.fauna.kfm_gbif_answer_service import with_spec_hash

def build_ui_cards_and_layers(answer: dict[str,Any], query: dict[str,Any]):
    cards=[]; layers=[]
    for claim in answer.get("claims",[]):
        cits=claim.get("citations",[])
        card={"card_id":f"gbif_card_{claim['claim_id']}","card_type":"gbif_occurrence_aggregate_summary","title":f"{query.get('scientific_name','Taxon')} — {query.get('geography_id','Geography')}","subtitle":"GBIF-reported public occurrence aggregate","body":f"{claim.get('record_count',0)} reported GBIF occurrence records were aggregated for public display.","badges":["reported occurrence","public generalized","not confirmed presence"],"claim_refs":[claim["claim_id"]],"citations":[{k:v for k,v in cit.items() if k in {"source_system","source_evidence_bundle_id","download_key","source_aggregate_id","geoprivacy_receipt_ref","kfm:spec_hash"}} for cit in cits],"forbidden_fields_absent":True}
        cards.append(with_spec_hash(card,{"card_id"}))
        if query.get("include_geometry") and cits:
            layers.append(with_spec_hash({"layer_id":f"gbif_layer_{claim['claim_id']}","layer_type":"generalized_public_occurrence_area","geometry_role":"generalized_public_area","aggregation_unit":query.get("aggregation_unit","county"),"geography_id":query.get("geography_id"),"display_name":query.get("geography_id"),"source_aggregate_ids":[cits[0].get("source_aggregate_id")],"geoprivacy_receipt_ref":cits[0].get("geoprivacy_receipt_ref")},{"layer_id"}))
    return cards,layers
