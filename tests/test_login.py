import pytest

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element("id", "user-name").send_keys("wrong_user")
    driver.find_element("id", "password").send_keys("wrong_pass")
    driver.find_element("id", "login-button").click()
    error = driver.find_element("css selector", "h3[data-test='error']").text
    assert "Username and password do not match" in error or "do not match any user" in error
