import allure
from data.data import TestData
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Ввод учётных данных и клик по кнопке "Войти"')
    def user_login(self, email, password):
        # Удаление мешающего модального окна
        self.remove_elements_by_script(
            PersonalAccountPageLocators.MODAL_WINDOW
        )

        # Клик по кнопке "Личный Кабинет"
        self.click_element_by_script_by_xpath(
            PersonalAccountPageLocators.BUTTON_PERSONAL_ACCOUNT
        )

        # Ввод персональных данных
        self.set_text_to_field_by_xpath(
            PersonalAccountPageLocators.INPUT_EMAIL, email
        )
        self.set_text_to_field_by_xpath(
            PersonalAccountPageLocators.INPUT_PASSWORD, password
        )

        # Клик по кнопке "Войти"
        self.click_element_by_xpath(
            PersonalAccountPageLocators.BUTTON_ENTER
        )

        # Явное ожидание для загрузки страницы после входа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            PersonalAccountPageLocators.BUTTON_ORDER,
            3
        )

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_personal_account_button(self):
        # Клик по кнопке "Личный Кабинет"
        self.click_element_by_script_by_xpath(
            PersonalAccountPageLocators.BUTTON_PERSONAL_ACCOUNT
        )

        # Явное ожидание для загрузки страницы профиля
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            PersonalAccountPageLocators.LINK_ORDER_HISTORY,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие странице профиля')
    def check_profile_url(self):
        # Проверка URL-адреса на соответствие странице профиля
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["profile"]
        )

    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        # Клик по кнопке "История заказов"
        self.click_element_by_script_by_xpath(
            PersonalAccountPageLocators.LINK_ORDER_HISTORY
        )

    @allure.step('Проверка URL-адреса на соответствие странице истории заказов')
    def check_order_history_url(self):
        # Проверка URL-адреса на соответствие страницы истории заказов
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["order_history"]
        )

    @allure.step('Клик по кнопке "Выйти"')
    def click_exit_button(self):
        # Клик по кнопке "Выйти"
        self.click_element_by_script_by_xpath(
            PersonalAccountPageLocators.BUTTON_EXIT
        )

        # Явное ожидание для загрузки страницы после выхода
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            PersonalAccountPageLocators.BUTTON_ENTER,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие странице логина')
    def check_login_url(self):
        # Проверка URL-адреса на соответствие страницы логина
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["login"]
        )