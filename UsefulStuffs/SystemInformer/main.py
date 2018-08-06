import SystemDrives as sd
import OsInfo as oi
import NetworkInfo as ni
import SoftwareInfo as si

print('{:*^65s}'.format('Operating System Information'))
o1=oi.OsInfo()
for i in o1.Osinfo().items():
    print('{}:{}'.format(i[0],i[1]))

print('\n\n{:*^65s}'.format('Drives On System'))
s1=sd.SystemDrives()
for s in s1.GetDrives():
    print('{}'.format(s))

print('\n\n{:*^65s}'.format('Network Information'))
n1=ni.NetworkInfo()
for i in n1.networkinfo().items():
    print('{}:{}'.format(i[0],i[1]))


print('\n\n{:*^65s}'.format('Installed Software'))
s1=si.SoftwareInfo()
i=1
print('{} Softwares installed'.format(s1.softwareinfo()['count']))
for s in s1.softwareinfo()['lists']:
    print(s)
   
    
