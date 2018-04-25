#OS module
import os

#To get any module information or method just search dir(modulename)
print(dir(os))

'''To get current working directory'''
print(os.getcwd())


'''to change current working directory'''
os.chdir(r"C:\Users\ravi\PycharmProjects\PythonScript")
print(os.getcwd())


'''To get list of files and folders'''
files=os.listdir()
print(files)

'''To create a directory there are two ways
1.mkdir
2.makedirs-->this will create top level directories for example we want to create sub folder in main folder then makedirs work perfectly
'''

os.makedirs('main/sub/test')    #where mkdir() doesnot support is


'''To remove directory
1.rmdir
2.removedirs-->
'''
os.removedirs('main/sub/test')

print(os.listdir())



'''to rename a file'''
os.rename('t.txt','h.txt')


'''to print out info about a file '''
# print(os.stat('h.txt').st_mtime)


