import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск списка элементов по локатору")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу (с ожиданием кликабельности)")
    def click_element(self, locator):
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверка видимости элемента по локатору")
    def is_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Проверка видимости переданного WebElement")
    def is_visible_element(self, element):
        try:
            self.wait.until(lambda d: element.is_displayed() and element.is_enabled())
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание исчезновения элемента по локатору")
    def wait_for_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))