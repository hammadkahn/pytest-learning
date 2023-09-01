import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Page Objects
class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for(self, query):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.submit()


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_first_result(self):
        first_result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result.click()


class search_website:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, query):

        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "d-block my-5 font-14 gtm-ap-news-link font-weight-semi-bold"))
        )
        search_box.click()
        # search_box.send_keys(query)
        # search_box.submit()


# Test Case
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_and_click_first_result(browser):
    # Initialize Page Objects
    google_home_page = GoogleHomePage(browser)
    search_results_page = SearchResultsPage(browser)
    search_website1 = search_website(browser)

    # Test Data
    search_query = "computer"

    # Test Steps
    browser.get("https://www.google.com/")

    # Search for "computer"
    google_home_page.search_for(search_query)

    # Click on the first search result
    search_results_page.click_first_result()

    # search for computer
    search_query1 = "computer"
    search_website1.search_for_product(search_query1)

    # You can add assertions here to verify the content of the clicked page.
