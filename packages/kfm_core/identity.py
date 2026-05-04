def make_id(prefix: str, n: int) -> str:
    if not prefix or n < 0:
        raise ValueError("prefix required and n must be non-negative")
    return f"{prefix}-{n:03d}"
