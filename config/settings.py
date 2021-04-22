import os
import sys
import json

from pathlib import Path


# ROOT_DIR = os.path.abspath(__file__)
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

print(ROOT_DIR)