from selenium.webdriver.common.by import By

class MainLocators:
    TAB_CONSTRUCTOR = (By.CSS_SELECTOR, '[href="/ingredients"]')
    TAB_FEED = (By.CSS_SELECTOR, '[href="/feed"]')
    
    INGREDIENT_CARDS = (By.CSS_SELECTOR, '.card_item')
    INGREDIENT_NAME = (By.CSS_SELECTOR, '.card_title')
    
    ADD_BUTTON = (By.CSS_SELECTOR, '.card_button')
    ORDER_BUTTON = (By.CSS_SELECTOR, '[data-testid="order-button"]')

    COUNTER_ALL_TIME = (By.CSS_SELECTOR, '[data-testid="counter-all-time"]')
    COUNTER_TODAY = (By.CSS_SELECTOR, '[data-testid="counter-today"]')