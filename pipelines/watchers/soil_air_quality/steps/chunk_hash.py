"""chunk_hash step placeholder for soil_air_quality watcher."""

def run(context: dict) -> dict:
    context.setdefault("steps", []).append("chunk_hash")
    return context
