## Jupyter Notebook Shortcuts

Some Use full Information

![basic](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/basics.png)

### Open Jupyter NoteBook at Particular Directory

consider you want to open Jupyter notebook at the following path
```
C:\Users\ravi\Desktop\PythonScript
```

Simple Open Terminal(Command Prompt) and change path using cd.
```
cd "C:\Users\ravi\Desktop\PythonScript"
``` 

now just Type 
```
Jupyter Notebook
```

![path](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/path.png)

Note: Another simple Option is open directory and in the address bar type  **Jupyter Notebook** and hit Enter.



### New Jupyter Notebook Window

- When Jupyter Notebook running.
- Click on the **new** dropdown and select "python3" it Will Open A New Notebook
- To change the FIle name click on untitled and rename as you wish.
![basic](https://github.com/chavarera/PythonScript/blob/master/MachineLearning/JupyterNotebook/img/newfile.png)


#### How to run Python statement in jupyter Notebook
- Type your python code or statement and just click on run or just press *ctrl+Enter* it will show Output in the next line.


### Shortcuts
- The Jupyter Notebook has two different keyboard modes for shortcut purposes.

```
Command Mode
Edit Mode
```
#### Command Mode
- Command mode binds the keyboard to notebook level commands and is indicated by a grey cell border with a blue left margin.
- Press **Esc** To enable Command Mode

##### Some Important Command Mode Shortcuts
```
H: To show Available Keyboard Shortcuts

F: Find and Replace in the selected cell

#Cell Insertion
A: Insert cell above
B: Insert cell below

#Cut Copy Paste
X: Cut selected cells
C: Copy selected cells
V: Paste cells below
Shift+V: Paste cells above

# Cell Deletion
D,D  :  Delete Selected Cell(Press two Times D)
Z    :  Undo Cell Deletion
```

#### Edit Mode
- Edit mode allows you to type code or text into a cell and is indicated by a green cell border.
- Press **Enter** To enable Command Mode

##### Some Important Edit Mode Shortcuts
```
TAB: Simple Code completion

Ctrl-]  : give proper indent to statements
Ctrl-[  : Dedent(Remove Indent)
Ctrl-A  : Select All
Ctrl-Z  : Undo
Ctrl-/  : Add Comments


Ctrl-Enter: run selected cells
Alt-Enter: run the cell and insert below

Esc: To Enter in Command Mode
```


#### Some Toolbar Information

**1. Save:**
- Click on Save Option which is present in the toolbar.
- Simple Use Keyboard Shortcut ctrl+S

**2. Insert New Cell**
- Click on Plus (+) New Cell Is added.
- You can use the menu (Insert) for 
    - insert cell above
    - insert cell below
- Simply You can also use Keyboard shortcuts
```
A: insert cell above
B: insert cell below
```

**3. Cut Cell**
- A first select cell that you want to delete and click on the scissor icon to remove that cell.
- Or use keyboard Shortcuts
```
x: Cut Selected cell 
```

### Add Virtual Environment to Jupyter Notebook
```
pip install --user ipykernel
```

Next you can add your virtual environment to Jupyter by typing:
```
python -m ipykernel install --user --name=venv_Name
```
