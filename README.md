# logger_aux (v0.0.1)

## DESCRIPTION_SHORT
simple logging

## DESCRIPTION_LONG
designed for DRY simple/easy usage logging


## Features
1. keep all mostly used code in hidden class  


********************************************************************************
## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install logger-aux
```


## Import
```python
from logger_aux import *
```


********************************************************************************
## USAGE EXAMPLES
See tests and sourcecode for other examples.

------------------------------
### 1. example1.py
```python
from logger_aux import *

# NAMES -----------------------
logger0 = Logger()
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
```

------------------------------
### 2. logger__logger_first.log
```python
2024-04-25 15:41:46,314[DEBUG](logger_first(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,316[DEBUG](logger_first(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='C:\\__STARICHENKO_Element\\PROJECTS\\abc=logger_aux\\EXAMPLES\\logger__logger_first.log'
2024-04-25 15:41:46,316[DEBUG](logger_first(example1.py).<module>/thread19648(line8))hello1-1
2024-04-25 15:41:46,319[DEBUG](logger_first(example1.py).<module>/thread19648(line14))hello1-2
```

------------------------------
### 3. logger__logger_second.log
```python
2024-04-25 15:41:46,318[DEBUG](logger_second(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,318[DEBUG](logger_second(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='C:\\__STARICHENKO_Element\\PROJECTS\\abc=logger_aux\\EXAMPLES\\logger__logger_second.log'
2024-04-25 15:41:46,318[DEBUG](logger_second(example1.py).<module>/thread19648(line11))hello2-1
2024-04-25 15:41:46,319[DEBUG](logger_second(example1.py).<module>/thread19648(line15))hello2-2
```

------------------------------
### 4. logger__root.log
```python
2024-04-25 15:41:46,312[DEBUG](root(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,313[DEBUG](root(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='C:\\__STARICHENKO_Element\\PROJECTS\\abc=logger_aux\\EXAMPLES\\logger__root.log'
2024-04-25 15:41:46,313[DEBUG](root(example1.py).<module>/thread19648(line5))hello0-1
2024-04-25 15:41:46,314[DEBUG](logger_first(main.py).__init__/thread19648(line105))logger STREAM started
2024-04-25 15:41:46,314[DEBUG](logger_first(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,316[DEBUG](logger_first(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='C:\\__STARICHENKO_Element\\PROJECTS\\abc=logger_aux\\EXAMPLES\\logger__logger_first.log'
2024-04-25 15:41:46,316[DEBUG](logger_first(example1.py).<module>/thread19648(line8))hello1-1
2024-04-25 15:41:46,317[DEBUG](logger_second(main.py).__init__/thread19648(line105))logger STREAM started
2024-04-25 15:41:46,318[DEBUG](logger_second(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,318[DEBUG](logger_second(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='C:\\__STARICHENKO_Element\\PROJECTS\\abc=logger_aux\\EXAMPLES\\logger__logger_second.log'
2024-04-25 15:41:46,318[DEBUG](logger_second(example1.py).<module>/thread19648(line11))hello2-1
2024-04-25 15:41:46,319[DEBUG](root(example1.py).<module>/thread19648(line13))hello0-2
2024-04-25 15:41:46,319[DEBUG](logger_first(example1.py).<module>/thread19648(line14))hello1-2
2024-04-25 15:41:46,319[DEBUG](logger_second(example1.py).<module>/thread19648(line15))hello2-2
2024-04-25 15:41:46,320[DEBUG](logger_dir(main.py).__init__/thread19648(line105))logger STREAM started
2024-04-25 15:41:46,321[DEBUG](logger_dir(main.py).__init__/thread19648(line112))====================================================================================================
2024-04-25 15:41:46,321[DEBUG](logger_dir(main.py).__init__/thread19648(line113))logger FILE started self._handler_file.baseFilename='c:\\1\\logger__logger_dir.log'
2024-04-25 15:41:46,321[DEBUG](logger_dir(example1.py).<module>/thread19648(line19))hello_dir
```

********************************************************************************
