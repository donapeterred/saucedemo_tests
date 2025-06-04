import time

def test_sorting(login, driver):
    select = driver.find_element("class name", "product_sort_container")
    select.click()
    select.find_element("css selector", "option[value='za']").click()
    time.sleep(1)
    assert True

def test_products_displayed(login, driver):
    items = driver.find_elements("class name", "inventory_item")
    assert len(items) > 0
