class RecoverPasswordPageLocators:

    # Кнопка показа/скрытия пароля
    BUTTON_PASSEYE = './/div[contains(@class, "input_type_password")]/descendant::div'
    # Кнопка «Личный кабинет»
    BUTTON_PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]'
    # Кнопка «Восстановить»
    BUTTON_RECOVER = './/button[text()="Восстановить"]'
    # Кнопка «Сохранить»
    BUTTON_SAVE = './/button[text()="Сохранить"]'
    # Поле ввода пароля - показано
    FIELD_PASSWORD_VISIBLE = './/div[contains(@class, "input_type_text")]'
    # Поле ввода «Email»
    INPUT_EMAIL = './/label[text()="Email"]/following-sibling::input'
    # Ссылка «Восстановить пароль»
    LINK_RECOVER_PASSWORD = './/a[text()="Восстановить пароль"]'
    # Модальное окно
    MODAL_WINDOW = [
        './/section[contains(@class, "Modal_modal__P3_V5")]',
        './/div[contains(@class, "Modal_modal_overlay__x2ZCr")]'
    ]