import pytest
from selene.support.shared import browser

import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    from selenium import webdriver
    if config.options.browser_name == 'chrome':
        from webdriver_manager.chrome import ChromeDriverManager
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = config.options.browser_headless
        chrome_driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=chrome_options)
        browser.config.driver = chrome_driver
    elif config.options.browser_name == 'firefox':
        from webdriver_manager.firefox import GeckoDriverManager
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = config.options.browser_headless
        firefox_driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=firefox_options)
        browser.config.driver = firefox_driver

    browser.config.timeout = config.options.browser_config_timeout
    # browser.config.browser_name = config.options.browser_name
    yield
    if config.options.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()
