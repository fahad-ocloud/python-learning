import logging

logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger("OCloud Logger")
logger.setLevel(level=logging.DEBUG)

handler = logging.FileHandler("myLog.log")
logger.setLevel(level=logging.INFO)

formatter =logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("debug mails mails")
logger.info("info mails mails")