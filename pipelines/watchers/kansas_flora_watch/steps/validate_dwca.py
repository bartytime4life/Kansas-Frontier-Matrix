"""validate_dwca step placeholder for kansas_flora_watch."""

def run(context: dict) -> dict:
    context.setdefault("steps", []).append("validate_dwca")
    return context
