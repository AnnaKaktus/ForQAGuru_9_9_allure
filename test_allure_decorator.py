import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AnnaKaktus")
@allure.feature("Issues")
@allure.story("Searching issues")
def test_selene(open_browser):
    open()
    search()
    go()
    open_issue()
    found()

@allure.step("Открываем главную страницу")
def open():
    browser.open("https://github.com")

@allure.step("Ищем нужную репу")
def search():
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("AnnaKaktus/QAguru-test5")
    s("#query-builder-test").submit()

@allure.step("Переходим в репу")
def go():
    s(by.link_text("AnnaKaktus/QAguru-test5")).click()

@allure.step("Открываем Issues")
def open_issue():
    s("#issues-tab").click()

@allure.step("Находим нужную Issue")
def found():
    s(by.partial_text("#1")).should(be.visible)
