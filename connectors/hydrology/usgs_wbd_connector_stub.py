connector_enabled = False

def fetch(*_args, **_kwargs):
    raise RuntimeError('BLOCKED: connector disabled pending activation gate decision')
