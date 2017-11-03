
=====================================
Python2, Python3: coding for tomorrow
=====================================

-------
Summary
-------

+ The future is now
+ A brief history of Python3
+ Write hybrid code
+ Mypy

-----------------
Python 3.0 (2006)
-----------------

+ ``print`` is a function, not a keyword
+ ``1 / 2 = 0.5`` and not ``0``
+ strings are unicode (and Python2 strings are ``bytes``)
+ iterators instead of lists (dict.items(), ``map``, ``filter``, ``zip``, ``range``)
+ ordering is stricter (raises ``TypeError`` if undefined)
+ ``long`` is now merged with ``int``
+ functions annotations ``def pow2(a: "value") -> "result":``
+ stdlib cleaning: ``httplib`` -> ``http``

-----------------
Python 3.3 (2012)
-----------------

+ virtualenv module in ``stdlib`` (``venv``)
+ ``yield from`` can be used to yield from another generator
+ ``u'test'`` is valid Python (again)

-----------------
Python 3.4 (2014)
-----------------

+ PEP 453: ``pip`` bundled with Python
+ PEP 3156: new ``asyncio`` module
+ PEP 435: new ``enums`` module
+ PEP 428: new ``pathlib`` module
+ PEP 450: new ``statistics`` module

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

Mypy?

-------------------
How to use Python 3
-------------------

.. code-block:: python

 ROOT=/remote/tmp/rnd-ssp/ssp-adm-data-processing/python/

 virtualenv .env -p "$ROOT/Python-3.6.0/bin/python3"

-----------------
Write hybrid code
-----------------

When should I write hybrid code (Python2/3 compatible)?


---------------------------------
Write hybrid code: ``__future__``
---------------------------------

.. code-block:: python

 # Do not use
 print >> sys.stderr, 1, 2, 3

 # Use
 from __future__ import print_function

 print(1, 2, 3, file=sys.stderr)

---------------------------------
Write hybrid code: ``__future__``
---------------------------------

.. code-block:: python

 from __future__ import division

 1 / 2  # 0.5
 1 // 2 # 0

---------------------------------
Write hybrid code: ``__future__``
---------------------------------

.. code-block:: python

 from __future__ import unicode_literals

 s = 'test'  # u'test'

-------------------------------------
Write hybrid code: `unicode handling`
-------------------------------------

.. code-block:: python

 with open('README', 'b') as f:
     content = f.read()  # bytes

 content.decode('ascii')  # unicode

-----------------
Write hybrid code
-----------------

.. code-block:: python

 # Do not use
 a = {}
 if a.has_key('key'):

 # Use
 if 'key' in a:

------------------------
Write hybrid code: `six`
------------------------

.. code-block:: python

 # Do not use
 a.iteritems()

 # Use
 import six
 six.iteritems(a)

 # Or just
 a.items()  # list in Python2, iterator in Python3

------------------------
Write hybrid code: `six`
------------------------

Useful ``six`` functions:

+ ``iteritems``, ``itervalues``, ``iterkeys`` for manipulating dicts
+ ``add_metaclass``
+ ``reraise`` to re-raise an Exception from an except block

-----------------
Write hybrid code
-----------------

.. code-block:: python

 try:
     import httplib
 except ImportError:  # Python 3
     import http.client as httplib

------------------------------
Write hybrid code: `backports`
------------------------------

.. code-block:: python

 # setup.py
 REQUIRES = [ ... ]

 if sys.version_info < (2, 7):
     REQUIRES += [
         'ordereddict==1.1',
         'Counter==1.0.0',
     ]

 # in your code
 try:
     from collections import OrderedDict
 except ImportError:  # Python 2.6
     from ordereddict import OrderedDict

------------------------------
Write hybrid code: `backports`
------------------------------

.. code-block:: python

 # setup.py
 REQUIRES = [ ... ]

 if sys.version_info < (2, 7):
     REQUIRES.append('pydot2==1.0.33')
 else:  # Python 2.7+
     REQUIRES.append('pydot==1.2.2')

 # in your code
 import pydot

-----------------------
Test hybrid code: `tox`
-----------------------

Use ``tox`` to test your code against multiple Python versions

.. code-block:: ini

 [tox]
 skip_missing_interpreters = true
 envlist = py26,py27,py33,py34,py35,pypy,flake8

 [testenv]
 deps = pytest
 commands = py.test {posargs}

 [testenv:flake8]
 deps = flake8
 commands = flake8

--------------------------
Write hybrid code: summary
--------------------------

+ Use ``__future__`` statements to import Python3 behavior
+ Use ``six`` if necessary
+ Use ``tox`` to test your code against multiple Python versions

----
Mypy
----

Remember function annotations in Python 3.0+?

Remember the ``typing`` module in Python 3.5+?

.. code-block:: python

 from typing import Iterator


 def fib(n: int) -> Iterator[str]:
     a, b = 0, 1
     while a < n:
         yield a
         a, b = b, a + b

----
Mypy
----

Mypy does static analysis for the type hints!

.. code-block:: bash

 $ mypy test3.py
 In function "fib":
 Incompatible types in yield (actual type "int", expected "str")

----
Mypy
----

For Python2, you need the ``typing`` backport: ``pip install typing``

You can use comments to specify types!

.. code-block:: python

 from typing import Iterator


 def fib(n):  # type: (int) -> Iterator[str]
     a, b = 0, 1
     while a < n:
         yield a
         a, b = b, a + b

----
Mypy
----

Same error:

.. code-block:: bash

 $ mypy test2a.py
 In function "fib":
 Incompatible types in yield (actual type "int", expected "str")

----
Mypy
----

Mypy will infer most types, and lets you explicitely hint types for variables in comments.

.. code-block:: python

 from typing import Dict

 d = {}  # type: Dict[int, str]
 for key in [1, 2]:
     d[key] = float(key)

Let's test this:

.. code-block:: bash

 $ mypy test2b.py
 Incompatible types in assignment (expression has type "float", target is "str")

----
Mypy
----

Remember variable type annotations in Python 3.6+?

.. code-block:: python

 from typing import Dict

 d: Dict[int, str] = {}
 for key in [1, 2]:
     d[key] = float(key)

.. code-block:: bash

 $ mypy --fast-parser --python-version 3.6 test3b.py
 Incompatible types in assignment (expression has type "float", target is "str")

----
Mypy
----

Mypy itself requires Python3, you can install it globally with:

.. code-block:: bash

 python3 -m pip install --user mypy

Or inside a Python3 virtualenv:

.. code-block:: bash

 pip install mypy
