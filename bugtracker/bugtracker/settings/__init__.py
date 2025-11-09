import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env_type = os.getenv("ENV_TYPE", "dev")
env_path = BASE_DIR / ".env" / f".{env_type}"
load_dotenv(dotenv_path=env_path)