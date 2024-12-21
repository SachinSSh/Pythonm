import threading

#Thread Objects

"""The Thread class is used to represent a separate thread of control.A new thread can be
created as follows:"""

"""This creates a new Thread instance. group is None and is reserved for future extensions. target is a callable object invoked by the run() method when the thread starts.
By default, it’s None, meaning that nothing is called. name is the thread name. By
default, a unique name of the form "Thread-N" is created. args is a tuple of arguments
passed to the target function. kwargs is a dictionary of keyword arguments passed to
target."""
threading.Thread(group=None, target=None, name=None, args=(), kwargs={})

#A Thread instance t supports the following methods and attributes:

"""Starts the thread by invoking the run() method in a separate thread of control.This
method can be invoked only once."""
#t.start()

"""This method is called when the thread starts. By default, it calls the target function
passed in the constructor.This method can also be redefined in subclasses of Thread."""
#t.run()

"""Waits until the thread terminates or a timeout occurs. timeout is a floating-point number specifying a timeout in seconds.A thread cannot join itself, and it’s an error to join
a thread before it has been started."""
#t.join([timeout])

"""Returns True if the thread is alive and False otherwise.A thread is alive from the
moment the start() method returns until its run() method terminates. t.isAlive()
is an alias for this method in older code."""
#t.is_alive()

"""The thread name.This is a string that is used for identification only and which can be
changed to a more meaningful value if desired (which may simplify debugging). In
older code, t.getName() and t.setName(name) are used to manipulate the thread
name."""
#t.name

"""An integer thread identifier. If the thread has not yet started, the value is None."""
#t.ident

"""The thread’s Boolean daemonic flag.This must be set prior to calling start() and the
initial value is inherited from daemonic status of the creating thread.The entire Python
program exits when no active non-daemon threads are left.All programs have a main
thread that represents the initial thread of control and which is not daemonic. In older
code, t.setDaemon(flag) and t.isDaemon() are used to manipulate this value."""
#t.daemon

#Here is an example that shows how to create and launch a function (or other callable) as a thread:

import threading
import time
def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)
t = threading.Thread(target=clock, args=(15,))
t.daemon = True
t.start()

#Here is an example that shows how to define the same thread as a class:

import threading
import time
class ClockThread(threading.Thread):
        def __init__(self,interval):
                threading.Thread.__init__(self)
                self.daemon = True
                self.interval = interval
        def run(self):
                while True:
                        print("The time is %s" % time.ctime())
                        time.sleep(self.interval)
t = ClockThread(15)
t.start()

#Timer Objects
#A Timer object is used to execute a function at some later time.

"""Creates a timer object that runs the function func after interval seconds have
elapsed. args and kwargs provide the arguments and keyword arguments passed to
func.The timer does not start until the start() method is called."""
# Timer(interval, func[ args [ kwargs]])


#### A Timer object, t, has the following methods:

"""Starts the timer.The function func supplied to Timer() will be executed after the
specified timer interval."""
# t.start()

"""Cancels the timer if the function has not executed yet."""
# t.cancel()

"""Lock Objects
A primitive lock (or mutual exclusion lock) is a synchronization primitive that’s in either a
“locked” or “unlocked” state.Two methods, acquire() and release(), are used to
change the state of the lock. If the state is locked, attempts to acquire the lock are
blocked until the lock is released. If more than one thread is waiting to acquire the
lock, only one is allowed to proceed when the lock is released.The order in which
waiting threads proceed is undefined."""

#A new Lock instance is created using the following constructor:

# Lock()
#Creates a new Lock object that’s initially unlocked.

#A Lock instance, lock, supports the following methods:

"""Acquires the lock, blocking until the lock is released if necessary. If blocking is supplied
and set to False, the function returns immediately with a value of False if the lock
could not be acquired or True if locking was successful."""
# lock.acquire([blocking ])

"""Releases a lock. It’s an error to call this method when the lock is in an unlocked state
or from a different thread than the one that originally called acquire()."""
# lock.release()

