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
    def click_ingredient_card(self, index=0):
        cards = self.get_ingredient_cards()
        
        if index >= len(cards):
            raise IndexError(f"Недостаточно карточек ингредиентов. Запрошен индекс {index}, доступно {len(cards)}")
        
        card = cards[index]
        by, value = MainLocators.INGREDIENT_COUNTER

        try:
            add_btn = card.find_element(by, value)
            self.click_element_on_card(add_btn)
        except Exception:
            self.click_element_on_card(card)

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

    @allure.step("Вход в систему: заполнение полей и отправка формы")
    def login(self, email, password):
        email_field = self.find_element(MainLocators.LOGIN_INPUT)
        pass_field = self.find_element(MainLocators.PASSWORD_INPUT)
        
        email_field.clear()
        email_field.send_keys(email)
        pass_field.clear()
        pass_field.send_keys(password)
        pass_field.submit()

    @allure.step("Клик по элементу (карточка или кнопка)")
    def click_element_on_card(self, element):
        self.wait.until(lambda d: element.is_displayed() and element.is_enabled())
        element.click()