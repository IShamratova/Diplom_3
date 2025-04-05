import allure
from data.data import TestData
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверки на странице "Личный кабинет"')
    def test_personal_account(self, driver, created_user):
        # Создание объекта страницы
        personal_account_page = PersonalAccountPage(driver)

        # Открытие страницы логина
        personal_account_page.open_url(TestData.BASE_URL)

        # Логин пользователя
        personal_account_page.user_login(created_user["email"], created_user["password"])

        # Клик по кнопке "Личный Кабинет"
        personal_account_page.click_personal_account_button()

        # Проверка URL-адреса на соответствие профилю
        personal_account_page.check_profile_url()

        # Клик по кнопке "История заказов"
        personal_account_page.click_order_history_button()

        # Проверка URL-адреса на соответствие страницы истории заказов
        personal_account_page.check_order_history_url()

        # Клик по кнопке "Выйти"
        personal_account_page.click_exit_button()

        # Проверка URL-адреса на соответствие страницы логина
        personal_account_page.check_login_url()