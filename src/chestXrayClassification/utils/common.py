import os
import yaml

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml, "r") as yaml_file:
        return yaml.safe_load(yaml_file)

def create_directories(path_to_directories: list):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
