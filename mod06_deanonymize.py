import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux



def link_records(anon_df, aux_df):
    merged = pd.merge(
        anon_df,
        aux_df,
        on=["age", "gender", "zip3"]
    )
    counts = merged.groupby("anon_id")["name"].transform("count")
    unique_matches = merged[counts == 1].copy()
    return unique_matches[["anon_id", "name"]].rename(
        columns={"name": "matched_name"}
    )




def deanonymization_rate(matches_df, anon_df):
    rate = len(matches_df) / len(anon_df)
    return rate

