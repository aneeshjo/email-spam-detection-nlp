from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_file:Path
    local_data_file:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path
    data_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    input_data_file:Path
    transformed_data_file:Path
    

# ==========================================================
# Model Trainer Configuration
# ==========================================================

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    input_data_file: Path
    model_file: Path
    vectorizer_file: Path

    test_size: float
    random_state: int
    stratify: bool

# ==========================================================
# Model Evaluation Configuration
# ==========================================================

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    input_data_file: Path
    model_file: Path
    vectorizer_file: Path
    metric_file: Path

    test_size: float
    random_state: int
    stratify: bool

@dataclass(frozen=True)
class PredictionConfig:
    model_file: Path
    vectorizer_file: Path
