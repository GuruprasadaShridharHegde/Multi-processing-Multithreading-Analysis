# Multi-processing-Multithreading-Analysis ⚙
---------------------------------------------------------------------------------------------------- ### Task given by sameer.sinha@saarthi.ai
## What is Multi-Processing ?
Hello Sir, before going to start the approach what you had given during the interview I would like to brief about Multiprocessing. Multiprocessing is a package that supports spawning processes using an API similar to the threading module. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. 
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
## What is multithreading ? 🤔
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

### What is a Thread?
A thread is a unit of execution on concurrent programming. Multithreading is a technique which allows a CPU to execute many tasks of one process at the same time. These threads can execute individually while sharing their process resources.

### What is a Process?
A process is basically the program in execution. When you start an application in your computer (like a browser or text editor), the operating system creates a process.

What is Multithreading in Python?
Multithreading in Python programming is a well-known technique in which multiple threads in a process share their data space with the main thread which makes information sharing and communication within threads easy and efficient. Threads are lighter than processes. Multi threads may execute individually while sharing their process resources. The purpose of multithreading is to run multiple tasks and function cells at the same time.

In this tutorial, you will learn,

What is a Thread?
What is a Process?
What is Multithreading?
What is Multiprocessing?
Python Multithreading vs Multiprocessing
Why use Multithreading?
Python MultiThreading
The Thread and Threading modules
The Thread Module
The Threading Module
Deadlocks and Race conditions
Synchronizing threads
What is GIL?
Why was GIL needed?
What is Multiprocessing?
Multiprocessing allows you to run multiple unrelated processes simultaneously. These processes do not share their resources and communicate through IPC.

### Python Multithreading vs Multiprocessing
To understand processes and threads, consider this scenario: An .exe file on your computer is a program. When you open it, the OS loads it into memory, and the CPU executes it. The instance of the program which is now running is called the process.

### Every process will have 2 fundamental components:

-The Code
-The Data
Now, a process can contain one or more sub-parts called threads. This depends on the OS architecture,.You can think about a thread as a section of the process which can be executed separately by the operating system.

In other words, it is a stream of instructions which can be run independently by the OS. Threads within a single process share the data of that process and are designed to work together for facilitating parallelism.

Why use Multithreading?
Multithreading allows you to break down an application into multiple sub-tasks and run these tasks simultaneously. If you use multithreading properly, your application speed, performance, and rendering can all be improved.

Python MultiThreading
Python supports constructs for both multiprocessing as well as multithreading. In this tutorial, you will primarily be focusing on implementing multithreaded applications with python. There are two main modules which can be used to handle threads in Python:

-The thread module
-The threading module
However, in python, there is also something called a global interpreter lock (GIL). It doesn’t allow for much performance gain and may even reduce the performance of some multithreaded applications. You will learn all about it in the upcoming sections of this tutorial.
The Thread and Threading modules
The two modules that you will learn about in this tutorial are the thread module and the threading module.

However, the thread module has long been deprecated. Starting with Python 3, it has been designated as obsolete and is only accessible as __thread for backward compatibility.

You should use the higher-level threading module for applications which you intend to deploy. The thread module has only been covered here for educational purposes.

### The Thread Module
The syntax to create a new thread using this module is as follows:

thread.start_new_thread(function_name, arguments)
Alright, now you have covered the basic theory to start coding. So, open your IDLE or a notepad and type in the following:

import time
import _thread

def thread_test(name, wait):
   i = 0
   while i <= 3:
      time.sleep(wait)
      print("Running %s\n" %name)
      i = i + 1

   print("%s has finished execution" %name)

if __name__ == "__main__":
    
    _thread.start_new_thread(thread_test, ("First Thread", 1))
    _thread.start_new_thread(thread_test, ("Second Thread", 2))
    _thread.start_new_thread(thread_test, ("Third Thread", 3))
Save the file and hit F5 to run the program. If everything was done correctly, this is the output that you should see:

![Multithread1](https://user-images.githubusercontent.com/85961223/153413941-728fcd9d-49dd-4cc6-adeb-5178264aa628.png)
You will learn more about race conditions and how to handle them in the upcoming sections.

![Multithread2](https://user-images.githubusercontent.com/85961223/153414181-80065319-0291-4115-b5de-7a73ba8b0d66.png)

### CODE EXPLANATION
These statements import the time and thread module which are used to handle the execution and delaying of the Python threads.
Here, you have defined a function called thread_test, which will be called by the start_new_thread method. The function runs a while loop for four iterations and prints the name of the thread which called it. Once the iteration is complete, it prints a message saying that the thread has finished execution.
This is the main section of your program. Here, you simply call the start_new_thread method with the thread_test function as an argument.This will create a new thread for the function you pass as argument and start executing it. Note that you can replace this (thread_test) with any other function which you want to run as a thread.

![Multithread3](https://user-images.githubusercontent.com/85961223/153414331-743cf3b0-6792-4ba7-8e38-842670fa8133.png)


### The Threading Module
This module is the high-level implementation of threading in python and the de facto standard for managing multithreaded applications. It provides a wide range of features when compared to the thread module.

![Multithread4](https://user-images.githubusercontent.com/85961223/153414828-a2e8798f-f615-44e6-9f32-bfd991d14c97.png)


### Thank you Saarthi.AI and Team. 🤗
These tasks are like bit challenging and curious. I learnt so many things during the assignment and Rasa execution. Interview was conducted in a very smooth manner by Sameer Sinha Sir!! Looking forward to work under his team and guidance. My journey towards Chatbot creation has been started. I will try to apply in different domain and develop Chatbots in various field's using AI/ML and Python.

