from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')