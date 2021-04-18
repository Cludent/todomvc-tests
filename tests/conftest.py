import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def custom_wait_close_browser():
    browser.config.timeout = 7
    yield
    browser.clear_local_storage()
