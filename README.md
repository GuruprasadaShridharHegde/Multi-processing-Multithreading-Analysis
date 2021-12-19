# Multi-processing-Perfect-Number-Analysis
---------------------------------------------------------------------------------------------------- ## Task given by sameer.sinha@saarthi.ai
## What is Multi-Processing ?
Hell Sir, before going to start the approach what you had given during the interview I would like to brief about Multiprocessing. Multiprocessing is a package that supports spawning processes using an API similar to the threading module. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. 
* Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.
* A global interpreter lock (GIL) is a mechanism used in Python interpreter to synchronize the execution of threads so that only one native thread can execute at a time, even if run on a multi-core processor.
* The primary classes of the Python multiprocessing module are:

  1. Process
  2. Queue
  3. Lock
 * If I take the example of to find the perfect number between 1 to 10000 would be easy, but if i want to find perfect numbers between 1 to 30000000 then it may take more than one year and also consumes huge computer resources. So as a solution for this we have a multiprocess and multi threading package in python. Let us know what are they:
 ![Process vs thread](https://user-images.githubusercontent.com/85961223/146666604-7eceee1d-d41b-480b-994a-68726b93ecf8.png)
 ### Pros
* Less time consuming
* Separate memory space
* Code is usually straightforward
* Takes advantage of multiple CPUs & cores
* Avoids GIL limitations for cPython(instead, it's more of a communication model for IPC)
* Child processes are interruptible/killable
* Python multiprocessing module includes useful abstractions with an interface much like threading.
## What is multithreading ?
The ability of a process to execute multiple threads parallelly is called multithreading. Ideally, multithreading can significantly improve the performance of any program. And Python multithreading mechanism is pretty user-friendly, which you can learn quickly.

    Python offers two modules to implement threads in programs.
    
    <thread> module 
    <threading> module
### Pros
* Resource Sharing
* Responsiveness
* Utilization of Multiprocessor Architecture
* Economy
### Difference

![Thread vs process](https://user-images.githubusercontent.com/85961223/146673128-0f5fb9aa-d7fb-48df-a367-c997ff29d295.jpg)


### Thank you Saarthi.AI and Team. 
These tasks are like bit challenging and curious. I learnt so many things during the assignment and Rasa execution.Whether I get select or not in the interview process, I don't know but my journey towards Chatbot creation has been started. I will try to apply in different domain and develop Chatbots in various field's using AI/ML and Python.

