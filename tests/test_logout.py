def test_logout(login, driver):
    driver.find_element("id", "react-burger-menu-btn").click()
    driver.find_element("id", "logout_sidebar_link").click()
    assert "saucedemo.com" in driver.current_url
