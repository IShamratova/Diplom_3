class PersonalAccountPageLocators:

    # Кнопка «Войти»
    BUTTON_ENTER = './/button[text()="Войти"]'
    # Кнопка «Выход»
    BUTTON_EXIT = './/button[text()="Выход"]'
    # Кнопка «Оформить заказ»
    BUTTON_ORDER = './/button[text()="Оформить заказ"]'
    # Кнопка «Личный кабинет»
    BUTTON_PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]'
    # Поле ввода «Email»
    INPUT_EMAIL = './/label[text()="Email"]/following-sibling::input'
    # Поле ввода «Пароль»
    INPUT_PASSWORD = './/label[text()="Пароль"]/following-sibling::input'
    # Ссылка «Профиль»
    LINK_PROFILE = './/a[text()="Профиль"]'
    # Ссылка «История заказов»
    LINK_ORDER_HISTORY = './/a[text()="История заказов"]'
    # Модальное окно
    MODAL_WINDOW = [
        './/section[contains(@class, "Modal_modal__P3_V5")]',
        './/div[contains(@class, "Modal_modal_overlay__x2ZCr")]'
    ]
    # Секция истории заказов
    SECTION_ORDER_HISTORY = './/div[contains(@class, "OrderHistory")]'





