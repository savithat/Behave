Feature: OrangeHRM

  Background: common steps
     Given I launch the chrome browser
    When I open the orangehrm page

  Scenario: orange hrm logo present on the home page
    Then check the logo present on the home page
    And close the browser

  Scenario Outline: login to the orangehrm by giving proper credentials
    When enter user name "<user>" and password "<pwd>"
    And click on login button
    Then must login to orangehrm dashboard page

    Examples:
      | user  | pwd      |
      | Admin | admin123 |
      | hello | wrong    |
      | savi  | good123  |
      | sanju | verygd   |
