import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Получение заказов в разделе «В работе»")
    def get_work_orders_list(self):
        return self.find_elements_now(MainLocators.ORDERS_LIST)

    @allure.step("Получение первого номера заказа в разделе «В работе»")
    def get_first_order_number(self):
        for item in self.get_work_orders_list():
            text = item.text.strip()
            if text.isdigit():
                return text
        return None

    @allure.step("Ожидание номера заказа в разделе «В работе»")
    def check_order_exists_in_feed(self, expected_number):
        return self.wait_for_number_in_elements(MainLocators.ORDERS_LIST, expected_number)
