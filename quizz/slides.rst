
============
Python Quizz
============

-------
Summary
-------

No phones ;)
No laptops ;)
Find the value of the last statement.

--
1
--

.. code-block:: python

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

--
2
--

.. code-block:: python

    a = b = []
    a.append(1)
    b
    # A: []
    # B: [1]
    # C: an exception is raised
    # D: None

--
3
--

.. code-block:: python

    a = b = []
    a = a + [1]
    b
    # A: []
    # B: [1]
    # C: an exception is raised
    # D: None

--
4
--

.. code-block:: python

    a = b = []
    a += [1]
    b
    # A: []
    # B: [1]
    # C: an exception is raised
    # D: None

--
5
--

.. code-block:: python

    a = []

    def f():
        a.append(1)

    f()
    a
    # A: []
    # B: [1]
    # C: an exception is raised
    # D: None

--
6
--

.. code-block:: python

    a = 0

    def f():
        a = 1

    f()
    a
    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
7
--

.. code-block:: python

    a = 0

    def f():
        a += 1

    f()
    a
    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
8
--

.. code-block:: python

    class A(object):
        pass

    a = A()
    a.attribute = 1
    a.attribute

    # A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
9
--

.. code-block:: python

    class A(object):
        __slots__ = []

    a = A()
    a.attribute = 1
    a.attribute

    # A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
10
--

.. code-block:: python

    all([0, 1, 2])

    # A: [0, 1, 2]
    # B: False
    # C: True
    # D: []

--
11
--

.. code-block:: python

    any([])

    # A: []
    # B: False
    # C: True
    # D: an exception is raised

--
12
--

.. code-block:: python

    1 or 2 and 3

    # A: 1
    # B: 3
    # C: True
    # D: False

--
13
--

.. code-block:: python

    r'\ntest'.strip()

    # A: 'test'
    # B: '\ntest'
    # C: '\\ntest'
    # D: r'\\ntest'

--
14
--

.. code-block:: python

    [i for i in a for a in [[1], [2]]]

    # A: [1, 2]
    # B: [2, 1]
    # C: an exception is raised
    # D: []

--
15
--

.. code-block:: python

    a = {1: 2}
    a.get(1.0, 3)

    # A: 2
    # B: 3
    # C: an exception is raised
    # D: None

--
16
--

.. code-block:: python

    import itertools

    [a for a in itertools.chain([1, 2], (3,))]

    # A: [1, 2, 3]
    # B: [[1, 2], [3]]
    # C: [[1, 2], (3)]
    # D: an exception is raised

--
17
--

.. code-block:: python

    getattr('1', 'isdigit')

    # A: True
    # B: False
    # C: <function>
    # D: an exception is raised

--
18
--

.. code-block:: python

    isinstance(1, (float, str))
    # A: True
    # B: False
    # C: 1
    # D: an exception is raised

--
19
--

.. code-block:: python

    'test'.startswith(('T', 't'))

    # A: True
    # B: False
    # C: 'test'
    # D: an exception is raised

--
20
--

.. code-block:: python

    temp = 0
    a = 'hot' if temp > 25 else 'cold'
    a

    # A: True
    # B: False
    # C: 0
    # D: 'cold'

--
21
--

.. code-block:: python

    next(enumerate(['A', 'B'], start=1))[0]

    # A: 'A'
    # B: 'B'
    # C: 0
    # D: 1

--
22
--

.. code-block:: python

    next(iter([2, 3], 2))

    # A: 2
    # B: 3
    # C: an exception is raised
    # D: None

--
23
--

.. code-block:: python

    class A(object):
        def __init__(self, value):
            self.value = value
        def __format__(self, fmt):
            return fmt

    '{0:short}'.format(A(1))

    # A: 'short'
    # B: '1'
    # C: an exception is raised
    # D: '<object>'

--
24
--

.. code-block:: python

    a = (i for i in range(10))
    a[0]

    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

---
End
---
--
1
--

