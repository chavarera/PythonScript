import socket
from collections import OrderedDict
from uuid import getnode as get_mac
class NetworkInfo:
    allid={}
    allid=OrderedDict()
    def networkinfo(self):
        self.mac = get_mac()
        self.macid=':'.join(("%012X" % self.mac)[i:i+2] for i in range(0, 12, 2))
        self.ip=socket.gethostbyname(socket.gethostname())
        self.allid['Ipv4']=self.ip
        self.allid['Mac_Address']=self.macid
        return self.allid
        

