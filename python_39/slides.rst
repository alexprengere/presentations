
==========
Python 3.9
==========

+ 3.9.0 rc1: 2020-08-11
+ 3.9.0 rc2: 2020-09-14
+ 3.9.0 final: 2020-10-05

----------
Vocabulary
----------

+ Python is the language, created in 1991 by Guido Van Rossum
+ CPython is the interpreter (a C program that executes Python code)

--------
Builtins
--------

+ No import needed

::

    % python
    >>> print([])

----------------
Standard library
----------------

+ Import needed

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

+ PEP 8016: the Steering Council model
+ PEP 572: assignment expressions: ``while block := f.read(256):``
+ PEP 570: positional only parameters ``def f(a, /, b, *, c):``
+ PEP 578: Python Runtime Audit Hooks
+ PEP 587: Python Initialization Configuration
+ PEP 574: pickle protocol 5 with out-of-band data
+ multiple speed optimizations (C API, global variables access)
+ stdlib additions: `statistics`, `math`, `functools`, `asyncio`, `importlib`

-----------------
Python 3.9 (2020)
-----------------

+ PEP 602: Python adopts a stable annual release cadence
+ PEP 584: add Union Operators To dict
+ PEP 585: type Hinting Generics In Standard Collections
+ PEP 617: new parser
+ PEP 616: new `removeprefix()` and `removesuffix()` string methods
+ PEP 615: support for the IANA Time Zone Database in the Standard Library
+ `graphlib` that contains the graphlib.TopologicalSorter

-----------------
Python 3.9 (2020)
-----------------

+ PEP 584: add Union Operators To dict

.. code:: python

    # a and b are dicts
    merged = a | b

    # Roughly equivalent to
    merged = dict(a)
    merged.update(b)

    # Inplace version
    a |= b

-----------------
Python 3.9 (2020)
-----------------

+ PEP 585: type Hinting Generics In Standard Collections

.. code:: python

    from typing import List, Dict, Tuple

    d: Dict[Tuple, List] = {}  # before
    d: dict[tuple, list] = {}  # after

-----------------
Python 3.9 (2020)
-----------------

+ PEP 616: new `removeprefix()` and `removesuffix()` string methods

.. code:: python

    # Never
    name.rstrip("test_")

    # Before
    if name.startswith("test_"):
        name = name[5:]

    # After
    name.removeprefix("test_")

-----------------
Python 3.9 (2020)
-----------------

+ PEP 615: support for the IANA Time Zone Database in the Standard Library

.. code:: python

    # Before: install pytz or python-dateutil
    # After: use zoneinfo
    from zoneinfo import ZoneInfo

    zone = ZoneInfo("Pacific/Kwajalein")
    dt = datetime(2020, 4, 1, 3, 15, tzinfo=zone)

-----------------
Python 3.9 (2020)
-----------------

+ `graphlib` that contains the graphlib.TopologicalSorter

.. code:: python

    >>> graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    >>> ts = TopologicalSorter(graph)
    >>> tuple(ts.static_order())
    ('A', 'C', 'B', 'D')

------------------
Python 3.10 (2021)
------------------

Already accepted or implemented:

+ PEP 604: Complementary syntax for Union[]: ``str|int`` vs ``Union[int,str]``
+ PEP 618: Add Optional Length-Checking To zip
+ `int.bit_count()`

Under review by the steering council:

+ PEP 622: Structural Pattern Matching
+ PEP 603: Adding a frozenmap type to collections
