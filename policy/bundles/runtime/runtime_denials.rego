package kfm.runtime.denials

# Runtime denials are explicit and fail-closed.
default deny := false

deny if {
  input.request.actor.blocked == true
}

deny if {
  input.request.resource.restricted == true
}

deny_reason := "blocked_actor" if input.request.actor.blocked == true
deny_reason := "restricted_resource" if input.request.resource.restricted == true
