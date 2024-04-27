import os
import time
import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
from logger_aux import *


# =====================================================================================================================
class Test__1:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass
        # self.VICTIM = type("VICTIM", (Logger,), {})

    def teardown_method(self, method):
        pass

    # -----------------------------------------------------------------------------------------------------------------
    def test__maxRecursion(self):
        class Victim(Logger):
            pass

        victim = Victim()
        for i in range(3):
            victim.LOGGER.debug(f"hello-{i}")

        assert True

    def test__disable(self):
        class VictimDisabled(Logger):
            LOG_ENABLE = False

        victim = VictimDisabled()
        victim.LOGGER.debug(f"VictimDisabled")

        time.sleep(0.2)

        assert not victim.LOG_FILEPATH.exists()


# =====================================================================================================================
