from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, page_url):
        self.driver = driver
        self.base_url = page_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message="Can't find element by locator {}".format(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)