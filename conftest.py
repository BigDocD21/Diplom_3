import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage

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
    start_url = "https://stellarburgers.education-services.ru/"
    driver.get(start_url)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def user_data():
    return {
        "email": "test_user_123@mail.ru", 
        "password": "TestTest123" 
    }

@pytest.fixture
def main_page(driver):
    base_url = driver.current_url.rstrip('/')
    return MainPage(driver, base_url)

@pytest.fixture
def ingredient_modal(driver):
    base_url = driver.current_url.rstrip('/')
    return IngredientModal(driver, base_url)

@pytest.fixture
def order_feed_page(driver):
    base_url = driver.current_url.rstrip('/')
    return OrderFeedPage(driver, base_url)

@pytest.fixture
def logged_in_main_page(driver, user_data):
    email = user_data["email"]
    password = user_data["password"]
    
    base_url = driver.current_url.rstrip('/')
    
    login_page = LoginPage(driver, base_url)
    
    login_page.open_login_page()
    login_page.login(email, password)
    
    return MainPage(driver, base_url)