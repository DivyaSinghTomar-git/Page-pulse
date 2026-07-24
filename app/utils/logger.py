import logging
import json


logger = logging.getLogger("pagepulse")

logging.basicConfig(level=logging.INFO)


def log(data):
    logger.info(json.dumps(data))