"""RLock
A reentrant lock is a synchronization primitive that’s similar to a Lock object, but it can
be acquired multiple times by the same thread.This allows the thread owning the lock
to perform nested acquire() and release() operations. In this case, only the outermost release() operation resets the lock to its unlocked state."""

###A new RLock object is created using the following constructor:
# RLock()

#Creates a new reentrant lock object.An RLock object, rlock, supports the following methods:

"""Acquires the lock, blocking until the lock is released if necessary. If no thread owns the
lock, it’s locked and the recursion level is set to 1. If this thread already owns the lock,
the recursion level of the lock is increased by one and the function returns immediately."""
# rlock.acquire([blocking ])

"""Releases a lock by decrementing its recursion level. If the recursion level is zero after
the decrement, the lock is reset to the unlocked state. Otherwise, the lock remains
locked.This function should only be called by the thread that currently owns the lock."""
# rlock.release()

#Semaphore and Bounded Semaphore

"""A semaphore is a synchronization primitive based on a counter that’s decremented by
each acquire() call and incremented by each release() call. If the counter ever
reaches zero, the acquire() method blocks until some other thread calls release()."""

"""Creates a new semaphore. value is the initial value for the counter. If omitted, the
counter is set to a value of 1."""
# Semaphore([value])

#A Semaphore instance, s, supports the following methods:

"""Acquires the semaphore. If the internal counter is larger than zero on entry, this method
decrements it by 1 and returns immediately. If it’s zero, this method blocks until another
thread calls release().The blocking argument has the same behavior as described for
Lock and RLock objects."""
# s.acquire([blocking])

"""Releases a semaphore by incrementing the internal counter by 1. If the counter is zero
and another thread is waiting, that thread is awakened. If multiple threads are waiting,
only one will be returned from its acquire() call.The order in which threads are
released is not deterministic."""
# s.release()

"""Creates a new semaphore. value is the initial value for the counter. If value is omitted,
the counter is set to a value of 1.A BoundedSemaphore works exactly like a
Semaphore except the number of release() operations cannot exceed the number of
acquire() operations."""
# BoundedSemaphore([value])


"""A subtle difference between a semaphore and a mutex lock is that a semaphore can
be used for signaling. For example, the acquire() and release() methods can be
called from different threads to communicate between producer and consumer threads."""

produced = threading.Semaphore(0)
consumed = threading.Semaphore(1)

def producer():
        while True:
                consumed.acquire()
                #produce_item()
                produced.release()
def consumer():
        while True:
                produced.acquire()
                #item = get_item()
                consumed.release()
        
def Event():
        while False:
                consumed._value()
                consumed.acquire()
                produced.release(1)

"""Events
Events are used to communicate between threads. One thread signals an “event,” and
one or more other threads wait for it.An Event instance manages an internal flag that
can be set to true with the set() method and reset to false with the clear() method.
The wait() method blocks until the flag is true."""

"""Creates a new Event instance with the internal flag set to false.An Event instance, e,
supports the following methods"""
# Event()

"""Returns true only if the internal flag is true.This method is called isSet() in older
code."""
# e.is_set()

"""Sets the internal flag to true.All threads waiting for it to become true are awakened."""
# e.set()

"""Resets the internal flag to false."""
# e.clear()

"""Blocks until the internal flag is true. If the internal flag is true on entry, this method
returns immediately. Otherwise, it blocks until another thread calls set() to set the flag
to true or until the optional timeout occurs. timeout is a floating-point number specifying a timeout period in seconds."""
# e.wait([timeout])


"""Although Event objects can be used to signal other threads, they should not be used
to implement the kind of notification that is typical in producer/consumer problems.
For example, you should avoid code like this:"""

evt = Event()

def producer():
        while True:
                    # produce item
                    ...
                    evt.signal()
def consumer():
        while True:
                # Wait for an item
                evt.wait()
                # Consume the item
                ...
                # Clear the event and wait again
                evt.clear()

