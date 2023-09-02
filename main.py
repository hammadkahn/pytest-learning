import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Search_first_site import search_website
from Search_page_result import SearchResultsPage
from google_home_page import GoogleHomePage

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
    google_home_page.assert_search_results_displayed()
    # google_home_page.assert_no_search_results()

    # Click on the first search result
    search_results_page.click_first_result()

    # search for computer
    search_query1 = "computer"
    search_website1.search_for_product()
    time.sleep(5)
    search_website1.select_from_dropdown("Animals & Nature")
    search_website1.select_from_thumbnail()
    # search_website1.play_audio()

    # You can add assertions here to verify the content of the clicked page.
