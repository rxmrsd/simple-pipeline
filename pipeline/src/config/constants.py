"""constants.py"""
import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID", "")
LOCATION = os.environ.get("LOCATION", "")
PIPELINE_ROOT = os.environ.get("PIPELINE_ROOT", "")
SERVICE_ACCOUNT = os.environ.get("SERVICE_ACCOUNT", "")
BUILD_ACCOUNT = os.environ.get("BUILD_ACCOUNT", "")
REGISTY_PATH = os.environ.get("REGISTY_PATH", "")
