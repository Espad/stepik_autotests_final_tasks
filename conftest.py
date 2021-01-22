import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser: en,es,ru")


@pytest.fixture(scope="function")
def browser(request):
    # get browser name
    browser_name = request.config.getoption("browser_name")

    # get language
    user_language = request.config.getoption("language")
    if user_language is None:
        raise pytest.UsageError("--language should be not empty, eg es, fr")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        # options.add_argument('headless')
        options.add_argument('window-size=1920x935')
        browser = webdriver.Chrome(options=options)
        browser.delete_all_cookies()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    yield browser

    print("\nquit browser..")

    browser.close()
    browser.quit()
