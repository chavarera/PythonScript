##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:13/03/2019
#File_des:Introduction of Logging
#Offical Documentation:https://docs.python.org/2/library/logging.html
##------------------------------------------------------------------------------------------------------

import logging as log

#To configure logging use log.basicconfig(parametere) for initilization
'''
some of the commonly used paramter for basicconfig
1.level: The root logger will be set to the specified severity level.
2.filename: This specifies the file.
3.filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
4.format: This is the format of the log message.
'''
#Configure loggging
loger=log.getLogger(__name__)
log.basicConfig(filename='simplelog.log',level=log.INFO,format='[%(asctime)s-%(levelname)s]-%(message)s')

loger.info("Simple logMessage")
loger.debug("This is debug Message")
loger.error("this is Error Log")

#Foloowing are the some log records attributes format
'''
%(asctime)s     :-Asctime
%(created)f     :-created 
%(filename)s    :-filename where log generated
%(funcName)s    :Function name
%(levelname)s   :-level name
%(message)s      :-logger passing messgae
%(pathname)s    :-Full pathname of the source file where the logging call was issued (if available).
%(process)d     :-if process id is Avialable
'''




