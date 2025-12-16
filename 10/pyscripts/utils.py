import os
def relative_path_resolver(path: str) -> str:
    """Resolve a path relative to the script's directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, path)