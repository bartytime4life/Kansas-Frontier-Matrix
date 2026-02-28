# RBAC Matrix

| Role | Public data | Restricted metadata | Policy override |
|---|---|---|---|
| public | allow | deny | deny |
| staff | allow | limited | deny |
| researcher | allow | reviewed | deny |
| admin | allow | allow | reviewed |
