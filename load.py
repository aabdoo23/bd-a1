import argparse
import pandas as pd
import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    return args.file_path

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def call_next_script():
    print("Calling dpre.py...")
    subprocess.run(["python3", "dpre.py"])

if __name__ == "__main__":
    file_path = parse_arguments()
    df = load_dataset(file_path)
    print(df.head())
    call_next_script()
