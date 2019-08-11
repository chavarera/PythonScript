## Modules

- A module is a Python file containing python definitions statements.
- A module can define functions, classes, and variables, Methods also contain runnable code.
- Grouping similar type of code into a file and whenever it required to use it 


### some python inbuilt modules
    1.os
    2.string
    3.threading
    4.sys
    5.collection
    6.argparse
    7.sqlit3
    8.raw
    9.re
    10.pip
    .... and much more

### How to Get List of Installed modules list in python?
you can write down following code into an interactive shell or in the python file
```python
help('modules')
```
you will get the result

Please wait a moment while I gather a list of all available modules...
```
FileSearchEngine    _testcapi           ftplib              reprlib
GetFiles            _testcapi_d         functools           requests
PIL                 _testconsole        gc                  rlcompleter
PyQt5               _testconsole_d      genericpath         runpy
SqliteHandler       _testimportmultiple getopt              sched
Test                _testimportmultiple_d getpass             secrets
__future__          _testmultiphase     gettext             select
_abc                _testmultiphase_d   glob                select_d
_ast                _thread             gzip                selectors
_asyncio            _threading_local    hashlib             selenium
_asyncio_d          _tkinter            heapq               setuptools
_bisect             _tkinter_d          hmac                shelve
_blake2             _tracemalloc        html                shlex
_bootlocale         _warnings           html5lib            shutil
_bz2                _weakref            http                signal
...........    ................    ...........         ....
```

### How To import module in python program?
We can use any Python source file as a module by executing an import statement in some other Python source file.
- You can import the module using **import** keywords

Syntax:
```python
import <moduleName>
```
Example:
```python
#import required module
import platform
```

### How to rename imported modules?
- **as** keyword is used to bind a new name to an object.
- If you import a module directly and then import the same module but with a different name via as both names will point to the same object.

Syntax:
```python
import <moduleName> as <newObjectName>
```
Example
```python

#Normal way to import a module
import platform

#using as Keyword import a module
import platform as plt

#if you check the id of object 
#platform and plt both will point to the same object
print(id(platform))
print(id(plt))

'''
#Result you will get the location of an object
139950267344280
139950267344280
'''
```

### How to list all functions in a Python module?
you can use the following two different functions to achieve function names, variables, and documentation
    1.help()
    2.dir()
### 1.help()
- **help()** function is used to get the  all function with docuemantation

Syntax:
```python
help(moduleName)
```

Example:
```python
#import module
import platform

#get documentation
print(help(platform))
'''
#Result
Help on module platform:

NAME
    platform

MODULE REFERENCE
    https://docs.python.org/3.6/library/platform
    
DESCRIPTION
    This module tries to retrieve as much platform-identifying data as possible.
    It makes this information available via function APIs.
    
CLASSES
    builtins.tuple(builtins.object)
        uname_result
    
    class uname_result(builtins.tuple)
     |  uname_result(system, node, release, version, machine, processor)

FUNCTIONS
    architecture(executable='/usr/local/bin/python3', bits='', linkage='')
        Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.
        
        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable

DATA
    DEV_NULL = '/dev/null'
    __copyright__ = '\n    Copyright (c) 1999-2000, Marc-Andre Lemburg.

VERSION
    1.0.8

FILE
    /usr/lib/python3.6/platform.py

None
'''
```

### 2.dir()
- To simply list the names of all the functions and variables defined in the module.

Syntax:
```python
dir(moduleName)
```

Example:
```python
#import module
import platform

#get function names and variable name
print(dir(platform))
'''
#Result
['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', 
'_WIN32_SERVER_RELEASES', '__builtins__', '__cached__',
'__copyright__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', '__version__',
'_codename_file_re','_default_architecture', '_dist_try_harder',
'_distributor_id_file_re', '_follow_symlinks', 
'_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', 
'_java_getprop', 
'_libc_search','_linux_distribution', '_lsb_release_version', 
'_mac_ver_xml', '_node', 
'_norm_version', '_parse_release_file','_platform', 
'_platform_cache', '_pypy_sys_version_parser',
'_release_file_re', '_release_filename', '_release_version',
'_supported_dists', '_sys_version',
'_sys_version_cache', '_sys_version_parser',
'_syscmd_file', '_syscmd_uname','_syscmd_ver',
'_uname_cache', '_ver_output', 'architecture', 
'collections', 'dist', 'java_ver', 'libc_ver', 
'linux_distribution', 'mac_ver', 'machine', 'node',
'os', 'platform', 'popen', 'processor',
'python_branch', 'python_build','python_compiler',
'python_implementation', 'python_revision',
'python_version', 'python_version_tuple', 're',
'release', 'subprocess', 'sys', 'system',
'system_alias', 'uname', 'uname_result', 'version',
'warnings', 'win32_ver']
'''
```

### How to use the function, methods of modules?

- if you want to check the python version from platform module there is one method called **python_version()**

Syntax:
```python
moduleName.<MethodName>()
```

Example:
```python
#import module
import platform

#Call python_version() from platform
version=platform.python_version()
print(version)

#Result:3.7.3
```

How to import a specific method or function name from Module?



Syntax:
```python
from <moduleName> import methodName,methodName2
```

Example import only python_version()
```python
#import required module
from platform import python_version

#get python version
version=python_version()
print(version)
#Result:3.7.3
```

