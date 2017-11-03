#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from aggregate import aggregate, aggregate_spark

def test_aggregate(flights):
    assert aggregate(flights) == {'NCE': 4.}


def test_aggregate_empty(empty_flights):
    assert aggregate(empty_flights) == {}


def test_aggregate_spark():
    assert aggregate_spark('flights.csv') == {'CDG': 8, 'ORY': 1}

