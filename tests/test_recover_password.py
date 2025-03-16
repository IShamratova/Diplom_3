from data.data import TestData
from locators.constructor_and_feed_page_locators import ConstructorAndFeedPageLocators
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage


class TestRecoverPassword:

    def test_recover_password(self, driver, created_user):
        # Создание объекта страницы
        recover_password_page = BasePage(driver)

        # Открытие главной страницы
        recover_password_page.open_url(TestData.BASE_URL)

        # Удаление мешающего модального окна
        recover_password_page.remove_elements_by_script()

        # Клик по кнопке "Личный Кабинет"
        recover_password_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Явное ожидание для загрузки ссылки "Восстановить пароль"
        recover_password_page.wait_for_visibility_of_element_by_xpath_by_timeout(RecoverPasswordPageLocators.LINK_RECOVER_PASSWORD, 3)

        # Клик по ссылке "Восстановить пароль"
        recover_password_page.click_element_by_script_by_xpath(RecoverPasswordPageLocators.LINK_RECOVER_PASSWORD)

        # Проверка URL-адреса на соответствие восстановлению пароля
        recover_password_page.check_url(TestData.BASE_URL + TestData.ROUTES["forgot_password"])

        # Явное ожидание для загрузки кнопки "Восстановить"
        recover_password_page.wait_for_visibility_of_element_by_xpath_by_timeout(RecoverPasswordPageLocators.BUTTON_RECOVER, 3)

        # Ввод почты
        recover_password_page.set_text_to_field_by_xpath(RecoverPasswordPageLocators.INPUT_EMAIL, TestData.EMAIL_TEXT)

        # Клик по кнопке "Восстановить"
        recover_password_page.click_element_by_script_by_xpath(RecoverPasswordPageLocators.BUTTON_RECOVER)

        # Явное ожидание для загрузки кнопки "Сохранить"
        recover_password_page.wait_for_visibility_of_element_by_xpath_by_timeout(RecoverPasswordPageLocators.BUTTON_SAVE, 3)

        # Проверка URL-адреса на соответствие сброса пароля
        recover_password_page.check_url(TestData.BASE_URL + TestData.ROUTES["reset_password"])

        # Клик по кнопке показа/скрытия пароля
        recover_password_page.click_element_by_script_by_xpath(RecoverPasswordPageLocators.BUTTON_PASSEYE)

        assert "input_status_active" in recover_password_page.find_element_by_xpath(RecoverPasswordPageLocators.FIELD_PASSWORD_VISIBLE).get_attribute("class")

