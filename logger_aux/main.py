from typing import *
import pathlib
import logging
from logging.handlers import RotatingFileHandler


# =====================================================================================================================
def _example():
    LEVEL = logging.DEBUG
    PATTERN = '%(asctime)s[%(levelname)s](%(name)s(%(filename)s).%(funcName)s/thread%(thread)s(line%(lineno)d))%(msg)s'
    formatter = logging.Formatter(PATTERN)

    logger = logging.getLogger()
    logger.setLevel(LEVEL)

    handler_file = logging.FileHandler(f"SerialServer_Base.log")
    handler_file.setLevel(LEVEL)
    handler_file.setFormatter(formatter)
    logger.addHandler(handler_file)

    handler_stream = logging.StreamHandler()
    handler_stream.setLevel(LEVEL)
    handler_stream.setFormatter(formatter)
    logger.addHandler(handler_stream)

    # logger.log(10, 'ЛОГ10')   #DEBUG=ЛОГ10
    # logger.log(11, 'ЛОГ11')   #Level 11=ЛОГ11
    logger.warning('MSG_DEFAULT')     # 2024-03-19 15:27:21,644[WARNING](root(t001.py).<module>/thread18536(line21))MSG_DEFAULT


# =====================================================================================================================
class Logger:
    # SETTINGS ---------------------------------------
    NAME: None | str = None     # None="root"

    LEVEL: int = logging.DEBUG
    PATTERN: str = '%(asctime)s[%(levelname)s](%(name)s(%(filename)s).%(funcName)s/thread%(thread)s(line%(lineno)d))%(msg)s'

    DIRPATH: None | pathlib.Path = None

    FILENAME_START: None | str = None
    FILENAME_EXTENTION: None | str = None
    FILE_MAXBYTES: int = 1024*100
    FILE_BACKUPCOUNT: int = 3

    USE_STREAM: bool = True
    USE_FILE: bool = True

    # AUX ---------------------------------------
    _formatter: logging.Formatter

    @property
    def FILENAME(self) -> str:
        return f"{self.FILENAME_START or 'logger'}__{self.NAME or 'root'}.{self.FILENAME_EXTENTION or 'log'}"

    @property
    def FILEPATH(self) -> pathlib.Path:
        if self.DIRPATH is None:
            return pathlib.Path(self.FILENAME)
        else:
            return self.DIRPATH.joinpath(self.FILENAME)

    def __init__(
            self,
            name: None | str = None,
            dirpath: None | str | pathlib.Path = None,
            level: None | int = None,
            use_stream: None | bool = None,
            use_file: None | bool = None,
    ):
        # PARAMS ------------------------------------------
        if name is not None:
            self.NAME = name

        if dirpath is not None:
            self.DIRPATH = pathlib.Path(dirpath)

        if level is not None:
            self.LEVEL = level

        if use_stream is not None:
            self.USE_STREAM = use_stream

        if use_file is not None:
            self.USE_FILE = use_file

        # PREPARE ------------------------------------------
        # TODO: create DIRPATH

        # INIT ---------------------------------------------
        self.LOGGER = logging.getLogger(self.NAME)
        self.LOGGER.setLevel(self.LEVEL)

        self._formatter = logging.Formatter(self.PATTERN)

        self._handler_stream = None
        self._handler_file = None

        # WORK ---------------------------------------------
        if self.USE_STREAM:
            self._handler_stream = logging.StreamHandler()
            # self._handler_stream.setLevel(self.LEVEL)
            self._handler_stream.setFormatter(self._formatter)
            self.LOGGER.addHandler(self._handler_stream)
            self.LOGGER.debug(f"logger STREAM started")

        if self.USE_FILE:
            self._handler_file = RotatingFileHandler(self.FILEPATH, maxBytes=self.FILE_MAXBYTES, backupCount=self.FILE_BACKUPCOUNT)
            # self._handler_file.setLevel(self.LEVEL)
            self._handler_file.setFormatter(self._formatter)
            self.LOGGER.addHandler(self._handler_file)
            self.LOGGER.debug("="*100)
            self.LOGGER.debug(f"logger FILE started {self._handler_file.baseFilename=}")


# =====================================================================================================================
if __name__ == "__main__":
    pass


# =====================================================================================================================
