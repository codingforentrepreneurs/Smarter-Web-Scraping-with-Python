import pathlib
from functools import lru_cache

from decouple import Config, RepositoryEnv

HELPERS_MODULE_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = HELPERS_MODULE_DIR.parent
BASE_DIR_ENV_PATH = BASE_DIR / ".env"
REPO_DIR = BASE_DIR.parent
REPO_DIR_ENV_PATH = REPO_DIR / ".env"

@lru_cache
def get_config():
    if BASE_DIR_ENV_PATH.exists():
        return Config(RepositoryEnv(str(BASE_DIR_ENV_PATH)))
    if REPO_DIR_ENV_PATH.exists():
        return Config(RepositoryEnv(str(REPO_DIR_ENV_PATH)))
    from decouple import config
    return config


config = get_config()