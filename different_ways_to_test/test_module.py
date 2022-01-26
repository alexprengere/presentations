from datetime import datetime, timedelta, timezone
from hypothesis import strategies as st, given, settings
import pytest

from module import absolute_diff


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


# PARAMETRIZED FIXTURES
#
@pytest.fixture(
    params=[
        datetime(2020, 1, 1, 0),
        datetime(2020, 1, 2, 0),
        datetime(2020, 1, 1, 1),
    ]
)
def dt1(request):
    return request.param


@pytest.fixture(
    params=[
        datetime(2020, 1, 1, 0),
        datetime(2020, 1, 2, 0),
        datetime(2020, 1, 1, 1),
    ]
)
def dt2(request):
    return request.param


def test_positivity(dt1, dt2):
    assert absolute_diff(dt1, dt2) >= 0


def test_symmetry(dt1, dt2):
    assert absolute_diff(dt1, dt2) == absolute_diff(dt2, dt1)


# HYPOTHESIS CORNER
#
@settings(max_examples=100)
@given(
    st.datetimes(timezones=st.timezones()),
    st.datetimes(timezones=st.timezones()),
)
def test_hyp_positivity(dt1, dt2):
    assert absolute_diff(dt1, dt2) >= 0


@given(
    st.datetimes(timezones=st.timezones()),
    st.datetimes(timezones=st.timezones()),
)
def test_hyp_symmetry(dt1, dt2):
    assert absolute_diff(dt1, dt2) == absolute_diff(dt2, dt1)


@settings(max_examples=100_000)
@given(
    st.datetimes(
        timezones=st.timezones(),
        min_value=datetime(2010, 10, 20),
        max_value=datetime(2010, 10, 30),
    )
)
def test_one_hour_later(dt):
    dt_utc = dt.astimezone(timezone.utc)
    dt_plus_one = (dt_utc + timedelta(hours=1)).astimezone(dt.tzinfo)
    assert absolute_diff(dt_plus_one, dt) == 3600
