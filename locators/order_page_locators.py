class OrderPageLocators:

    # Кнопка булки «Флюоресцентная булка R2-D3»
    BUTTON_BUN_FLUO = './/p[text()="Флюоресцентная булка R2-D3"]'
    # Кнопка закрытия модального окна
    BUTTON_CLOSE_MODAL = './/button[contains(@class, "close")]'
    # Кнопка «Войти»
    BUTTON_ENTER = './/button[text()="Войти"]'
    # Кнопка «Лента Заказов»
    BUTTON_FEED = './/p[text()="Лента Заказов"]/parent::a'
    # Кнопка начинки «Мясо бессмертных моллюсков Protostomia»
    BUTTON_FILLING_PROTO = './/p[text()="Мясо бессмертных моллюсков Protostomia"]'
    # Кнопка начинки «Сыр с астероидной плесенью»
    BUTTON_FILLING_CHEESE = './/p[text()="Сыр с астероидной плесенью"]'
    # Кнопка «Оформить заказ»
    BUTTON_ORDER = './/button[text()="Оформить заказ"]'
    # Кнопка «Личный кабинет»
    BUTTON_PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]'
    # Кнопка булки «Соус Spicy-X»
    BUTTON_SAUCE_SPICY = './/p[text()="Соус Spicy-X"]'
    # Заголовок «Лента заказов»
    HEADER_ORDER_FEED = './/h1[text()="Лента заказов"]'
    # Заголовок всплывающего окна «Детали ингредиента»
    HEADER_ORDER_DETAILS = './/div[contains(@class, "Modal_orderBox")]/h2'
    # Заголовок всплывающего окна «идентификатор заказа»
    HEADER_ORDER_ID = './/p[text()="идентификатор заказа"]/preceding-sibling::h2'
    # Поле ввода «Email»
    INPUT_EMAIL = './/label[text()="Email"]/following-sibling::input'
    # Поле ввода «Пароль»
    INPUT_PASSWORD = './/label[text()="Пароль"]/following-sibling::input'
    # Ссылка «История заказов»
    LINK_ORDER_HISTORY = './/a[text()="История заказов"]'
    # Ссылка «Профиль»
    LINK_PROFILE = './/a[text()="Профиль"]'
    # Текст «Выполнено за сегодня»
    TEXT_ORDERS_DONE_TODAY = './/p[text()="Выполнено за сегодня:"]/following-sibling::p'
    # Текст «Выполнено за все время»
    TEXT_ORDERS_DONE_TOTAL = './/p[text()="Выполнено за все время:"]/following-sibling::p'
    # Текст с идентификатором заказа
    TEXT_ORDER_HISTORY_LIST_ITEM = './/li[contains(@class, "OrderHistory_listItem")]/descendant::p'
    # Текст с идентификатором заказа
    TEXT_ORDER_HISTORY_DIV = './/div[contains(@class, "OrderHistory_textBox")]/p'
    # Текст «В работе» - Все текущие заказы готовы
    TEXT_ORDERS_IN_WORK_ALL_DONE = 'Все текущие заказы готовы!'
    # Текст «В работе» первого элемента списка
    TEXT_ORDERS_IN_WORK_FIRST_LIST_ITEM = './/p[text()="В работе:"]/following-sibling::ul[2]/li'
    # Текст «В работе» элементы списка
    TEXT_ORDERS_IN_WORK_LIST_ITEMS = './/li[contains(@class, "text_type_digits")]'
    # Текст всплывающего окна «идентификатор заказа»
    TEXT_ORDER_ID = './/p[text()="идентификатор заказа"]'
    # Текст названия заказа
    TEXT_ORDER_NAME = 'Spicy бессмертный флюоресцентный астероидный бургер'
    # Секция добавления ингредиентов
    SECTION_DRAG_BUN_HERE = './/section[contains(@class, "basket")]'