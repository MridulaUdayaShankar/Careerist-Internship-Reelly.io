# Created by mridulas_macair at 24/04/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can click on offplan and select sale status

    Given click on Off-plan at the left side menu
    Then verify the right page opens
    When click on filter by sale status
    When click on announced filter
    Then verify each product contains the filter Announced
