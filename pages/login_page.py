from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Login page is not opened"

        # not correct due to different languages in URL
        # assert "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" == self.browser.current_url, "Login page is not opened"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрируем нового пользователя

        # fill email form
        reg_email_form = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        reg_email_form.send_keys(email)

        # fill password form
        reg_password_form = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD)
        reg_password_form.send_keys(email)

        # repeat password
        reg_password_form_conf = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        reg_password_form_conf.send_keys(email)

        # click register
        reg_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
