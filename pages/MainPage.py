from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

class MainPage(PageObject):
    URL_MAIN = 'https://www.discourse.org/'
    class_menu_items = 'wrapper'
    txt_demo = 'Demo'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_main_page_url()

    def open_main_page_url(self):
        self.driver.get(self.URL_MAIN)

    def is_url_main_page(self):
        return self.driver.current_url == self.URL_MAIN

    def click_demo_item(self):
        item = self.driver.find_element_by_xpath("//div[@class='wrapper']//a[contains(text(),'Demo')]")
        print(item.get_attribute('href'))
        item.click()

        # self.driver.get(item.get_attribute('href'))
