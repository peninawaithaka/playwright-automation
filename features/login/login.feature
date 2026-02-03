Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given I am on the login page

  Scenario Outline: Successful login with valid credentials
    # When I login as "standard" user
    When I login with username "<username>" and password "<password>" on the sauce demo page
    Then I should see a "<results>" message
    Examples:
    | username        | password      | results  |
    | standard_user   | secret_sauce  | success |
    | locked_out_user | secret_sauce  | error   |
    | invalid_user    | wrong_pass    | error   |


