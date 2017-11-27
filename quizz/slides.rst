
============
Python Quizz
============

-------
Summary
-------

Find the value of the last statement.

The code may raise exceptions, but never syntax errors, so do not look for missing colons ;)

Assume the code is Python2.6+, but the answers would be the same with Python3.

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

--
25
--

.. code-block:: python

    False == False in [False]

    # A: True
    # B: False
    # C: an exception is raised
    # D: None

--
26
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattr__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
27
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
28
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return object.__getattribute__(name)

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
29
--

.. code-block:: python

    s = set([1, None, [], ()])
    1 in s

    # A: True
    # B: False
    # C: None
    # D: an exception is raised

--
30
--

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    l[:3] + l[3:-1]

    # A: [1, 2, 4, 5]
    # B: [1, 2, 3, 5]
    # C: [1, 2, 3, 4]
    # D: [1, 2, 3, 4, 5]

--
31
--

.. code-block:: python

    a = set([1, 2, 3])
    b = set([4, 5])
    c = set([1, 5])
    a | b & c

    # A: set([1, 5])
    # B: set([1, 2, 3, 5])
    # C: [1, 2, 3, 5]
    # D: an exception is raised

--
32
--

.. code-block:: python

    f = lambda (a, b): NotImplemented
    f(1, 2)

    # A: None
    # B: NotImplemented
    # C: (1, 2)
    # D: an exception is raised

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
    # D: [1, 1]

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
    # B: [1]
    # C: an exception is raised
    # D: None

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
    # A: 0
    # B: 1
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

    # A: 1
    # B: None
    # C: an exception is raised
    # D: 0

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
    > C: an exception is raised
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
    # B: False
    # C: True
    # D: an exception is raised

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

    # A: 1
    # B: 3
    # C: True
    # D: False

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
    # C: '\\ntest'
    # D: r'\\ntest'

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
    # C: an exception is raised
    # D: []

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

    # A: 2
    # B: 3
    # C: an exception is raised
    # D: None

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

    # A: [1, 2, 3]
    # B: [[1, 2], [3]]
    # C: [[1, 2], (3)]
    # D: an exception is raised

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
    # C: <function>
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
    # B: False
    # C: 1
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

    # A: True
    # B: False
    # C: 'test'
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
    # D: 'cold'

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
    # D: 1

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
    # C: an exception is raised
    # D: None

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

    # A: 'short'
    # B: '1'
    # C: an exception is raised
    # D: '<object>'

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
    # C: an exception is raised
    # D: None

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

--
25
--

.. code-block:: python

    False == False in [False]

    # A: True
    # B: False
    # C: an exception is raised
    # D: None

--
25
--

.. code-block:: python

    False == False in [False]

    > A: True
    # B: False
    # C: an exception is raised
    # D: None

--
26
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattr__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
26
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattr__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    > B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
27
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
27
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return 0

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    > C: (0, 0)
    # D: an exception is raised

--
28
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return object.__getattribute__(name)

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    # D: an exception is raised

--
28
--

.. code-block:: python

    class Obj(object):
        def __init__(self):
            self.attr = None
        def __getattribute__(self, name):
            return object.__getattribute__(name)

    o = Obj()
    (o.titi, o.attr)
    # A: (None, 0)
    # B: (0, None)
    # C: (0, 0)
    > D: an exception is raised

--
29
--

.. code-block:: python

    s = set([1, None, [], ()])
    1 in s

    # A: True
    # B: False
    # C: None
    # D: an exception is raised

--
29
--

.. code-block:: python

    s = set([1, None, [], ()])
    1 in s

    # A: True
    # B: False
    # C: None
    > D: an exception is raised

--
30
--

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    l[:3] + l[3:-1]

    # A: [1, 2, 4, 5]
    # B: [1, 2, 3, 5]
    # C: [1, 2, 3, 4]
    # D: [1, 2, 3, 4, 5]

--
30
--

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    l[:3] + l[3:-1]

    # A: [1, 2, 4, 5]
    # B: [1, 2, 3, 5]
    > C: [1, 2, 3, 4]
    # D: [1, 2, 3, 4, 5]

--
31
--

.. code-block:: python

    a = set([1, 2, 3])
    b = set([4, 5])
    c = set([1, 5])
    a | b & c

    # A: set([1, 5])
    # B: set([1, 2, 3, 5])
    # C: [1, 2, 3, 5]
    # D: an exception is raised

--
31
--

.. code-block:: python

    a = set([1, 2, 3])
    b = set([4, 5])
    c = set([1, 5])
    a | b & c

    # A: set([1, 5])
    > B: set([1, 2, 3, 5])
    # C: [1, 2, 3, 5]
    # D: an exception is raised

--
32
--

.. code-block:: python

    f = lambda (a, b): NotImplemented
    f(1, 2)

    # A: None
    # B: NotImplemented
    # C: (1, 2)
    # D: an exception is raised

--
32
--

.. code-block:: python

    f = lambda (a, b): NotImplemented
    f(1, 2)

    # A: None
    # B: NotImplemented
    # C: (1, 2)
    > D: an exception is raised
