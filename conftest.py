import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal
from pages.order_feed_page import OrderFeedPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    
    driver.maximize_window()
    driver.get("https://stellarburgers.ru")
    
    yield driver
    
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def ingredient_modal(driver):
    return IngredientModal(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture
def logged_in_main_page(driver):
    page = MainPage(driver)
    email = "test@test.com"
    password = "password123"
    
    page.login(email, password)

    return page