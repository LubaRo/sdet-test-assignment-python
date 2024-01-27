from helpers.files_helper import get_test_file_absolute_path
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage(BasePage):
    def __init__(self, driver):
        url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, url)

    def fill_form(self, form_data):
        self.fill_firstname(form_data.get('firstName'))
        self.fill_lastname(form_data.get('lastName'))
        self.fill_email(form_data.get('email'))

        self.select_gender(form_data.get('gender'))

        self.fill_mobile(form_data.get('phone'))
        self.fill_birthday(*form_data.get('birthday').values())
        self.fill_subjects(form_data.get('subjects'))

        self.attach_picture(form_data.get('picture'))

        self.fill_address(form_data.get('address'))
        self.select_state(form_data.get('state'))
        self.select_city(form_data.get('city'))

    def fill_firstname(self, value):
        self.find_and_fill_input_by_id('firstName', value)

    def fill_lastname(self, value):
        self.find_and_fill_input_by_id('lastName', value)

    def fill_email(self, value):
        self.find_and_fill_input_by_id('userEmail', value)

    def select_gender(self, value):
        option = self.driver.find_element(
            By.XPATH,
            f"//input[@name='gender' and @value='{value}']/parent::div"
        )
        option.click()

    def fill_mobile(self, value):
        self.find_and_fill_input_by_id('userNumber', value)

    def fill_birthday(self, day, month, year):
        self.fill_date_picker('dateOfBirth', day, month, year)

    def fill_subjects(self, values):
        elem = self.driver.find_element(By.ID, 'subjectsInput')

        for value in values:
            elem.send_keys(value)
            elem.send_keys(Keys.TAB)

    def attach_picture(self, picture_name):
        file_path = get_test_file_absolute_path(picture_name)
        elem = self.driver.find_element(By.ID, 'uploadPicture')
        elem.send_keys(file_path)

    def fill_address(self, value):
        self.find_and_fill_input_by_id('currentAddress', value)

    def select_state(self, value):
        self.select_with_automoplete('state', 'Select State', value)

    def select_city(self, value):
        self.select_with_automoplete('city', 'Select City', value)

    def submit_form(self):
        submit_button = self.driver.find_element(By.ID, 'submit')
        submit_button.click()

    def check_form_submission(self, form_data):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.modal-content')
        ))

        modal_title = self.driver.find_element(
            By.ID,
            'example-modal-sizes-title-lg'
        ).text

        modal_content = self.driver.find_element(
            By.CLASS_NAME,
            'modal-body'
        ).text

        assert 'Thanks for submitting the form' in modal_title
        assert form_data.get('firstName') in modal_content
        assert form_data.get('lastName') in modal_content
        assert form_data.get('email') in modal_content
        assert form_data.get('phone') in modal_content
        assert form_data.get('gender') in modal_content
        # assert form_data.get('subjects') in modal_content
        # assert form_data.get('birthday') in modal_content
        assert form_data.get('picture') in modal_content
        assert form_data.get('address') in modal_content
        assert form_data.get('state') in modal_content
        assert form_data.get('city') in modal_content
