# Retired account-based PC inference

The owner removed application login on 2026-10-19. The former account-backed PC
inference service, owner provisioning/worker scripts, invitations, password
verification, session handlers and `/api/pc-ai` routes have been removed from this
hosted composition. The old setup instructions are no longer applicable.

Public hosted Qwen continues through `/api/ai`; it does not depend on the owner's
computer or a user account. Its guest isolation, evidence checks and resource
budgets remain in place. The shared evidence reader now lives in
`app/hosted-ai-evidence.ts`.

Existing `/private/` files were not deleted or migrated. The application no longer
opens the retired account database. See `login-removal-20261019.md` for current
scope and validation. Historical implementations remain in Git history.

## Successor: home inference PC (proposed, default off)

The [home Ollama inference plan](home-ollama-inference.md) is a different design,
not a revival of this one. It has no visitor or owner login and no `/api/pc-ai`
route, and it does not reuse `KFM_PC_*` or account secrets. Public chat keeps
using anonymous `/api/ai` guest jobs. When the owner selects
`KFM_AI_PROVIDER=home-ollama`, the server sends bounded discussions to a signed,
loopback-only gateway on the owner's second Linux PC. Setup files are in
[`scripts/home-inference/`](../scripts/home-inference/README.md).
