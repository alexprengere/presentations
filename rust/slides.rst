
====
Rust
====

-------
History
-------

+ First commits from 2006
+ Fist release 2010
+ Version 1.0 in 2015
+ Currently 1.45.2

-------
History
-------

+ Statically compiled: C, C++, Go, Java, Rust
+ Dynamically compiled: Python, Javascript

-------
History
-------

Memory management:

+ Automatic: Python, Go, Java, Rust
+ Manual: C, C++

-------
History
-------

Garbage collected:

+ Yes: Python, Go, Java
+ No: C, C++, Rust

---------
Ownership
---------

Each value in Rust has a variable thatâ€™s called its owner.
There can only be one owner at a time.
When the owner goes out of scope, the value will be dropped.

--
1
--

.. code-block:: rust

    def f(a=[]):
        a.append(1)
        return a

    f([2, 3])
    f()
    f()
    # A: []
    # B: [2, 3, 1, 1]
    # C: [1]
    # D: [1, 1]
