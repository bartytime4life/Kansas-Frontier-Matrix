import os
print('ABSTAIN network probe disabled; set KFM_ALLOW_NETWORK=1 for metadata-only probes' if os.getenv('KFM_ALLOW_NETWORK')!='1' else 'WARN network-enabled mode not executed in CI')
