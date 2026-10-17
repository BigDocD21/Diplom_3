import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

@allure.feature("UI Main Flow")
@allure.story("Order Feed & Counters")
class TestOrderFeed:

    @allure.title("Счётчики «Выполнено за всё время» и «За сегодня» увеличиваются при заказе")
    def test_counters_increase_after_order(self, driver):
        page = MainPage(driver)
        wait = WebDriverWait(driver, 10)

        with allure.step("Переход на ленту заказов и получение начальных значений счетчиков"):
            page.go_to_feed()
            wait.until(EC.visibility_of_element_located(page.locators.COUNTER_ALL_TIME))
            wait.until(EC.visibility_of_element_located(page.locators.COUNTER_TODAY))
            
            initial_all_time, initial_today = page.get_counters()
            initial_all_time = int(initial_all_time)
            initial_today = int(initial_today)

        with allure.step("Переход на конструктор, добавление ингредиента и оформление заказа"):
            page.go_to_constructor()
            page.click_add_button_on_card(index=0)
            driver.find_element(By.CSS_SELECTOR, '[data-testid="order-button"]').click()

        with allure.step("Возврат на ленту и ожидание обновления счетчиков"):
            page.go_to_feed()
            wait.until(lambda d: int(page.get_text(page.locators.COUNTER_ALL_TIME)) > initial_all_time)
            wait.until(lambda d: int(page.get_text(page.locators.COUNTER_TODAY)) > initial_today)

            new_all_time, new_today = page.get_counters()
            new_all_time = int(new_all_time)
            new_today = int(new_today)

        with allure.step("Проверка: оба счетчика увеличились"):
            assert new_all_time > initial_all_time
            assert new_today > initial_today

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_appears_in_work_section(self, driver):
        page = MainPage(driver)
        wait = WebDriverWait(driver, 10)

        with allure.step("Оформление заказа через конструктор"):
            page.go_to_constructor()
            page.click_add_button_on_card(index=0)
            driver.find_element(By.CSS_SELECTOR, '[data-testid="order-button"]').click()

        with allure.step("Переход на ленту заказов и ожидание появления заказа"):
            page.go_to_feed()
            wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, '[data-testid="work-order-item"]')) > 0)

        with allure.step("Проверка наличия номера заказа в списке"):
            order_items = driver.find_elements(By.CSS_SELECTOR, '[data-testid="work-order-item"]')
            assert len(order_items) > 0
            first_order_text = order_items[0].text
            assert "#" in first_order_text or any(char.isdigit() for char in first_order_text)