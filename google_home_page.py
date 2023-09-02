from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for(self, query):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.submit()

    def assert_search_results_displayed(self):
        # Wait for search results to be visible (you may need to adjust the locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search")),
            "Search results were not displayed."
        )

    def assert_no_search_results(self):
        # Wait for the "No results found" message to be visible (you may need to adjust the locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "no-results-message")),
            "No results message was not displayed."
        )
