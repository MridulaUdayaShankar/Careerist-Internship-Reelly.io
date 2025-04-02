# Created by mridulas_macair at 20/03/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open market tab and add company option
    # Enter steps here
    Given Open reelly main page
    Then Enter email
    Then Enter password
    When Click continue

    When Click on Market button
    Then Verify market page opens
    When Click on Add Company button
    Then Verify Publish my company button is available