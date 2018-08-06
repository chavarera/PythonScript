import os
import platform
from collections import OrderedDict

class OsInfo:
    osinfo={}
    osinfo=OrderedDict()
    def Osinfo(self):
        self.osinfo['Os_name']=platform.system()#os name
        self.osinfo['Os_full_name']='{} {}'.format(platform.system(),platform.release())
        self.osinfo['Network_name']=platform.node()# computer network name
        self.osinfo['Release_name']= platform.release()#Release Name
        self.osinfo['Version']= platform.version()
        self.osinfo['Machine']=platform.machine()#Print the machine hardware name
        self.osinfo['Processor']=platform.processor()#Print the processor type
        return self.osinfo
