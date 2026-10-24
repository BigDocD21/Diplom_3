import pytest
import allure
import re
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_modal import IngredientModal

@allure.feature("Order Feed & Global Counters")
@allure.story("Order Verification")
class TestOrderFeed:

    @allure.title("Переход в раздел «Лента заказов»")
    def test_navigate_to_feed(self, logged_in_main_page):
        page = logged_in_main_page
        page.go_to_feed()
        assert "/feed" in page.get_current_url()

    @allure.title("Счётчик «Выполнено за всё время» увеличивается при оформлении заказа")
    def test_counter_all_time_increases(self, logged_in_main_page):
        page = logged_in_main_page
        
        page.go_to_feed()
        initial_all, _ = page.get_counters()
        initial_all = int(initial_all)
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        page.go_to_feed()
        new_all, _ = page.get_counters()
        new_all = int(new_all)
        
        assert new_all > initial_all

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается при оформлении заказа")
    def test_counter_today_increases(self, logged_in_main_page):
        page = logged_in_main_page
        
        page.go_to_feed()
        _, initial_today = page.get_counters()
        initial_today = int(initial_today)
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        page.go_to_feed()
        _, new_today = page.get_counters()
        new_today = int(new_today)
        
        assert new_today > initial_today

    @allure.title("Номер созданного заказа появляется в разделе «В работе»")
    def test_order_appears_in_work_section(self, logged_in_main_page, order_feed_page, ingredient_modal):
        page = logged_in_main_page
        feed_page = order_feed_page
        modal = ingredient_modal
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        modal_text = modal.get_modal_title()
        numbers_in_modal = re.findall(r'\d+', modal_text)
        expected_order_number = numbers_in_modal[0]
        
        modal.wait_for_modal_to_close()
        page.go_to_feed()
        
        order_items = feed_page.get_work_orders_list()
        
        assert any(expected_order_number in item.text for item in order_items)