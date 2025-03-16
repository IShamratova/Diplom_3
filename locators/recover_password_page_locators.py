class RecoverPasswordPageLocators:

    # Кнопка показа/скрытия пароля
    BUTTON_PASSEYE = './/div[contains(@class, "input_type_password")]/descendant::div'
    # Кнопка "Восстановить"
    BUTTON_RECOVER = './/button[text()="Восстановить"]'
    # Кнопка "Сохранить"
    BUTTON_SAVE = './/button[text()="Сохранить"]'
    # Поле ввода пароля - показано
    FIELD_PASSWORD_VISIBLE = './/div[contains(@class, "input_type_text")]'
    # Поле ввода "Email"
    INPUT_EMAIL = './/label[text()="Email"]/following-sibling::input'
    # Ссылка "Восстановить пароль"
    LINK_RECOVER_PASSWORD = './/a[text()="Восстановить пароль"]'