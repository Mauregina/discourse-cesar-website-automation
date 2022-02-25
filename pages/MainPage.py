import time

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
        self.driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/ul/li[4]/a').click()

        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        print(self.driver.current_url)

        scroll_pause_time = 2

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

        # all_topics = self.driver.find_elements_by_xpath("//href[contains(text(), '#lock')]")
        #
        # print(all_topics)



