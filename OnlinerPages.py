from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class OnlinerMainPageLocators:
    CATALOG_LINK_LOCATOR = (By.XPATH, "/html//div[@id='container']//nav[@class='b-top-navigation']/ul["
                                      "@class='b-main-navigation']//a[@href='https://catalog.onliner.by/']/span["
                                      "@class='b-main-navigation__text']")


class CatalogLocators:
    CATEGORY_BUTTON_LOCATOR = (By.XPATH, '//*[@id="container"]/div/div/div/div/div[1]/ul/li[@data-id="1"]')
    SUBCATEGORY_LINK_LOCATOR = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']//div["
                                          "@class='g-middle-i']/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div["
                                          "@class='catalog-navigation-list__aside-title']")
    PRODUCT_CATEGORY_LINK_LOCATOR = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/"
                                               "div[@class='l-gradient-wrapper']//div[@class='g-middle-i']/"
                                               "div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div["
                                               "@class='catalog-navigation-list__dropdown']/ "
                                               "div[@class='catalog-navigation-list__dropdown-list']/a[@href='https://"
                                               "catalog.onliner.by/mobile']//span["
                                               "@class='catalog-navigation-list__dropdown-description']")
    PRODUCT_LINK_LOCATOR = (By.XPATH, "/html//div[@id='schema-products']/div[7]/div[@class='schema-product "
                                      "schema-product_narrow-sizes']/div[@class='schema-product__part "
                                      "schema-product__part_2']/div[@class='schema-product__part "
                                      "schema-product__part_4']/div[@class='schema-product__title']/a["
                                      "@href='https://catalog.onliner.by/mobile/apple/iphone1164b']/span[.='Смартфон "
                                      "Apple iPhone 11 64GB (черный)']")
    SEARCH_FIELD_LOCATOR = (
        By.XPATH, "//div[@id='fast-search']/form[@action='//catalog.onliner.by/search/']/input[@name='query']")
    PRODUCT_TITLE_LOCATOR = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/div["
                                       "@class='l-gradient-wrapper']/div[@class='g-middle']//h1["
                                       "@class='catalog-masthead__title']")
    PRODUCT_PRICE_LOCATOR = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/div["
                                       "@class='l-gradient-wrapper']/div[@class='g-middle']/div["
                                       "@class='g-middle-i']/div[@class='catalog-content js-scrolling-area']/div["
                                       "1]//div[@class='offers-description__price "
                                       "offers-description__price_primary']/a["
                                       "@class='offers-description__link offers-description__link_nodecor']")
    SEARCH_IFRAME_LOCATOR = (By.XPATH, '//*[@id="fast-search-modal"]/div/div/iframe')
    FIRST_PRODUCT_PRICE_LOCATOR = (By.XPATH, '//*[@id="search-page"]/div[2]/ul/li[1]/div/div/div[1]/div/div[1]/a/span')


class OnlinerPageHelper(BasePage):

    def go_to_catalog(self):
        self.find_element(OnlinerMainPageLocators.CATALOG_LINK_LOCATOR).click()

    def choose_category(self):
        self.find_element(CatalogLocators.CATEGORY_BUTTON_LOCATOR).click()

    def choose_subcategory(self):
        ActionChains(self.driver).move_to_element(self.find_element(CatalogLocators.SUBCATEGORY_LINK_LOCATOR)).perform()

    def click_on_product_category(self):
        self.find_element(CatalogLocators.PRODUCT_CATEGORY_LINK_LOCATOR).click()

    def click_on_phone(self):
        self.find_element(CatalogLocators.PRODUCT_LINK_LOCATOR).click()

    def get_price(self):
        return self.find_element(CatalogLocators.PRODUCT_PRICE_LOCATOR).text

    def get_title(self):
        return self.find_element(CatalogLocators.PRODUCT_TITLE_LOCATOR).text

    def search_by_title(self, title):
        search_field = self.find_element(CatalogLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(title)

    def switch_to_iframe(self):
        iframe = self.find_element(CatalogLocators.SEARCH_IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)

    def get_price_from_search_result(self):
        return self.find_element(CatalogLocators.FIRST_PRODUCT_PRICE_LOCATOR).text
