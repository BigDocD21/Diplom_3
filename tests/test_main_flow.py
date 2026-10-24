import pytest
import allure
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal

@allure.feature("Constructor & Ingredients")
@allure.story("Main Flow Verification")
class TestMainFlow:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, logged_in_main_page):
        page = logged_in_main_page
        page.go_to_feed()
        page.go_to_constructor()
        assert page.is_visible(MainPage.locators.ORDER_SUBMIT_BTN)

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, logged_in_main_page, ingredient_modal):
        page = logged_in_main_page
        modal = ingredient_modal
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        
        assert modal.is_modal_open()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_modal_closes_on_click(self, logged_in_main_page, ingredient_modal):
        page = logged_in_main_page
        modal = ingredient_modal
        
        page.go_to_constructor()
        page.click_ingredient_card(index=0)
        
        modal.close_modal()
        modal.wait_for_modal_to_close()
        
        assert not modal.is_modal_open()

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, logged_in_main_page):
        page = logged_in_main_page
        
        page.go_to_constructor()
        
        initial_all, initial_today = page.get_counters()
        initial_all = int(initial_all)
        initial_today = int(initial_today)
        
        page.click_ingredient_card(index=0)
        
        new_all, new_today = page.get_counters()
        new_all = int(new_all)
        new_today = int(new_today)
        
        assert new_all > initial_all and new_today > initial_today