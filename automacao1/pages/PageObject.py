from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

class PageObject:

    def __init__(self, browser=None, driver=None):
        if driver:
            self.driver = driver
            self.driver.implicitly_wait(3)
        else:
            if browser == 'chrome':
                opts = ChromeOptions()
                opts.add_experimental_option("detach", True)

                chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=chrome_service, options=opts)

    def close(self):
        self.driver.quit()