.. code-block:: python

    def f(a=[]):
        a.append(1)
        return a

    f([2, 3])
    f()
    f()
    # A: []
    # B: [2, 3, 1, 1]
    # C: [1]
    > D: [1, 1]

--
2
--

.. code-block:: python

    a = b = []
    a.append(1)
    b
    # A: []
    > B: [1]
    # C: an exception is raised
    # D: None

--
3
--

.. code-block:: python

    a = b = []
    a = a + [1]
    b
    > A: []
    # B: [1]
    # C: an exception is raised
    # D: None

--
4
--

.. code-block:: python

    a = b = []
    a += [1]
    b
    # A: []
    > B: [1]
    # C: an exception is raised
    # D: None

--
5
--

.. code-block:: python

    a = []

    def f():
        a.append(1)

    f()
    a
    # A: []
    > B: [1]
    # C: an exception is raised
    # D: None

--
6
--

.. code-block:: python

    a = 0

    def f():
        a = 1

    f()
    a
    > A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
7
--

.. code-block:: python

    a = 0

    def f():
        a += 1

    f()
    a
    # A: 0
    # B: 1
    > C: an exception is raised
    # D: None

--
8
--

.. code-block:: python

    class A(object):
        pass

    a = A()
    a.attribute = 1
    a.attribute

    > A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
9
--

.. code-block:: python

    class A(object):
        __slots__ = []

    a = A()
    a.attribute = 1
    a.attribute

    > A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
10
--

.. code-block:: python

    all([0, 1, 2])

    # A: [0, 1, 2]
    > B: False
    # C: True
    # D: []

--
11
--

.. code-block:: python

    any([])

    # A: []
    > B: False
    # C: True
    # D: an exception is raised

--
12
--

.. code-block:: python

    1 or 2 and 3

    > A: 1
    # B: 3
    # C: True
    # D: False

--
13
--

.. code-block:: python

    r'\ntest'.strip()

    # A: 'test'
    # B: '\ntest'
    > C: '\\ntest'
    # D: r'\\ntest'

--
14
--

.. code-block:: python

    [i for i in a for a in [[1], [2]]]

    # A: [1, 2]
    # B: [2, 1]
    > C: an exception is raised
    # D: []

--
15
--

.. code-block:: python

    a = {1: 2}
    a.get(1.0, 3)

    > A: 2
    # B: 3
    # C: an exception is raised
    # D: None

--
16
--

.. code-block:: python

    import itertools

    [a for a in itertools.chain([1, 2], (3,))]

    > A: [1, 2, 3]
    # B: [[1, 2], [3]]
    # C: [[1, 2], (3)]
    # D: an exception is raised

--
17
--

.. code-block:: python

    getattr('1', 'isdigit')

    # A: True
    # B: False
    > C: <function>
    # D: an exception is raised

--
18
--

.. code-block:: python

    isinstance(1, (float, str))
    # A: True
    > B: False
    # C: 1
    # D: an exception is raised

--
19
--

.. code-block:: python

    'test'.startswith(('T', 't'))

    > A: True
    # B: False
    # C: 'test'
    # D: an exception is raised

--
20
--

.. code-block:: python

    temp = 0
    a = 'hot' if temp > 25 else 'cold'
    a

    # A: True
    # B: False
    # C: 0
    > D: 'cold'

--
21
--

.. code-block:: python

    next(enumerate(['A', 'B'], start=1))[0]

    # A: 'A'
    # B: 'B'
    # C: 0
    > D: 1

--
22
--

.. code-block:: python

    next(iter([2, 3], 2))

    # A: 2
    # B: 3
    > C: an exception is raised
    # D: None

--
23
--

.. code-block:: python

    class A(object):
        def __init__(self, value):
            self.value = value
        def __format__(self, fmt):
            return fmt

    '{0:short}'.format(A(1))

    > A: 'short'
    # B: '1'
    # C: an exception is raised
    # D: '<object>'

--
24
--

.. code-block:: python

    a = (i for i in range(10))
    a[0]

    # A: 0
    # B: 1
    > C: an exception is raised
    # D: None

