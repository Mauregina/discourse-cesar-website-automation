import pytest

from automacao2.pages.MainPage import MainPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run tests")

@pytest.fixture(scope="session")
def tc_setup(request):
    selected_browser = request.config.getoption('browser').lower()

    if selected_browser not in ['chrome']:
        raise Exception(f'Browser is not supported: {selected_browser.upper()}')

    print("Launch browser")
    tc_setup = MainPage(browser=selected_browser)

    yield tc_setup

    print("Close browser")
    tc_setup.close()

