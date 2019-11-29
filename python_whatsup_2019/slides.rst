
==================
Python: what's up?
==================

----------
Vocabulary
----------

+ Python is the language, created in 1991 by Guido Van Rossum
+ CPython is the interpreter (a C program that executes Python code)

------------------------
Organization before 2019
------------------------

+ *Core developers* develop CPython
+ *PEP* are *Python Enhancement Proposal*, documents proposing changes to Python
+ Guido accepts or rejects PEPs, or delegates the decision

---
PSF
---

The Python Software Foundation (PSF) is a non-profit corporation that holds the intellectual property rights behind the Python programming language.

Also: organizes PyCon US, support other Python conferences, funding.

-----------------------------
Development *of* the language
-----------------------------

+ python-committers, python-dev, python-ideas mailing lists
+ *discuss.python.org* forum (more recently)
+ CPython sources are now on GitHub
+ Bug tracker is at *bugs.python.org* aka "bpo"

--------
Builtins
--------

+ No import needed
+ API may change with every major Python release (2.x, 3.x)

::

    % python
    >>> print([])

----------------
Standard library
----------------

+ Import needed
+ API may change with every minor Python release (2.6.x, 2.7.x)

::

    % python
    >>> import datetime
    >>> datetime.date

----
PyPI
----

+ Automated installation from *pypi.python.org* with ``easy_install`` or ``pip``
+ API may change anytime

::

    % pip install numpy
    % python
    >>> import numpy
    >>> numpy.array

-----------------
Python 3.5 (2015)
-----------------

+ PEP 492: ``async`` and ``await`` are new keywords
+ PEP 465: ``@`` is new operator for matrix multiplication: ``a @ b`` (``__matmul__``)
+ PEP 484: new ``typing`` module


-----------------
Python 3.6 (2016)
-----------------

+ PEP 506: new ``secrets`` module
+ PEP 498: formatted string literals: ``f'Next year is {1 + today().year}'``
+ PEP 515: underscores in numeric literals: ``1_000_000``
+ PEP 526: syntax for variable annotations: ``a: Dict[int, int] = {}``
+ PEP 525: asynchronous generators: ``async`` in generators
+ PEP 530: asynchronous comprehensions: ``async`` in comprehensions
+ Multiple speed optimizations

-----------------
Python 3.7 (2018)
-----------------

+ PEP 563: postponed evaluation of type annotations
+ PEP 567: Context Variables
+ PEP 557: Data Classes
+ PEP 553: the new breakpoint() function.
+ PEP 562: customization of access to module attributes.
+ PEP 560: core support for typing module and generic types.
+ dicts are sorted

-----------------
Python 3.8 (2019)
-----------------

+ PEP 8016: The Steering Council Model
+ PEP 572: assignment expressions: ``while block := f.read(256):``
+ PEP 570: positional only parameters ``def f(a, /, b, *, c):``
+ PEP 578: Python Runtime Audit Hooks
+ PEP 587: Python Initialization Configuration
+ PEP 574: Pickle protocol 5 with out-of-band data
+ Multiple speed optimizations (C API, global variables access)
+ stdlib additions: `statistics`, `math`, `functools`, `asyncio`, `importlib`

-------------------------
PEP 8016: Core developers
-------------------------

+ elected for life by 2/3 of positive votes and no veto by steering council
+ can modify PEP8016 by 2/3 of the vote
+ can be declared inactive after 2 years of inactivity, and loose nomination, voting, and committing rights
+ can regain their active status

--------------------------
PEP 8016: Steering council
--------------------------

+ 5 people elected using Condorcet method, by the core developers
+ candidates must be nominated by a core developer, and can themselves be core developer or not
+ self nomination are allowed for core developers
+ a term last for a feature release
+ no more than 2 people working for the same employer
+ can eject core developers with a 2/3 vote (effectively 4:1)
+ vote of no confidence can happen by a 2/3 vote from the core developers

---------------------------------
PEP 8016: Steering council powers
---------------------------------

+ Accept or reject PEPs
+ Enforce or update the project's code of conduct
+ Work with the PSF to manage any project assets
+ Delegate parts of their authority to other subcommittees or processes

-----------------
Python 3.9 (2020)
-----------------

+ PEP 602: Python adopts a stable annual release cadence

-------
PEP 602
-------

+ One feature release every year
+ 7 months alphas, 3 months betas (only bug fixes), 2 months release candidates
+ 1.5 years of bug fixes updates, 3.5 years of security updates (source only)
+ a release manager is elected to manage 2 feature releases and their maintenance releases

-------
PEP 602
-------

.. image:: pep_602.png
   :scale: 90 %
   :align: center

-------
PEP 602
-------

+ makes releases smaller
+ puts features and bug fixes in hands of users sooner
+ creates a more gradual upgrade path for users
+ creates a predictable calendar for releases where the final release is always in October
+ increases the explicit alpha release phase, which provides meaningful snapshots of progress on new features

-----------
Coming next
-----------

Draft PEPs:

+ PEP 603: Adding a frozenmap type to collections
+ PEP 604: Complementary syntax for Union[]: ``str|int`` vs ``Union[int,str]``
+ PEP 585: Type Hinting Generics In Standard Collections ``def find(haystack: dict[str, list[int]]) -> int:``

Python 2.7 last maintenance release in 2020.
