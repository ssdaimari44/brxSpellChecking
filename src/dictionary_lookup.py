import os

def load_dictionary(dict_path: str) -> list:
    """Load Hindi dictionary words from a file."""
    if not os.path.exists(dict_path):
        raise FileNotFoundError(f"Dictionary file not found: {dict_path}")
    with open(dict_path, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return words
