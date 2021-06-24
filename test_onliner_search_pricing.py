import unittest
from selenium import webdriver

from OnlinerPages import *


class TestPageUI(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.maximize_window()
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_onliner_search(self):
        onliner_page = OnlinerPageHelper(self.driver)
        onliner_page.go_to_site()
        onliner_page.go_to_catalog()
        onliner_page.choose_category()
        onliner_page.choose_subcategory()
        onliner_page.click_on_product_category()
        onliner_page.click_on_phone()
        price = onliner_page.get_price()
        title = onliner_page.get_title()
        onliner_page.search_by_title(title)
        onliner_page.switch_to_iframe()
        search_result_price = onliner_page.get_price_from_search_result()
        self.assertEqual(price, search_result_price)


if __name__ == '__main__':
    unittest.main()
