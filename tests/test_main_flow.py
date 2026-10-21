import pytest
import allure
import re

@allure.feature("UI Main Flow")
@allure.story("Constructor & Ingredients")
class TestMainFlow:

    @allure.title("Переход в «Конструктор» со страницы ленты (проверка навигации)")
    def test_navigate_to_constructor(self, logged_in_main_page):
     
        page = logged_in_main_page

        page.go_to_feed()

        page.go_to_constructor()

        assert "/ingredients" in page.get_current_url()

    @allure.title("При клике на карточку ингредиента открывается модальное окно")
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

    @allure.title("Счётчик ингредиентов увеличивается при добавлении")
    def test_ingredient_counter_increases(self, logged_in_main_page):
        page = logged_in_main_page
        
        page.go_to_constructor()

        initial_text = page.get_order_button_text()
        initial_count = int(re.findall(r'\d+', initial_text)[-1])

        page.click_ingredient_card(index=0)

        new_text = page.get_order_button_text()
        new_count = int(re.findall(r'\d+', new_text)[-1])

        assert new_count == initial_count + 1 