from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from cookies import USER_COOKIES, USER_PROFILE


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")
    driver.delete_all_cookies()

    for name, value in USER_COOKIES.items():
        driver.add_cookie({"name": name, "value": value})

    driver.refresh()

    driver.get(USER_PROFILE)
    WebDriverWait(driver, 10).until(
        lambda d: USER_PROFILE in d.current_url
    )

    assert USER_PROFILE in driver.current_url

    driver.quit()
