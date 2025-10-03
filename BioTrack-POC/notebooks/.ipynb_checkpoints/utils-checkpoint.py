import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000"

def fetch_observacoes() -> pd.DataFrame:
    """Fetches observations from the API and returns them in a Pandas DataFrame"""
    resp = requests.get(f"{API_URL}/observacoes/")
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data)

    # Normalizes column condicoes (JSON) for individual columns
    if "condicoes" in df.columns:
        cond_df = pd.json_normalize(df["condicoes"])
        df = pd.concat([df.drop(columns=["condicoes"]), cond_df], axis=1)
    return df

