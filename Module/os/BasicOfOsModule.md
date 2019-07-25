## os Module


#### Basic of os Module
- **os** module provide a way to handle functionality related to operating system.
- The os module is a part of the standard library.
- The primary use of os module create folder,remove folder,rename,access files with path and name.
- The OS module in python provides functions for interacting with the operating system.

import os module
```python
import os
```

List of Avialable Functions
 - To get the list of avialable function use **dir()**.

Example:
```python
#import os module
import os

#Get Help of os module
print(help(os))

#Get avialable Function list
print(dir(os))
```

Important Functions related to directory
#### 1.name

- Returns the Operating system name such as,nt,posix,java,os2,ce

Example:
```python
import os

#Get Name 
name=os.name
print(name)
#Result:nt
```

#### 2.getcwd()

- Return current working dirctory name.
- The path of the file used to execute the code.

Example:
```python
#import required module
import os

#Get Current Working directory
direct=os.getcwd()

print(direct)
#Result:C:\\python3
```

#### 3.chdir(path)

- Chidr() used to change the working directory of current path

syntax:
```python
os.chdir(path)
```

Example:
```python
#import module
import os

#get current working path
print(os.getcwd())
#Result:C:\\python3

#Change directory path to C:\Users\ravi\Desktop\demo
path=r'C:\Users\ravi\Desktop\demo'
os.chdir(path)

#Now get the new path
print(os.getcwd())
#Result:C:\\Users\\ravi\\Desktop\\demo
```

### 4.mkdir(path)

- **mkdir()** create a specified folder.
- If specified folder is alredy exists it will Generate a Error
```
Cannot create a file when that file already exists: 'FolderName'
```

Syntax:
```python
os.mkdir(path)
```

Example:
```python
import os

#This will create a folder at os.getcwd() location
os.mkdir('testFolder')
```

#### 5.makedirs()

- makedirs() is the super version of mkdir()
- It is used to create a leaf directory.
- If folder is already exists it will gives an error.
- If parent directory is not avialable makedirs() function create a parent directory.

Syntax:
```python
os.makedirs('directory1/Directory2/dirname')
```

Example:
```python
#import required module
import os

#make tree like folder directory.
os.makedirs('test/testFolders')
'''
this will create a testFolders folder in test directory
if test directory is not present makedirs() will create it
'''
```

#### 6.rename()
- **rename()** used to rename the directory name. It will Return error if specified directory is not avialable

Syntax:
```python
os.name(oldFolderName,newFolderName)
```

Example:
```python
#import module
import os

#Create a folder with name testFolder
os.mkdir('testFolder')

#Rename That testFolder with newFolderName
os.rename('testFolder','newFolderName')
```


#### 7.rmdir(path)
- **rmdir()** function used to remove the empty folder only if folder contains files it will generate error.
- if folder is not avialable it will give Error.

Syntax:
```python
os.rmdir('folderName')
```

Example:
```python
#import module
import os

#Remove testFolder
os.rmdir('testFolder')
```


#### 8.removedirs()
- **removedirs()** is the super version of rmdir will remove empty directory .
- remove a leaf directory and all empty intermediate ones.

Syntax:
```python
os.removedirs(path)
```

Example:
```python
import os

os.removedirs('tst/testFolder')
```

#### 9.chmod()
- **chmod()** function used to change the mod of director and files

Syntax:
```python
chmod(path,mode)
```

**path**:-This is the path for which mode would be set.

**chmod**:-This may take one of the following mentioned values
```
stat.S_ISUID − Set user ID on execution.
stat.S_ISGID − Set group ID on execution.
stat.S_ENFMT − Record locking enforced.
stat.S_ISVTX − Save text image after execution.
stat.S_IREAD − Read by owner.
stat.S_IWRITE − Write by owner.
stat.S_IEXEC − Execute by owner.
stat.S_IRWXU − Read, write, and execute by owner.
stat.S_IRUSR − Read by owner.
stat.S_IWUSR − Write by owner.
stat.S_IXUSR − Execute by owner.
stat.S_IRWXG − Read, write, and execute by group.
stat.S_IRGRP − Read by group.
stat.S_IWGRP − Write by group.
stat.S_IXGRP − Execute by group.
stat.S_IRWXO − Read, write, and execute by others.
stat.S_IROTH − Read by others.
stat.S_IWOTH − Write by others.
stat.S_IXOTH − Execute by others.
```

Example:
```python
import os
# Set a file write by others.
os.chmod("/test/filename.txt", stat.S_IWOTH)
```
