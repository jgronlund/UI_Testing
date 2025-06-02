
Feature: Login Functionality

    Scenario: Successful Login
        Given the user enters the username "admin" and password "1234"
        When they click the login button
        Then they should be redirected to the dashboard
    
    Scenario: Failed Login
        Given the user enters the username "admin" and password "1235"
        When they click the login button
        Then they should see an error message