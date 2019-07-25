## File Name Accessing

### Functions For Reading FileNames and Directory

following are the some function used to accessing filename and directory using os module in python
1. scandir()
2. listdir()
3. walk()

#### 1.scandir()

- Iterator of DirEntry objects for given path
- When you not pass a path parameter defualt **path='.'** is passed to scandir() function which is current working path.
- To get the help documentation of **os.scandir()** use **help()** functiona and pass the os.scandir() as object
```
help(os.scandir)
```

Syntax:
```python
os.scandir(path)
```

Example:
```python
#import required module
import os

#os.scandir() return as iterator object
directory_data=os.scandir()

#print type of directory_data
print(type(directory_data))
#Result:<class 'posix.ScandirIterator'>


#iterate scandir object
for d in directory_data:
    print(d)

'''
#Result
<class 'posix.ScandirIterator'>
<DirEntry 'main.py'>
<DirEntry 'test.py'>
<DirEntry 'folderName'>
'''
```

#### 2.listdir()

- Return a list containing the names of the files in the directory. The filenames returned will be str.
- If path is None, uses the path='.'

Syntax:
```python
os.listdir('path of directory')
```

Example:
```python
#import required module
import os

#Get the current working path as path to scan files and directory
path=os.getcwd()

#Get List of filenames avialable inside path
files=os.listdir(path)
print(files)

#Result:['main.py', 'test.py', 'folderName']
```


#### 3.walk()

- **walk()** is a Directory tree generator.
- For each directory in the directory tree rooted at top (including top itself, but excluding '.' and '..')
- **walk()** Returns the 3 different tuple for
     ```
    dirpath, dirnames, filenames 
     ```
     
    **dirpath**:Is a string path to the directory.
    
    **dirnames**:Is the list of the subdirectories inside the dirpath. (excluding '.' and '..')
    
    **filename**:Is the list of the name of the non directory files in dirpath
 
    **Note**: that the filenames in the lists are just names, with no path components.
    you can get the full path of file name using 
```
os.path.join(dirpath,filenames)
```

Syntax:
```python
os.walk('path of Root Directory')
```

Example:
```python
#import required module
import os

#Get Current directory path
path=os.getcwd()

#os.walk(path) return iteraable object
for dirpath, dirnames, filenames in os.walk(path):

    print("*Directory path*")
    print(dirpath)

    print("\n***List of Directory*")
    print(dirnames)

    print("\n***List of files*")
    print(filenames)

'''
#Result
*Directory path*
/Demo/Python

*List of Directory*
[]

*List of files*
['main.py', 'test.py', 'folderName']

*Directory path*
/Demo/Python1

*List of Directory*
[]

*List of files*
['help.txt']
'''
```
