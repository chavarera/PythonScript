## os.path module

#### The os.path module from the os module
- **os.path** the module used for common pathname manipulation.
- This module implements some useful functions on pathnames.
- Different operating systems have different pathname conventions.

different path styles:
```
- posixpath for UNIX-style paths
- ntpath for Windows paths
- macpath for old-style MacOS paths
```
#### import os.path module

- Instead of directly importing the os.path name module first import os root module and access os.path from it.
```python
#import os module
import os
```

use os.path for further operation

Get documentation of os.path
```python
#import os module
import os

#Get help Documentation of os.path
print(help(os.path))

#Get Avialable Function list in os.path module
print(dir(os.path))
```

Important Function in os.path Module

#### 1.curdir():
- Return a period
- An attribute reference is a primary followed by a period and a name:

   attributeref ::= primary "." identifier

primary must evaluate to an object of a type that supports
attribute references, which most objects do.  This object is then
asked to produce the attribute whose name is the identifier

Example:
```python
#import os

#get curdir 
print(os.path.curdir)
```
Output:
```
.
```

#### 2.abspath:

- Return an absolute path.
- Normally it joins using normspath **os.getcwd()** and path and return it.


Syntax:
```python
os.path.abspath(path)

# path parameter is mandatory
```

Example:
```python
import os

#path
path=r"C:/Test"
print(os.path.abspath(path))
```
Output:
```
currentdirectorypath/C:/Test
```

#### 3.basename:
- Returns the lat component of given path.

Consider following example
```
fullpath:"C:/Test/final"
basename:final

full_path:"C:/Test/final/"
basename:

full_path:"C:/Test/final/filename.txt"
basename:filename.txt
```

Syntax:
```python
os.path.basename(path)
```

Example:
```
#Import Required module
import os

#Full path
full_path=r"C:/Test/final/filename.txt"

#Get basename
basename=os.path.basename(full_path)

print(basename)
```
Output:
```
filename.txt
```

#### 4.commonpath

- From  2 given path, returns the longest common sub-path.
Consider
```
path1="C:/test/folder/amaze"
path2="C:/test/folder"

commonpath:C:/test/folder
```

Syntax:
```python
os.path.commonpath(['path1','path2','path3'])
```

Example:
```python

# import require module
import os

#path list
paths=['/usr/lib', '/usr/local/lib']

#To get Common Path
common=os.path.commonpath(paths)

#print the commonpath
print(common)
```
Ouput:
```
/usr
```

#### 5.commonprefix()

- From a list of pathnames, returns the longest common leading path.

Consider following Example
```
path1="C:/test/folder/amaze"
path2="C:/test/fntl/test"

commonprefix path:C:/test/f
```

Syntax:
```python
os.path.commonprefix(['path1','path2'])
```

Example:
```python
# import require dmodule
import os

#Initialize paths
path1="C:/test/folder/amaze"
path2="C:/test/fntl/test"

#get common prefix in path
comonprefix=os.path.commonprefix([path1,path2])

#print Common prefix path
print(comonprefix)
```
OutPut:
```
C:/test/f
```


#### 6.dirname:
- Return the directory path of given pathname

Consider
```
pathname="C:/test/folder/amaze.txt"
dirname:C:/test/folder
```

Syntax:
```python
os.path.dirname('path')
```

Example:
```python
# import require dmodule
import os

#Initialize paths
path1="C:/test/folder/amaze.txt"

#Get dir name
name=os.path.dirname(path1)


#print the dirname
print(name)
```
OutPut:
```
C:/test/folder
```


#### 7.exists

- Return True if the given pathname is existed otherwise return False

Syntax:
```
os.path.exists('pathname')
```

Example:
```python
import os
path=r"C:/test/folder/amaze.txt"
print(os.path.exists(path))
```
Output:
```
False
```

#### 8.isfile

- Return True if the given pathname is a file

Syntax:
```python
os.path.isfile(path)
```

Example:
```python
import os
path=r"C:/test/folder/amaze.txt"
print(os.path.isfile(path))

#Result is True if that file exists and it is a file otherwise False
```
Output:
```
True
```
#### 9.isdir

- Return True if the given pathname is a directory

Syntax:
```python
os.path.isdir(path)
```

Example:
```python
import os
path=r"C:/test/folder"
print(os.path.isdir(path))

#Result is True if that directory exists and it is a directory otherwise False
```
Output:
```
True
```

#### 10.join:
- join two or more pathname paths, by inserting **'/'** as needed.

Syntax:
```python
os.path.join(path1,path2)
```

Example:
```python
#import required module
import os

path1=r"c:"
path2=r"foldername"

#join path1 and path2
joined_path=os.path.join(path1,path2)

print(joined_path)
```
Output:
```
c:/foldername
```


#### 11.split:
- split(path) Return a tuple containing 
(head,tail)

**tail**: where the tail is everything after the final slash may be empty sometime

- The tail part will never contain a slash.
- If the path is empty, both head and tail are empty.

Syntax:
```python
os.path.split()
```

Example:
```python
#import required module
import os

#Simple Example 1
path1=r"C:/Test/help.txt"
splited_path1=os.path.split(path1)
print(splited_path1)
#Result:('C:/Test', 'help.txt')

#Example 2
path2=r"C:/Test/"
splited_path2=os.path.split(path2)
print(splited_path2)
#Result:('C:/Test', '')

#Example 3
path3=r""
splited_path3=os.path.split(path3)
print(splited_path3)
#Result:('', '')
```
Output:
```
('C:/Test', 'help.txt')
('C:/Test', '')
('', '')
```

Some Other Important os.path available Function

**12.splitdrive:**
- Split a pathname into drive and path,

**13.splittext**
- Split the extension from a pathname.

**14.relpath(path, start=os.curdir)**
 - Return a relative filepath to path either from the current directory or from an optional start directory
