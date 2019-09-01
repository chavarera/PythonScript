## Jupyter Notebook
- Jupyter Notebook is a very popular and flexible tool that allows us to put all our code and output of code with visualization in the same documents.
- Jupyter notebook is an open-source web application that allows you to create and share documents that contain live code
(our normal program), equations, visualizations, and narrative text.
- If you are not familiar with any programming language and you want to start a programming career from python then use only python default python idle that makes help you to remember most of the python syntaxes.

![Jupyter](https://jupyter.org/assets/jupyterpreview.png)

#### Why To Use Jupyter Notebook?
- Jupyter supports over 40 programmings (Including python, R, Scala)
- Jupyter Notebook can be shared through Email, Dropbox, GitHub and many others.
- You can produce Interactive output such as HTML, table, images, video.
- Easy to integrate with big data.


### Installation and Setup of Jupyter Notebook

My System Specification where I am installing Jupyter notebook

```
machine name: Windows 10
bit Operating: 64 bit
Ram: 6 GB
HDD: 596 GB
Python version: Python 3.7.3 
```

if you want to check your python version open your terminal and hit the following command

```
python --version
```

Output:
```
Python 3.7.3
#my installed python version may your other
```


### You Can Install Jupyter Notebook in different environments

#### Installing Jupyter Notebook with pip

consider you are working on python 3.7.X version and you want to install a jupyter notebook in your windows machine.
follow simple steps:
- Open Windows Terminal(Command prompt, Powershell)
- And Run followings statements
```
pip install --upgrade pip
```

if you Get **"pip is not recognized as an internal or external command"** such error then add python path to system variable

- After completion of first command run following command
```
pip install jupyter
```

- It will take some time to install a jupyter notebook and its dependent packages.

you will found the following window after completion 

![installed](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/pip.png)

now jupyter is installed on your local machine.

### Installing Jupyter Notebook with anaconda
- Download anaconda from here https://www.anaconda.com/downloads according to your system requirement.
- Install the version of Anaconda which you downloaded, following the instructions on the download page.
- anaconda distribution will installed along with  Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.



### How To Test Jupyter Notebook After completion of Installation

- Open command prompt and type following command

```
jupyter notebook
```
and press enter key now one webpage automatically opened in your default web browser

```
URL:http://localhost:8888/tree
```
![open](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/open.png)


- Now click on the new dropdown list and create any folder **"PythonScript"**(or with any name) or just select any folder showing inside the directory.
- Click on the new dropdown and select **"python3"** it will show following window
![new](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/new.png)

![opened](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/opened.png)


- Now Type anything and press **ctrl+Enter** to run that or click on the run button above the file it will show the result in the second line.
![run](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/run.png)


Now you have successfully installed a jupyter notebook and test normal print any statement. Some shortcuts and features of jupyter notebook will be continued in the next lessons


