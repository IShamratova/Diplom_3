class ConstructorAndFeedPageLocators:

    # Кнопка «Конструктор»
    BUTTON_CONSTRUCTOR = './/p[text()="Конструктор"]/parent::a'
    # Кнопка «Лента Заказов»
    BUTTON_FEED = './/p[text()="Лента Заказов"]/parent::a'
    # Кнопка «Личный кабинет»
    BUTTON_PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]'
    # Кнопка «Оформить заказ»
    BUTTON_ORDER = './/button[text()="Оформить заказ"]'
    # Кнопка булки «Флюоресцентная булка R2-D3»
    BUTTON_BUN_FLUO = './/p[text()="Флюоресцентная булка R2-D3"]'
    # Кнопка булки «Соус Spicy-X»
    BUTTON_SAUCE_SPICY = './/p[text()="Соус Spicy-X"]'
    # Кнопка начинки «Мясо бессмертных моллюсков Protostomia»
    BUTTON_FILLING_PROTO = './/p[text()="Мясо бессмертных моллюсков Protostomia"]'
    # Кнопка начинки «Сыр с астероидной плесенью»
    BUTTON_FILLING_CHEESE = './/p[text()="Сыр с астероидной плесенью"]'
    # Кнопка закрытия модального окна
    BUTTON_CLOSE_MODAL = './/button[contains(@class, "close")]'
    # Счетчик количества ингредиентов
    COUNTER_QUANTITY_INGREDIENTS = BUTTON_BUN_FLUO + '/preceding-sibling::div/p[contains(@class, "counter")]'
    # Заголовок «Соберите бургер»
    HEADER_ASSEMBLE_BURGER = './/h1[text()="Соберите бургер"]'
    # Заголовок всплывающего окна «Детали ингредиента»
    HEADER_INGREDIENT_DETAILS = './/h2[text()="Детали ингредиента"]'
    # Заголовок всплывающего окна «Детали ингредиента»
    HEADER_ORDER_DETAILS = './/div[contains(@class, "Modal_orderBox")]/h2'
    # Заголовок «Лента заказов»
    HEADER_ORDER_FEED = './/h1[text()="Лента заказов"]'
    # Заголовок всплывающего окна «идентификатор заказа»
    HEADER_ORDER_ID = './/p[text()="идентификатор заказа"]/preceding-sibling::h2'
    # Текст «Выполнено за все время»
    TEXT_ORDERS_DONE_TOTAL = './/p[text()="Выполнено за все время:"]/following-sibling::p'
    # Текст «Выполнено за сегодня»
    TEXT_ORDERS_DONE_TODAY = './/p[text()="Выполнено за сегодня:"]/following-sibling::p'
    # Текст «В работе» первого элемента списка
    TEXT_ORDERS_IN_WORK_FIRST_LIST_ITEM = './/p[text()="В работе:"]/following-sibling::ul[2]/li'
    # Текст «В работе» элементы списка
    TEXT_ORDERS_IN_WORK_LIST_ITEMS = './/li[contains(@class, "text_type_digits")]'
    # Текст «В работе» - Все текущие заказы готовы
    TEXT_ORDERS_IN_WORK_ALL_DONE = 'Все текущие заказы готовы!'
    # Текст с идентификатором заказа
    TEXT_ORDER_HISTORY_LIST_ITEM = './/li[contains(@class, "OrderHistory_listItem")]/descendant::p'
    # Текст с идентификатором заказа
    TEXT_ORDER_HISTORY_DIV = './/div[contains(@class, "OrderHistory_textBox")]/p'
    # Текст всплывающего окна «идентификатор заказа»
    TEXT_ORDER_ID = './/p[text()="идентификатор заказа"]'
    # Текст названия заказа
    TEXT_ORDER_NAME = 'Spicy бессмертный флюоресцентный астероидный бургер'
    # Секция добавления ингредиентов
    SECTION_DRAG_BUN_HERE = './/section[contains(@class, "basket")]'