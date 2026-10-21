import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.feed_locators import FeedLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step("Получение списка карточек заказов в разделе «В работе»")
    def get_work_orders_list(self):
        return self.find_elements(FeedLocators.WORK_ORDER_ITEM)

    @allure.step("Получение номера первого заказа из списка")
    def get_first_order_number(self):
        orders = self.get_work_orders_list()
        if not orders:
            return None

        first_order_card = orders[0]
        by, value = FeedLocators.ORDER_NUMBER
        number_element = first_order_card.find_element(by, value)
        
        self.wait.until(EC.visibility_of(number_element))
        return number_element.text

    @allure.step("Проверка наличия конкретного номера заказа в ленте")
    def check_order_exists_in_feed(self, expected_number):
        orders = self.get_work_orders_list()
        for order in orders:
            try:
                by, value = FeedLocators.ORDER_NUMBER
                number_element = order.find_element(by, value)
                current_number_text = number_element.text
                if str(expected_number) in current_number_text:
                    return True
            except Exception:
                continue
        return False