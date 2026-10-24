import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Переход на вкладку «Конструктор»")
    def go_to_constructor(self):
        self.click_element(MainLocators.TAB_CONSTRUCTOR)

    @allure.step("Переход на вкладку «Лента заказов»")
    def go_to_feed(self):
        self.click_element(MainLocators.TAB_FEED)

    @allure.step("Получение списка карточек ингредиентов")
    def get_ingredient_cards(self):
        return self.find_elements(MainLocators.INGREDIENT_CARD)

    @allure.step("Клик по зоне ингредиента/счетчику на карточке (индекс {index})")
    def click_add_button_on_card(self, index=0):
        cards = self.get_ingredient_cards()
        
        if index >= len(cards):
            raise IndexError(f"Недостаточно карточек ингредиентов. Запрошен индекс {index}, доступно {len(cards)}")
        
        card = cards[index]
        by, value = MainLocators.INGREDIENT_COUNTER
        
        try:
            add_btn = card.find_element(by, value)
            self.wait.until(lambda d: add_btn.is_enabled() and add_btn.is_displayed())
            add_btn.click()
        except Exception:
            self.wait.until(lambda d: card.is_enabled() and card.is_displayed())
            card.click()

    @allure.step("Клик по кнопке «Оформить заказ»")
    def click_order_button(self):
        self.click_element(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение текста кнопки заказа")
    def get_order_button_text(self):
        return self.get_text(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение значений счетчиков")
    def get_counters(self):
        all_time = self.get_text(MainLocators.COUNTER_ALL_TIME)
        today = self.get_text(MainLocators.COUNTER_TODAY)
        return all_time, today