import time

from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from collections import Counter

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


        # PRIMEIRO DESAFIO
        topics_closed = self.driver.find_elements_by_xpath("//tr[contains(@class, 'closed ember-view')]")

        for topic in topics_closed:
            print(topic.find_element_by_tag_name('span').text)

        # SEGUNDO DESAFIO
        topics = self.driver.find_elements_by_xpath("//table[@id='ember50']/tbody/tr")
        total_topics = len(topics)
        topics_with_category_lst = self.driver.find_elements_by_xpath("//a[contains(@class, 'badge-wrapper bullet')]")
        total_topics_with_category = len(topics_with_category_lst)
        total_topics_no_category = total_topics - total_topics_with_category

        print(f'Uncategorized - {total_topics_no_category}')

        category_dict = Counter(list(i.text for i in topics_with_category_lst))

        for frequency, category in category_dict.items():
            print(f'{frequency} - {category}')

        # TERCEIRO DESAFIO
        topics_dict = {}
        for topic in topics:
            columns_lst = topic.find_elements_by_tag_name('td')
            title_txt = columns_lst[0].find_element_by_tag_name('span').text
            views_txt = columns_lst[3].text

            # criar metodo -----------------------
            if "k" in views_txt.lower():
                views_float = float(views_txt[:-1])*1000
                views_int = int(views_float)
            else:
                views_int = int(views_txt)
            # ------------------------------------

            topics_dict[title_txt] = views_int

        print(max(topics_dict, key=topics_dict.get))



















