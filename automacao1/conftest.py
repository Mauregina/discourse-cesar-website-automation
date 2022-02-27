import pytest

from automacao1.pages.MainPage import MainPage
from automacao1.pages.DemoPage import DemoPage

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run tests")

@pytest.fixture(scope="session")
def tc_setup(request):
    selected_browser = request.config.getoption('browser').lower()

    if selected_browser not in ['chrome']:
        raise Exception(f'Browser is not supported: {selected_browser.upper()}')

    print("\n Launch browser")
    tc_setup = MainPage(browser=selected_browser)
    assert tc_setup.is_url_main_page(), 'Main page is not current URL!'
    assert tc_setup.is_demo_link_displayed(), 'Demo link not displayed!'
    tc_setup.click_demo_item()

    demoPage = DemoPage(tc_setup.driver)
    assert demoPage.is_url_demo_page(), 'Demo page is not current URL!'
    assert demoPage.is_demo_page(), 'Demo page not loaded properly!'
    demoPage.scroll_page_to_bottom()
    assert demoPage.is_at_bottom_page(), 'Demo page not at bottom of the page!'

    yield tc_setup

    print("Close browser")
    tc_setup.close()

