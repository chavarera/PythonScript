'''
Threading

  Threading library in Python. Multiple threads live in the same process in the same space, 
each thread will do a specific task, have its own code, own stack memory, instruction pointer, and share heap memory. 
If a thread has a memory leak it can damage the other threads and parent process

MultiThreading
  Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
  
  In Python threading Module used to achieve Above Things
  
  The fact that Python on the CPython interpreter does not support true multi-core execution via multithreading. 
  However, Python DOES have a Threading library. 
  So what is the benefit of using the library if we (supposedly) cannot make use of multiple cores?
  
  Many programs, particularly those relating to network programming or data input/output (I/O) are often network-bound or I/O bound. 
  This means that the Python interpreter is awaiting the result of a function call that is manipulating data from a "remote" source such as a network address or hard disk. 
  Such access is far slower than reading from local memory or a CPU-cache.
  Hence, one means of speeding up such code if many data sources are being accessed is to generate a thread for each data item needing to be accessed.
  
'''
#import threading
import threading

#function to multiply a single number with 10000
def Func1(num):
    cal=num*10000
    print("\nI am From Func1 {}".format(cal))

#function to print given num*num
def Func2(num): 
    print("\nI am from Func2".format(num * num))
    
#main Program start from here 
if __name__ == "__main__":
   
   #Create A Thread 
   #Syntax threading.Thread(target=<Functionname without ()>,args=<tuple data>)
   t1 = threading.Thread(target=Func1, args=(10,)) 
   t2=threading.Thread(target=Func2,args=(11,))
  

   #After Thread creation we need to start that particular thread using threadobject.start()   
   t1.start()
   t2.start()
   
   '''
    join() method which allows one thread to wait until another thread completes its execution. 
    If t is a Thread object whose thread is currently executing, 
    then t.join() will make sure that t is terminated before the next instruction is executed by the program.
   '''
   t1.join()
   t2.join()
   print("\nDone")
