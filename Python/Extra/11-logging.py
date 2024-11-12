import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Neural Nine Logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")
