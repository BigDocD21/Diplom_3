import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class IngredientModal(BasePage):
    @allure.step("Проверка видимости модального окна с ингредиентом")
    def is_modal_open(self):
        return self.is_visible(MainLocators.MODAL_WINDOW)

    @allure.step("Получение заголовка модального окна")
    def get_modal_title(self):
        return self.get_text(MainLocators.MODAL_WINDOW)

    @allure.step("Получение деталей ингредиента")
    def get_ingredient_details(self):
        return self.get_text(MainLocators.MODAL_WINDOW)

    @allure.step("Закрытие модального окна кликом по крестику")
    def close_modal(self):
        self.click_element(MainLocators.MODAL_CLOSE_BTN)

    @allure.step("Ожидание полного закрытия модального окна")
    def wait_for_modal_to_close(self):
        self.wait_for_invisibility(MainLocators.MODAL_WINDOW)