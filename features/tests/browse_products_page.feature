Feature: Browse Products

  Scenario: Sorting high to low displays products in the correct order
    Given I open the Gettop home page
    When I click on Mac in the header
    And I change to sort high to low
    Then products are displayed from high to low price

  Scenario: Sorting low to high displays products in the correct order
    Given I open the Gettop home page
    When I click on Mac in the header
    And I change to sort low to high
    Then products are displayed from low to high price
