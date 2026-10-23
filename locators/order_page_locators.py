from selenium.webdriver.common.by import By

class OrderPageLocators:
    HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')
    
    COUNTER_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COUNTER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li')