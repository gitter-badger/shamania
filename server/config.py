import os
from enum import Enum


class OutputMode(Enum):
    VERBOSE = 1
    DEBUG = 2
    MINIMAL = 3

APP_NAME = 'Shamania'
OUTPUT_MODE = OutputMode.VERBOSE
TEMPLATES_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'templates'
)
TEMPLATE_EXTENSION = '.j2'
