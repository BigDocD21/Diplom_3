import re
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открытие страницы по относительному пути")
    def open_page(self, path):

        full_url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        self.driver.get(full_url)

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск списка элементов по локатору")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу (с ожиданием кликабельности)")
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Перетаскивание элемента в целевую зону")
    def drag_and_drop_element(self, source_element, target_locator):
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        if self.driver.capabilities.get("browserName") == "firefox":
            self.driver.execute_async_script(
                """
                const [source, target, done] = arguments;
                const dataTransfer = new DataTransfer();
                const rect = target.getBoundingClientRect();
                const coords = {
                    clientX: rect.x + rect.width / 2,
                    clientY: rect.y + rect.height / 2,
                };
                const fire = (element, type, position) => element.dispatchEvent(
                    new DragEvent(type, {
                        bubbles: true, cancelable: true, dataTransfer, ...position,
                    })
                );
                fire(source, 'dragstart', {});
                // React DnD обрабатывает перемещение в следующем кадре.
                setTimeout(() => {
                    fire(target, 'dragenter', coords);
                    fire(target, 'dragover', coords);
                }, 100);
                setTimeout(() => {
                    fire(target, 'drop', coords);
                    fire(source, 'dragend', coords);
                    done();
                }, 250);
                """,
                source_element,
                target,
            )
            return
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target).perform()

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверка видимости элемента по локатору")
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Проверка видимости переданного WebElement")
    def is_visible_element(self, element):
        try:
            self.wait.until(lambda d: element.is_displayed() and element.is_enabled())
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание исчезновения элемента по локатору")
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание видимости элемента по локатору: {locator}")
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Быстрый поиск элементов")
    def find_elements_now(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по видимому элементу (проверка перед кликом)")
    def click_visible_element(self, element):
        if not self.is_visible_element(element):
            raise TimeoutException("Элемент не стал доступен для клика")
        element.click()

    @allure.step("Клик по элементу, когда он не перекрыт")
    def click_when_unobstructed(self, locator, timeout=30):
        def click(driver):
            element = driver.find_element(*locator)
            if not element.is_displayed() or not element.is_enabled():
                return False
            element.click()
            return True

        return WebDriverWait(
            self.driver, timeout,
            ignored_exceptions=(ElementClickInterceptedException, StaleElementReferenceException),
        ).until(click)


    @staticmethod
    @allure.step("проверка готовности, возврат данных")
    def _ready_item(driver, index, loading_locator, item_locator, target_locator,
                    image_locator, counter_locator):
        if any(element.is_displayed() for element in driver.find_elements(*loading_locator)):
            return False
        items = driver.find_elements(*item_locator)
        if index < 0 or index >= len(items):
            return False
        item = items[index]
        target = driver.find_element(*target_locator)
        if not item.is_displayed() or not target.is_displayed():
            return False
        if not item.find_element(*image_locator).get_property("complete"):
            return False
        text = item.find_element(*counter_locator).text.strip()
        return (item, int(text)) if text.isdigit() else False
    
    
    @allure.step("Ожидание готовности ингредиента")
    def wait_for_ready_item(self, index, loading_locator, item_locator, target_locator,
                            image_locator, counter_locator, previous_value=None):
        if index < 0:
            raise ValueError("Индекс ингредиента не может быть отрицательным")

        def ready(driver):
            result = self._ready_item(
                driver, index, loading_locator, item_locator, target_locator,
                image_locator, counter_locator,
            )
            if previous_value is None:
                return result
            return result[1] if result and result[1] > previous_value else False

        message = (
            "Не удалось дождаться готовности конструктора и ингредиента за 30 секунд"
            if previous_value is None else
            "Счётчик ингредиента не увеличился за 30 секунд после перетаскивания"
        )
        return WebDriverWait(
            self.driver, 30, ignored_exceptions=(StaleElementReferenceException,)
        ).until(ready, message)

    @staticmethod
    @allure.step("извлекаем, возвращаем")
    def _read_numeric_counter(driver, locator):
        digits = re.sub(r"\D", "", driver.find_element(*locator).text)
        return (int(digits),) if digits else False

    @allure.step("Ожидание числового значения счётчика")
    def wait_for_numeric_counter(self, locator, previous_value=None):
        def counter(driver):
            result = self._read_numeric_counter(driver, locator)
            if not result:
                return False
            if previous_value is None:
                return result
            return result[0] if result[0] > previous_value else False

        result = self.wait.until(counter)
        return result[0] if previous_value is None else result
    @allure.step("Ожидание появления номера заказа")
    def wait_for_order_number(self, loading_locator, number_locator):
        def visible_number(driver):
            if any(element.is_displayed() for element in driver.find_elements(*loading_locator)):
                return False
            for element in driver.find_elements(*number_locator):
                text = element.text.strip()
                if element.is_displayed() and re.fullmatch(r"\d+", text) and int(text) != 9999:
                    return text
            return False

        return WebDriverWait(self.driver, 40).until(visible_number)

    @allure.step("Ожидание скрытия модального окна")
    def wait_for_modal_and_overlay_hidden(self, modal_locator, overlay_locator):
        def hidden(driver):
            try:
                if any(element.is_displayed() for element in driver.find_elements(*modal_locator)):
                    return False
                return driver.execute_script(
                    """
                    return !Array.from(document.querySelectorAll(arguments[0])).some(el => {
                        const style = getComputedStyle(el);
                        return style.visibility === 'visible' && style.pointerEvents !== 'none'
                            && Array.from(el.getClientRects()).some(rect => rect.width > 0 && rect.height > 0);
                    });
                    """,
                    overlay_locator[1],
                )                                                                                                                           
            except StaleElementReferenceException:
                return False

        return self.wait.until(hidden)

    @allure.step("Ожидание наличия числа")
    def wait_for_number_in_elements(self, locator, expected_number):
        expected = int(expected_number)

        def number_is_present(driver):
            try:
                for item in driver.find_elements(*locator):
                    number = item.text.strip()
                    if number.isdigit() and int(number) == expected:
                        return True
            except StaleElementReferenceException:
                return False
            return False

        try:
            return self.wait.until(number_is_present)
        except TimeoutException:
            return False
