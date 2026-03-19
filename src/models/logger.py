from logging import getLogger
from logging.config import dictConfig

from src.config import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
logger = getLogger()