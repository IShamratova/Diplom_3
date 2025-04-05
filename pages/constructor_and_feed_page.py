import allure
from data.data import TestData
from locators.constructor_and_feed_page_locators import ConstructorAndFeedPageLocators
from pages.base_page import BasePage


class ConstructorAndFeedPage(BasePage):

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_feed_button(self):
        # Клик по кнопке "Лента Заказов"
        self.click_element_by_script_by_xpath(
            ConstructorAndFeedPageLocators.BUTTON_FEED
        )

        # Явное ожидание для загрузки заголовка "Лента Заказов"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            ConstructorAndFeedPageLocators.HEADER_ORDER_FEED,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие странице ленты заказов')
    def check_feed_url(self):
        # Проверка URL-адреса на соответствие странице ленты заказов
        self.check_url(
            TestData.BASE_URL + TestData.ROUTES["feed"]
        )

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constuctor_button(self):
        # Клик по кнопке "Конструктор"
        self.click_element_by_script_by_xpath(
            ConstructorAndFeedPageLocators.BUTTON_CONSTRUCTOR
        )

        # Явное ожидание для загрузки заголовка "Соберите бургер"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            ConstructorAndFeedPageLocators.HEADER_ASSEMBLE_BURGER,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие базовой странице')
    def check_base_url(self):
        # Проверка URL-адреса на соответствие базовой странице
        self.check_url(
            TestData.BASE_URL
        )

    @allure.step('Клик по ингредиенту и ожидание появления модального окна деталей ингредиента')
    def click_ingredient_button_and_watch_details(self):
        # Клик по кнопке "Флюоресцентная булка"
        self.click_element_by_script_by_xpath(
            ConstructorAndFeedPageLocators.BUTTON_BUN_FLUO
        )

        # Явное ожидание для загрузки заголовка "Детали ингредиента"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            ConstructorAndFeedPageLocators.HEADER_INGREDIENT_DETAILS,
            3
        )

    @allure.step('Проверка URL-адреса на соответствие страницы ингредиента')
    def check_text_ingredient_in_url(self):
        # Проверка URL-адреса на соответствие страницы ингредиента
        self.check_text_in_current_url(
            "/ingredient/"
        )

    @allure.step('Клик по кнопке "Закрыть" модального окна деталей ингредиента')
    def click_close_ingredient_details_modal_button(self):
        # Клик по кнопке закрытия окна "Детали ингредиента"
        self.click_element_by_script_by_xpath(
            ConstructorAndFeedPageLocators.BUTTON_CLOSE_MODAL
        )

        # Явное ожидание для загрузки счётчика количества ингредиента
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS,
            3
        )

    @allure.step('Проверка счётчика ингредиента на соответствие количеству')
    def check_ingredient_counter_quantity(self, quantity):
        # Проверка счётчика ингредиента на соответствие количеству
        assert self.find_element_by_xpath(
            ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS
        ).text.strip() == quantity

    @allure.step('Перетаскивание ингредиента')
    def drag_n_drop_ingredient(self, quantity):
        # Перетаскивание элемента
        self.drag_n_drop_element(
            ConstructorAndFeedPageLocators.BUTTON_BUN_FLUO,
            ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE
        )

        # Явное ожидание для загрузки счётчика ингредиента с заданным количеством
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            ConstructorAndFeedPageLocators.COUNTER_QUANTITY_INGREDIENTS + f'[text()="{quantity}"]',
            3
        )