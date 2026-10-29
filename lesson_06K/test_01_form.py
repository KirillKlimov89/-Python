from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    options = EdgeOptions()
    driver = webdriver.Edge(options=options)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    fields = {
        "first-name": "ван",
        "last-name": "етров",
        "address": "енина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "осква",
        "country": "оссия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    submit_button = driver.find_element(
        By.XPATH, "/html/body/main/div/form/div[5]/div/button"
    )
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", submit_button
    )
    driver.execute_script("arguments[0].click();", submit_button)

    wait.until(
        lambda d: "alert"
        in d.find_element(By.ID, "zip-code").get_attribute("class")
    )

    zip_class = driver.find_element(
        By.ID, "zip-code"
    ).get_attribute("class")
    assert "alert-danger" in zip_class

    for field_name in fields:
        field_class = driver.find_element(
            By.ID, field_name
        ).get_attribute("class")
        assert "alert-success" in field_class

    driver.quit()
