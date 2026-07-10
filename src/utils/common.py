from pathlib import Path
from box import ConfigBox
from src.logger import logging
from src.exception import CustomException
import sys
from typing import Iterable
import yaml


def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file) or {}

            logging.info(f"YAML file loaded successfully: {path_to_yaml}")

            return ConfigBox(content)
    except Exception as e:
        logging.exception(
            f"Failed to load YAML file: {path_to_yaml}"
        )
        raise CustomException(e, sys)
    
def create_directories(path_to_directories: Iterable[Path], verbose=True):
    """
    Create multiple directories.
    """
    for path in path_to_directories:
        Path(path).mkdir(
            parents=True,
            exist_ok=True
        )

        if verbose:
            logging.info(
                f"Created directory: {path}"
            )