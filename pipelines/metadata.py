import pandas as pd
from datetime import datetime

def update_metadata(file_path, records: list):

    df = pd.DataFrame(records)

    df["ingested_at"] = datetime.utcnow()

    if file_path.exists():
        old = pd.read_csv(file_path)
        df = pd.concat([old, df], ignore_index=True)
        df = df.drop_duplicates(subset=["url"], keep="last")

    df.to_csv(file_path, index=False)