from data.data import TestData
from locators.constructor_and_feed_page_locators import ConstructorAndFeedPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.login_page import LoginPage


class TestOrder:

    def test_order(self, driver, created_user):
        # Создание объекта страницы
        order_page = LoginPage(driver)

        # Открытие главной страницы
        order_page.open_url(TestData.BASE_URL)

        # Клик по кнопке "Лента Заказов"
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_FEED)

        # Явное ожидание для загрузки кнопки "Лента Заказов"
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_FEED, 3)

        # Проверка количества всех заказов на неравенство пустой строке
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TOTAL, "", 10)

        # Сохранение промежуточного значения количества всех заказов
        count_orders_total = int(order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TOTAL).text.strip())

        # Проверка количества заказов за сегодня на неравенство пустой строке
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TODAY, "", 10)

        # Сохранение промежуточного значения количества заказов за сегодня
        count_orders_today = int(order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TODAY).text.strip())

        # Клик по кнопке "Личный Кабинет"
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Ввод учетных данных
        order_page.login(created_user["email"], created_user["password"])

        # Явное ожидание для загрузки страницы после входа
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.BUTTON_ORDER, 3)

        # Перетаскивание элемента ингредиента
        order_page.drag_n_drop_element(ConstructorAndFeedPageLocators.BUTTON_BUN_FLUO, ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE)

        # Скроллинг до элемента ингредиента
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.BUTTON_SAUCE_SPICY)

        # Перетаскивание элемента ингредиента
        order_page.drag_n_drop_element(ConstructorAndFeedPageLocators.BUTTON_SAUCE_SPICY, ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE)

        # Скроллинг до элемента ингредиента
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.BUTTON_FILLING_PROTO)

        # Перетаскивание элемента ингредиента
        order_page.drag_n_drop_element(ConstructorAndFeedPageLocators.BUTTON_FILLING_PROTO, ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE)

        # Скроллинг до элемента ингредиента
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.BUTTON_FILLING_CHEESE)

        # Перетаскивание элемента ингредиента
        order_page.drag_n_drop_element(ConstructorAndFeedPageLocators.BUTTON_FILLING_CHEESE, ConstructorAndFeedPageLocators.SECTION_DRAG_BUN_HERE)

        # Скроллинг до кнопки "Оформить заказ"
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.BUTTON_ORDER)

        # Клик по кнопке "Оформить заказ"
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_ORDER)

        # Явное ожидание для загрузки текста модального окна
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDER_ID, 3)

        # Проверка идентификатора заказа на неравенство "9999"
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_ID, "9999", 10)

        # Сохранение идентификатора заказа
        created_order_id = order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.HEADER_ORDER_ID).text.strip()

        # Клик по кнопке закрытия модального окна
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_CLOSE_MODAL)

        # Явное ожидание для загрузки кнопки "Лента Заказов"
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.BUTTON_FEED, 3)

        # Клик по кнопке "Лента Заказов"
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_FEED)

        # Явное ожидание для загрузки кнопки "Лента Заказов"
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_FEED, 3)

        # Проверка идентификаторов заказов в работе на неравенство строке "Все текущие заказы готовы!"
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDERS_IN_WORK_FIRST_LIST_ITEM, ConstructorAndFeedPageLocators.TEXT_ORDERS_IN_WORK_ALL_DONE, 30)

        # Проверка нахождения номера заказа в работе
        assert any(created_order_id in ''.join(li.text.strip()) for li in order_page.find_elements_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_IN_WORK_LIST_ITEMS))

        # Проверка количества всех заказов на неравенство предыдущему значению
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TOTAL, count_orders_total, 10)

        # Проверка увеличения промежуточного значения количества всех заказов
        assert count_orders_total < int(order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TOTAL).text.strip())

        # Скроллинг до элемента "Выполнено за сегодня"
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TODAY)

        # Проверка количества заказов за сегодня на неравенство предыдущему значению
        order_page.wait_for_text_differing_from_given_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TODAY, count_orders_today, 10)

        # Проверка увеличения промежуточного значения количества заказов за сегодня
        assert count_orders_today < int(order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDERS_DONE_TODAY).text.strip())

        # Скроллинг до кнопки "Личный Кабинет"
        order_page.scroll_to_element_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Явное ожидание для загрузки идентификатора заказа
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDER_HISTORY_LIST_ITEM + '[contains(text(), "#0' + created_order_id + '")]', 15)

        # Клик по идентификатору заказа
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDER_HISTORY_LIST_ITEM + '[contains(text(), "#0' + created_order_id + '")]/ancestor::a')

        # Явное ожидание для загрузки страницы профиля
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_DETAILS, 3)

        assert ConstructorAndFeedPageLocators.TEXT_ORDER_NAME == order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.HEADER_ORDER_DETAILS).text.strip()

        # Клик по кнопке закрытия модального окна
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_CLOSE_MODAL)

        # Клик по кнопке "Личный Кабинет"
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.BUTTON_PERSONAL_ACCOUNT)

        # Явное ожидание для загрузки страницы профиля
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY, 3)

        # Клик по кнопке "История заказов"
        order_page.click_element_by_script_by_xpath(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)

        # Проверка URL-адреса на соответствие истории заказов
        order_page.check_url(TestData.BASE_URL + TestData.ROUTES["order_history"])

        # Явное ожидание для загрузки созданного заказа
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.TEXT_ORDER_HISTORY_DIV + '[contains(text(), "#0' + created_order_id + '")]', 3)

        # Клик по идентификатору заказа
        order_page.click_element_by_script_by_xpath(ConstructorAndFeedPageLocators.TEXT_ORDER_HISTORY_DIV + '[contains(text(), "#0' + created_order_id + '")]')

        # Явное ожидание для загрузки модального окна
        order_page.wait_for_visibility_of_element_by_xpath_by_timeout(ConstructorAndFeedPageLocators.HEADER_ORDER_DETAILS, 3)

        assert ConstructorAndFeedPageLocators.TEXT_ORDER_NAME == order_page.find_element_by_xpath(ConstructorAndFeedPageLocators.HEADER_ORDER_DETAILS).text.strip()