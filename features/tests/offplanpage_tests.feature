# Created by mridulas_macair at 24/04/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can click on offplan and select sale status

    Given Open reelly main page
    Then Enter email
    Then Enter password
    When Click continue

    Given Click on Off-plan at the left side menu
    Then Verify the offplan page opens
    When Click on filter by sale status
    When Click on announced filter
    Then Verify each product contains the filter Announced
