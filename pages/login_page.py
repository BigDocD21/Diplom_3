import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_PATH = "/login"

    @allure.step("Переход на страницу входа")
    def open_login_page(self):

        current_url = self.get_current_url()

        if self.LOGIN_PATH in current_url:
            return

        self.open_page(self.LOGIN_PATH)

    @allure.step("Ввод данных и отправка формы входа")
    def login(self, email, password):
        self.open_login_page()
        
        email_field = self.find_element(MainLocators.LOGIN_INPUT)
        pass_field = self.find_element(MainLocators.PASSWORD_INPUT)
        
        email_field.clear()
        email_field.send_keys(email)
        pass_field.clear()
        pass_field.send_keys(password)
        pass_field.submit()