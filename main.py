import argparse
from CSVSplitter import CSVSplitter

if __name__ == "__main__":
    # Create an argument parser for the input file argument
    parser = argparse.ArgumentParser(description="Split a CSV file by entity")
    parser.add_argument("input_file", help="Path to the input CSV file")

    # Parse the input file argument
    args = parser.parse_args()

    print(f"Scanning file {args.input_file}")
    # Call the split_csv_by_entity function with the input file argument
    splitter = CSVSplitter(args.input_file)
    splitter.split_by_entity()