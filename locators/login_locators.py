from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    BUTTON = (By.XPATH, '//button[text()="Войти"]')