Feature: Get title and url on Godaddy website

  Scenario:  Check title and get url on Godaddy
    Given Launch chrome browser
    When Open this URL - https://www.godaddy.com/
    And maximize the window
    And get title of the page
    Then get the url of the page
    And close the browser



