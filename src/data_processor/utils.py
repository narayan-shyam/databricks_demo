# src/data_processor/utils.py
def calculate_metrics(df: pd.DataFrame) -> Dict:
    return {
        "total_records": len(df),
        "average_value": df["value"].mean() if "value" in df else 0,
    }
