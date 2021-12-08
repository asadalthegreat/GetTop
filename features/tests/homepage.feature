Feature: Homepage

  Scenario: Top banner arrows wrap and dots move banner image
    Given I open the Gettop home page
    Then the iPad banner is visible
    And I click on the Next banner arrow
    Then the Macbook banner is visible
    And I click on the Next banner arrow
    Then the iPad banner is visible
    And I click on the Previous banner arrow
    Then the Macbook banner is visible
    And I click on the Previous banner arrow
    Then the iPad banner is visible
    And I click on bottom dot 2
    Then the Macbook banner is visible
    And I click on bottom dot 1
    Then the iPad banner is visible

  Scenario Outline: Product banner links to the correct category page
    Given I open the Gettop home page
    When I click on the <device> banner
    Then I verify that I've navigated to the <device> category page
  Examples:
    |device |
    |iPad|
    |MacBook|

  Scenario Outline: Browse Categories links function correctly
    Given I open the Gettop home page
    When Browse Our Categories text is visible
    Then I click on the <device> category
    And I verify that I've navigated to the <device> category page
  Examples:
    |device |
    |Accessories|
    |iPad|
    |iPhone|
    |MacBook|
