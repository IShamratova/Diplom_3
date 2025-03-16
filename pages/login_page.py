from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, email, password):

        # Ввод данных
        self.set_text_to_field_by_xpath(LoginPageLocators.INPUT_EMAIL, email)
        self.set_text_to_field_by_xpath(LoginPageLocators.INPUT_PASSWORD, password)

        # Клик по кнопке "Войти"
        self.click_element_by_xpath(LoginPageLocators.BUTTON_ENTER)
