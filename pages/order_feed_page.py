import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step("Получение списка карточек заказов в разделе «В работе»")
    def get_work_orders_list(self):

        return self.find_elements(MainLocators.ORDERS_LIST)

    @allure.step("Получение номера первого заказа из списка")
    def get_first_order_number(self):
        orders = self.get_work_orders_list()
        
        if not orders:
            return None
        
        first_order_card = orders[0]

        if not self.is_visible_element(first_order_card):

            return None
            
        return first_order_card.text

    @allure.step("Проверка наличия конкретного номера заказа в ленте")
    def check_order_exists_in_feed(self, expected_number):
        orders = self.get_work_orders_list()
        target_str = str(expected_number)
        
        for order in orders:

            if not self.is_visible_element(order):

                continue
            
            order_text = order.text
            if target_str in order_text:
                return True
                
        return False