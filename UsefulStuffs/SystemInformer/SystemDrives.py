import re
import os
import string
class SystemDrives:
    drives=[]
    def GetDrives(self):
        for d in string.ascii_uppercase:
            if os.path.exists('{}:'.format(d)):
                self.drives.append(d)
        if(len(self.drives)==0):
            return False
        else:
            return self.drives
