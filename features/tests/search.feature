Feature: Search products

  Scenario: Search for existing product and see correct results
    Given I open the Gettop home page
    When I click on the search icon
    And I input ipad into the search bar and hit enter
    Then I verify the results are in the ipad category

  Scenario: Search for non-existing product and see 'no products' message
    Given I open the Gettop home page
    When I click on the search icon
    And I input android into the search bar and hit enter
    Then I verify the text No products were found matching your selection.