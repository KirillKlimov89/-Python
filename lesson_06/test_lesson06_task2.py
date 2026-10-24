from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from cookies import (
    USER1_COOKIES,
    USER1_PROFILE,
    USER2_COOKIES,
    USER2_PROFILE,
)


def _login_and_get_profile_url(driver, cookies, profile_url):
    driver.get("https://gitflic.ru/")
    driver.delete_all_cookies()

    for name, value in cookies.items():
        driver.add_cookie({"name": name, "value": value})

    driver.refresh()
    driver.get(profile_url)

    WebDriverWait(driver, 10).until(
        lambda d: profile_url in d.current_url
    )
    return driver.current_url


def test_session_storage_auth():
    driver = webdriver.Chrome()

    url_user1 = _login_and_get_profile_url(
        driver, USER1_COOKIES, USER1_PROFILE
    )

    driver.delete_all_cookies()

    url_user2 = _login_and_get_profile_url(
        driver, USER2_COOKIES, USER2_PROFILE
    )

    assert url_user1 != url_user2

    driver.quit()
