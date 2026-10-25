import allure
from locators.main_locators import MainLocators
from pages.base_page import BasePage
import re
from selenium.common.exceptions import TimeoutException

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

    @allure.step("Клик по карточке ингредиента (открывает модальное окно)")
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
    @allure.step("Перетаскивание ингредиента в зону конструктора (добавляет в заказ)")
    def add_ingredient_via_drag_and_drop(self, index=0):
        cards = self.get_ingredient_cards()
        
        if index >= len(cards):
            raise IndexError(f"Недостаточно карточек ингредиентов. Запрошен индекс {index}, доступно {len(cards)}")
        
        source_card = cards[index]
        target_zone = MainLocators.CONSTRUCTOR_DROP_AREA
        
        self.drag_and_drop_element(source_card, target_zone)

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

    @allure.step("Клик по элементу (карточка или кнопка)")
    def click_element_on_card(self, element):
        if not self.is_visible_element(element):
            raise TimeoutException(f"Элемент не стал видимым для клика: {element}")
        element.click()

    @allure.step("Проверка видимости кнопки «Оформить заказ»")
    def is_order_button_visible(self):
        return self.is_visible(MainLocators.ORDER_SUBMIT_BTN)

    @allure.step("Получение значения счётчика ингредиента на карточке (индекс {index})")
    def get_ingredient_counter_value(self, index=0):
        cards = self.get_ingredient_cards()
        
        if index >= len(cards):
            raise IndexError(f"Недостаточно карточек ингредиентов. Запрошен индекс {index}, доступно {len(cards)}")
        
        target_card = cards[index]
        by, value = MainLocators.INGREDIENT_COUNTER
        
        counter_element = target_card.find_element(by, value)
        text = counter_element.text
        numbers = re.findall(r'\d+', text)
        
        if not numbers:
            raise ValueError(f"Не удалось найти число в тексте счётчика: '{text}'")
            
        return int(numbers[-1])