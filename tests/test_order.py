import allure
from data.data import TestData
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка создания заказа')
    def test_logged_user_can_create_order(self, driver, created_user):
        # Создание объекта страницы
        order_page = OrderPage(driver)

        # Открытие главной страницы
        order_page.open_url(TestData.BASE_URL)

        # Логин пользователя
        order_page.user_login(created_user["email"], created_user["password"])

        # Оформление заказа
        order_page.create_order()

        # Проверка идентификатора созданного заказа
        order_page.check_created_order_id("9999")

    @allure.title('Проверка заказа в работе')
    def test_order_in_work(self, driver, created_user):
        # Создание объекта страницы
        order_page = OrderPage(driver)

        # Открытие главной страницы
        order_page.open_url(TestData.BASE_URL)

        # Логин пользователя
        order_page.user_login(created_user["email"], created_user["password"])

        # Оформление заказа
        order_page.create_order()

        # Проверка идентификатора созданного заказа на неравенство "9999"
        order_page.check_created_order_id("9999")

        # Сохранение идентификатора заказа
        created_order_id = order_page.return_created_order_id()

        # Клик по кнопке закрытия модального окна с деталями созданного заказа
        order_page.click_close_order_details_modal_button()

        # Клик по кнопке "Лента Заказов"
        order_page.click_feed_button()

        # Проверка нахождения номера созданного заказа в разделе "В работе"
        order_page.check_created_order_id_in_work(created_order_id)

    @allure.title('Проверка счетчиков заказа')
    def test_order_counts(self, driver, created_user):
        # Создание объекта страницы
        order_page = OrderPage(driver)

        # Открытие главной страницы
        order_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Лента Заказов"
        order_page.click_feed_button()

        # Сохранение (проверка и выдача) значения счётчика "Выполнено за всё время" на неравенство пустой строке
        value_count_orders_total = order_page.check_and_return_orders_done_total_quantity("")

        # Сохранение (проверка и выдача) значения счётчика "Выполнено за сегодня" на неравенство пустой строке
        value_count_orders_today = order_page.check_and_return_orders_done_today_quantity("")

        # Логин пользователя
        order_page.user_login(created_user["email"], created_user["password"])

        # Оформление заказа
        order_page.create_order()

        # Проверка идентификатора созданного заказа на неравенство "9999"
        order_page.check_created_order_id("9999")

        # Сохранение идентификатора заказа
        created_order_id = order_page.return_created_order_id()

        # Клик по кнопке закрытия модального окна с деталями созданного заказа
        order_page.click_close_order_details_modal_button()

        # Клик по кнопке "Лента Заказов"
        order_page.click_feed_button()

        # Сохранение (проверка и выдача) нового значения счётчика "Выполнено за всё время" на неравенство предыдущему значению
        new_value_count_orders_total = order_page.check_and_return_orders_done_total_quantity(value_count_orders_total)

        # Проверка увеличения значения счётчика "Выполнено за всё время"
        order_page.check_incrementation_of_orders_count(value_count_orders_total, new_value_count_orders_total)

        # Прокрутка страницы до счётчика "Выполнено за сегодня"
        order_page.scroll_to_orders_done_today()

        # Сохранение (проверка и выдача) нового значения счётчика "Выполнено за сегодня" на неравенство предыдущему значению
        new_value_count_orders_today = order_page.check_and_return_orders_done_today_quantity(value_count_orders_today)

        # Проверка увеличения значения счётчика "Выполнено за сегодня"
        order_page.check_incrementation_of_orders_count(value_count_orders_today, new_value_count_orders_today)

    @allure.title('Проверка отображения заказов на странице «Лента заказов»')
    def test_order_history(self, driver, created_user):
        # Создание объекта страницы
        order_page = OrderPage(driver)

        # Открытие главной страницы
        order_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Лента Заказов"
        order_page.click_feed_button()

        # Логин пользователя
        order_page.user_login(created_user["email"], created_user["password"])

        # Оформление заказа
        order_page.create_order()

        # Проверка идентификатора созданного заказа на неравенство "9999"
        order_page.check_created_order_id("9999")

        # Сохранение идентификатора созданного заказа
        created_order_id = order_page.return_created_order_id()

        # Клик по кнопке закрытия модального окна с деталями созданного заказа
        order_page.click_close_order_details_modal_button()

        # Клик по кнопке "Лента Заказов"
        order_page.click_feed_button()

        # Клик по идентификатору созданного заказа
        order_page.click_created_order_id(created_order_id)

        # Проверка наименования созданного заказа
        order_page.check_order_name()

        # Клик по кнопке закрытия модального окна с деталями созданного заказа
        order_page.click_close_order_details_modal_button()

        # Клик по кнопке "Личный Кабинет"
        order_page.click_personal_account_button()

        # Клик по кнопке "История заказов"
        order_page.click_order_history_link()

        # Проверка URL-адреса на соответствие страницы "История заказов"
        order_page.check_order_history_url()

        # Клик по номеру созданного заказа
        order_page.click_created_order_number(created_order_id)

        # Проверка наименования созданного заказа
        order_page.check_order_name()