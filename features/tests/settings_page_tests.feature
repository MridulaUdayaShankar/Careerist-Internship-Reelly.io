# Created by mridulas_macair at 17/03/25
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User should be able to login to Reelly.io, Click on Settings menu,Click on the verification option, Verify the right page opens, Verify “upload image” and “Next step” buttons are available.
    Given Open reelly main page
    Then Enter email
    Then Enter password
    When Click continue

    When Click on Settings
    Then Click on the verification option
    Then Verify if upload image page opens
    Then Verify upload image button is available
    Then Verify next step button is available
