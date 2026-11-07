from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_name):
        self.wait.until(EC.url_contains("inventory"))
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button[text()='Add to cart']",
        ).click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
