from pathlib import Path 
def resolve_path_relative_to_script(relative_path: str) -> Path:
    script_dir = Path(__file__).resolve().parent
    relative_path = Path(relative_path)
    return script_dir / relative_path

def check_me():
    BASE_PATH = Path(__file__).resolve().parent
    RELATIVE_DATA_PATH = "../data/myFile.csv"
    ABSOLUTE_PATH = resolve_path_relative_to_script(RELATIVE_DATA_PATH)

    print("I'm running at:", BASE_PATH)
    print("RELATIVE_DATA_PATH:", RELATIVE_DATA_PATH)
    print("ABSOLUTE_PATH:", ABSOLUTE_PATH)