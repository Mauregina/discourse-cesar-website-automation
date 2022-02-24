import pytest

from pages.MainPage import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run tests")

@pytest.fixture(scope="session")
def main_page_open(request):
    selected_browser = request.config.getoption('browser').lower()

    if selected_browser not in ['chrome']:
        raise Exception(f'Browser is not supported: {selected_browser.upper()}')

    print("Launch browser")
    mainPage = MainPage(browser=selected_browser)

    yield mainPage

    print("Close browser")

