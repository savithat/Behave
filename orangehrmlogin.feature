Feature: orangehrm login page

  Scenario: login to the orangehrm by giving proper credentials
    Given I launch the chrome browser
    When I open the orangehrm page
    And enter user name "Admin" and password "admin123"
    And click on login button
    Then must login to orangehrm dashboard page


  Scenario Outline: login to the orangehrm by giving proper credentials
    Given I launch the chrome browser
    When I open the orangehrm page
    And enter user name "<user>" and password "<pwd>"
    And click on login button
    Then must login to orangehrm dashboard page

    Examples:
      | user  | pwd      |
      | Admin | admin123 |
      | hello | wrong    |
      | savi  | good123  |
      | sanju | verygd   |

