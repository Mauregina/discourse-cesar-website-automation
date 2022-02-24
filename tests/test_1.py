class Test1:

    def test_view_title_all_closed_topics(self, main_page_open):
        print("Executing test -> Print the title of all closed topics")
        assert main_page_open.is_url_main_page(), 'Page https://www.discourse.org/ not found!'
        main_page_open.click_demo_item()

    def test_view_number_items_category(self, main_page_open):
        print("Print number of items in each category and those that do not have a category")

    def test_view_topic_title_most_view(self, main_page_open):
        print("Print the topic title that has the most views")
