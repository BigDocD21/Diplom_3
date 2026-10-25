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
        assert page.is_order_button_visible()

    @allure.title("При клике на ингредиент открывается всплывающее окно с деталями")
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

    @allure.title("При добавлении ингредиента счётчик на карточке увеличивается")
    def test_ingredient_counter_increases(self, logged_in_main_page):
        page = logged_in_main_page
        page.go_to_constructor()
        initial_count = page.get_ingredient_counter_value(index=0)
        page.add_ingredient_via_drag_and_drop(index=0)
        new_count = page.get_ingredient_counter_value(index=0)

        assert new_count > initial_count