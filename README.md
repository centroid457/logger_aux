# logger_aux (v0.0.10)

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
logger0 = Logger(log_enable=True)
# ObjectInfo(logger0.LOGGER).print()

# logger0.LOGGER.debug()    # TypeError: Logger.debug() missing 1 required positional argument: 'msg'
logger0.LOGGER.debug(None)  # OK
logger0.LOGGER.debug(True)  # OK
logger0.LOGGER.debug("")    # OK
logger0.LOGGER.debug("hello0-1")

logger1 = Logger("logger_first", log_enable=True)
logger1.LOGGER.debug("hello1-1")

logger2 = Logger("logger_second", log_enable=True)
logger2.LOGGER.debug("hello2-1")

logger0.LOGGER.debug("hello0-2")
logger1.LOGGER.debug("hello1-2")
logger2.LOGGER.debug("hello2-2")

# LOG_DIRPATH -----------------------
logger_dir = Logger("logger_dir", "c:\\1", log_enable=True)
logger_dir.LOGGER.debug("hello_dir")

print(f"{logger_dir.LOG_DIRPATH=}")
print(f"{logger_dir.LOG_FILEPATH=}")


# USAGE-2=NESTING ===================================
class Example(Logger):
    LOG_ENABLE = True

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
2024-04-27 14:55:45,097[DEBUG]Example(main.py).__init__(line152)/thread50340::====================================================================================================
2024-04-27 14:55:45,098[DEBUG]Example(main.py).__init__(line155)/thread50340::[Logger.Example] start STREAM
2024-04-27 14:55:45,098[DEBUG]Example(main.py).__init__(line158)/thread50340::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:55:45,098[DEBUG]Example(example1.py).meth(line41)/thread50340::hello123
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line155)/thread39932::[Logger.Example] start STREAM
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line158)/thread39932::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:56:35,121[DEBUG]Example(example1.py).meth(line41)/thread39932::hello123
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line155)/thread31224::[Logger.Example] start STREAM
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line158)/thread31224::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:56:41,420[DEBUG]Example(example1.py).meth(line41)/thread31224::hello123
2024-04-27 14:57:41,958[DEBUG]Example(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,959[DEBUG]Example(main.py).__init__(line155)/thread32520::[Logger.Example] start STREAM
2024-04-27 14:57:41,959[DEBUG]Example(main.py).__init__(line158)/thread32520::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:57:41,959[DEBUG]Example(example1.py).meth(line41)/thread32520::hello123
2024-04-27 15:27:49,968[DEBUG]Example(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,968[DEBUG]Example(main.py).__init__(line155)/thread28020::[Logger.Example] start STREAM
2024-04-27 15:27:49,969[DEBUG]Example(main.py).__init__(line158)/thread28020::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 15:27:49,969[DEBUG]Example(example1.py).meth(line41)/thread28020::hello123
```

------------------------------
### 3. logger__logger_first.log
```
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line155)/thread39932::[Logger.logger_first] start STREAM
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line158)/thread39932::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:56:35,115[DEBUG]logger_first(example1.py).<module>(line16)/thread39932::hello1-1
2024-04-27 14:56:35,117[DEBUG]logger_first(example1.py).<module>(line22)/thread39932::hello1-2
2024-04-27 14:56:41,414[DEBUG]logger_first(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,414[DEBUG]logger_first(main.py).__init__(line155)/thread31224::[Logger.logger_first] start STREAM
2024-04-27 14:56:41,415[DEBUG]logger_first(main.py).__init__(line158)/thread31224::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:56:41,415[DEBUG]logger_first(example1.py).<module>(line16)/thread31224::hello1-1
2024-04-27 14:56:41,417[DEBUG]logger_first(example1.py).<module>(line22)/thread31224::hello1-2
2024-04-27 14:57:41,954[DEBUG]logger_first(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,954[DEBUG]logger_first(main.py).__init__(line155)/thread32520::[Logger.logger_first] start STREAM
2024-04-27 14:57:41,955[DEBUG]logger_first(main.py).__init__(line158)/thread32520::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:57:41,955[DEBUG]logger_first(example1.py).<module>(line16)/thread32520::hello1-1
2024-04-27 14:57:41,957[DEBUG]logger_first(example1.py).<module>(line22)/thread32520::hello1-2
2024-04-27 15:27:49,963[DEBUG]logger_first(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,963[DEBUG]logger_first(main.py).__init__(line155)/thread28020::[Logger.logger_first] start STREAM
2024-04-27 15:27:49,964[DEBUG]logger_first(main.py).__init__(line158)/thread28020::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 15:27:49,964[DEBUG]logger_first(example1.py).<module>(line16)/thread28020::hello1-1
2024-04-27 15:27:49,966[DEBUG]logger_first(example1.py).<module>(line22)/thread28020::hello1-2
```

------------------------------
### 4. logger__logger_second.log
```
2024-04-27 14:56:35,115[DEBUG]logger_second(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,116[DEBUG]logger_second(main.py).__init__(line155)/thread39932::[Logger.logger_second] start STREAM
2024-04-27 14:56:35,116[DEBUG]logger_second(main.py).__init__(line158)/thread39932::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:56:35,116[DEBUG]logger_second(example1.py).<module>(line19)/thread39932::hello2-1
2024-04-27 14:56:35,117[DEBUG]logger_second(example1.py).<module>(line23)/thread39932::hello2-2
2024-04-27 14:56:41,415[DEBUG]logger_second(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,415[DEBUG]logger_second(main.py).__init__(line155)/thread31224::[Logger.logger_second] start STREAM
2024-04-27 14:56:41,416[DEBUG]logger_second(main.py).__init__(line158)/thread31224::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:56:41,416[DEBUG]logger_second(example1.py).<module>(line19)/thread31224::hello2-1
2024-04-27 14:56:41,417[DEBUG]logger_second(example1.py).<module>(line23)/thread31224::hello2-2
2024-04-27 14:57:41,955[DEBUG]logger_second(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,956[DEBUG]logger_second(main.py).__init__(line155)/thread32520::[Logger.logger_second] start STREAM
2024-04-27 14:57:41,956[DEBUG]logger_second(main.py).__init__(line158)/thread32520::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:57:41,956[DEBUG]logger_second(example1.py).<module>(line19)/thread32520::hello2-1
2024-04-27 14:57:41,957[DEBUG]logger_second(example1.py).<module>(line23)/thread32520::hello2-2
2024-04-27 15:27:49,964[DEBUG]logger_second(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,965[DEBUG]logger_second(main.py).__init__(line155)/thread28020::[Logger.logger_second] start STREAM
2024-04-27 15:27:49,965[DEBUG]logger_second(main.py).__init__(line158)/thread28020::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 15:27:49,966[DEBUG]logger_second(example1.py).<module>(line19)/thread28020::hello2-1
2024-04-27 15:27:49,966[DEBUG]logger_second(example1.py).<module>(line23)/thread28020::hello2-2
```

------------------------------
### 5. logger__root.log
```
2024-04-27 14:56:35,111[DEBUG]root(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,111[DEBUG]root(main.py).__init__(line155)/thread39932::[Logger.root] start STREAM
2024-04-27 14:56:35,112[DEBUG]root(main.py).__init__(line158)/thread39932::[Logger.root] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__root.log]
2024-04-27 14:56:35,112[DEBUG]root(example1.py).<module>(line10)/thread39932::None
2024-04-27 14:56:35,112[DEBUG]root(example1.py).<module>(line11)/thread39932::True
2024-04-27 14:56:35,113[DEBUG]root(example1.py).<module>(line12)/thread39932::
2024-04-27 14:56:35,113[DEBUG]root(example1.py).<module>(line13)/thread39932::hello0-1
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line155)/thread39932::[Logger.logger_first] start STREAM
2024-04-27 14:56:35,114[DEBUG]logger_first(main.py).__init__(line158)/thread39932::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:56:35,115[DEBUG]logger_first(example1.py).<module>(line16)/thread39932::hello1-1
2024-04-27 14:56:35,115[DEBUG]logger_second(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,116[DEBUG]logger_second(main.py).__init__(line155)/thread39932::[Logger.logger_second] start STREAM
2024-04-27 14:56:35,116[DEBUG]logger_second(main.py).__init__(line158)/thread39932::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:56:35,116[DEBUG]logger_second(example1.py).<module>(line19)/thread39932::hello2-1
2024-04-27 14:56:35,117[DEBUG]root(example1.py).<module>(line21)/thread39932::hello0-2
2024-04-27 14:56:35,117[DEBUG]logger_first(example1.py).<module>(line22)/thread39932::hello1-2
2024-04-27 14:56:35,117[DEBUG]logger_second(example1.py).<module>(line23)/thread39932::hello2-2
2024-04-27 14:56:35,118[DEBUG]logger_dir(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,118[DEBUG]logger_dir(main.py).__init__(line155)/thread39932::[Logger.logger_dir] start STREAM
2024-04-27 14:56:35,119[DEBUG]logger_dir(main.py).__init__(line158)/thread39932::[Logger.logger_dir] start FILE=[c:\1\logger__logger_dir.log]
2024-04-27 14:56:35,119[DEBUG]logger_dir(example1.py).<module>(line27)/thread39932::hello_dir
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line152)/thread39932::====================================================================================================
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line155)/thread39932::[Logger.Example] start STREAM
2024-04-27 14:56:35,120[DEBUG]Example(main.py).__init__(line158)/thread39932::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:56:35,121[DEBUG]Example(example1.py).meth(line41)/thread39932::hello123
2024-04-27 14:56:41,413[DEBUG]root(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,413[DEBUG]root(main.py).__init__(line155)/thread31224::[Logger.root] start STREAM
2024-04-27 14:56:41,413[DEBUG]root(main.py).__init__(line158)/thread31224::[Logger.root] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__root.log]
2024-04-27 14:56:41,413[DEBUG]root(example1.py).<module>(line10)/thread31224::None
2024-04-27 14:56:41,413[DEBUG]root(example1.py).<module>(line11)/thread31224::True
2024-04-27 14:56:41,414[DEBUG]root(example1.py).<module>(line12)/thread31224::
2024-04-27 14:56:41,414[DEBUG]root(example1.py).<module>(line13)/thread31224::hello0-1
2024-04-27 14:56:41,414[DEBUG]logger_first(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,414[DEBUG]logger_first(main.py).__init__(line155)/thread31224::[Logger.logger_first] start STREAM
2024-04-27 14:56:41,415[DEBUG]logger_first(main.py).__init__(line158)/thread31224::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:56:41,415[DEBUG]logger_first(example1.py).<module>(line16)/thread31224::hello1-1
2024-04-27 14:56:41,415[DEBUG]logger_second(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,415[DEBUG]logger_second(main.py).__init__(line155)/thread31224::[Logger.logger_second] start STREAM
2024-04-27 14:56:41,416[DEBUG]logger_second(main.py).__init__(line158)/thread31224::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:56:41,416[DEBUG]logger_second(example1.py).<module>(line19)/thread31224::hello2-1
2024-04-27 14:56:41,417[DEBUG]root(example1.py).<module>(line21)/thread31224::hello0-2
2024-04-27 14:56:41,417[DEBUG]logger_first(example1.py).<module>(line22)/thread31224::hello1-2
2024-04-27 14:56:41,417[DEBUG]logger_second(example1.py).<module>(line23)/thread31224::hello2-2
2024-04-27 14:56:41,417[DEBUG]logger_dir(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,418[DEBUG]logger_dir(main.py).__init__(line155)/thread31224::[Logger.logger_dir] start STREAM
2024-04-27 14:56:41,418[DEBUG]logger_dir(main.py).__init__(line158)/thread31224::[Logger.logger_dir] start FILE=[c:\1\logger__logger_dir.log]
2024-04-27 14:56:41,418[DEBUG]logger_dir(example1.py).<module>(line27)/thread31224::hello_dir
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line152)/thread31224::====================================================================================================
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line155)/thread31224::[Logger.Example] start STREAM
2024-04-27 14:56:41,419[DEBUG]Example(main.py).__init__(line158)/thread31224::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:56:41,420[DEBUG]Example(example1.py).meth(line41)/thread31224::hello123
2024-04-27 14:57:41,953[DEBUG]root(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,953[DEBUG]root(main.py).__init__(line155)/thread32520::[Logger.root] start STREAM
2024-04-27 14:57:41,953[DEBUG]root(main.py).__init__(line158)/thread32520::[Logger.root] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__root.log]
2024-04-27 14:57:41,953[DEBUG]root(example1.py).<module>(line10)/thread32520::None
2024-04-27 14:57:41,954[DEBUG]root(example1.py).<module>(line11)/thread32520::True
2024-04-27 14:57:41,954[DEBUG]root(example1.py).<module>(line12)/thread32520::
2024-04-27 14:57:41,954[DEBUG]root(example1.py).<module>(line13)/thread32520::hello0-1
2024-04-27 14:57:41,954[DEBUG]logger_first(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,954[DEBUG]logger_first(main.py).__init__(line155)/thread32520::[Logger.logger_first] start STREAM
2024-04-27 14:57:41,955[DEBUG]logger_first(main.py).__init__(line158)/thread32520::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 14:57:41,955[DEBUG]logger_first(example1.py).<module>(line16)/thread32520::hello1-1
2024-04-27 14:57:41,955[DEBUG]logger_second(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,956[DEBUG]logger_second(main.py).__init__(line155)/thread32520::[Logger.logger_second] start STREAM
2024-04-27 14:57:41,956[DEBUG]logger_second(main.py).__init__(line158)/thread32520::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 14:57:41,956[DEBUG]logger_second(example1.py).<module>(line19)/thread32520::hello2-1
2024-04-27 14:57:41,957[DEBUG]root(example1.py).<module>(line21)/thread32520::hello0-2
2024-04-27 14:57:41,957[DEBUG]logger_first(example1.py).<module>(line22)/thread32520::hello1-2
2024-04-27 14:57:41,957[DEBUG]logger_second(example1.py).<module>(line23)/thread32520::hello2-2
2024-04-27 14:57:41,957[DEBUG]logger_dir(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,958[DEBUG]logger_dir(main.py).__init__(line155)/thread32520::[Logger.logger_dir] start STREAM
2024-04-27 14:57:41,958[DEBUG]logger_dir(main.py).__init__(line158)/thread32520::[Logger.logger_dir] start FILE=[c:\1\logger__logger_dir.log]
2024-04-27 14:57:41,958[DEBUG]logger_dir(example1.py).<module>(line27)/thread32520::hello_dir
2024-04-27 14:57:41,958[DEBUG]Example(main.py).__init__(line152)/thread32520::====================================================================================================
2024-04-27 14:57:41,959[DEBUG]Example(main.py).__init__(line155)/thread32520::[Logger.Example] start STREAM
2024-04-27 14:57:41,959[DEBUG]Example(main.py).__init__(line158)/thread32520::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 14:57:41,959[DEBUG]Example(example1.py).meth(line41)/thread32520::hello123
2024-04-27 15:27:49,962[DEBUG]root(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,962[DEBUG]root(main.py).__init__(line155)/thread28020::[Logger.root] start STREAM
2024-04-27 15:27:49,962[DEBUG]root(main.py).__init__(line158)/thread28020::[Logger.root] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__root.log]
2024-04-27 15:27:49,962[DEBUG]root(example1.py).<module>(line10)/thread28020::None
2024-04-27 15:27:49,963[DEBUG]root(example1.py).<module>(line11)/thread28020::True
2024-04-27 15:27:49,963[DEBUG]root(example1.py).<module>(line12)/thread28020::
2024-04-27 15:27:49,963[DEBUG]root(example1.py).<module>(line13)/thread28020::hello0-1
2024-04-27 15:27:49,963[DEBUG]logger_first(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,963[DEBUG]logger_first(main.py).__init__(line155)/thread28020::[Logger.logger_first] start STREAM
2024-04-27 15:27:49,964[DEBUG]logger_first(main.py).__init__(line158)/thread28020::[Logger.logger_first] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_first.log]
2024-04-27 15:27:49,964[DEBUG]logger_first(example1.py).<module>(line16)/thread28020::hello1-1
2024-04-27 15:27:49,964[DEBUG]logger_second(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,965[DEBUG]logger_second(main.py).__init__(line155)/thread28020::[Logger.logger_second] start STREAM
2024-04-27 15:27:49,965[DEBUG]logger_second(main.py).__init__(line158)/thread28020::[Logger.logger_second] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__logger_second.log]
2024-04-27 15:27:49,966[DEBUG]logger_second(example1.py).<module>(line19)/thread28020::hello2-1
2024-04-27 15:27:49,966[DEBUG]root(example1.py).<module>(line21)/thread28020::hello0-2
2024-04-27 15:27:49,966[DEBUG]logger_first(example1.py).<module>(line22)/thread28020::hello1-2
2024-04-27 15:27:49,966[DEBUG]logger_second(example1.py).<module>(line23)/thread28020::hello2-2
2024-04-27 15:27:49,966[DEBUG]logger_dir(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,967[DEBUG]logger_dir(main.py).__init__(line155)/thread28020::[Logger.logger_dir] start STREAM
2024-04-27 15:27:49,968[DEBUG]logger_dir(main.py).__init__(line158)/thread28020::[Logger.logger_dir] start FILE=[c:\1\logger__logger_dir.log]
2024-04-27 15:27:49,968[DEBUG]logger_dir(example1.py).<module>(line27)/thread28020::hello_dir
2024-04-27 15:27:49,968[DEBUG]Example(main.py).__init__(line152)/thread28020::====================================================================================================
2024-04-27 15:27:49,968[DEBUG]Example(main.py).__init__(line155)/thread28020::[Logger.Example] start STREAM
2024-04-27 15:27:49,969[DEBUG]Example(main.py).__init__(line158)/thread28020::[Logger.Example] start FILE=[C:\__STARICHENKO_Element\PROJECTS\abc=logger_aux\EXAMPLES\logger__Example.log]
2024-04-27 15:27:49,969[DEBUG]Example(example1.py).meth(line41)/thread28020::hello123
```

********************************************************************************
