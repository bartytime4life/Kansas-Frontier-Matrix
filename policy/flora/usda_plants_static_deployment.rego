package flora.usda_plants_static_deployment

deny[msg] { not input.deployment_approval.approved_by; msg := "missing human approval" }
deny[msg] { input.deployment_approval.approval_actor_type != "human"; msg := "non-human approval" }
deny[msg] { some r in input.refs; contains(r,"/raw/") or contains(r,"/work/") or contains(r,"/quarantine/"); msg := "raw/work/quarantine refs" }
deny[msg] { some k; k := input.claims[_]; contains(lower(k),"occurrence_lat") or contains(lower(k),"occurrence_lon"); msg := "occurrence coordinate leaks" }
deny[msg] { input.claims.external_basemap == true; msg := "external basemap claims" }
deny[msg] { input.claims.long_lived_secrets == true; msg := "long-lived secret claims" }
deny[msg] { count(input.hashes) == 0; msg := "missing hashes" }
deny[msg] { not contains(lower(input.attribution),"usda plants") ; msg := "bad attribution" }
deny[msg] { input.claims.auto_merge == true; msg := "auto-merge claims" }

deny[msg] { input.github_pages_manifest.environment == "github-pages"; input.github_pages_manifest.required_permissions.pages != "write"; msg := "github pages missing pages:write" }
deny[msg] { input.github_pages_manifest.environment == "github-pages"; input.github_pages_manifest.required_permissions["id-token"] != "write"; msg := "github pages missing id-token:write" }
deny[msg] { input.github_pages_manifest.environment == "github-pages"; input.github_pages_manifest.requires_environment_protection != true; msg := "github pages missing environment protection" }
deny[msg] { input.github_pages_manifest.environment == "github-pages"; input.github_pages_manifest.uses_long_lived_secrets == true; msg := "github pages uses long-lived secrets" }
deny[msg] { input.github_pages_manifest.environment == "github-pages"; input.github_pages_manifest.claims.auto_merge == true; msg := "github pages auto-merge claims" }
deny[msg] { some r in input.github_pages_manifest.refs; contains(r,"/raw/") or contains(r,"/work/") or contains(r,"/quarantine/"); msg := "github pages raw/work/quarantine refs" }
