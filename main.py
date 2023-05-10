import argparse
import pandas as pd

def split_csv_by_entity(input_file):
    # Read the input file into a pandas dataframe
    df = pd.read_csv(input_file)

    # Get a list of unique entities
    unique_entities = df["sub_entity"].unique()

    # Loop through each unique entity
    print('Looping through entities')
    for entity in unique_entities:
        # Create a new dataframe containing only rows with the current entity
        entity_df = df[df["sub_entity"] == entity]

        # Write the new dataframe to a CSV file named after the entity
        entity_df.to_csv(f"{entity}.csv", header=[x.upper() for x in entity_df.columns], index=False)

    print('Finished looping through entities and created csv files')

if __name__ == "__main__":
    # Create an argument parser for the input file argument
    parser = argparse.ArgumentParser(description="Split a CSV file by entity")
    parser.add_argument("input_file", help="Path to the input CSV file")

    # Parse the input file argument
    args = parser.parse_args()

    print(f"Scanning file {args.input_file}")
    # Call the split_csv_by_entity function with the input file argument
    split_csv_by_entity(args.input_file)