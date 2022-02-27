import pytest

from automacao2.pages.MainPage import MainPage
from automacao2.pages.MenuPage import MenuPage
from automacao2.pages.BlogPage import BlogPage

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run tests")

@pytest.fixture(scope="session")
def tc_setup(request):
    selected_browser = request.config.getoption('browser').lower()

    if selected_browser not in ['chrome']:
        raise Exception(f'Browser is not supported: {selected_browser.upper()}')

    print("Launch browser")
    tc_setup = MainPage(browser=selected_browser)
    assert tc_setup.is_url_main_page(), 'Main page is not current URL!'

    menuPage = MenuPage(tc_setup.driver)
    assert menuPage.is_menu_page_displayed(), 'Menu page not displayed!'
    assert menuPage.is_menu_school_displayed(), 'Menu school not displayed!'
    menuPage.open_menu_school()
    assert menuPage.is_submenu_blog_displayed(), 'Submenu blog not displayed!'
    menuPage.click_submenu_blog()

    blogPage = BlogPage(tc_setup.driver)
    assert blogPage.is_url_blog_page(), 'Blog page is not current URL!'
    assert blogPage.is_blog_page(), 'Blog page not loaded properly!'
    assert blogPage.is_pagination_displayed(), 'Blog page pagination not displayed!'
    blogPage.click_next_page()
    assert blogPage.is_next_page(), 'Blog page not at next page!'

    yield tc_setup

    print("Close browser")
    tc_setup.close()

