from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()


def test_eight_components():
    service = webdriver.ChromeService(
        executable_path=os.getenv('PATH_TO_CROMEDRIVER')
    )
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()
