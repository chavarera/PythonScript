'''
Threading

  Threading library in Python. Multiple threads live in the same process in the same space, 
each thread will do a specific task, have its own code, own stack memory, instruction pointer, and share heap memory. 
If a thread has a memory leak it can damage the other threads and parent process

MultiThreading
  Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
  
  In Python threading Module used to achieve Above Things
  
  
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
