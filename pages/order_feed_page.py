from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class OrderFeedPage(BasePage):
    def get_work_orders_list(self):
        return self.find_elements(FeedLocators.WORK_ORDERS_LIST)

    def get_first_order_number(self):
        orders = self.get_work_orders_list()
        if not orders:
            return None
        try:
            return self.get_text(FeedLocators.ORDER_NUMBER)
        except Exception:
            return None

    def get_counters_values(self, main_page):
        return main_page.get_counters()