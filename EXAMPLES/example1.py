from logger_aux import *

# NAMES -----------------------
logger0 = Logger()
# logger0.LOGGER.debug()    # TypeError: Logger.debug() missing 1 required positional argument: 'msg'
logger0.LOGGER.debug(None)  # OK
logger0.LOGGER.debug(True)  # OK
logger0.LOGGER.debug("")    # OK
logger0.LOGGER.debug("hello0-1")

logger1 = Logger("logger_first")
logger1.LOGGER.debug("hello1-1")

logger2 = Logger("logger_second")
logger2.LOGGER.debug("hello2-1")

logger0.LOGGER.debug("hello0-2")
logger1.LOGGER.debug("hello1-2")
logger2.LOGGER.debug("hello2-2")

# DIRPATH -----------------------
logger_dir = Logger("logger_dir", "c:\\1")
logger_dir.LOGGER.debug("hello_dir")

print(f"{logger_dir.DIRPATH=}")
print(f"{logger_dir.FILEPATH=}")
