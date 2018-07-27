import zipfile
import os
'''
Created_By:Ravi chavare

This Script is used to Read data fom a zip file
'''

zf=zipfile.ZipFile('filename.zip')
for filename in ['readme.txt','testmyknowledge.txt']:
    try:
        data=zf.read(filename)
    except KeyError:
        print("Error:\nDid not find {}".format(filename))
    else:
        print(filename)
        print(repr(data))
zf.close()
