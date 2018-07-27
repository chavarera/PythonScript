'''
To read or write archives files we need to import zipfile module

'''
import datetime
import zipfile
files=['test.csv','filename.zip','orgdata.zip']

#Testing Zip Files
'''
zipfile.is_zipfile(filename)

this will genereate output
True:if the file is present and if its extension is valid
False:if file is not present or not valid Zip file
'''
for f in files:
    print('{}\t:{}'.format(f,zipfile.is_zipfile(f)))




#Read Metadata From a Zip File
'''To read the names of the files in an existing archive, use namelist()'''
zf=zipfile.ZipFile('filename.zip','r')
print(zf.namelist()) #['readme.txt'] return file list


#To access all of the meta-data about the ZIP contents, use the infolist() or getinfo() methods
print(zf.infolist())
for info in zf.infolist():
    print('Filename:{}'.format(info.filename))#List of filesname
    print('Comments:{}'.format(info.comment))
    print('date time:{}'.format(datetime.datetime(*info.date_time)))
    print('Created System:{} -(0=windows,3=Unix)'.format(info.create_system))
    print('Zip Version:{}'.format(info.create_version))
    print('Uncompressed Size:{} bytes'.format(info.file_size))
    print('compressed Size:{} bytes'.format(info.compress_size))
zf.close()
