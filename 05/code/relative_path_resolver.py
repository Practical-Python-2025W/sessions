from pathlib import Path 
def resolve_path_relative_to_script(relative_path: str) -> Path:
    """
    Resolve a relative path to an absolute path based on the script's location.
    This function takes a relative path as input and returns the absolute path
    by combining it with the directory of the currently executing script.
    This function contains a rather unnecessary intermediate variable, but it is kept for better readability.
    More gravely, there is an assumption in this function that might cause rather ugly issues in certain scenarios.
    Can you spot it? (And fix it?)
    """
    script_dir = Path(__file__).resolve().parent
    relative_path = Path(relative_path)
    return script_dir / relative_path

def check_me():
    BASE_PATH = Path(__file__).resolve().parent
    RELATIVE_DATA_PATH = "../data/myFile.csv"
    absolute_path = resolve_path_relative_to_script(RELATIVE_DATA_PATH)

    print("I'm running at:", BASE_PATH)
    print("RELATIVE_DATA_PATH:", RELATIVE_DATA_PATH)
    print("ABSOLUTE_PATH:", absolute_path)