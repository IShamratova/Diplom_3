class ConstructorAndFeedPageLocators:

    # Кнопка булки «Флюоресцентная булка R2-D3»
    BUTTON_BUN_FLUO = './/p[text()="Флюоресцентная булка R2-D3"]'
    # Кнопка закрытия модального окна
    BUTTON_CLOSE_MODAL = './/button[contains(@class, "close")]'
    # Кнопка «Конструктор»
    BUTTON_CONSTRUCTOR = './/p[text()="Конструктор"]/parent::a'
    # Кнопка «Лента Заказов»
    BUTTON_FEED = './/p[text()="Лента Заказов"]/parent::a'
    # Счетчик количества ингредиентов
    COUNTER_QUANTITY_INGREDIENTS = BUTTON_BUN_FLUO + '/preceding-sibling::div/p[contains(@class, "counter")]'
    # Заголовок «Соберите бургер»
    HEADER_ASSEMBLE_BURGER = './/h1[text()="Соберите бургер"]'
    # Заголовок всплывающего окна «Детали ингредиента»
    HEADER_INGREDIENT_DETAILS = './/h2[text()="Детали ингредиента"]'
    # Заголовок «Лента заказов»
    HEADER_ORDER_FEED = './/h1[text()="Лента заказов"]'
    # Секция добавления ингредиентов
    SECTION_DRAG_BUN_HERE = './/section[contains(@class, "basket")]'