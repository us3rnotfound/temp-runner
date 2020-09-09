# config_parser.py file

import yaml

def read_config():
    with open(r'config.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        config_dict = yaml.load(file, Loader=yaml.FullLoader)
        return config_dict

def write_config(config_dict):
    with open(r'config.yaml', 'w') as file:
        yaml.dump(config_dict, file)