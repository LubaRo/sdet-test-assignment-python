from selenium.webdriver.common.by import By
from pages.practice_form_page import PracticeFormPage


def test_eight_components(driver):
    practice_form_page = PracticeFormPage(driver)
    practice_form_page.open_page()

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
