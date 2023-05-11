import pandas as pd

class CSVSplitter:
    def __init__(self, input_file):
        self.df = pd.read_csv(input_file)
        self.unique_entities = self.df["sub_entity"].unique()
    
    def split_by_entity(self):
        for entity in self.unique_entities:
            entity_df = self.df[self.df["sub_entity"] == entity]
            entity_df.to_csv(f"{entity}.csv", header=[x.upper() for x in entity_df.columns], index=False)

        print('Finished looping through entities and created csv')