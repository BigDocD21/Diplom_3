import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Переход на вкладку «Конструктор»")
    def go_to_constructor(self):
        self.click_element(MainLocators.TAB_CONSTRUCTOR)
        self.wait_for_visibility(MainLocators.CONSTRUCTOR_HEADER)

    @allure.step("Переход на вкладку «Лента заказов»")
    def go_to_feed(self):
        self.click_element(MainLocators.TAB_FEED)
        self.wait_for_visibility(MainLocators.FEED_HEADER)

    @allure.step("Получение списка карточек ингредиентов")
    def get_ingredient_cards(self):
        return self.find_elements(MainLocators.INGREDIENT_CARD)

    @allure.step("Получение карточки ингредиента по индексу")
    def _ingredient_card(self, index):
        cards = self.get_ingredient_cards()
        if index < 0 or index >= len(cards):
            raise IndexError(
                f"Недостаточно карточек ингредиентов: индекс {index}, доступно {len(cards)}"
            )
        return cards[index]

    @allure.step("Ожидание загрузки конструктора и ингредиента")
    def wait_for_constructor_ready(self, index=0):
        return self.wait_for_ready_item(
            index, MainLocators.LOADING_INDICATOR, MainLocators.INGREDIENT_CARD,
            MainLocators.CONSTRUCTOR_DROP_AREA, MainLocators.INGREDIENT_IMAGE,
            MainLocators.INGREDIENT_COUNTER,
        )

    @allure.step("Открытие карточки ингредиента")
    def click_ingredient_card(self, index=0):
        self.click_element_on_card(self._ingredient_card(index))

    @allure.step("Перетаскивание ингредиента в конструктор")
    def add_ingredient_via_drag_and_drop(self, index=0):
        card, _ = self.wait_for_constructor_ready(index)
        self.drag_and_drop_element(card, MainLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Клик по кнопке «Оформить заказ»")
    def click_order_button(self):
        self.click_element(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение текста кнопки заказа")
    def get_order_button_text(self):
        return self.get_text(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение значений счётчиков заказов")
    def get_counters(self):
        return (
            self._counter_value(MainLocators.COUNTER_ALL_TIME),
            self._counter_value(MainLocators.COUNTER_TODAY),
        )

    
    @allure.step("Чтение значения счётчика по локатору")
    def _counter_value(self, locator):
        return self.wait_for_numeric_counter(locator)

    @allure.step("Ожидание увеличения счётчика заказов")
    def wait_for_order_counter_increase(self, locator, previous_value):
        return self.wait_for_numeric_counter(locator, previous_value)

    @allure.step("Клик по карточке ингредиента")
    def click_element_on_card(self, element):
        self.click_visible_element(element)

    @allure.step("Проверка видимости конструктора")
    def is_constructor_visible(self):
        return self.is_visible(MainLocators.CONSTRUCTOR_HEADER)

    @allure.step("Проверка видимости кнопки «Оформить заказ»")
    def is_order_button_visible(self):
        return self.is_visible(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение счётчика выбранного ингредиента")
    def get_ingredient_counter_value(self, index=0):
        _, counter = self.wait_for_constructor_ready(index)
        return counter

    @allure.step("Ожидание увеличения счётчика ингредиента")
    def wait_for_ingredient_counter_increase(self, previous_value, index=0):
        return self.wait_for_ready_item(
            index, MainLocators.LOADING_INDICATOR, MainLocators.INGREDIENT_CARD,
            MainLocators.CONSTRUCTOR_DROP_AREA, MainLocators.INGREDIENT_IMAGE,
            MainLocators.INGREDIENT_COUNTER, previous_value=previous_value,
        )


    @allure.step("Ждать увеличения счётчика «Выполнено за всё время»")
    def wait_for_all_time_counter_increase(self, previous_value):
        return self.wait_for_order_counter_increase(MainLocators.COUNTER_ALL_TIME, previous_value)

    @allure.step("Ждать увеличения счётчика «Выполнено за сегодня»")
    def wait_for_today_counter_increase(self, previous_value):
        return self.wait_for_order_counter_increase(MainLocators.COUNTER_TODAY, previous_value)
