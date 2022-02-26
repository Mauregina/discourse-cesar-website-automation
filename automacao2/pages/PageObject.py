from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PageObject:

    def __init__(self, browser):
        if browser == 'chrome':
            opts = ChromeOptions()
            opts.add_experimental_option("detach", True)
            opts.add_argument("--start-maximized")

            caps = DesiredCapabilities().CHROME
            caps["pageLoadStrategy"] = "eager"

            chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=opts, desired_capabilities=caps)
            self.driver.implicitly_wait(10)

