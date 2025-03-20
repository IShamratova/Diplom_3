import allure
from data.data import TestData
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_feed_button(self):
        # Клик по кнопке "Лента Заказов"
        self.click_element_by_script_by_xpath(OrderPageLocators.BUTTON_FEED)

        # Явное ожидание для загрузки заголовка "Лента Заказов"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.HEADER_ORDER_FEED,
            3
        )
        
    @allure.step('Проверка и выдача значения счётчика "Выполнено за всё время" на неравенство заданному тексту')
    def check_and_return_orders_done_total_quantity(self, given_text):
        # Проверка значения счётчика "Выполнено за всё время" на неравенство заданной строке
        self.wait_for_text_differing_from_given_by_timeout(
            OrderPageLocators.TEXT_ORDERS_DONE_TOTAL,
            given_text,
            10)

        # Выдача значения счётчика "Выполнено за всё время"
        return int(
            self.find_element_by_xpath(
                OrderPageLocators.TEXT_ORDERS_DONE_TOTAL
            ).text.strip()
        )

    @allure.step('Проверка и выдача значения счётчика "Выполнено за сегодня" на неравенство заданному тексту')
    def check_and_return_orders_done_today_quantity(self, given_text):
        # Проверка значения счётчика "Выполнено за сегодня" на неравенство заданной строке
        self.wait_for_text_differing_from_given_by_timeout(
            OrderPageLocators.TEXT_ORDERS_DONE_TODAY,
            given_text, 
            10)

        # Выдача значения счётчика "Выполнено за сегодня"
        return int(
            self.find_element_by_xpath(
                OrderPageLocators.TEXT_ORDERS_DONE_TODAY
            ).text.strip()
        )

    @allure.step('Ввод учётных данных и нажатие кнопки "Войти"')
    def user_login(self, email, password):
        # Клик по кнопке "Личный Кабинет"
        self.click_element_by_script_by_xpath(
            OrderPageLocators.BUTTON_PERSONAL_ACCOUNT
        )

        # Ввод персональных данных
        self.set_text_to_field_by_xpath(
            OrderPageLocators.INPUT_EMAIL, email
        )
        self.set_text_to_field_by_xpath(
            OrderPageLocators.INPUT_PASSWORD, password
        )

        # Клик по кнопке "Войти"
        self.click_element_by_xpath(
            OrderPageLocators.BUTTON_ENTER
        )

        # Явное ожидание для загрузки страницы после входа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.BUTTON_ORDER, 
            3
        )

    @allure.step('Оформление заказа')
    def create_order(self):
        # Перетаскивание элемента ингредиента
        self.drag_n_drop_element(
            OrderPageLocators.BUTTON_BUN_FLUO,
            OrderPageLocators.SECTION_DRAG_BUN_HERE
        )

        # Скроллинг до элемента ингредиента
        self.scroll_to_element_by_xpath(
            OrderPageLocators.BUTTON_SAUCE_SPICY
        )

        # Перетаскивание элемента ингредиента
        self.drag_n_drop_element(
            OrderPageLocators.BUTTON_SAUCE_SPICY,
            OrderPageLocators.SECTION_DRAG_BUN_HERE
        )

        # Скроллинг до элемента ингредиента
        self.scroll_to_element_by_xpath(
            OrderPageLocators.BUTTON_FILLING_PROTO
        )

        # Перетаскивание элемента ингредиента
        self.drag_n_drop_element(
            OrderPageLocators.BUTTON_FILLING_PROTO,
            OrderPageLocators.SECTION_DRAG_BUN_HERE
        )

        # Скроллинг до элемента ингредиента
        self.scroll_to_element_by_xpath(
            OrderPageLocators.BUTTON_FILLING_CHEESE
        )

        # Перетаскивание элемента ингредиента
        self.drag_n_drop_element(
            OrderPageLocators.BUTTON_FILLING_CHEESE,
            OrderPageLocators.SECTION_DRAG_BUN_HERE
        )

        # Скроллинг до кнопки "Оформить заказ"
        self.scroll_to_element_by_xpath(
            OrderPageLocators.BUTTON_ORDER
        )

        # Клик по кнопке "Оформить заказ"
        self.click_element_by_script_by_xpath(
            OrderPageLocators.BUTTON_ORDER
        )

    @allure.step('Проверка идентификатора созданного заказа')
    def check_created_order_id(self, given_text):
        # Явное ожидание для загрузки текста модального окна с деталями созданного заказа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.TEXT_ORDER_ID,
            3)

        # Проверка идентификатора созданного заказа на неравенство заданному тексту
        self.wait_for_text_differing_from_given_by_timeout(
            OrderPageLocators.HEADER_ORDER_ID,
            given_text,
            10
        )

    @allure.step('Выдача идентификатора созданного заказа')
    def return_created_order_id(self):
        # Выдача идентификатора созданного заказа
        return self.find_element_by_xpath(
            OrderPageLocators.HEADER_ORDER_ID
        ).text.strip()

    @allure.step('Клик по кнопке закрытия модального окна с деталями созданного заказа')
    def click_close_order_details_modal_button(self):
        # Клик по кнопке закрытия модального окна с деталями созданного заказа
        self.click_element_by_script_by_xpath(
            OrderPageLocators.BUTTON_CLOSE_MODAL
        )

        # Явное ожидание для загрузки кнопки "Лента Заказов"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.BUTTON_FEED, 
            3
        )

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_feed_button(self):
        # Клик по кнопке "Лента Заказов"
        self.click_element_by_script_by_xpath(
            OrderPageLocators.BUTTON_FEED
        )

        # Явное ожидание для загрузки заголовка "Лента заказов"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.HEADER_ORDER_FEED,
            3
        )

    @allure.step('Проверка нахождения номера созданного заказа в разделе "В работе"')
    def check_created_order_id_in_work(self, created_order_id):
        # Проверка идентификаторов заказов в работе на неравенство строке "Все текущие заказы готовы!"
        self.wait_for_text_differing_from_given_by_timeout(
            OrderPageLocators.TEXT_ORDERS_IN_WORK_FIRST_LIST_ITEM,
            OrderPageLocators.TEXT_ORDERS_IN_WORK_ALL_DONE,
            30
        )

        # Проверка идентификаторов заказов в работе на неравенство строке "Все текущие заказы готовы!"
        self.wait_for_text_equals_to_given_by_timeout(
            OrderPageLocators.TEXT_ORDERS_IN_WORK_FIRST_LIST_ITEM,
            '0' + created_order_id,
            30
        )

        # Проверка нахождения номера созданного заказа в разделе "В работе"
        assert any(
            created_order_id in ''.join(li.text.strip())
                for li in
                   self.find_elements_by_xpath(
                       OrderPageLocators.TEXT_ORDERS_IN_WORK_LIST_ITEMS
                   )
        )

    @allure.step('Прокрутка страницы до счётчика "Выполнено за сегодня"')
    def scroll_to_orders_done_today(self):
        # Скроллинг до элемента "Выполнено за сегодня"
        self.scroll_to_element_by_xpath(
            OrderPageLocators.TEXT_ORDERS_DONE_TODAY
        )

    @allure.step('')
    def check_incrementation_of_orders_count(self, count_value, new_count_value):
        assert int(count_value) < int(new_count_value)

    @allure.step('Клик по идентификатору созданного заказа')
    def click_created_order_id(self, created_order_id):
        # Явное ожидание для загрузки идентификатора созданного заказа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.TEXT_ORDER_HISTORY_LIST_ITEM + '[contains(text(), "#0' + created_order_id + '")]', 
            15
        )

        # Клик по идентификатору созданного заказа
        self.click_element_by_script_by_xpath(
            OrderPageLocators.TEXT_ORDER_HISTORY_LIST_ITEM + '[contains(text(), "#0' + created_order_id + '")]/ancestor::a'
        )

        # Явное ожидание для загрузки заголовка модального окна с деталями созданного заказа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.HEADER_ORDER_DETAILS, 
            3
        )

    @allure.step('Проверка наименования созданного заказа')
    def check_order_name(self):
        # Явное ожидание для загрузки модального окна с деталями созданного заказа 
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.HEADER_ORDER_DETAILS,
            3
        )
        
        assert OrderPageLocators.TEXT_ORDER_NAME == self.find_element_by_xpath(
            OrderPageLocators.HEADER_ORDER_DETAILS
        ).text.strip()

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_personal_account_button(self):
        # Явное ожидание для загрузки кнопки "Личный Кабинет"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.BUTTON_PERSONAL_ACCOUNT,
            3
        )

        # Клик по кнопке "Личный Кабинет"
        self.click_element_by_script_by_xpath(
            OrderPageLocators.BUTTON_PERSONAL_ACCOUNT
        )

    @allure.step('Клик по ссылке "История заказов"')
    def click_order_history_link(self):
        # Явное ожидание для загрузки ссылки "История заказов"
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.LINK_ORDER_HISTORY, 
            3
        )

        # Клик по ссылке "История заказов"
        self.click_element_by_script_by_xpath(
            OrderPageLocators.LINK_ORDER_HISTORY
        )

    @allure.step('Проверка URL-адреса на соответствие страницы "История заказов"')
    def check_order_history_url(self):
        # Проверка URL-адреса на соответствие страницы "История заказов"
        self.check_url(TestData.BASE_URL + TestData.ROUTES["order_history"])

    @allure.step('Клик по номеру созданного заказа')
    def click_created_order_number(self, created_order_id):
        # Явное ожидание для загрузки идентификатора созданного заказа
        self.wait_for_visibility_of_element_by_xpath_by_timeout(
            OrderPageLocators.TEXT_ORDER_HISTORY_DIV + '[contains(text(), "#0' + created_order_id + '")]',
            3)

        # Клик по идентификатору созданного заказа
        self.click_element_by_script_by_xpath(
            OrderPageLocators.TEXT_ORDER_HISTORY_DIV + '[contains(text(), "#0' + created_order_id + '")]')