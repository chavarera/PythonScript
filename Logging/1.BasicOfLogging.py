##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:13/03/2019
#File_des:Introduction of Logging
#Offical Documentation:https://docs.python.org/2/library/logging.html
##------------------------------------------------------------------------------------------------------



'''
Logging is a very useful tool in a programmer’s toolbox.
It can help you develop a better understanding of the flow of a program
and discover scenarios that you might not even have thought of while developing.

Python provides a logging system as a part of its standard library, so you can quickly add logging to your application

Import logging module in python as follow
import logging as log
'''
#importing logging module
import logging as log

'''
Following Are some By Defualt Logging Levels with thier numeric values
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
'''

#Simple Log Message print on shell

log.debug("This is debug messgae")
log.info("This is info message ")
log.warning("THis is warning Message")
log.error("This is Error Message")
log.critical("This is Critical Message")

'''
When you will run above code then only warning ,error,critical log will run
because python bydefualt logging level set to 30 
you can check python logging level using log.root.level
'''
loglevel=log.root.level
print(loglevel)


#logging module shows log from given log to upwards means if we set loglevel =20
#then ppython show info,warning,error,critical logging

#how to change Logging

log.root.level=20 #you must ned to set this when loging imported to apply to all file
print(log.root.level) #here you will get 20 as logger value if you give log now then from 20 to onwards log will show
#After Setting logger value to 20
log.debug("This is debug messgae")
log.info("This is info message ")
log.warning("THis is warning Message")
log.error("This is Error Message")
log.critical("This is Critical Message")