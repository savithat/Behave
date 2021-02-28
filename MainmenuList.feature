Feature: MainmenuList on HRM page

  Scenario: login to the orangehrm by giving proper credentials
    Given I launch the chrome browser
    When I open the orangehrm page
    And enter user name "Admin" and password "admin123"
    And click on login button
    Then must login to orangehrm dashboard page

  Scenario:Collect list of elements in the 1st main `Menu bar


