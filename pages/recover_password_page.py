import allure
from data.data import TestData
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage


class RecoverPasswordPage(BasePage):

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_personal_account_button(self):
        # Удаление мешающего модального окна
        self.remove_elements_by_script(
            RecoverPasswordPageLocators.MODAL_WINDOW
        )

        # Клик по кнопке "Личный Кабинет"
        self.click_element_by_script_by_xpath(
            RecoverPasswordPageLocators.BUTTON_PERSONAL_ACCOUNT
        )

        # Явное ожидание для загрузки ссылки "Восстановить пароль"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RecoverPasswordPageLocators.LINK_RECOVER_PASSWORD,
            3
        )

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recover_password_link(self):
        # Клик по ссылке "Восстановить пароль"
        self.click_element_by_script_by_xpath(
            RecoverPasswordPageLocators.LINK_RECOVER_PASSWORD
        )

        # Явное ожидание для загрузки кнопки "Восстановить"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RecoverPasswordPageLocators.BUTTON_RECOVER,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие страницы восстановления пароля')
    def check_forgot_password_url(self):
        # Проверка URL-адреса на соответствие страницы восстановления пароля
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["forgot_password"]
        )

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recover_button(self):
        # Ввод почты
        self.set_text_to_field_by_xpath(
            RecoverPasswordPageLocators.INPUT_EMAIL, TestData.EMAIL_TEXT
        )

        # Клик по кнопке "Восстановить"
        self.click_element_by_script_by_xpath(
            RecoverPasswordPageLocators.BUTTON_RECOVER
        )

        # Явное ожидание для загрузки кнопки "Сохранить"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RecoverPasswordPageLocators.BUTTON_SAVE,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие страницы сброса пароля')
    def check_reset_password_url(self):
        # Проверка URL-адреса на соответствие страницы сброса пароля
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["reset_password"]
        )

    @allure.step('Клик по кнопке показа/скрытия пароля')
    def click_passeye_button(self):
        # Клик по кнопке показа/скрытия пароля
        self.click_element_by_script_by_xpath(
            RecoverPasswordPageLocators.BUTTON_PASSEYE
        )

        # Явное ожидание для загрузки поля "Пароль"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            RecoverPasswordPageLocators.FIELD_PASSWORD_VISIBLE,
            3
        )

    @allure.step('Проверка нахождения класса "input_status_active" в элементе поля "Пароль"')
    def check_class_in_field_password_visible(self, class_name):
        # Проверка нахождения класса "input_status_active" в элементе поля "Пароль" во время показа пароля
        assert class_name in self.find_element_by_xpath(
            RecoverPasswordPageLocators.FIELD_PASSWORD_VISIBLE
        ).get_attribute("class")