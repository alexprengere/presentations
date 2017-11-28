
==================================
Concurrent programming with Python
==================================

-------
Summary
-------

+ Disclaimers
+ Concurrency
+ GIL
+ Multithreading
+ Multiprocessing
+ Summary
+ Hands on

----------
Disclaimer
----------

We are going to talk about *CPython*, the "usual" Python implementation. So, no:

+ Jython
+ StacklessPython
+ Pypy

----------
Disclaimer
----------

We are going to talk about the standard library. So, no:

+ eventlet
+ Twisted
+ parallel Python
+ Circus

http://wiki.python.org/moin/Concurrency/

----------
Disclaimer
----------

.. image:: xVyoSl.jpg
   :scale: 120 %
   :align: center

-----------------
About concurrency
-----------------

"Concurrency is not parallelism."
  -- Rob Pikes

http://blog.golang.org/2013/01/concurrency-is-not-parallelism.html

-----------------
About concurrency
-----------------

"But when people hear the word concurrency they often think of parallelism, a related but quite distinct concept. In programming, concurrency is the composition of independently executing processes, while parallelism is the simultaneous execution of (possibly related) computations. Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once."
  -- Rob Pikes

---------------------
Threads and processes
---------------------

+ threads are lightweight and share memory
+ processes do not share memory

  -- Wikipedia

-----------------------
Global Interpreter Lock
-----------------------

In CPython, the *global interpreter lock*, or *GIL*, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.
 -- Python Wiki

---------------------
Python multithreading
---------------------

``threading`` module in the standard library.

+ Multiple threads will (often) not run in parallel
+ Multiple threads will run concurrently

Some operations release the GIL, like IO operations.

----------------------
Python multiprocessing
----------------------

``multiprocessing`` module in the standard library.

+ The Python interpreter runs in a single process.
+ ``multiprocessing`` forks the interpreter

-------
Summary
-------

+ Use ``threading`` to handle IO-bound problems
+ Use ``multiprocessing`` to handle CPU-bound problems (CPython 2.6+, Pypy 1.5+)

-------
Summary
-------

For Python 3.2+, use ``concurrent.futures``, unifying both APIs.

-------
Summary
-------

If you want to run jobs on several *machines*, try ``parallel python``.

---------
Hands on!
---------

