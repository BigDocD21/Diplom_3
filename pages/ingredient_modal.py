import allure
from locators.modal_locators import ModalLocators
from pages.base_page import BasePage

class IngredientModal(BasePage):
    @allure.step("Проверка видимости модального окна")
    def is_modal_open(self):
        return self.is_visible(ModalLocators.MODAL_WINDOW)

    @allure.step("Получение заголовка модального окна")
    def get_modal_title(self):
        return self.get_text(ModalLocators.MODAL_TITLE)

    @allure.step("Получение деталей ингредиента")
    def get_ingredient_details(self):
        return self.get_text(ModalLocators.INGREDIENT_DETAILS)

    @allure.step("Закрытие модального окна кликом по крестику")
    def close_modal(self):
        self.click_element(ModalLocators.MODAL_CLOSE_BTN)

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_modal_to_close(self):
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_WINDOW))