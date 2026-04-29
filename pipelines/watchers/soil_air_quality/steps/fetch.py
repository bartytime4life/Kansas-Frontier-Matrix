"""fetch step placeholder for soil_air_quality watcher."""

def run(context: dict) -> dict:
    context.setdefault("steps", []).append("fetch")
    return context
