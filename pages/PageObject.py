from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class PageObject:

    def __init__(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.implicitly_wait(5)

