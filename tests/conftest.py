import pytest
from selene.support.shared import browser
from selenium import webdriver
import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver = _set_custom_driver(config.settings)
    if driver:
        browser.config.driver = driver
    else:
        browser.config.browser_name = config.settings.browser_name
    yield
    if config.settings.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()


def _set_custom_driver(settings: config.Settings) -> webdriver:
    options = None
    if settings.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = settings.browser_headless
    elif settings.browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = settings.browser_headless

    if settings.remote_url:
        options.set_capability('enableVNC', settings.remote_enableVNC)
        options.set_capability('screen_Resolution', settings.remote_screenResolution)
        driver = webdriver.Remote(
            settings.remote_url, options=options
        )
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        driver = {
            'chrome': lambda: webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options
            ),
            'firefox': lambda: webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options
            )
        }[settings.browser_name]()

    if settings.browser_window_maximize:
        driver.maximize_window()
    else:
        driver.set_window_size(
            width=settings.browser_window_width,
            height=settings.browser_window_height
        )

    return driver
