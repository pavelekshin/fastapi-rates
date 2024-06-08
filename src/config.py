from dotenv import find_dotenv, load_dotenv
from pydantic import RedisDsn
from pydantic_settings import BaseSettings

from src.constants import Environment

load_dotenv(find_dotenv(".env"))


class BaseConfig(BaseSettings):
    REDIS_URL: RedisDsn
    EXCHANGE_SERVICE_APIKEY: str
    APP_VERSION: str = "0.1"
    ENVIRONMENT: Environment = Environment.LOCAL
