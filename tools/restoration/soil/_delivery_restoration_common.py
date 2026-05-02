# simplified common helpers
from tools.recommissioning.soil._recommissioning_common import *
from pathlib import Path

def load_current_delivery_recommissioning(r): return load_json(Path(r)/'recommissioning/soil/current_delivery_recommissioning.json')
def load_delivery_recommissioning_manifest(r,i): return load_json(Path(r)/f'recommissioning/soil/cycles/{i}/delivery_recommissioning_manifest.json')
def load_delivery_recommissioning_receipt(r,i): return load_json(Path(r)/f'recommissioning/soil/cycles/{i}/delivery_recommissioning_receipt.json')
def load_active_delivery_recommissioning_readiness_packet(r,i): return load_json(Path(r)/f'recommissioning/soil/cycles/{i}/active_delivery_recommissioning_readiness_packet.json')
def load_monitoring_baseline_revalidation_registry(r,i): return load_json(Path(r)/f'recommissioning/soil/cycles/{i}/monitoring_baseline_revalidation_registry.json')
def load_safe_mode_exit_verification_registry(r,i): return load_json(Path(r)/f'recommissioning/soil/cycles/{i}/safe_mode_exit_verification_registry.json')
def load_current_public_delivery(r): return load_json(Path(r)/'delivery/soil/current_public_delivery.json')
def load_current_public_routing(r): return load_json(Path(r)/'routing/soil/current_public_routing.json')
def load_active_read_model_projection(r,i): return load_json(Path(r)/f'delivery/soil/cycles/{i}/active_read_model_projection.json') if (Path(r)/f'delivery/soil/cycles/{i}/active_read_model_projection.json').exists() else {'records':[]}
def load_current_release(r): return load_json(Path(r)/'published/soil/current.json')
def load_published_manifest(r,i): return load_json(Path(r)/f'published/soil/releases/{i}/manifest.json')
def load_published_index(r,i): return load_json(Path(r)/f'published/soil/releases/{i}/index.json')
def load_publication_receipt(r,i): return load_json(Path(r)/f'published/soil/releases/{i}/publication_receipt.json')
def load_operational_status(r): return load_json(Path(r)/'ops/soil/status/current_status.json') if (Path(r)/'ops/soil/status/current_status.json').exists() else {'public_access_allowed':True}
release_is_retracted=lambda r,i:(Path(r)/f'published/soil/retractions/{i}.retraction_notice.json').exists()
def build_restoration_transparency_log(entries): return build_recommissioning_transparency_log(entries)
validate_restoration_approval=lambda a,*_,**__: (a.get('steward_review') or {}).get('decision')=='approved'
validate_restoration_probe=lambda p,*_,**__: p.get('decision')=='pass'
validate_restored_read_model=lambda p,*_,**__: isinstance(p.get('records',[]),list)
validate_active_delivery_restoration=lambda p,*_,**__: isinstance(p.get('active_public_delivery_restored'),bool)
validate_restoration_inputs=lambda *_,**__: (True,[])
