from data.data import TestData
from locators.constructor_and_feed_page_locators import ConstructorAndFeedPageLocators
from pages.base_page import BasePage


class TestConstructorAndFeed:

    def test_constructor_and_feed(self, driver, created_user):
        # Создание объекта страницы
        constructor_and_feed_page = BasePage(driver)

        # Открытие главной страницы
        constructor_and_feed_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Лента Заказов"
        constructor_and_feed_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_FEED)

        # Явное ожидание для загрузки кнопки "Лента Заказов"
        constructor_and_feed_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_FEED, 3)

        # Проверка URL-адреса на соответствие ленте заказов
        constructor_and_feed_page.check_url(TestData.BASE_URL + TestData.ROUTES["feed"])

        # Клик по кнопке "Конструктор"
        constructor_and_feed_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_CONSTRUCTOR)

        # Явное ожидание для загрузки заголовка "Соберите бургер"
        constructor_and_feed_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ASSEMBLE_BURGER, 3)

        # Проверка URL-адреса на соответствие базовой странице
        constructor_and_feed_page.check_url(TestData.BASE_URL)

        # Клик по кнопке "Флюоресцентная булка"
        constructor_and_feed_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_BUN_FLUO)

        # Явное ожидание для загрузки заголовка "Детали ингредиента"
        constructor_and_feed_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_INGREDIENT_DETAILS, 3)

        # Проверка URL-адреса на соответствие ингредиенту
        assert "/ingredient/" in driver.current_url

        # Клик по кнопке закрытия окна "Детали ингредиента"
        constructor_and_feed_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_CLOSE_MODAL)

        # Проверка счётчика ингредиента на соответствие 0
        assert constructor_and_feed_page.find_element_by_xpath(ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS).text.strip() == "0"

        # Перетаскивание элемента
        constructor_and_feed_page.drag_n_drop_element(ConstructorAndFeedPageLocators.BUTTON_BUN_FLUO, ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE)

        # Явное ожидание для загрузки заголовка "Детали ингредиента"
        constructor_and_feed_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS + '[text()="2"]', 3)

        # Проверка счётчика ингредиента на соответствие 2
        assert constructor_and_feed_page.find_element_by_xpath(ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS).text.strip() == "2"