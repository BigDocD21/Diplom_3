from pages.base_page import BasePage
from locators.modal_locators import ModalLocators

class IngredientModal(BasePage):
    def is_modal_open(self):
        return self.is_visible(ModalLocators.MODAL_WINDOW)

    def get_modal_title(self):
        return self.get_text(ModalLocators.MODAL_TITLE)

    def get_ingredient_details(self):
        return self.get_text(ModalLocators.INGREDIENT_DETAILS)

    def close_modal(self):
        self.click_element(ModalLocators.MODAL_CLOSE_BTN)

    def wait_for_modal_to_close(self):
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.invisibility_of_element_located(ModalLocators.MODAL_WINDOW))