import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function")
def driver():
    service = webdriver.ChromeService(
        executable_path=os.getenv('PATH_TO_CROMEDRIVER')
    )
    driver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()
