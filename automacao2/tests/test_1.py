from automacao2.pages.BlogPage import BlogPage
from automacao2.pages.MenuPage import MenuPage
from automacao2.pages.FooterPage import FooterPage

class Test1:

    def test_view_info_articles(self, main_page_open):
        menuPage = MenuPage(main_page_open.driver)
        menuPage.open_menu_school()
        menuPage.click_submenu_blog()

        blogPage = BlogPage(main_page_open.driver)
        blogPage.click_next_page()
        title_second_article = blogPage.get_article_title(post_order=2)
        date_published_second_article = blogPage.get_article_date_published(post_order=2)
        title_third_article = blogPage.get_article_title(post_order=3)
        author_third_article = blogPage.get_article_author(post_order=3)
        print(title_second_article)
        print(date_published_second_article)
        print(title_third_article)
        print(author_third_article)

        footerPage = FooterPage(main_page_open.driver)
        footerPage.scroll_page_to_bottom()
        address_str = footerPage.get_address()
        print(address_str)



