import yaml
import os
from ultralytics import YOLO


def verify_model_loading(model_name):
    """
    Verify that a YOLO model can be loaded by name using ultralytics.

    :param model_name: Name of the YOLO model to load.
    :return: None
    """
    try:
        _ = YOLO(model_name)
        print(f"Successfully loaded model: {model_name}")
    except Exception as e:
        print(f"Failed to load model: {model_name}. Error: {e}")


if __name__ == "__main__":
    yaml_file_path = "models.yaml"
    size = ["small", 'medium', 'large', 'xlarge']

    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)

    for s in size:
        models = config[s]
        for model_name in models:
            verify_model_loading(os.path.join(config['DATA_PATH'], model_name))
