def test_add_to_cart_and_validate_total(login, driver):
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()
    item_price = driver.find_element("class name", "inventory_item_price").text
    driver.find_element("id", "checkout").click()
    driver.find_element("id", "first-name").send_keys("John")
    driver.find_element("id", "last-name").send_keys("Doe")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    summary_price = driver.find_element("class name", "inventory_item_price").text
    assert item_price == summary_price
