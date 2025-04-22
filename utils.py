import yaml
import os


def load_config():
    with open('models.yaml', 'r') as file:
        configs = yaml.safe_load(file)

    config_path = 'config.yaml' if os.path.isfile('config.yaml') else 'default_config.yaml'
    with open(config_path, 'r') as file:
        configs.update(yaml.safe_load(file))
    
    return configs