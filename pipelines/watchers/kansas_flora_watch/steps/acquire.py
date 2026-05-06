"""acquire step placeholder for kansas_flora_watch."""

def run(context: dict) -> dict:
    context.setdefault("steps", []).append("acquire")
    return context
