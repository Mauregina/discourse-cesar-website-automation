from automacao1.conftest import main_page_open
from automacao1.pages.DemoPage import DemoPage


class Test1:

    def test_view_info_demo(self, main_page_open):
        demoPage = DemoPage(main_page_open.driver)
        demoPage.scroll_page_to_bottom()

        title_all_topics_closed_lst = demoPage.get_title_all_topics_closed()
        for i in title_all_topics_closed_lst:
            print(i)

        frequency_items_category_dict = demoPage.get_frequency_items_category()

        for frequency, category in frequency_items_category_dict.items():
            print(f'{frequency} - {category}')

        topic_most_view = demoPage.get_topic_most_view()

        print(topic_most_view)



