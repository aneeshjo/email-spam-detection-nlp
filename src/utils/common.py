from pathlib import Path
from box import ConfigBox
from src.logger import logging
from typing import List

import yaml


def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox.
    """
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)

        logging.info(f"YAML file loaded successfully: {path_to_yaml}")

        return ConfigBox(content)