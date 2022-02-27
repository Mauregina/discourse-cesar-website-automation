import time

from selenium.common.exceptions import NoSuchElementException
from automacao1.pages.PageObject import PageObject
from collections import Counter

class DemoPage(PageObject):
    URL_DEMO = 'https://try.discourse.org/'
    txt_page_title = 'demo'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_url_demo_page(self) -> bool:
        return self.driver.current_url == self.URL_DEMO

    def is_demo_page(self) -> bool:
        try:
            demo_class_title = self.driver.find_element_by_xpath('//*[@id="site-text-logo"]').text.lower()

            topics_list = self.get_all_topics()

            return demo_class_title == self.txt_page_title and topics_list

        except NoSuchElementException:
            return False

    def is_at_bottom_page(self) -> bool:
        try:
            return self.driver.find_element_by_xpath('//*[@id="ember191"]/h3').is_displayed()

        except NoSuchElementException:
            return False

    def scroll_page_to_bottom(self):
        scroll_pause_time = 2
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    def get_title_all_topics_closed(self) -> list:
        try:
            topics_closed = self.driver.find_elements_by_xpath('//tr[contains(@class, "closed ember-view")]')
            return [topic.find_element_by_tag_name('span').text for topic in topics_closed]

        except NoSuchElementException:
            return None

    def get_all_topics(self) -> list:
        try:
            return self.driver.find_elements_by_xpath('//table[@id="ember50"]/tbody/tr')

        except NoSuchElementException:
            return None

    def get_frequency_items_category(self) -> dict:
        try:
            topics = self.get_all_topics()
            total_topics = len(topics)
            topics_with_category_lst = self.driver.find_elements_by_xpath('//a[contains(@class, "badge-wrapper bullet")]')
            total_topics_with_category = len(topics_with_category_lst)
            total_topics_no_category = total_topics - total_topics_with_category

            frequency_items_category_dict = Counter(list(i.text for i in topics_with_category_lst))
            frequency_items_category_dict['Uncategorized'] = total_topics_no_category

            return frequency_items_category_dict

        except NoSuchElementException:
            return None

    def convert_number_views_to_int(self, views: str) -> int:
        if "k" in views.lower():
            views_float = float(views[:-1]) * 1000
            return int(views_float)

        return int(views)

    def get_title_topic_most_view(self) -> str:
        try:
            topics = self.get_all_topics()

            topics_dict = {}
            for topic in topics:
                columns_lst = topic.find_elements_by_tag_name('td')
                title_txt = columns_lst[0].find_element_by_tag_name('span').text
                views_txt = columns_lst[3].text
                topics_dict[title_txt] = self.convert_number_views_to_int(views_txt)

            return max(topics_dict, key=topics_dict.get)

        except NoSuchElementException:
            return ''


















