import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_selene(open_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем нужную репу"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("AnnaKaktus/QAguru-test5")
        s("#query-builder-test").submit()

    with allure.step("Переходим в репу"):
        s(by.link_text("AnnaKaktus/QAguru-test5")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Находим нужную Issue"):
        s(by.partial_text("#1")).should(be.visible)
