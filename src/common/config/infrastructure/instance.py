import os
from common.config.infrastructure.config import Config

__APP_ENV = os.getenv("APP_ENV")
config = Config(env_path = f"../config/.{__APP_ENV}.env")