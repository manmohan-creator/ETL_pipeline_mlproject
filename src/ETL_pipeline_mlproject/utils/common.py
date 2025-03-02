import os
import yaml
from src.ETL_pipeline_mlproject import logger
import json
import logging
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

    
from src.ETL_pipeline_mlproject import logger
import yaml
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            logger.error(f"YAML file {path_to_yaml} is empty or not formatted correctly.")
            raise ValueError("YAML file is empty or invalid.")

        logger.info(f"YAML file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)

    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise ValueError("YAML file is empty or invalid.")
    except Exception as e:
        logger.error(f"Error loading YAML file {path_to_yaml}: {e}")
        raise e

    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create list of directories
    Args: 
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created.
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    "save json data"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    "load json files data"
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    "save binary files"
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    "load binary data"

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data