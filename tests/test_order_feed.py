import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature("Order Feed & Global Counters")
@allure.story("Order Verification")
class TestOrderFeed:

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_navigate_to_feed(self, logged_in_main_page):
        page = logged_in_main_page
        page.go_to_feed()
        assert "/feed" in page.get_current_url()

    @allure.title("При создании заказа счётчики «Выполнено за всё время» и «Выполнено за сегодня» увеличиваются")
    def test_global_counters_increase(self, logged_in_main_page):
        page = logged_in_main_page
        
        page.go_to_feed()
        initial_all, initial_today = page.get_counters()
        initial_all = int(initial_all)
        initial_today = int(initial_today)
    
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()

        page.go_to_feed()
        new_all, new_today = page.get_counters()
        new_all = int(new_all)
        new_today = int(new_today)
        
        assert new_all > initial_all and new_today > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_work_section(self, logged_in_main_page, order_feed_page):
        page = logged_in_main_page
        feed_page = order_feed_page
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        page.click_order_button()
        
        page.go_to_feed()

        order_items = feed_page.get_work_orders_list()
        assert len(order_items) > 0 and any(char.isdigit() for char in order_items[0].text), \
            "В ленте не найден созданный заказ или в карточке отсутствует номер"