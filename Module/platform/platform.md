## Platform

### Introduction
- The **platform** module in Python is used to access the underlying platform’s data,
such as, hardware, operating system, and interpreter version information.
- This module tries to retrieve as much platform-identifying data as possible.

### How to install platform module in python?
- **platform** module is come with python basic library so we don't need to install it Externally.

### How to import platform module
You can start with importing the *platform*  module in your program

Syntax:
```python
#without alias
import platform

#With Alias
import platform as <AnyShortName>
```

Example:
```python
#without alias
import platform

#With Alias
import platform as pl
```

### How to get list of avilables function in platform
```python
#to Get the help of platform module use
print(help(platform))

#To get the list of functions and Variables
print(dir(platform))
```

## Important Functions From platfrom Module

### 1.system()
- **System()** returns the Operating system Name e.g. 'Linux','windows','Java'

Example
```python
import platform

#Get operating system name
name=platform.system()

print(name)
#Result:Windows
```

### 2.architecture()
- Returns a tuple (bits, linkage) which contain information about the bit architecture 
and the linkage format used for the executable. 
- Both values are returned as strings.
Example:
```python
import platform

#Get operating architecture
name=platform.architecture()

print(name)
#Result:('64bit', 'WindowsPE')
```

### 3.node()
- **node()** returns an Computer network name.
- An empty string is returned if value can not be determined.

Example:
```python
import platform

#Get computer name in network
name=platform.node()

print(name)
#Result:'EKPubgikar'
```

### 4 .processor()
- Returns The Actual processor name of machine.
Example:
```python
import platform

#Get processor name
name=platform.processor()
print(name)
#Result:'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel'
```

### 5.machine()
- Retruns the machine type e.g.'AMD64'
Example:
```python
import platform

#Get the machine type
name=platform.machine()

print(name)
#Result:'AMD64'
```

### 6.version()
- Return the Operating system release version
Example:
```python
import platform

#Get the Release Version
name=platform.version()

print(name)
#Result:'10.0.17763'
```

### 7.python_version()
- Returns the python version
Example:
```python
import platform

#Get the pthon version
name=platform.python_version()

print(name)
#Result:'3.7.3'
```

### 8.uname()
-  Returns a tuple of strings (system, node, release, version, machine, processor)
Example:
```python
import platform

#Get the Uname Details
details=platform.uname()

print(details)
'''
#Result:uname_result(system='Windows',
node='EKPubgikar', 
release='10', 
version='10.0.17763', 
machine='AMD64', 
processor='Intel64 Family 6 Model 58 Stepping 9, GenuineIntel')
'''
```
## Other Remaing Function

### 9.python_build()
- Returns a tuple (buildno, builddate) stating the Python build number and date as strings.

### 10.python_compiler()
- Returns a string identifying the compiler used for compiling Python.

platform module official documentation [Here](https://docs.python.org/3/library/platform.html)
