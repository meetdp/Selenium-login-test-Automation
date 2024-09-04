# Selenium Login Test Automation

This project demonstrates automated login tests using Selenium WebDriver for the demo website at [Katalon Demo CURA Healthcare Service](https://katalon-demo-cura.herokuapp.com/). The script includes multiple test cases to verify the behavior of the login system under various conditions.

## Prerequisites

Before running the tests, ensure that you have the following installed:

- Python 3.x
- Selenium WebDriver
- Google Chrome browser
- ChromeDriver (for Chrome WebDriver compatibility)

## Structure

This project contains multiple test functions to check different login scenarios

1. **test_valid_login()**
   - Verifies login with a valid username and password. 
   - Inputs:  
     - Username: `John Doe`  
     - Password: `ThisIsNotAPassword`
   - Expected result: Successful login.

   
2. **test_invalid_login_username()**
   - Verifies the login attempt with an incorrect username and a valid password.
   - Inputs:  
     - Username: `InvalidUsername`  
     - Password: `ThisIsNotAPassword`
   - Expected result: Failed login due to incorrect username.
   
4. **test_invalid_login_password()**
   - Verifies the login attempt with a correct username and an incorrect password.
   - Inputs:  
     - Username: `John Doe`  
     - Password: `InvalidPassword`
   - Expected result: Failed login due to incorrect password.
   
5. **test_invalid_login_none()**
   - Attempts to log in with both fields left blank.
   - Inputs:  
     - Username: Empty  
     - Password: Empty
   - Expected result: Failed login due to missing credentials.
   
6. **test_invalid_login_empty_username()**
   - Tests login with an empty username and a valid password.
   - Inputs:  
     - Username: Empty  
     - Password: `ThisIsNotAPassword`
   - Expected result: Failed login due to empty username.
   
7. **test_invalid_login_empty_password()**
   - Tests login with a valid username but an empty password.
   - Inputs:  
     - Username: `John Doe`  
     - Password: Empty
   - Expected result: Failed login due to empty password.
   
8. **test_invalid_login_specialCaracther()**
   - Attempts to log in with special characters in both the username and password.
   - Inputs:  
     - Username: `John!@#$%^&()_+`  
     - Password: `Doe!@#$%^&()_+`
   - Expected result: Failed login due to invalid credentials with special characters.

  

