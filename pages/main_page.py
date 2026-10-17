from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click_element(MainLocators.TAB_CONSTRUCTOR)

    def go_to_feed(self):
        self.click_element(MainLocators.TAB_FEED)

    def get_ingredient_cards(self):
        return self.find_elements(MainLocators.INGREDIENT_CARDS)

    def click_add_button_on_card(self, index=0):
        cards = self.get_ingredient_cards()

        card = cards[index]
        add_btn = card.find_element(*MainLocators.ADD_BUTTON)
        add_btn.click()

    def get_order_button_text(self):
        return self.get_text(MainLocators.ORDER_BUTTON)

    def get_counters(self):
        all_time = self.get_text(MainLocators.COUNTER_ALL_TIME)
        today = self.get_text(MainLocators.COUNTER_TODAY)
        return all_time, today