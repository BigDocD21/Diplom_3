from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False