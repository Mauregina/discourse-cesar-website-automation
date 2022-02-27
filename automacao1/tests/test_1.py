from automacao1.pages.DemoPage import DemoPage

class Test1:

    def test_view_title_all_topics_closed(self, tc_setup):
        demoPage = DemoPage(tc_setup.driver)
        title_all_topics_closed_lst = demoPage.get_title_all_topics_closed()
        assert title_all_topics_closed_lst, 'Topics closed list empty!'

        if title_all_topics_closed_lst:
            print('\n*** The title of all closed topics ***')
            row = 1
            for title in title_all_topics_closed_lst:
                print(f'Title {row}: {title}')
                row+=1

    def test_frequency_items_category(self, tc_setup):
        demoPage = DemoPage(tc_setup.driver)
        frequency_items_category_dict = demoPage.get_frequency_items_category()
        assert frequency_items_category_dict, 'Frequency items category list empty!'

        if frequency_items_category_dict:
            print('\n*** Number of items in each category ***')
            for category, frequency in frequency_items_category_dict.items():
                print(f'{category.capitalize()} - {frequency}')

    def test_view_topic_most_view(self, tc_setup):
        demoPage = DemoPage(tc_setup.driver)
        title_topic_most_view = demoPage.get_title_topic_most_view()
        assert title_topic_most_view, 'Topic most view is empty!'

        if title_topic_most_view:
            print('\n*** The title of the topic that has the most views ***')
            print(title_topic_most_view)



