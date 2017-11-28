#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def hello(name='World'):
    """
    This says hello.

    >>> hello()
    See you World!
    """
    print 'See you %s!' % name


def _test():
    """Testing!
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':

    _test()

    if len(sys.argv) > 1:
        hello(sys.argv[1])
    else:
        hello()
