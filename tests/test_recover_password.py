import allure
from data.data import TestData
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPassword:

    @allure.title('Проверка на странице "Восстановление пароля"')
    def test_recover_password(self, driver, created_user):
        # Создание объекта страницы
        recover_password_page = RecoverPasswordPage(driver)

        # Открытие главной страницы
        recover_password_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Личный Кабинет"
        recover_password_page.click_personal_account_button()

        # Клик по ссылке "Восстановить пароль"
        recover_password_page.click_recover_password_link()

        # Проверка URL-адреса на соответствие страницы восстановления пароля
        recover_password_page.check_forgot_password_url()

        # Клик по кнопке "Восстановить"
        recover_password_page.click_recover_button()

        # Проверка URL-адреса на соответствие сброса пароля
        recover_password_page.check_reset_password_url()

        # Клик по кнопке показа/скрытия пароля
        recover_password_page.click_passeye_button()

        # Проверка нахождения класса "input_status_active" в элементе поля "Пароль" во время показа пароля
        recover_password_page.check_class_in_field_password_visible("input_status_active")

