from .constants import REQUIRED_LAYER15_KEYS

def validate_layer15_inputs(m):
 li=m.get("layer15_inputs",{})
 return [k for k in REQUIRED_LAYER15_KEYS if k not in li]
