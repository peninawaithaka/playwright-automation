Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given I am on the login page

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I login as "standard" user
    # Then I should see an Swag Labs

