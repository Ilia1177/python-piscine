import sys
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    '''load data file in csv format'''
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def main():
    '''Program to read data set'''
    if len(sys.argv) != 2:
        print("Usage: uv run python load_csv.py <path_to_csv_file>")
        return
    path = sys.argv[1]
    data = load(path)
    if data is not None:
        print("Loading dataset of dimensions ", data.shape)
        print(data)


if __name__ == "__main__":
    main()
