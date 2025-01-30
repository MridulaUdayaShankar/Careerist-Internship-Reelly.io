# Created by mridulas_macair at 16/01/25
@smoke
Feature: Mobile testing
  # Enter feature description here
  Scenario: Mobile Web testing
    Given Open reelly main page
    Then Enter email
    Then Enter password
    When Click continue

    Then Verify "Off-plan" tab is opened
    When Click on “Secondary” option at the left side menu for mobile

    Given Click on Filters
    When Filter the products by “want to buy”
    When Click on Apply Filter
    Then Verify “want to buy” is seen on each card

    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button


