##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:10/04/2019
#File_des:Difference Between Multiprocessing and Multithreading
##------------------------------------------------------------------------------------------------------
'''
Multiprocessing and Multithreading both adds performance to the system. 

-Multiprocessing is adding more number of or CPUs/processors to the system which 
increases the computing speed of the system. 

-Multithreading is allowing a process to create more threads which increase the 
responsiveness of the system

In Python, because of GIL (Global Interpreter Lock) a single python process cannot run threads 
in parallel (utilize multiple cores). 
It can however run them concurrently (context switch during I/O bound operations)
'''

#--------------------------------------------------------------------------------------------------#
#                                   MultiProcessing
#--------------------------------------------------------------------------------------------------#
'''
Pros:-
-Multiprocessing achieves true parallelism and is used for CPU-bound tasks
-Multiprocessing adds CPUs to increase computing power.
-Multiple processes are executed concurrently.
-Separate memory space.
-Avoids GIL limitations for cPython(Global Interpreter Lock for accessing Same Memory Location)
-Child processes are interruptible/killable
-multiprocessing module is used in Python

Cons:-

-Larger memory footprint
Memory footprint refers to the amount of main memory that a program uses or references while running.

'''

#--------------------------------------------------------------------------------------------------#
#                                   MultiThreading
#--------------------------------------------------------------------------------------------------#
'''
Pros:-

-Multithreading is concurrent and is used for IO-bound tasks
-Multithreading creates multiple threads of a single process to increase computing power.
-Multiple threads of a single process are executed concurrently.
-Shared memory - makes access to state from another context easier
-Allows you to easily make responsive UIs
-Lightweight - low memory footprint

Cons:-

-Complex debugging and testing processes
-Increased potential for deadlock occurrence(When Memory Leak)
'''
