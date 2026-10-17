import pytest
import allure
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal

@allure.feature("UI Main Flow")
@allure.story("Constructor & Modals")
class TestMainFlow:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        page = MainPage(driver)
        with allure.step("Клик на вкладку «Конструктор»"):
            page.go_to_constructor()
        with allure.step("Проверка URL"):
            assert "/ingredients" in driver.current_url

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_navigate_to_feed(self, driver):
        page = MainPage(driver)
        with allure.step("Клик на вкладку «Лента заказов»"):
            page.go_to_feed()
        with allure.step("Проверка URL"):
            assert "/feed" in driver.current_url

    @allure.title("Всплывающее окно с деталями ингредиента")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        modal = IngredientModal(driver)
        
        with allure.step("Переход на конструктор"):
            page.go_to_constructor()
        
        with allure.step("Клик на первую карточку ингредиента"):
            page.click_add_button_on_card(index=0)
        
        with allure.step("Проверка появления модального окна"):
            assert modal.is_modal_open()
        
        with allure.step("Проверка заголовка модального окна"):
            title = modal.get_modal_title()
            assert title != ""
            assert "г" in title or " " in title  # Простая проверка, что там есть название, а не пусто

    @allure.title("Закрытие модального окна кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        page = MainPage(driver)
        modal = IngredientModal(driver)
        
        with allure.step("Переход на конструктор и открытие модального окна"):
            page.go_to_constructor()
            page.click_add_button_on_card(index=0)
            assert modal.is_modal_open()
        
        with allure.step("Клик по кнопке закрытия (крестик)"):
            modal.close_modal()
        
        with allure.step("Проверка исчезновения модального окна"):
            modal.wait_for_modal_to_close()
            assert not modal.is_modal_open()

    @allure.title("При добавлении ингредиента счетчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        
        with allure.step("Переход на конструктор"):
            page.go_to_constructor()
        
        with allure.step("Получение начального значения счетчика"):
            initial_text = page.get_order_button_text()
            initial_count = int(initial_text.split()[1]) if len(initial_text.split()) > 1 else 0
        
        with allure.step("Клик на первый ингредиент для добавления"):
            page.click_add_button_on_card(index=0)
        
        with allure.step("Получение нового значения счетчика"):
            new_text = page.get_order_button_text()
            new_count = int(new_text.split()[1]) if len(new_text.split()) > 1 else 0
        
        with allure.step("Проверка увеличения счетчика"):
            assert new_count > initial_count