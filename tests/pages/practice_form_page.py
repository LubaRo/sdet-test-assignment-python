from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.selenium.dev/selenium/web/web-form.html'
        super().__init__(driver, url)
