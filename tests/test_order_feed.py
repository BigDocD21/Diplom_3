import pytest
import allure
import re
from pages.order_feed_page import OrderFeedPage

@allure.feature("UI Main Flow")
@allure.story("Order Feed & Counters")
class TestOrderFeed:

    @allure.title("Счётчики увеличиваются при оформлении заказа")
    def test_counters_increase_after_order(self, logged_in_main_page):
        page = logged_in_main_page

        page.go_to_feed()
        initial_all_time, initial_today = page.get_counters()

        initial_all_time = int(initial_all_time)
        initial_today = int(initial_today)


        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        page.go_to_feed()
        new_all_time, new_today = page.get_counters()
        new_all_time = int(new_all_time)
        new_today = int(new_today)

        assert new_all_time > initial_all_time and new_today > initial_today

    @allure.title("В ленте появляется номер именно созданного заказа")
    def test_order_appears_in_work_section(self, logged_in_main_page, order_feed_page):
        page = logged_in_main_page
        feed_page = order_feed_page

        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        order_text = page.get_order_button_text()
        target_number = re.findall(r'\d+', order_text)[-1]

        page.go_to_feed()
        order_items = feed_page.get_work_orders_list()

        assert any(target_number in item.text for item in order_items)