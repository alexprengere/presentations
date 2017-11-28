
=====================================================
Document and test your Python code, even with pyspark
=====================================================

-------
Summary
-------

+ Documentation
+ Doctests
+ pytest and its plugins
+ Virtualenvs
+ Tox
+ Testing pyspark code offline with pysparkling

-------------
Documentation
-------------

Where you should put your documentation

+ high level description in ``README.md``
+ ``doc`` directory: API documentation (Sphinx), examples
+ multi-line strings at the *top level* of modules, classes, functions

-------------
Documentation
-------------

.. code-block:: python

    """
    Top level comment
    """

    def function():
        """Function short description.

        Details here
        """
        # code here

--------
Doctests
--------

.. code-block:: python

    def square(i):
        """Squarify things.

        >>> square(5)
        25
        """
        return i ** 2

--------
unittest
--------

.. code-block:: python

    import unittest; import doctest; import module

    class SquareTest(unittest.TestCase):
        def test_square(self):
            self.assertEquals(module.square(0), 0)
            self.assertEquals(module.square(4), 16)

    def main():
        s = unittest.TestSuite()
        s.addTests(unittest.makeSuite(SquareTest))
        s.addTests(doctest.DocTestSuite(module))
        return s

    if __name__ == '__main__':
        unittest.main(defaultTest='main')

------
pytest
------

.. code-block:: python

    from module import square

    def test_square():
        assert square(0) == 0
        assert square(4) == 16

------
pytest
------

``unittest`` revamped

+ no boilerplate code
+ automatic tests discovery
+ helpful reports when tests fail
+ really simple: only use ``assert``
+ lots of third party plugins (pytest-benchmark, pytest-coverage)

----------
virtualenv
----------

Run your code isolated from the system.

.. code-block:: bash

 virtualenv --no-site-packages --clear .env
 source .env/bin/python
 # check $ which python

---
Tox
---

``tox`` runs all your tests in separate Virtualenvs, automatically.

.. code-block:: bash

 tox
 # creating multiple virtualenvs
 # running tests
 # reporting

-------
tox.ini
-------

::

    [tox]
    envlist = py26,py27,py33,py34,py35,pypy

    [testenv]
    install_command =
        pip install {opts} {packages}
    deps =
        pytest
        pytest-benchmark
    commands = py.test {posargs}

-----------
pysparkling
-----------

A pure Python implementation of Spark's RDD interface.

`https://github.com/svenkreiss/pysparkling`

