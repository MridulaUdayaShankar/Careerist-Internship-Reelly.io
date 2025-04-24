# Created by mridulas_macair at 24/04/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can click on offplan and select sale status

    Given Click on Off-plan at the left side menu
    Then Verify the right page opens
    When Filter by sale status of Announced
    Then Verify each product contains the filter Announced
