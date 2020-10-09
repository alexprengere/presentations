import pytest
from pytest_bdd import scenario, given, when, then

from datetime import datetime
from module import absolute_diff


@pytest.fixture
def dt1():
    return datetime(2020, 1, 1, 12)


@pytest.fixture
def dt2():
    return datetime(2020, 1, 1, 13)


@given("A datetime")
def a_datetime(dt1):
    return dt1


@given("Two datetime objects")
def two_datetime(dt1, dt2):
    return dt1, dt2


@when("I do their difference")
@when("I do the difference with itself")
def diff(dt1):
    # datetimes being immutable, you cannot change their value,
    # so this step is actually done in the "Then"
    # But on mutable objects, here is the step where you update them
    # There is no easy way to pass data from When to Then
    pass


@then("difference should be zero")
def zero(dt1):
    assert absolute_diff(dt1, dt1) == 0


@then("difference should be positive")
def positive(dt1, dt2):
    assert absolute_diff(dt1, dt2) >= 0


@scenario("app.feature", "Difference with itself")
def test_self_diff():
    pass


@scenario("app.feature", "Positivity")
def test_positivity():
    pass
