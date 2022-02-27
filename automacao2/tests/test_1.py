from automacao2.pages.BlogPage import BlogPage
from automacao2.pages.FooterPage import FooterPage

class Test1:

    def test_view_info_second_article(self, tc_setup):
        blogPage = BlogPage(tc_setup.driver)
        title_second_article = blogPage.get_article_title(post_order=2)
        assert title_second_article, 'Title second post is empty!'
        if title_second_article:
            print(f'\nTitle second post: {title_second_article}')

        date_published_second_article = blogPage.get_article_date_published(post_order=2)
        assert date_published_second_article, 'Date second post is empty!'
        if date_published_second_article:
            print(f'Date second post: {date_published_second_article}')

    def test_view_info_third_article(self, tc_setup):
        blogPage = BlogPage(tc_setup.driver)
        title_third_article = blogPage.get_article_title(post_order=3)
        assert title_third_article, 'Title third post is empty!'
        if title_third_article:
            print(f'\nTitle third post: {title_third_article}')

        author_third_article = blogPage.get_article_author(post_order=3)
        assert author_third_article, 'Author third post is empty!'
        if author_third_article:
            print(f'Author third post: {author_third_article}')

    def test_view_info_address(self, tc_setup):
        blogPage = BlogPage(tc_setup.driver)
        footerPage = FooterPage(tc_setup.driver)
        footerPage.scroll_page_to_bottom()
        assert footerPage.is_footer_displayed(), 'Blog page not at bottom of the page!'
        address_str = footerPage.get_address()
        assert address_str, 'Address is empty!'
        if address_str:
            print(f'\nAddress Cesar School: {address_str}')



