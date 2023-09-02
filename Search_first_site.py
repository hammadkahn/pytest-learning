from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class search_website:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "nav-toggle"))
        )
        search_box.click()

        # search_box.send_keys("computer")
        # search_box.submit()

    def select_from_dropdown(self, text):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        dropdown.click()

    def select_from_thumbnail(self):
        thumbnail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "font-weight-bold ")))
        assert thumbnail.is_displayed(), "Expected element is visible"
        thumbnail.click()

    # def play_audio(self):
    #     audio = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "md-crosslink")))
    #
    #     audio.click()
    #     assert audi.is_displayed(), "Expected element is not visible"
