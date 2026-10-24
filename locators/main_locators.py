from selenium.webdriver.common.by import By

class MainLocators:
    TAB_CONSTRUCTOR = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Конструктор']]")
    TAB_FEED = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Лента Заказов']]")
    
    INGREDIENT_CARD = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]")
    INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@href, '/ingredient/')]//p[contains(@class, 'counter')])[1]")
    
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")
    ORDER_SUBMIT_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')
    
    COUNTER_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COUNTER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')