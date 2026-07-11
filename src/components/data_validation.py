import sys
from pathlib import Path

import pandas as pd

from src.entity.config_entity import DataValidationConfig
from src.exception import CustomException
from src.logger import logging

class DataValidation:

    EXPECTED_COLUMNS = {"label", "message"}
    EXPECTED_LABELS = {"ham", "spam"}

    def __init__(self, config: DataValidationConfig):
        self.config = config
    def validate_dataset(self) -> bool:
        try:
            logging.info("Starting data validation...")

            df = pd.read_csv(self.config.data_file)

            if set(df.columns) != self.EXPECTED_COLUMNS:
                raise ValueError(
                    f"Expected columns {self.EXPECTED_COLUMNS}, "
                    f"but found {set(df.columns)}"
                )
            missing_values = df.isnull().sum().sum()

            if missing_values > 0:
                raise ValueError(
                    f"Dataset contains {missing_values} missing values."
                )
            labels = set(df["label"].unique())

            if not labels.issubset(self.EXPECTED_LABELS):
                raise ValueError(
                    f"Unexpected labels found: {labels}"
                )
            duplicate_rows = df.duplicated().sum()

            status = (
                "STATUS: PASS\n"
                f"Rows: {len(df)}\n"
                f"Columns: {list(df.columns)}\n"
                f"Missing Values: {missing_values}\n"
                f"Duplicate Rows: {duplicate_rows}\n"
                f"Labels: {sorted(labels)}\n"
            )
            with open(self.config.status_file, "w") as f:
                f.write(status)

            logging.info("Data validation completed successfully.")
            return True
        except Exception as e:

            logging.exception("Data validation failed.")

            raise CustomException(e, sys)