#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aggregator

>>> with open('flights.csv') as f:
...     data = aggregate(f)
>>> data['CDG']
8.0
>>> data['ORY']
1.0
"""

from __future__ import with_statement, print_function

from collections import defaultdict
import operator

from pysparkling import Context

def aggregate(f):
    """Aggregate stuff

    >>> with open('flights.csv') as f:
    ...     data = aggregate(f)
    >>> data['CDG']
    8.0
    >>> data['ORY']
    1.0
    """
    data = defaultdict(int)

    for row in f:
        if not row or row.startswith('#'):
            continue
        ori, _, count = row.rstrip().split('^')
        data[ori] += float(count)

    return dict(data)


def extract(row):
    ori, _, count = row.rstrip().split('^')
    return ori, int(count)


def aggregate_spark(source):
    sc = Context()
    return dict(
        (sc.textFile(source)
            .map(extract)
            .reduceByKey(operator.add)
            .collect()))


if __name__ == '__main__':
    with open('flights.csv') as f:
        print(aggregate(f))

    print(aggregate_spark('flights.csv'))
