from selenium.webdriver.common.by import By

class ModalLocators:
    MODAL_WINDOW = (By.CSS_SELECTOR, '.modal')
    MODAL_TITLE = (By.CSS_SELECTOR, '.modal-title')
    MODAL_CLOSE_BTN = (By.CSS_SELECTOR, '.modal-close')
    INGREDIENT_DETAILS = (By.CSS_SELECTOR, '.ingredient-details')