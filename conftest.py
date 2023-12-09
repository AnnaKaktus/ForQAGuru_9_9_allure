import pytest
from selene.support.shared import browser

@pytest.fixture()
def open_browser():
    browser.driver.set_window_size(width=1920, height=1080)
    yield browser
    browser.quit()
