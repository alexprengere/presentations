
Feature: Datetime difference
    A module handling datetime utilities

    Scenario: Difference with itself
        Given A datetime
        When I do the difference with itself
        Then difference should be zero

    Scenario: Positivity
        Given Two datetime objects
        When I do their difference
        Then difference should be positive
