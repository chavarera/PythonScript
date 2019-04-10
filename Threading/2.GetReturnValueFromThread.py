##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:10/04/2019
#File_des:How to get Return value from running Thread
##------------------------------------------------------------------------------------------------------


'''
To get Return value From thread function we can use queue

The queue module implements multi-producer, multi-consumer queues. 
It is especially useful in threaded programming when information must be exchanged safely between multiple threads
'''
import queue #import queue
from threading import Thread  #import Threading

#Simple Function retrun the value
def foo(val):
    print('I am From Foo Function and val={0}'.format(val))
    return val*val

#Create a Blank Queue for adding thread
que = queue.Queue()

#Create a anonymous function using lambda that will call foo() and and add that calling method to queue
#for further processing
fn=lambda q,arg1:q.put(foo(arg1))

#Now Normal Create A Thread using Threading.Thread(target=anomous function,args=(que,elements))
t = Thread(target=fn, args=(que, 5))

#Start That Thread 
t.start()

#WAit Untill to Thread Execution
t.join()

#Now Main Part to get the result from foo Function call que.get() to get the return value 
result = que.get()

#Print The Result Which is stored using que.get()
print(result)
