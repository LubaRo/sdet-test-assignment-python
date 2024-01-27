import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="function")
def driver():
    service = webdriver.ChromeService(
        executable_path=os.getenv('PATH_TO_CROMEDRIVER')
    )
    driver = webdriver.Chrome(service=service)

    # FIXME: if tests should pass for default window size
    driver.maximize_window()

    yield driver

    driver.quit()
