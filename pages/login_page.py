import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    @allure.step("Переход на страницу входа")
    def open_login_page(self):
        current_url = self.driver.current_url

        if "/login" in current_url:
            return
        
        parts = current_url.split('://', 1)
        protocol = parts[0]
        rest = parts[1] if len(parts) > 1 else current_url
        domain = rest.split('/', 1)[0]
        
        login_url = f"{protocol}://{domain}/login"
        self.driver.get(login_url)

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