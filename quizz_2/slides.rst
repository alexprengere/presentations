
============
Python Quizz
============

-------
Summary
-------

Find the value of the last statement.

The code may raise exceptions, but never syntax errors, so do not look for missing colons ;)

Assume the code is Python3.8a3, but the answers would be the same with Python2.

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

    a = []
    b = a
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

    a = []
    b = a
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

    a = 0

    def func():
        print(a)
        a = 1
        return a

    func()

    # A: 0
    # B: 1
    # C: None
    # D: an exception is raised

--
3
--

.. code-block:: python

    a = 0

    def func():
        print(a)
        a = 1
        return a

    func()

    # A: 0
    # B: 1
    # C: None
    > D: an exception is raised

--
4
--

.. code-block:: python

    res = None
    try:
        res = float('not a float')
    except ValueError:
        res = 0
    finally:
        res = 1
    res
    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
4
--

.. code-block:: python

    res = None
    try:
        res = float('not a float')
    except ValueError:
        res = 0
    finally:
        res = 1
    res
    # A: 0
    > B: 1
    # C: an exception is raised
    # D: None

--
5
--

.. code-block:: python

    def func():
        try:
            return float('not a float')
        except ValueError:
            res = 0
            return res
        finally:
            res = 1
            return res
    func()
    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
5
--

.. code-block:: python

    def func():
        try:
            return float('not a float')
        except ValueError:
            res = 0
            return res
        finally:
            res = 1
            return res
    func()
    # A: 0
    > B: 1
    # C: an exception is raised
    # D: None

--
6
--

.. code-block:: python

    import time
    try:
        res = 0
        time.sleep(10)  # CTRL+C after 2 seconds
        res = 1
    except Exception:
        res = 2
    res
    # A: 0
    # B: 1
    # C: an exception is raised
    # D: 2

--
6
--

.. code-block:: python

    import time
    try:
        res = 0
        time.sleep(10)  # CTRL+C after 2 seconds
        res = 1
    except Exception:
        res = 2
    res
    # A: 0
    # B: 1
    > C: an exception is raised
    # D: 2

--
7
--

.. code-block:: python

    class A():
        pass

    a = A()
    a.attribute = 1
    a.attribute

    # A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
7
--

.. code-block:: python

    class A():
        pass

    a = A()
    a.attribute = 1
    a.attribute

    > A: 1
    # B: None
    # C: an exception is raised
    # D: 0

--
8
--

.. code-block:: python

    1 or 2 and 3

    # A: 1
    # B: 3
    # C: True
    # D: False

--
8
--

.. code-block:: python

    1 or 2 and 3

    > A: 1
    # B: 3
    # C: True
    # D: False

--
9
--

.. code-block:: python

    isinstance(True, (str, int))

    # A: True
    # B: False
    # C: 1
    # D: an exception is raised

--
9
--

.. code-block:: python

    isinstance(True, (str, int))

    > A: True
    # B: False
    # C: 1
    # D: an exception is raised

--
10
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
10
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
11
--

.. code-block:: python

    a, b = enumerate(['A', 'B'], start=1)
    b
    # A: 'B'
    # B: 2
    # C: 1
    # D: (2, 'B')

--
11
--

.. code-block:: python

    a, b = enumerate(['A', 'B'], start=1)
    b
    # A: 'B'
    # B: 2
    # C: 1
    > D: (2, 'B')

--
12
--

.. code-block:: python

    a = (i for i in range(10))
    a[0]

    # A: 0
    # B: 1
    # C: an exception is raised
    # D: None

--
12
--

.. code-block:: python

    a = (i for i in range(10))
    a[0]

    # A: 0
    # B: 1
    > C: an exception is raised
    # D: None

--
13
--

.. code-block:: python

    False == False in [False]

    # A: True
    # B: False
    # C: an exception is raised
    # D: None

--
13
--

.. code-block:: python

    False == False in [False]

    > A: True
    # B: False
    # C: an exception is raised
    # D: None

--
14
--

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    l[:3] + l[3:-1]

    # A: [1, 2, 4, 5]
    # B: [1, 2, 3, 5]
    # C: [1, 2, 3, 4]
    # D: [1, 2, 3, 4, 5]

--
14
--

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    l[:3] + l[3:-1]

    # A: [1, 2, 4, 5]
    # B: [1, 2, 3, 5]
    > C: [1, 2, 3, 4]
    # D: [1, 2, 3, 4, 5]

--
15
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
15
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
16
--

.. code-block:: python

    a = [1, 2, -4, 0]
    max(a, key=abs)

    # A: 2
    # B: -4
    # C: 4
    # D: an exception is raised

--
16
--

.. code-block:: python

    a = [1, 2, -4, 0]
    max(a, key=abs)

    # A: 2
    > B: -4
    # C: 4
    # D: an exception is raised

--
17
--

.. code-block:: python

    from collections import defaultdict

    d = defaultdict(lambda: {})
    d[1]['a'] = 0
    d[1]

    # A: 'a'
    # B: 0
    # C: {'a': 0}
    # D: an exception is raised

--
17
--

.. code-block:: python

    from collections import defaultdict

    d = defaultdict(lambda: {})
    d[1]['a'] = 0
    d[1]

    # A: 'a'
    # B: 0
    > C: {'a': 0}
    # D: an exception is raised

--
18
--

.. code-block:: python

    from collections import Counter

    c1 = Counter('aabbb')
    c2 = Counter('abcabca')

    (c1 - c2)['a']


    # A: ''
    # B: 0
    # C: -1
    # D: an exception is raised

--
18
--

.. code-block:: python

    from collections import Counter

    c1 = Counter('aabbb')
    c2 = Counter('abcabca')

    (c1 - c2)['a']


    # A: ''
    > B: 0
    # C: -1
    # D: an exception is raised


--
19
--

.. code-block:: python

    import string
    from itertools import izip_longest  # zip_longest if Py3

    letters = string.letters
    list(izip_longest(range(5), letters))[-1]

    # A: (4, 'e')
    # B: (5, 'e')
    # C: (None, 'Z')
    # D: an exception is raised

--
19
--

.. code-block:: python

    import string
    from itertools import izip_longest  # zip_longest if Py3

    letters = string.letters
    list(izip_longest(range(5), letters))[-1]

    # A: (4, 'e')
    # B: (5, 'e')
    > C: (None, 'Z')
    # D: an exception is raised


--
20
--

.. code-block:: python

    if a := 0:
        a = 1
    a

    # A: 0
    # B: 1
    # C: None
    # D: an exception is raised

--
20
--

.. code-block:: python

    if a := 0:
        a = 1
    a

    > A: 0
    # B: 1
    # C: None
    # D: an exception is raised

--
20
--

.. code-block:: python

    a = 'this'
    f'{a[::-1]} is nice'

    # A: 'siht is nice'
    # B: 'this is nice'
    # C: f'this is nice'
    # D: an exception is raised

--
21
--

.. code-block:: python

    a = 'this'
    f'{a[::-1]} is nice'

    > A: 'siht is nice'
    # B: 'this is nice'
    # C: f'this is nice'
    # D: an exception is raised

--
22
--

.. code-block:: python

    a: int = 2

    def f(integer: float) -> None:
        return False

    f(NotImplemented)

    # A: 0
    # B: None
    # C: False
    # D: an exception is raised

--
22
--

.. code-block:: python

    a: int = 2

    def f(integer: float) -> None:
        return False

    f(NotImplemented)

    # A: 0
    # B: None
    > C: False
    # D: an exception is raised
