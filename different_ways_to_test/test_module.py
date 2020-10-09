from datetime import datetime
from module import absolute_diff

import pytest


# PARAMETRIZED TESTS
#
@pytest.mark.parametrize(
    "dt1,dt2,result",
    [
        (datetime(2020, 1, 1, 0), datetime(2020, 1, 2, 0), 3600 * 24),
        (datetime(2020, 1, 1, 12), datetime(2020, 1, 1, 13), 3600),
    ],
)
def test_difference(dt1, dt2, result):
    assert absolute_diff(dt1, dt2) == result


# PARAMETRIZED FIXTURES REUSED ACCROSS TESTS
#
@pytest.fixture(
    params=[
        (datetime(2020, 1, 1, 0), datetime(2020, 1, 2, 0)),
        (datetime(2020, 1, 1, 1), datetime(2020, 1, 2, 1)),
        (datetime(2020, 1, 1, 1), datetime(2020, 1, 2, 1)),
        (datetime(2020, 1, 1, 1), datetime(2020, 1, 2, 1)),
    ]
)
def interval(request):
    return request.param

def test_positivity(interval):
    assert absolute_diff(*interval) >= 0

def test_symmetry(interval):
    dt1, dt2 = interval
    assert absolute_diff(dt1, dt2) == absolute_diff(dt2, dt1)


# HYPOTHESIS CORNER
#
from hypothesis import strategies as st, given, settings
from hypothesis.extra.dateutil import timezones

@settings(max_examples=100)
@given(st.datetimes(timezones=timezones()),
       st.datetimes(timezones=timezones()))
def test_hyp_positivity(dt1, dt2):
    assert absolute_diff(dt1, dt2) >= 0


@given(st.datetimes(timezones=timezones()),
       st.datetimes(timezones=timezones()))
def test_hyp_symmetry(dt1, dt2):
    assert absolute_diff(dt1, dt2) == absolute_diff(dt2, dt1)
