class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get(self):
        self.driver.get(self.url)

    def open_page(self):
        self.driver.get(self.url)
