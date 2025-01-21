# Created by mridulas_macair at 16/01/25
Feature: # Enter feature name here
  # Enter feature description here
  Scenario: User should be able to login to Reelly.io,click on "Secondary" menu option and verify if the page opens,choose filter option "want to buy" and apply, verify if filter is applied
    Given Open reelly main page
    Then Enter email
    Then Enter password
    When Click continue

    Then Verify "Off-plan" tab is opened
    When Click on “Secondary” option at the left side menu
    Then Verify the right page opens

    Given Click on Filters
    When Filter the products by “want to buy”
    When Click on Apply Filter
    Then Verify “want to buy” is seen on each card




