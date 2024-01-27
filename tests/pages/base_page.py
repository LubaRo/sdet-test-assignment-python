from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)

    def find_and_fill_input_by_id(self, elem_id, value):
        elem = self.driver.find_element(By.ID, elem_id)
        elem.send_keys(value)

    def fill_date_picker(self, picker_block_id, day, month, year):
        self.driver.find_element(
            By.XPATH,
            f"//div[@id='{picker_block_id}']//input"
        ).click()

        month_select = Select(self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f"#{picker_block_id} select.react-datepicker__month-select"
        ))
        month_select.select_by_visible_text(month)

        year_select = Select(self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f"#{picker_block_id} select.react-datepicker__year-select"
        ))
        year_select.select_by_visible_text(year)

        # NOTE: we check aria-label on month presence
        # for situation when the same day such as 31 can appear
        # for two different months at the same time
        self.driver.find_element(
            by=By.XPATH,
            value=f'''//div[
                contains(@class, 'react-datepicker__day')
                and contains(@aria-label, '{month}')
                and text()='{day}'
            ]'''
        ).click()

    def select_with_automoplete(self, block_id, placeholder, value):
        select_block = self.driver.find_element(
            By.XPATH,
            f"//div[@id='{block_id}']//div[text()='{placeholder}']"
        )
        select_block.click()

        select_option = self.driver.find_element(
            By.XPATH,
            f"//div[@id='{block_id}']//div[text()='{value}']"
        )
        select_option.click()
