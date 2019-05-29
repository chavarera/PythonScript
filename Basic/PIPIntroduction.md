## Python Package Index(PIP).

### What is pip?
- PIP stands for 'Python Package Index'
- PIP is a package manager for Python packages, or modules.
- pip is a package-management system used to install and manage software packages written in Python.
- Many packages can be found in the default source for packages and their dependencies
- Python Package Index. Python 2.7.9 and later, and Python 3.4 and later include pip by default.

### Check if PIP is Installed?
-Open  command prompt and type the following

 `>pip --version`

If above shows pip version then pip is already installed on your system.


### How to upgrade PIP
Open  command prompt and type the following
```python
  >python -m pip install –upgrade pip
```

### Use of PIP
You can install packages in two different way

#### 1.Normal package without. Whl file
  - Go to https://pypi.org
  - Search required packages such as pandas, numpy, opencv.
  - Now type on terminal
  ```python
  >pip install pacakagename
  ```
  - Which packagename is showing in the website portal


#### 2.use the wheel of that package
   - Just open https://pypi.org
   - Search required packages such as pandas, numpy, opencv.
   - Do to download section and download .whl file which is archive for packages.
   - Go to download folder. And open command prompt their and type
   ```python
    >pip install downloadedpackage.whl
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

### How to create requirement.txt file using pip
- Save all the packages in the file with
Example:
```python
  >pip freeze >requirements.txt
```
Keep in mind that in this case, requirements.txt file will list all packages that have been installed in system,
So before creating any project first create a environment and run above command to list out required pacakagename in requirements.txt


### Install project dependencies using requirements.txt
- first go to folder where requirements.txt file is placed and type following command in terminal
Example:
```python
  >pip install -r requirements.txt
```
