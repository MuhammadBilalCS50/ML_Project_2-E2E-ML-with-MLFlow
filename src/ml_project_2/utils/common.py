import os
from box.exceptions import BoxValueError
import yaml
from ml_Project_2 import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded file {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"{path} directory has been created successfully")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at path: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"json file {path} has been loaded successfully")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    with open(path, "w") as f:
        joblib.dump(value=data, filename=path)
    logger.info(f"bin file saved at path: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    with open(path) as bin_file:
        content = joblib.load(bin_file)
    logger.info(f"bin file {path} has been loaded successfully")
    return content


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"


