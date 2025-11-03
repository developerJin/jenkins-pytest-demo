import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
class TestWeb:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

    def teardown_method(self):
        self.driver.quit()

    def test_google_title(self):
        self.driver.get('https://www.google.com')
        assert 'Google' in self.driver.title

    def test_google_search_box(self):
        self.driver.get('https://www.google.com')
        search_box = self.driver.find_element(By.NAME, 'q')
        assert search_box is not None