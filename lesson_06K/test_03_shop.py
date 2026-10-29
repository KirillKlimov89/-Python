from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_purchase():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory"))

    for item_name in (
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ):
        driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button[text()='Add to cart']",
        ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )
    total_text = total_element.text

    driver.quit()

    assert total_text == "Total: $58.29"
