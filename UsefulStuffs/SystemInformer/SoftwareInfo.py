import win32com.client
class SoftwareInfo:
    def softwareinfo(self):
        
        strComputer = "."
        softs={}
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Product")
        softwares=[]
        for objItem in colItems:
            softwares.append(objItem.Caption)
        if(len(softwares)==0):
            return False
        else:
            softs['count']=len(softwares)
            softs['lists']=softwares
            return softs
