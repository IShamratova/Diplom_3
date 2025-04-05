import allure
from data.data import TestData
from pages.constructor_and_feed_page import ConstructorAndFeedPage


class TestConstructorAndFeed:

    @allure.title('Проверки на страницах "Конструктор" и "Лента заказов"')
    def test_constructor_and_feed(self, driver, created_user):
        # Создание объекта страницы
        constructor_and_feed_page = ConstructorAndFeedPage(driver)

        # Открытие главной страницы
        constructor_and_feed_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Лента Заказов"
        constructor_and_feed_page.click_feed_button()

        # Проверка URL-адреса на соответствие странице ленты заказов
        constructor_and_feed_page.check_feed_url()

        # Клик по кнопке "Конструктор"
        constructor_and_feed_page.click_constuctor_button()

        # Проверка URL-адреса на соответствие базовой странице
        constructor_and_feed_page.check_base_url()

        # Клик по ингредиенту и ожидание появления модального окна с деталями
        constructor_and_feed_page.click_ingredient_button_and_watch_details()

        # Проверка URL-адреса на соответствие страницы ингредиента
        constructor_and_feed_page.check_text_ingredient_in_url()

        # Клик по кнопке закрытия модального окна с деталями ингредиента
        constructor_and_feed_page.click_close_ingredient_details_modal_button()

        # Проверка счётчика ингредиента на соответствие тексту "0"
        constructor_and_feed_page.check_ingredient_counter_quantity("0")

        # Перетаскивание элемента и ожидание счётчика ингредиента с текстом "2"
        constructor_and_feed_page.drag_n_drop_ingredient("2")

        # Проверка счётчика ингредиента на соответствие тексту "2"
        constructor_and_feed_page.check_ingredient_counter_quantity("2")