"""This code does not work reliably because the producer might produce a new item in
between the evt.wait() and evt.clear() operations. However, by clearing the
event, this new item won’t be seen by the consumer until the producer creates a new
item. In the best case, the program will experience a minor hiccup where the processing"""

#Condition Variables
"""A condition variable is a synchronization primitive, built on top of another lock that’s used
when a thread is interested in a particular change of state or event occurring.A typical
use is a producer-consumer problem where one thread is producing data to be consumed by another thread.A new Condition instance is created using the following
constructor:"""

"""Creates a new condition variable. lock is an optional Lock or RLock instance. If not
supplied, a new RLock instance is created for use with the condition variable."""
# Condition([lock])

#A condition variable, cv, supports the following methods:

"""Acquires the underlying lock.This method calls the corresponding acquire(*args)
method on the underlying lock and returns the result."""
# cv.acquire(*args)

"""Releases the underlying lock.This method calls the corresponding release() method
on the underlying lock."""
# cv.release()

"""Waits until notified or until a timeout occurs.This method is called after the calling
thread has already acquired the lock.When called, the underlying lock is released, and
the thread goes to sleep until it’s awakened by a notify() or notifyAll() call performed on the condition variable by another thread. Once awakened, the thread reacquires the lock and the method returns. timeout is a floating-point number in seconds.
If this time expires, the thread is awakened, the lock reacquired, and control returned."""
# cv.wait([timeout])

"""Wakes up one or more threads waiting on this condition variable.This method is called
only after the calling thread has acquired the lock, and it does nothing if no threads are
waiting. n specifies the number of threads to awaken and defaults to 1.Awakened
threads don’t return from the wait() call until they can reacquire the lock."""
# cv.notify([n])

"""Wakes up all threads waiting on this condition.This method is called notifyAll() in
older code."""
# cv.notify_all()

#Here is an example that provides a template of using condition variables:

cv = threading.Condition()
def producer():
        while True:
                cv.acquire()
                #produce_item()
                cv.notify()
                cv.release()
def consumer():
        while True:
                cv.acquire()
                while not InterruptedError():
                            cv.wait() # Wait for an item to show up
                cv.release()
                #consume_item()

"""A subtle aspect of using condition variables is that if there are multiple threads waiting
on the same condition, the notify() operation may awaken one or more of them (this
behavior often depends on the underlying operating system). Because of this, there is
always a possibility that a thread will awaken only to find that the condition of
interest no longer holds.This explains, for instance, why a while loop is used in the
consumer() function. If the thread awakens, but the produced item is already gone, it
just goes back to waiting #for the next signal"""

class StoppableThread(threading.Thread):
        def __init__(self):
                threading.Thread.__init__()
                self._terminate = False
                self._suspend_lock = threading.Lock()
        def terminate(self):
                self._terminate = True
        def suspend(self):
                self._suspend_lock.acquire()
        def resume(self):
                self._suspend_lock.release()
        def run(self):
                while True:
                            if self._terminate:
                                break
                            self._suspend_lock.acquire()
                            self._suspend_lock.release()


#Utility Functions

#The following utility functions are available:

"""Returns the number of currently active Thread objects."""
# active_count()

"""Returns the Thread object corresponding to the caller’s thread of control."""
# current_thread()

"""Returns a list of all currently active Thread objects."""
# enumerate()

"""Returns a local object that allows for the storage of thread-local data.This object is
guaranteed to be unique in each thread"""
# local()

"""Sets a profile function that will be used for all threads created. func is passed to
sys.setprofile() before each thread starts running."""
# setprofile(func)

"""Sets a tracing function that will be used for all threads created. func is passed to
sys.settrace() before each thread starts running"""
# settrace(func)

"""Returns the stack size used when creating new threads. If an optional integer size is
given, it sets the stack size to be used for creating new threads. size can be a value that
is 32768 (32KB) or greater and a multiple of 4096 (4KB) for maximum portability"""
# stack_size([size])


