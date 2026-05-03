POLICY_DECISIONS = {"ALLOW", "ABSTAIN", "DENY", "ERROR"}
PUBLIC_SENSITIVITY = {"PUBLIC_SAFE", "GENERALIZED"}


def allow_public(sensitivity: str) -> bool:
    return sensitivity in PUBLIC_SENSITIVITY


def policy_decision_for_sensitivity(sensitivity: str) -> str:
    return "ALLOW" if allow_public(sensitivity) else "DENY"
