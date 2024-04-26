# logger_aux (v0.0.5)

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
from object_info import ObjectInfo


# USAGE-1=DIRECT ===================================
logger0 = Logger()
# ObjectInfo(logger0.LOGGER).print()

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

# LOG_DIRPATH -----------------------
logger_dir = Logger("logger_dir", "c:\\1")
logger_dir.LOGGER.debug("hello_dir")

print(f"{logger_dir.LOG_DIRPATH=}")
print(f"{logger_dir.LOG_FILEPATH=}")


# USAGE-2=NESTING ===================================
class Example(Logger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def meth(self):
        self.LOGGER.debug("hello123")


Example().meth()

# ObjectInfo(logger0.LOGGER).print()
```

------------------------------
### 2. logger__Example.log
```
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line148)/thread21536::[Logger.Example] start STREAM
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line151)/thread21536::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-26 12:12:34,977[DEBUG]Example(example1.py).meth(line39)/thread21536::hello123
```

------------------------------
### 3. logger__logger_first.log
```
2024-04-26 12:12:34,970[DEBUG]logger_first(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,970[DEBUG]logger_first(main.py).__init__(line148)/thread21536::[Logger.logger_first] start STREAM
2024-04-26 12:12:34,971[DEBUG]logger_first(main.py).__init__(line151)/thread21536::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-26 12:12:34,971[DEBUG]logger_first(example1.py).<module>(line16)/thread21536::hello1-1
2024-04-26 12:12:34,974[DEBUG]logger_first(example1.py).<module>(line22)/thread21536::hello1-2
```

------------------------------
### 4. logger__logger_second.log
```
2024-04-26 12:12:34,972[DEBUG]logger_second(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,973[DEBUG]logger_second(main.py).__init__(line148)/thread21536::[Logger.logger_second] start STREAM
2024-04-26 12:12:34,973[DEBUG]logger_second(main.py).__init__(line151)/thread21536::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-26 12:12:34,973[DEBUG]logger_second(example1.py).<module>(line19)/thread21536::hello2-1
2024-04-26 12:12:34,974[DEBUG]logger_second(example1.py).<module>(line23)/thread21536::hello2-2
```

------------------------------
### 5. logger__root.log
```
2024-04-26 12:12:34,965[DEBUG]root(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,965[DEBUG]root(main.py).__init__(line148)/thread21536::[Logger.root] start STREAM
2024-04-26 12:12:34,965[DEBUG]root(main.py).__init__(line151)/thread21536::[Logger.root] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__root.log]
2024-04-26 12:12:34,965[DEBUG]root(example1.py).<module>(line10)/thread21536::None
2024-04-26 12:12:34,965[DEBUG]root(example1.py).<module>(line11)/thread21536::True
2024-04-26 12:12:34,968[DEBUG]root(example1.py).<module>(line12)/thread21536::
2024-04-26 12:12:34,968[DEBUG]root(example1.py).<module>(line13)/thread21536::hello0-1
2024-04-26 12:12:34,970[DEBUG]logger_first(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,970[DEBUG]logger_first(main.py).__init__(line148)/thread21536::[Logger.logger_first] start STREAM
2024-04-26 12:12:34,971[DEBUG]logger_first(main.py).__init__(line151)/thread21536::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-26 12:12:34,971[DEBUG]logger_first(example1.py).<module>(line16)/thread21536::hello1-1
2024-04-26 12:12:34,972[DEBUG]logger_second(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,973[DEBUG]logger_second(main.py).__init__(line148)/thread21536::[Logger.logger_second] start STREAM
2024-04-26 12:12:34,973[DEBUG]logger_second(main.py).__init__(line151)/thread21536::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-26 12:12:34,973[DEBUG]logger_second(example1.py).<module>(line19)/thread21536::hello2-1
2024-04-26 12:12:34,974[DEBUG]root(example1.py).<module>(line21)/thread21536::hello0-2
2024-04-26 12:12:34,974[DEBUG]logger_first(example1.py).<module>(line22)/thread21536::hello1-2
2024-04-26 12:12:34,974[DEBUG]logger_second(example1.py).<module>(line23)/thread21536::hello2-2
2024-04-26 12:12:34,975[DEBUG]logger_dir(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,975[DEBUG]logger_dir(main.py).__init__(line148)/thread21536::[Logger.logger_dir] start STREAM
2024-04-26 12:12:34,976[DEBUG]logger_dir(main.py).__init__(line151)/thread21536::[Logger.logger_dir] start FILE=[c:\1\logger__logger_dir.log]
2024-04-26 12:12:34,976[DEBUG]logger_dir(example1.py).<module>(line27)/thread21536::hello_dir
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line145)/thread21536::====================================================================================================
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line148)/thread21536::[Logger.Example] start STREAM
2024-04-26 12:12:34,977[DEBUG]Example(main.py).__init__(line151)/thread21536::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-26 12:12:34,977[DEBUG]Example(example1.py).meth(line39)/thread21536::hello123
```

********************************************************************************
