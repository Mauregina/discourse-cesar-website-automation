import time

from selenium.webdriver.common.by import By
from automacao1.pages.PageObject import PageObject
from collections import Counter

class DemoPage(PageObject):
    class_menu_items = 'wrapper'
    txt_demo = 'Demo'

    def __init__(self, driver):
        super().__init__(driver=driver)

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
        topics_closed = self.driver.find_elements_by_xpath("//tr[contains(@class, 'closed ember-view')]")

        return [topic.find_element_by_tag_name('span').text for topic in topics_closed]

    def get_all_topics(self) -> list:
        return self.driver.find_elements_by_xpath("//table[@id='ember50']/tbody/tr")

    def get_frequency_items_category(self) -> dict:
        topics = self.get_all_topics()
        total_topics = len(topics)
        topics_with_category_lst = self.driver.find_elements_by_xpath("//a[contains(@class, 'badge-wrapper bullet')]")
        total_topics_with_category = len(topics_with_category_lst)
        total_topics_no_category = total_topics - total_topics_with_category

        # print(f'Uncategorized - {total_topics_no_category}')
        frequency_items_category_dict = Counter(list(i.text for i in topics_with_category_lst))
        frequency_items_category_dict['Uncategorized'] = total_topics_no_category

        return frequency_items_category_dict

    def convert_number_views_to_int(self, views: str) -> int:
        if "k" in views.lower():
            views_float = float(views[:-1]) * 1000
            return int(views_float)

        return int(views)

    def get_topic_most_view(self) -> int:
        topics = self.get_all_topics()

        topics_dict = {}
        for topic in topics:
            columns_lst = topic.find_elements_by_tag_name('td')
            title_txt = columns_lst[0].find_element_by_tag_name('span').text
            views_txt = columns_lst[3].text
            topics_dict[title_txt] = self.convert_number_views_to_int(views_txt)

        return max(topics_dict, key=topics_dict.get)



















