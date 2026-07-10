"""
Project Template Generator
--------------------------
This script creates the complete folder and file structure
for the Brain Tumor Classification project.

Run:
    python template.py
"""

from pathlib import Path
import os
import logging

# ==========================================================
# Logging Configuration
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s:"
)

logging.info("Template creation started...")

list_of_files=[
    # Configuration
    "config/config.yaml",
    "config/params.yaml",

    # Research & Notebooks
    "research/trials.ipynb",
    "notebook/01_data_exploration.ipynb",
    "notebook/02_model_experiment.ipynb",

    # Root Files
    "README.md",
    "requirements.txt",
    "setup.py",
    ".gitignore",

    # Application
    "app.py",
    "main.py",

    "src/__init__.py",
    "src/components/__init__.py",
    "src/config/__init__.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",

    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",


    "src/config/configuration.py",

    "src/entity/config_entity.py",

    # Pipeline
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    "src/utils/common.py",

    "src/logger.py",
    "src/exception.py",

    # Test Folder
    "tests/__init__.py",

    # Artifacts
    "artifacts/.gitkeep"

]

# Iterate through each file path in the provided list
for file_path in list_of_files:
    
    # Ensure file_path is a Path object (safe for filesystem operations)
    file_path = Path(file_path)

    # Extract the parent directory of the file
    file_dir = file_path.parent

    
    file_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    logging.info(
        f"Ensured directory exists: {file_dir}"
    )
    # If the file itself does not exist, create an empty file
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    else:
        # If the file already exists, log that information
        logging.info(f"File already exists: {file_path}")
    
   
        

        


