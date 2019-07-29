## Python Package installer(PIP) :postal_horn:.

### What is pip?
- PIP stands for **Python Package installer**.
- PIP is a package manager for Python packages or modules.
- Pip is a package management system used to install and manage software packages written in Python.
- We can find Many packages in the default source for packages and their dependencies.
- Python Package installer. Python 2.7.9 and later, and Python 3.4 and later include pip by default.

### Check if PIP is Installed?
-Open command prompt  and type the following

`>pip --version`

If the above shows the pip version, then pip is already installed on your system.

### How to upgrade PIP
Open the command prompt and type the following
```python
>python -m pip install –upgrade pip
```

### Use of PIP
You can install packages in 2 different ways.

#### 1.Normal package without .Whl file 
- Go to https://pypi.org
- Search required packages such as pandas, numpy, OpenCV.
- Now type in the terminal
  
```python
>pip install pacakagename
```
- Which package name is showing in the website portal

#### 2.use the wheel  of that package
- Just open https://pypi.org
- Search required packages such as pandas, numpy, OpenCV.
- Do to download section and download .whl file which is an archive for packages.
- Go to the download folder. And open command prompt their and type
   
```python
>pip install downloaded_package.whl
```

### Get List of installed packages list 
Use the list command to list all the packages installed on your system:
Example
```python
>pip list
```
### How to Remove Uninstall Packages 
Use the uninstall command to remove a package:

Example
```python
>pip uninstall pacakagename
````

### How to create requirement.txt  file using pip
- Save all the packages in the file with
Example:
```python
>pip freeze >requirements.txt
```
Keep in mind that in this case, **requirements.txt** file will list all packages that have been installed in the system.
So before creating any project first create an environment and run above command to list out required package name in **requirements.txt**

### Install project dependencies using requirements.txt 
- first, go to the folder where **requirements.txt** file is placed and type the following command in terminal 
Example:
```python
>pip install -r requirements.txt
```
