# src/data_processor/processor.py
from typing import Dict, List
import pandas as pd


class DataProcessor:
    def __init__(self, spark_session=None):
        self.spark = spark_session

    def process_data(self, data: List[Dict]) -> pd.DataFrame:
        df = pd.DataFrame(data)
        df["processed_date"] = pd.Timestamp.now()
        return df

    def validate_schema(self, df: pd.DataFrame) -> bool:
        required_columns = ["id", "value"]
        return all(col in df.columns for col in required_columns)
