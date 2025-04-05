import json
from pathlib import Path

def load_class_index():
    with open(Path(__file__).parent / 'imagenet_class_index.json') as f: # like home/Downloads/image_net_.json
        return json.load(f) # dictionary

# __name__ / __path__ contains the current path of file / current name of file