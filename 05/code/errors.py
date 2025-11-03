import operations
import json
from relative_path_resolver import resolve_path_relative_to_script

def load_json_config(filepath):
    with open(filepath, 'r') as file:
        config = json.load(file)
    return config


def setup_result_dir(outpath):
    import os
    directory = os.path.dirname(outpath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def calculate_statistics(config):
    count = config.get("count", 20)
    min_val = config.get("min_val", 0)
    max_val = config.get("max_val", 100)
    threshold = config.get("threshold", 50)
    numbers = operations.generate_random_numbers(count, min_val, max_val)
    print(f"Generated numbers: {numbers}")
    filtered_numbers = operations.filter_numbers(numbers, threshold)
    print(f"Filtered numbers (greater than {threshold}): {filtered_numbers}")
    mean = operations.calculate_mean(filtered_numbers)
    median = operations.calculate_median(filtered_numbers)
    mode = operations.calculate_mode(filtered_numbers)
    std_dev = operations.calculate_standard_deviation(filtered_numbers)
    outpath = config.get("output_path", "results.txt")
    setup_result_dir(outpath)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")
    with open(outpath, "w") as file:
        file.write("Statistics Results:\n")
        file.write(f"Original Numbers: {numbers}\n")
        file.write(f"Filtered Numbers: {filtered_numbers}\n")
        file.write(f"Mean: {mean}\n")
        file.write(f"Median: {median}\n")
        file.write(f"Mode: {mode}\n")
        file.write(f"Standard Deviation: {std_dev}\n")


def main():
    print("Welcome to the Statistics Calculator!")
    json_path = resolve_path_relative_to_script("config.json")
    config = load_json_config(json_path)
    rounds = config.get("rounds", 1)
    user_input = input("Do you want to proceed? (yes/no): ")
    if user_input == "yes":
        for _ in range(rounds):
            calculate_statistics(config)
    else:
       print("Exiting the script.")

if __name__ == "__main__":
   main()