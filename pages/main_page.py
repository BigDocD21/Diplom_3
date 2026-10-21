import allure
from selenium.webdriver.support import expected_conditions as EC
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
        return self.find_elements(MainLocators.INGREDIENT_CARDS)

    @allure.step("Клик по кнопке добавления ингредиента на карточке")
    def click_add_button_on_card(self, index=0):
        cards = self.get_ingredient_cards()
        card = cards[index]
        by, value = MainLocators.ADD_BUTTON
        add_btn = card.find_element(by, value)
        self.wait.until(EC.element_to_be_clickable(add_btn))
        add_btn.click()

    @allure.step("Получение текста кнопки заказа")
    def get_order_button_text(self):
        return self.get_text(MainLocators.ORDER_BUTTON)

    @allure.step("Получение значений счетчиков")
    def get_counters(self):
        all_time = self.get_text(MainLocators.COUNTER_ALL_TIME)
        today = self.get_text(MainLocators.COUNTER_TODAY)
        return all_time, today