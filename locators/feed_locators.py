from selenium.webdriver.common.by import By

class FeedLocators:
    WORK_ORDERS_LIST = (By.CSS_SELECTOR, '[data-testid="work-orders-list"]')
    WORK_ORDER_ITEM = (By.CSS_SELECTOR, '[data-testid="work-order-item"]')
    ORDER_NUMBER = (By.CSS_SELECTOR, '.order-number')