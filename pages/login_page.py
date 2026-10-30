import allure
from selenium.common.exceptions import TimeoutException
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_PATH = "/login"


    @allure.step("Клик по кнопке входа (с учётом перекрытия элементами)")
    def _submit_login_when_unobstructed(self):
        self.click_when_unobstructed(MainLocators.LOGIN_SUBMIT_BTN)

    @allure.step("Переход на страницу входа")
    def open_login_page(self):

        current_url = self.get_current_url()

        if self.LOGIN_PATH in current_url:
            return

        self.open_page(self.LOGIN_PATH)


    @allure.step("авторизация")
    def login(self, email, password):
            self.open_login_page()
            email_field = self.find_element(MainLocators.LOGIN_INPUT)
            pass_field = self.find_element(MainLocators.PASSWORD_INPUT)
            email_field.clear()
            email_field.send_keys(email)
            pass_field.clear()
            pass_field.send_keys(password)
            self._submit_login_when_unobstructed()

            try:
                self.wait_for_visibility(MainLocators.CONSTRUCTOR_HEADER)       
            except TimeoutException as exc:
                raise TimeoutException(
                    "Не удалось подтвердить вход"
                ) from exc
