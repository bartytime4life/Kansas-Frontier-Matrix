from .ids import stable_id

MAP={
 "FIX_CHECKSUM_MISMATCH":("checksum","P0","OPEN_TEMPLATE_ONLY"),
 "ADD_REQUIRED_DISCLAIMER":("disclaimer","P1","OPEN_TEMPLATE_ONLY"),
 "REDACT_HUMAN_DOC_COORDINATES":("coordinate_sensitivity","P0","OPEN_TEMPLATE_ONLY"),
 "PUBLICATION_DENIED_BY_POLICY":("policy_denial","P0","BLOCKED_BY_POLICY"),
}

def classify(code,severity="REQUIRED",status="FAIL"):
    if code in MAP: return MAP[code]
    if status=="WARN": return ("documentation","P2","OPEN_TEMPLATE_ONLY")
    if status=="INFO": return ("needs_verification","P3","NEEDS_VERIFICATION")
    return ("unknown","P3","NEEDS_MANUAL_INPUT")
