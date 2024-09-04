from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url_login = "https://katalon-demo-cura.herokuapp.com/"

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()

    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()

    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('valid login test completed')


def test_invalid_login_username():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('InvalidUsername')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('invalid login username test completed')

def test_invalid_login_password():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('InvalidPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('valid login password test completed')

def test_invalid_login_none():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()

    print('testing invalid login for no input - completed')

def test_invalid_login_empty_username():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('testing invalid login for empty username - completed')

def test_invalid_login_empty_password():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('testing invalid login for empty password - completed')

def test_invalid_login_specialCaracther():
    driver = webdriver.Chrome()
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John!@#$%^&()_+')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('Doe!@#$%^&()_+')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()
    print('testing special characters - completed')


test_valid_login()
test_invalid_login_username()
test_invalid_login_password()
test_invalid_login_none()
test_invalid_login_empty_username()
test_invalid_login_empty_password()
test_invalid_login_specialCaracther()