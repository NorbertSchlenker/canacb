#!/bin/env python3
"""Canadian ACB calculator - configuration"""

import os


APP_NAME = "CAN-ACB"
APP_VERSION = "0.3"
APP_AUTHORS = "Norbert Schlenker"
APP_LICENSE = "MIT"

SRC_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SRC_FOLDER, "data", "canacb.json")
MENU_IMAGE = os.path.join(SRC_FOLDER, "images", "tinyleaf.png")
COPY_IMAGE = os.path.join(SRC_FOLDER, "images", "tinycopy.png")
