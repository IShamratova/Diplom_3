from data.data import TestData
from locators.login_page_locators import LoginPageLocators
from locators.constructor_and_feed_page_locators import ConstructorAndFeedPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.login_page import LoginPage


class TestPersonalAccount:

    def test_personal_account(self, driver, created_user):
        # Создание объекта страницы
        login_page = LoginPage(driver)

        # Открытие страницы логина
        login_page.open_url(TestData.BASE_URL)

        # Удаление мешающего модального окна
        login_page.remove_elements_by_script()

        # Клик по кнопке "Личный Кабинет"
        login_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Ввод учетных данных
        login_page.login(created_user["email"], created_user["password"])

        # Явное ожидание для загрузки страницы после входа
        login_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.BUTTON_ORDER, 3)

        # Клик по кнопке "Личный Кабинет"
        login_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Явное ожидание для загрузки страницы профиля
        login_page.wait_for_visibility_of_element_by_xpath_by_timeout(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY, 3)

        # Проверка URL-адреса на соответствие профилю
        login_page.check_url(TestData.BASE_URL + TestData.ROUTES["profile"])

        # Клик по кнопке "История заказов"
        login_page.click_element_by_script_by_xpath(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)

        # Проверка URL-адреса на соответствие истории заказов
        login_page.check_url(TestData.BASE_URL + TestData.ROUTES["order_history"])

        # Клик по кнопке "Выйти"
        login_page.click_element_by_script_by_xpath(PersonalAccountPageLocators.BUTTON_EXIT)

        # Явное ожидание для загрузки страницы после выхода
        login_page.wait_for_visibility_of_element_by_xpath_by_timeout(LoginPageLocators.BUTTON_ENTER, 3)

        # Проверка URL-адреса на соответствие профилю
        login_page.check_url(TestData.BASE_URL + TestData.ROUTES["login"])



