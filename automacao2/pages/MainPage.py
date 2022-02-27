from automacao2.pages.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage(PageObject):
    URL_MAIN = 'https://www.cesar.school/'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_main_page_url()
        self.accept_cookies()

    def is_url_main_page(self) -> bool:
        return self.driver.current_url == self.URL_MAIN

    def open_main_page_url(self):
        self.driver.get(self.URL_MAIN)

    def accept_cookies(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/a[2]'))).click()






























